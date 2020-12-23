from geometry_solver.reinforcement_learning.mcts_pure.mcts_pure import run_mcts
from utils import get_practical_problems


problems = get_practical_problems(range(1, 131))
all_steps = []

for i, problem in enumerate(problems):
    n_steps = run_mcts(problem)
    print(f'problem {i} take {n_steps} steps')
    all_steps.append(n_steps)

print(f'Average steps: {sum(all_steps)/len(all_steps)}')
