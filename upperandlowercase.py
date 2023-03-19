input_string = str(input("Enter the string:", ))
def string_num(input_string):
    n=len(input_string)
    n_upper=0
    n_lower=0
    for i in range(n):
        if input_string[i].isalpha():
            if input_string[i].isupper():
                n_upper+=1
            else:
                 n_lower+=1
    
    return n_upper,n_lower
n_upper,n_lower=string_num(input_string)   
print("no of upper:", n_upper)
print("no of lower:", n_lower)

