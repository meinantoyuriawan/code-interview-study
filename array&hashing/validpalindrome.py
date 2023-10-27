# two pointer problems

def isPalindrome(s):
    s = (''.join(ch for ch in s if ch.isalnum())).lower()

    l = 0
    r = len(s)-1

    while l<r:
        if s[l] == s[r]:
            l+=1
            r-=1
        else:
            return False
    
    return True

def run_testcase():
    input = ['babab', 'race a car', 'ivan gunakan :P', 'A man, a plan, a canal: Panama']
    output = [True, False, False, True]
    for i in range(len(input)):
        vals = isPalindrome(input[i])
        if output[i] == vals:
            print("Testcase %s success, input: %s, outcome: %s" % (i+1, 
                input[i], output[i]))
        else:
            print("Testcase %s failed, input: %s, outcome: %s" % (i+1, 
                input[i], output[i]))
            
if __name__ == "__main__":
    run_testcase()