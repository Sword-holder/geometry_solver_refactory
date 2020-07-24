import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import gym
env = gym.make('CartPole-v1')
env.reset()

# DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
DEVICE = torch.device('cpu')

training_epoch = 1000
EPSILON = 0.8
N_ACTIONS = env.action_space.n
N_STATES = env.observation_space.shape[0]
LR = 0.001

GAMMA = 0.9

BATCH_SIZE = 1
TARGET_REPLACE_ITER = 100
MEMORY_CAPACITY = 2000


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.linear1 = nn.Linear(N_STATES, 64)
        self.linear2 = nn.Linear(64, 16)
        self.v_linear = nn.Linear(16, 1)
        self.a_linear = nn.Linear(16, N_ACTIONS)

    def forward(self, s):
        # print(s)
        x = s.float()
        common_out = self.linear1(x)
        common_out = F.relu(common_out)
        common_out = self.linear2(common_out)
        common_out = F.relu(common_out)

        v = self.v_linear(common_out)
        a = self.a_linear(common_out)
        out = v + a
        return out


class DQN():

    def __init__(self, is_double_dqn=True):
        self.eval_net = Net().to(DEVICE)
        self.target_net = Net().to(DEVICE)
        self.learn_step_counter = 0
        self.optimizer = torch.optim.Adam(self.eval_net.parameters(), lr=LR)
        self.loss_func = nn.MSELoss()

        self.memory_index = 0
        self.memory = np.zeros((MEMORY_CAPACITY, N_STATES * 2 + 2))

        self.learn_step_counter = 0

        self.is_double_dqn = is_double_dqn


    def choose_action(self, s, epsilon=EPSILON):
        s = torch.unsqueeze(torch.FloatTensor(s), dim=0).to(DEVICE)
        if np.random.uniform() < epsilon:
            actions_value = self.eval_net.forward(s)
            action = torch.max(actions_value, 1)[1].data.cpu().numpy()
            action = action[0]
        else:
            action = np.random.randint(N_ACTIONS)
        return action

    
    def store_transition(self, s, a, r, s_next):
        index = self.memory_index % MEMORY_CAPACITY
        transition = np.hstack((s, a, r, s_next))
        self.memory[index] = transition
        self.memory_index += 1


    def learn(self):

        if self.learn_step_counter % TARGET_REPLACE_ITER == 0:
            self.target_net.load_state_dict(self.eval_net.state_dict())
        self.learn_step_counter += 1

        sample_index = np.random.choice(MEMORY_CAPACITY, BATCH_SIZE)
        b_memory = self.memory[sample_index]
        b_s = torch.FloatTensor(b_memory[:, :N_STATES]).to(DEVICE)
        b_a = torch.LongTensor(b_memory[:, N_STATES:N_STATES + 1]).to(DEVICE)
        b_r = torch.FloatTensor(b_memory[:, N_STATES + 1: N_STATES + 2]).to(DEVICE)
        b_s_next = torch.FloatTensor(b_memory[:, -N_STATES:]).to(DEVICE)

        # with torch.no_grad():
        q_eval = self.eval_net(b_s).gather(1, b_a)

        if self.is_double_dqn:
            q_eval_next = self.eval_net(b_s_next).detach()
            selected_actions = torch.argmax(q_eval_next, dim=1).view(BATCH_SIZE, 1)
            q_next = self.target_net(b_s_next).detach()
            target_value = torch.gather(q_next, 1, selected_actions)
            q_target = b_r + GAMMA * target_value
        else:
            q_next = self.target_net(b_s_next).detach()
            q_target = b_r + GAMMA * q_next.max(dim=1)[0].view(BATCH_SIZE, 1)

        loss = self.loss_func(q_eval, q_target)

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()


dqn = DQN()

hist_r = []

for i in range(training_epoch):

    total_reward = 0
    s = env.reset()
    while True:
        # env.render()
        a = dqn.choose_action(s)
        s_next, r, done, info = env.step(a)

        # Modify reward.
        x, x_dot, theta, theta_dot = s_next
        r1 = (env.x_threshold - abs(x)) / env.x_threshold - 0.8
        r2 = (env.theta_threshold_radians - abs(theta)) / env.theta_threshold_radians - 0.5
        r_modified = r1 + r2

        dqn.store_transition(s, a, r_modified, s_next)

        if dqn.memory_index > MEMORY_CAPACITY:
            dqn.learn()

        s = s_next
        total_reward += r
        if done:
            # print('epoch: {}, get reward: {}'.format(i, total_reward))
            break

    if i % 50 == 0:
        total_reward = 0
        for _ in range(50):
            s = env.reset()
            while True:
                a = dqn.choose_action(s, epsilon=1)
                s, r, done, _ = env.step(a)
                total_reward += r
                if done:
                    break
        print('Epoch: {}, average reward = {}'.format(i, total_reward / 50))

    hist_r.append(total_reward)


env.close()

