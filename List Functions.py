# friends = ["Anthony", "Kevin", "Daniel", "Andrew", "Anthony", "Boomer", "Kai", "Yash","Angelica <3"]
# friends[3] = "Marcus"
# print(friends[2:5])

friends = ["Anthony", "Anthony", "Kevin", "Daniel", "Andrew", "Anthony", "Boomer", "Kai", "Yash","Angelica <3"]
luckyNumbers = [6,5,4,3,2,1]

friends.extend(luckyNumbers)
friends.append("But Angelica doe...")
friends.insert(2, "Buddha")
friends.remove("Andrew")
friends.pop()
# friends.clear()

print(friends.index("Angelica <3"))
print(friends.count("Anthony"))

luckyNumbers.sort()
luckyNumbers.reverse()

roll_the_dice = luckyNumbers.copy()

print(luckyNumbers)
print(friends)

print(roll_the_dice)