# createKey
def createKey(strInput):
    strK = str(sorted(strInput))
    return strK

# add to hash table
def appendToHash(strs):
    res = {}
    for item in strs:
        key = createKey(item)
        if key not in res:
            res[key] = [item]
        else:
            res[key].append(item)
    
    return res

# from hash to list
def hashToList(hashs):
    arr = []
    for _, v in hashs.items():
        arr.append(v)

    return arr

def groupAnagrams(strs):
   res = hashToList(appendToHash(strs))
   return res

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

result = groupAnagrams(strs)

print(result)