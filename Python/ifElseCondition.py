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



#WAP TO CHECK NUMBER IS ENTER BY USER IS EVEN OR ODD
if(mark %2 ==0):
    print("Even")
else:
    print("Odd")


# WAP TO FIND GREATEST 4 NUMBER ENTER BY THE USER
num1 = int(input("Enter First Number :"))  #10
num2 = int(input("Enter Second Number :")) #20
num3 = int(input("Enter Third Number :"))   #30
num4 = int(input("Enter four Number :"))   #40

if(num1 > num2 and num1 >num3 and num1 > num4):   # 10 > 20 and 10 > 30
    print("First number is Largest",num1)
elif(num2 > num3 and num2 > num4):
    print("Second number is Largest",num2)
elif(num3 > num4):
    print("Third number is largest", num3)
else:
    print("Four number is largest",num4)
