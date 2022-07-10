"""
Use a stack to check whether or not a string
has balanced usage of parenthesis.
Example:
    (), ()(), (({[]}))  <- Balanced.
    ((), {{{)}], [][]]] <- Not Balanced.
Balanced Example: {[]}
Non-Balanced Example: (()
Non-Balanced Example: ))
"""

def arePairs(open, close):
    if open == '[' and close == ']':
        return True
    if open == '{' and close == '}':
        return True
    if open == '(' and close == ')':
        return True
    return False

def Blanced(A):
    stack=[]
    for i in range(len(stack)):
        if A[i] == '[' or A[i]=='{' or A[i] == '(':
            stack.append(A[i])
        elif A[i] == ')' or A[i] == '}' or A[i] == ')':
            if arePairs(stack[-1],A[i] or len(stack) != 0):     #stack[-1] is a peek function
                stack.pop()
                return False
    if len(stack) == 0:
        return True
    else:
        return False


A = "[{()()}]"
print(Blanced(A))