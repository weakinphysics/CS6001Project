import pyspiel
from open_spiel.python.algorithms import cfr
from open_spiel.python.algorithms import exploitability
from open_spiel.python.algorithms import best_response, expected_game_score
from tqdm import tqdm
import time
import json 

import matplotlib.pyplot as plt





game = pyspiel.load_game("leduc_poker")


cfr_solver = cfr.CFRSolver(game)
vasto_lorder = cfr.CFRSolver(game)


policies = []
exps = []


iterations = 500 


for iter in range(1, iterations+1, 20):
    solver = cfr.CFRSolver(game)
    for _ in tqdm(range(iter)):
        solver.evaluate_and_update_policy()
        police = solver.average_policy()
    exploitability_value = exploitability.exploitability(game, police)
    policies.append(police)
    exps.append(exploitability_value)



player_id = 1
uniform_policy = pyspiel.UniformRandomPolicy(game)


br_values = []
uniform_values = []

for policy in policies:
    br_policy = best_response.BestResponsePolicy(game, player_id, policy)    
    br_value = br_policy.value(game.new_initial_state())
    uniform_value = abs(expected_game_score.policy_value(game.new_initial_state(), [policy, uniform_policy])[0])
    br_values.append(-br_value)
    uniform_values.append(uniform_value)

object = {
    0: [uniform_values, br_values, exps]
}

with open("results6.json", "w") as outfile:
    json.dump(object, outfile, indent=4)
    print("json dump complete")


r = list(range(1, iterations+1, 20))
plt.plot(r, exps, linestyle='-', marker='o')
plt.plot(r, br_values, linestyle='--', marker='o', color='red')
plt.plot(r, uniform_values, linestyle='--', marker='o', color='green')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Exploitability(Optimal play against known policy)')
plt.savefig("one.png")
plt.show()






