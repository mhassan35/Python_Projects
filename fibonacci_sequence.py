user_input = int(input("Enter number: "))

a,b = 0,1

for _ in range(user_input): 
  print(a , end = "")
  a , b = b , a + b