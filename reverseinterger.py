x = int(input("Enter the interger to reverse"))
rev_num = 0 

while x != 0: 
    digit = x % 10
    rev_num = rev_num * 10 + digit
    x //= 10
    

print(rev_num)
  
