def function(*args):
    print("Hello", args[0])
    print("Hello", args[1])
function("Emily", "Mike") 



def function(juice, *fruits):
    for fruit in fruits:
        print(juice, fruit)
function("Juice from", "apple", "tangerine")



def function(**kwargs):
    print("First name is", kwargs["fname"], "and last name is", kwargs["lname"])
function(fname = "Dastan",lname = "Satpayev")    



def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(key + ":", value)
my_function("emil123", age = 25, city = "Oslo", hobby = "coding")