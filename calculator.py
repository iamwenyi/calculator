tryagain = True
ans = ""

def add(ans,other_num):
    ans = ans + other_num
    return ans
    
def minus(ans,other_num):
    ans = ans - other_num
    return ans
    
def times(ans,other_num):
    ans = ans * other_num
    return ans
    
def divide(ans,other_num):
    ans = ans / other_num
    return ans
    
def main(ans,other_num):
    if operation == "+":
        ans = add(ans,other_num)
    elif operation == "-":
        ans = minus(ans,other_num)
    elif operation == "*":
        ans = times(ans,other_num)
    elif operation == "/":
        ans = divide(ans,other_num)
    return ans
    
while tryagain == True:
    if ans == "":
        first_num = int(input("Enter first number: "))
        ans = first_num
        
    other_num = int(input("Enter other number: "))
    print("+ - * /")
    operation = input("Enter an operation: ")
    
    ans = main(ans,other_num)
    print(f"The answer is {ans}")
    
    confirm = input("Add more? (yes or no): ")
    if confirm == "no":
        tryagain = False