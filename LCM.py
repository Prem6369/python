num1=int(input("enter the number1:"))
num2=int(input("enter the number2:"))
num3=int(input("enter the number3:"))

large=max(num1,num2,num3)

for i in range (100):
    if large % num1 == 0 and large % num2 == 0 and large % num3 == 0:
        print(large)
        break;
    large=large+large
