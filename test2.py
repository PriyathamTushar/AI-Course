numb1 = input("Please enter first range: ")
numb2 = input("Please enter second range: ")
name = input("Please enter your name: ")

print(type(name),type(numb1),type(numb2))
numb1 = int(numb1)
numb2 = int(numb2)
for i in range(numb1,numb2):
    print(name,i)
