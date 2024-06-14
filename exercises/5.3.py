def check_fermat(a, b, c, n):
    if a ** n + b ** n == c ** n:
        print "Fermat was wrong!"
    else:
        print "No, that doesn't work."
        
a = int(raw_input("Please enter a value for 'a'..."))
b = int(raw_input("Please enter a value for 'b'..."))
c = int(raw_input("Please enter a value for 'c'..."))
n = int(raw_input("Please enter a value for 'n'..."))

check_fermat(a, b, c, n)
