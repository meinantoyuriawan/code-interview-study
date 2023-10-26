def isAnagram(s, t):
    sortedS ="".join(sorted(s))
    sortedT ="".join(sorted(t))

    if sortedS == sortedT:
        return True