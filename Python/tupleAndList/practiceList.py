# WAP TO ASK THE USER TO ENTER NAME OF THER THREE FAV MOVIES AND STORE THERE LIST
# firstMOviesNAme  = input("Enter Movies name")
# secondMOviesNAme  = input("Enter Movies name")
# thirdMOviesNAme  = input("Enter Movies name")
# list =[]
# list.append(firstMOviesNAme)
# list.append(secondMOviesNAme)
# list.append(thirdMOviesNAme)
# print(list)

# Second Way
list = []
for i in range(0,3):
    moviesName = input("Enter movies name ::")
    list.append(moviesName)
print(list)


# WAP TO CHECK IF A LIST CONATIN PALINDROME OF ELEMENT
listElement = [1,2,3,2,1]
copyListElement = listElement.copy()
copyListElement.reverse()
if(copyListElement == listElement):
    print("List is palindrome")
else:
    print("List is Not Plaindrome")