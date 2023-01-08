list=[]
list1=[]
list2=[]
n = int (input("Enter no of Employees : "))
for emp in range(n):
    emp = emp + 1
    name = input("Enter the name : ")
    age = int(input("Enter the age : "))
    salary = int(input("Enter the salary : "))
    list.append(emp)
    list.append(name)
    list.append(age)
    list.append(salary)
    list1.append(age)
    list2.append(salary)
print(list)
tot=sum(list1)/len(list1)
print("Average age of employee is : ",tot)
print("Highest Salary is : ",max(list2))
print("Lowest Salary is : ", min(list2))


















