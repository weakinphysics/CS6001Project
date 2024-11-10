import json
import matplotlib.pyplot as plt
coll = {}

data = None
with open("results6.json", 'r') as file:
    data = json.load(file)


my = []
for value in data.values():
    my.append(value)

iterations = 500

r = list(range(1, iterations+1, 20))
plt.plot(r, my[0][0], linestyle='-', marker='o')


plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Value of game when playing against uniform random strategy')
plt.savefig("one.png")
plt.show()


plt.plot(r, my[0][1], linestyle='--', marker='o', color='red')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Value of game when playing against best response (tailored to CFR)')
plt.savefig("two.png")
plt.show()

plt.plot(r, my[0][2], linestyle='--', marker='o', color='green')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Exploitability of calculated average policy')
plt.savefig("three.png")
plt.show()