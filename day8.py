import matplotlib.pyplot as plt

# problem 1
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [15000, 18000, 17000, 22000, 25000, 30000]
plt.plot(months,sales,color="green",linestyle="--",marker="o")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.show()

#problem 2
departments = ["IT", "HR", "Finance", "Marketing"]
employees = [25, 15, 20, 10]
plt.bar(departments,employees,color="blue")
plt.xlabel("Employees")
plt.ylabel("Departments")
plt.title("Employees in Departments")
plt.show()

#problem 3
expenses = [40, 30, 20, 10]
labels = ["Salary", "Rent", "Marketing", "Misc"]
plt.pie(expenses,labels=labels,autopct="%1.1f%%")
plt.title("Expenses")
plt.show()

#problem 4
salary = [
42000,52000,65000,71000]
plt.hist(salary,bins=5)
plt.title("Salary")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

#problem 5
experience = [1,2,3,4,5,6,7,8,9,10]
salary = [25000,30000,36000,42000,50000,58000,65000,72000,80000,90000]
plt.scatter(experience, salary, color="red")
plt.plot(experience, salary, color="blue")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Experience vs Salary")
plt.show()