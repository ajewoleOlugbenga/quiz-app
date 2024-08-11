"""
hidden operators
NOT
OR
AND
"""
"""
instead of using elif we can use or to check for the other variables
"""
my_bool = True
my_num = 43

"""#not logical operator
if not my_bool:
    print("It's not True")
elif my_bool:
    print("Yes it is True")
else:
    print("Whatever")
"""
"""
#or operator --instead of elif statement

if not my_bool or my_num == 42:
    print("The statement pass")
else:
    print("The statement reject")
    """
#and operators to check if the two variable are true
#it will only run if the two condition is satisfied

if my_bool and my_num == 43:
    print("This condition is satisfied")
else:
    print("Error code.. Try again")