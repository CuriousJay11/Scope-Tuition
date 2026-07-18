import numpy as np


players = np.array(["Rohit", "Virat", "Rahul", "Gill"])
runs = np.array([124, 78, 45, 12])

print("Players:", players)
print("Runs:", runs)


print("\nTotal Runs:", np.sum(runs))

# Bester Scorer (Top Scorer)
top_scorer_index = np.argmax(runs)
print("Highest Runs:", players[top_scorer_index])


print("In players runs above 45:")
print(players[runs > 45])


low_scorer_index = np.argmin(runs)
print("Lowest Runs:", players[low_scorer_index])


print("\nSorted Runs:")
print(np.sort(runs))


print("\nLow/High Runs:")
for i in range(len(players)):
    if runs[i] > 45:
        print(players[i], "High")
    else:
        print(players[i], "Low")


print("\nPlayer Status:")
for i in range(len(players)):
    if runs[i] >= 100:
        status = 'Century (Excellent)'
    elif runs[i] >= 50:
        status = 'Half-Century (Good)'
    elif runs[i] >= 20:
        status = 'Average'
    else:
        status = 'Low Score'
    print(players[i], ":", status)