def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    temp = []
    
    if (len(s) <2):
        return False
    
    for i in range(len(s)):
        if s[i] in ['(', '{', '['] :
            temp.append(s[i])
        
        elif s[i] in [')', '}', ']']:
            if len(temp) == 0:
                return False
            else :
                if s[i] == '}' and '{' == temp[-1]:
                    temp.pop(-1)

                elif s[i] == ']' and '[' == temp[-1]:
                    temp.pop(-1)

                elif s[i] == ')' and '(' == temp[-1]:
                    temp.pop(-1)

                else:
                    return False
    if len(temp) == 0:
        return True
    else:
        return False
    
s = "()[]{}"
print(isValid(s))