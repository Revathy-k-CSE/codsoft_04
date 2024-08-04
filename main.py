def add(n1,n2):
  return n1 + n2
def subtract(n1,n2):
  return n1 - n2
def multiply(n1,n2):
  return n1 * n2
def divide(n1,n2):
  return n1 / n2
print("select the required operation:\n" \
      "1. ADD\n" \
      "2. SUBTRACT\n" \
      "3. MULTIPLY\n" \
      "4. DIVIDE\n")
select=int(input("Select your operation form 1,2,3,4:"))
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
if select==1:
    print(n1, "+", n2, "=", add(n1,n2))
elif select==2:
    print(n1, "-", n2, "=", subtract(n1,n2))
elif select==3:
    print(n1,"*", n2, "=", multiply(n1,n2))
elif select==4:
    print(n1,"/", n2, "=", divide(n1,n2))
else:
    print("Invalid operation")