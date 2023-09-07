
def balance_bracket_sequence(sentence):
    stack = []
    for char in sentence:
        if char == '(':
            stack.append(char)
        elif char == ")":
            if not stack or stack[-1] != '(':
                print("No")
                return 0
            stack.pop()
    print("Yes")
    return 1
        
    
Input_sentence = str(input())
balance_bracket_sequence(Input_sentence)
        


