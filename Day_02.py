# 1.Python Program to Check if a Number is Odd or Even

def even_odd(num): 
  if num%2 == 0:
    print("Number Is Even")
  else : 
    print("Number Is Odd")
    
even_odd(45)
even_odd(90)

# 2.Python Program to Check Leap Year

def leap_year(year): 
  if year % 4 == 0: 
    print("Year Is Leap")
  else: 
    print("Year Is Not Leap")
    
leap_year(2016)
leap_year(2021)

# 3.Python Program to Find the Largest Among Three Numbers

def large_num(num1,num2,num3): 
  if num1 > num2 and num1 > num3: 
    print(f"{num1} is Greater")
  elif num2 > num1 and num2 > num3: 
    print(f"{num2} is Greater")
  else: 
    print(f"{num3} is Greater")
    
large_num(3,4,-5)

# OR 

lst = [34,58,18,78,99]
let_max = lst[0]

for i in lst : 
  maxi = lst[0]
  if i >= maxi : 
    maxi = i
    
print(maxi)
