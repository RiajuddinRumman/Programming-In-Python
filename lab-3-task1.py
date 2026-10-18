#25

listName = []
listGoal = []
totalGoal = 0
player = int(input("number of player : "))
for i in range(player):
    a = input("Enter Player name : ")
    b = int(input("Enter Player Goal : "))
    listName.append(a)
    listGoal.append(b)

for i in range(player):
    print(f"Player {listName[i]} scored {listGoal[i]} goals")

totalGoal = sum(listGoal)

avgGoal = totalGoal/player

highestGoal = max(listGoal)

indexOfHighest = listGoal.index(highestGoal)

print(f"goals scored by the team {totalGoal}")
print(f"average goal is {avgGoal}")
print(f"highest goal scorer is {listName[indexOfHighest]}")