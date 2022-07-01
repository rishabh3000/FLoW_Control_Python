number=int(input("enter number:"))
t=number
rev=0
while t!=0:
    rev=(rev*10)+(t%10)
    t=t//10
if number==rev:
    print("number is palindrome")
else:
    print("number is not palindrome")
