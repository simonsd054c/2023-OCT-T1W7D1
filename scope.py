# Scope - global and local

fname = "Pat"
lname = "Cummins"

def greet():
    fname = "Steve"
    lname = "Smith"
    print("Inside the function")
    print(fname)
    print(lname)

print("Outside the function")
print(fname)
print(lname)
greet()