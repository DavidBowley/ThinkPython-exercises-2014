def compare(x, y):
    if x == y:
        return 0
    if x < y:
        return -1
    if x > y:
        return 1

print "Enter two numbers to compare..."
x = int(raw_input("X?"))
y = int(raw_input("Y?"))

print compare(x, y)
