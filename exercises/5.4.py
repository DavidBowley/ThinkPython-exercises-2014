def is_triangle(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        return False
    else:
        return True
        
print "This program checks to see if 3 lines can form a triangle. If one line is greater than the sum of the other two lines then a triangle cannot be formed."
a = int(raw_input("Please enter the value of the first line..."))
b = int(raw_input("Please enter the value of the second line..."))
c = int(raw_input("Please enter the value of the third line..."))

result = is_triangle(a, b, c)

if result == False:
    print "These lines are unable to form a triangle."
else:
    print "These lines are capable of forming a triangle."