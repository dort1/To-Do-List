#dominic +milly
#to-do list
#1/11/24

#functions

list = []
#main
print("welcome to food list maker. make your food list")
print("MENU")
print("1. Add task to list   \n2. View current list \n3. Mark task as completed  \n4. Remove task \n5. Remove all tasks \n6.Arrange Alphebetically \n7.Count \n8.EXIT")


while True:
# Collect input
    option=int(input("option: "))
    if (option == 1):
        food= input("what do you want to eat ")
        list.append(food)
        print(list)
    if (option == 2):
        print(list)
    if (option == 3):
       done = input("what food did you eat")
       a = list.index(done)
       list.insert(a,"X" )
       list.remove(done)
       print(list)
    if (option == 4):
        remove =  input("what do you want to remove")
        list.remove(remove)
        print(list)
    if (option == 5):
        list.clear()
        print(list)
    if (option == 6):
        list.sort()
        print(list)
    if (option == 7):
        print(len(list))
    if (option == 8):
        break
