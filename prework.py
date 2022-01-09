#Question 1
def hello_name(user_name):
    """Display a greeting for a user."""
    print("Hello_"+user_name.upper()+"!")
hello_name('zak')

#Question 2
def first_odds():
    """Prints odd numbers from 1-100 and returns nothing"""
    odd_numbers = list(range(1,100,2))
    print(odd_numbers)

first_odds()

#Question 3
def max_num_in_list(a_list):
    """Prints biggest number in a list"""
    max_num = max(a_list)
    print(max_num)

max_num_in_list([1,2,7,15])

#Question 4
def is_leap_year(a_year):
    """Advises if given year is a leap year"""
    if a_year % 400 == 0 or a_year % 100 != 0 and a_year % 4 == 0:
        True
        print(str(a_year) + " is a leap year.")
    else:
        False
        print(str(a_year) + " is not a leap year.")

is_leap_year(2000)

#Question 5
def is_consecutive(a_list):
    """Tells if list of numbers is consecutive"""
    if a_list[1] != a_list[0] + 1 and a_list[2] != a_list[1] + 1:
        return False
        print("Not Consecutive")
    else:
        return True
        print("Consecutive")

is_consecutive([1,2,3])