
num = 12

def is_even(a):
    if a%2 == 0:
        print("Even")
    else :
        print('False')
    
is_even(num)


# Above code have Error It should return TRUE or False 


def is_even(num):
    return num % 2 == 0  # Returns True/False (use this in conditions later)

print(is_even(12))  # Output: True