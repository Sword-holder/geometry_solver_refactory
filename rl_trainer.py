import numpy as np

from utils import test_all_problems, get_practical_problems
from geometry_solver.reinforcement_learning.pg.train import train
from geometry_solver.policy import RLPolicy


def test_rl_performance(agent):

    avg_trial_hist = []
    avg_before_prune_hist = []
    avg_after_prune_hist = []

    policy = RLPolicy(agent)
    for _ in range(10):
        avg_trial, avg_before_prune, avg_after_prune = test_all_problems(policy)
        avg_trial_hist.append(avg_trial)
        avg_before_prune_hist.append(avg_before_prune)
        avg_after_prune_hist.append(avg_after_prune)
        
    # print(avg_trial_hist)
    # print(avg_before_prune_hist)
    # print(avg_after_prune_hist)

    print('Average trial times: {}±{}'.format(np.mean(avg_trial_hist), np.std(avg_trial_hist)))
    print('Average solving step before prune: {}±{}'.format(np.mean(avg_before_prune_hist), np.std(avg_before_prune_hist)))
    print('Average solving step after prune: {}±{}'.format(np.mean(avg_after_prune_hist), np.std(avg_after_prune_hist)))


problems = get_practical_problems(range(1, 51))

for agent in train(problems):
    test_rl_performance(agent)

