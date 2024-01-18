#  Code for Sum(First Bullet)
num1 = 5
num2 = 6
sum = num1 + num2
print("The Sum is :",sum)
# Code for String(Second Bullet)
Spiderman = "With great power comes great responsiblity of the "
Spiderman += "World!"
print(Spiderman)
# Code for Boolean(Third Bullet)
is_python_fun = False
if is_python_fun:
    print("Python is fun!")
else:
    print("Python is snake in the sleeve(in urdu)") 
# Code for List(Fourth Bullet)
fruits = ["Watermellon","Pomegranate","Guava"]
print("original list:", fruits)
new_fruit = "Pitaya"
fruits.append(new_fruit)
print("updated list:",fruits)
# Code for Floats(Fifth Bullet)
price = 15.88
con = int(price)
print("The original price is:",price)
print("The converted price is:",con)
# Code for Dictionary(Sixth Bullet)
student_info = {'Name':'Abuzar','Age':'22','Grade':'A'}
print("Student Information:",student_info)
# Code for Age(Seventh Bullet)
age = int(input("Your Age :"))
if age<=0:
    print("Are you for real?")
elif age<13:
    print("Kid")
elif age<18:
    print("Teenager")
elif age<60:
    print("Adult")
elif age<100:
    print("Senior Citizen")   
elif age>=100:
    print("How in the World you are Alive!")  
# Code for Complex Number(Eighth Bullet)
comp_num = 4 + 6j
real_part = int(comp_num.real)
imaginary_part = int(comp_num.imag)
print("Real part is :",real_part)
print("Imaginary part is:",imaginary_part)
# Code for two strings(Nineth Bullet)
string1 = "I have put Python in the right path so"
string2 = "it will be in Jannah,Right!"
combined_string = string1 + " " + string2
length_of_combined_string = len(combined_string)
print(f"The combined string is: {combined_string}, and its length is: {length_of_combined_string}")
# Code for tuple(Tenth Bullet)
days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
third_day = days_of_week[2]
print("The third day of the week is:", third_day)