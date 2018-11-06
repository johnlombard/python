def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2) :
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothing")

def checklist(arg1, arg2):
    print(f"To Do: {arg1} \n {arg2}")

print_two("zed", "shaw")
print_two_again("zed", "shaw")
print_one("first!")
print_none()
checklist("work", "code")
