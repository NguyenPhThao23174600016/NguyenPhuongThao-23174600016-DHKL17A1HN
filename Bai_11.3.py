#list of animals
n=input("List of animals:").split(' ')
print("Number of animals:", len(n))
a=input("I want to find: ")
if a in n :
    print("There is",a, "in list of animals")
else:
    print("There isn't",a,"in list of animals")