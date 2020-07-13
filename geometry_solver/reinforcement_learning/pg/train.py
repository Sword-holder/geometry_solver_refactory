import torch
import torch.nn as nn
from torch.optim import Adam
from torch.distributions import Categorical
import gym
from tqdm import tqdm
import numpy as np

from geometry_solver.reinforcement_learning.pg.net import Net
from geometry_solver.reinforcement_learning.env import Environment
from geometry_solver.policy import RLPolicy

SPACE_SIZE = 4
ACTION_SIZE = 2
EPISODE = 100
SAMPLE_NUM = 10
TEST_NUM = 10
learning_rate = 0.01
gamma = 0.9


class Agent(object):
    
    def __init__(self):
        self.net = Net()

    def chose_action(self, obs):
        with torch.no_grad():
            probs = self.net(obs)
            d = Categorical(probs)
            action = d.sample()
        return action.cpu().data.numpy().astype(int)

    def update_policy(self, obs):
        action = torch.argmax(self.net(obs))
        return action


def test_performance(env, agent):
    print('Test performance...')
    final_score = []
    policy = RLPolicy(agent)
    
    for _ in range(TEST_NUM):
        obs = env.reset()
        total_reward = 0
        while True:
            action = agent.chose_action(obs)
            obs, reward, done, _ = env.step(action)
            total_reward += reward
            if done:
                break
            final_score.append(total_reward)

    print('Final score = {}'.format(sum(final_score) / len(final_score)))
    
    
def update_policy(agent, state_pool, action_pool, reward_pool, optimizer):
    print('Update policy...')
    optimizer.zero_grad()
    for a, s, r in zip(action_pool, state_pool, reward_pool):
        a = torch.tensor(a).long()
        probs = agent.net(s)
        m = Categorical(probs)
        loss = -m.log_prob(a) * r
        loss.backward()
    optimizer.step()
    

def interaction(env, agent):
    # sample experience.
    print('Begin to sample...')
    state_pool = []
    action_pool = []
    reward_pool = []
    for _ in tqdm(range(SAMPLE_NUM)):
        episode_state = []
        episode_action = []
        episode_reward = []
        obs = env.reset()
        while True:
            action = agent.chose_action(obs)
            episode_state.append(obs)
            episode_action.append(action)
            obs, reward, done, _ = env.step(action)
            episode_reward.append(reward)
            if done:
                running_reward = 0
                for i in reversed(range(len(episode_reward))):
                    running_reward += episode_reward[i]
                    episode_reward[i] = running_reward
                    running_reward *= gamma
                reward_pool += episode_reward
                state_pool += episode_state
                action_pool += episode_action
                break
    return state_pool, action_pool, reward_pool


def train(problems):
    env = Environment(problems)
    agent = Agent()
    optimizer = Adam(agent.net.parameters(), lr=learning_rate)

    for i in range(EPISODE):
        print('Episode {}'.format(i))
        state_pool, action_pool, reward_pool = interaction(env, agent)
        update_policy(agent, state_pool, action_pool, reward_pool, optimizer)
        test_performance(env, agent)
        yield agent

