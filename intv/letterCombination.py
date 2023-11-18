def letterCombination():
    letters = {'2':['a','b','c'] , '3':['d','e','f'] , '4':['g','h','i'] , '5':['j','k','l'] , '6':['m','n','o'] , '7':['p','q','r','s'] , '8':['t','u','v'], '9':['w','x','y','z']}
    res = []
    len_digit = len(digits)
    stack = []

    def dfs(index):
        if len(stack) == len_digit:
            return "".join(stack)

        if index == len_digit:
            return
        
        for j in letters[digits[index]]:
            stack.append(j)
            temp = dfs(index+1)
            if temp != None:
                res.append(temp)
            stack.pop()

    dfs(0)
    return res