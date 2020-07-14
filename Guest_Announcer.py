def guest_list(guests):
    name = ""
    age = ""
    job = ""
    for guest in guests:
        name = guest[0]
        age = guest[1]
        job = guest[2]
   
        print("{} is {} years old and works as {}".format(name, str(age) , job))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""