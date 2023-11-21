def letComb(digits):

    dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
            
    res=[]
    # path = ''

    # def backtrack(number, index, dic, path, res):
    #     if index >= len(number):
    #         res.append(path)
    #         return
        
    #     string1 = dic[number[index]]
    #     for i in string1:
    #         backtrack(number, index+1, dic, path+i, res)

    # backtrack(digits, 0, dic, path, res)
    # return res

    def dfs(i, path):
        if len(path) == len(digits):
            res.append(path)
            return

        for x in dic[digits[i]]:
            dfs(i+1,path+x)

    if digits:
        dfs(0, "")

    return res

print(letComb("23"))