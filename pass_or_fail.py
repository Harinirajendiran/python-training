student_name=input("enter the name:")
student_age=int(input("enter the age:"))
maths_mark=int(input("maths mark:"))
phy_mark=int(input("phy mark:"))
bio_mark=int(input("bio mark:"))
total=maths_mark+phy_mark+bio_mark
avg=total//3
print("name","age","total","avg")
print(student_name, student_age, total, avg)
if(avg>=90):
    print("first class")
elif(avg<=90 & avg>=80):
    print("second class")
elif(avg<=80 & avg>=70):
    print("third class")
else:
    print("fail")