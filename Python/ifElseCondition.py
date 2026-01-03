# Grade Student bassed on the mark

mark = int(input("Enter Student Mark :"))

if(mark >= 90):
    print("Grade A")
elif (mark >= 80 and mark < 90):
    print("Grade B")
elif (mark >= 70 and mark < 80):
    print("Grade C")
elif(mark >= 60 and mark < 60):
    print("Grade D")
else:
    print("Fail") 