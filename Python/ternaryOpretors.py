#Write a Python program to check whether a number is even or odd using a ternary operator.

num = int(input("Enter any number"))
checkNumber  = "NUmber is Even" if num %2 ==0 else "Number is odd"
print(checkNumber)
 
#Check voting eligibility
Status = "Voter Eligibil" if num >= 18 else "Voter Not eligible"
print(Status)
    