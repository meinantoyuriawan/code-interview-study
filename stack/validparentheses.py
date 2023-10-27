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
    
def isValidHash(s):
    htab = {
        ")":"(",
        "}":"{",
        "]":"["
    }
    stack = []
    for c in s:
        if c not in htab:
            stack.append(c)
            continue
        if not stack or stack[-1] != htab[c]:
            return False
        stack.pop()

    return not stack #true if the stack is empty at the end
    
def run_testcase():
    input = ["()", "()[]{}", "(]"]
    output = [True, True, False]
    print("testing using array")
    for i in range(len(input)):
        vals = isValid(input[i])
        if output[i] == vals:
            print("Testcase %s success, input: %s, outcome: %s" % (i+1, 
                input[i], output[i]))
        else:
            print("Testcase %s failed, input: %s, outcome: %s, but instead: %s" % (i+1, 
                input[i], output[i], vals))
    print("testing using hash table")
    for i in range(len(input)):
        vals = isValidHash(input[i])
        if output[i] == vals:
            print("Testcase %s success, input: %s, outcome: %s" % (i+1, 
                input[i], output[i]))
        else:
            print("Testcase %s failed, input: %s, outcome: %s, but instead: %s" % (i+1, 
                input[i], output[i], vals))
            
if __name__ == "__main__":
    run_testcase()