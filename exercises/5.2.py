def do_n(f, n):
    if n <= 0:
        return
    f()
    do_n(f, n-1)
    
def test_function():
    print "testing me testeree do daa"
    
do_n(test_function, 5)