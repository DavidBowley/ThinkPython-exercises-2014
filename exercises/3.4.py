def print_anything(text_to_print):
    print text_to_print
    
def do_twice(f, test_value):
    f(test_value)
    f(test_value)
    
def print_twice(string_to_print):
    print string_to_print
    print string_to_print
    
def do_four(f, test_value):
    do_twice(f, test_value)
    do_twice(f, test_value)
    
def do_four_no_arguments(f):
    f()
    f()
    f()
    f()
    
def grid_edge():
    print "+ - - - - + - - - - +"
    
def grid_middle():
    print "|         |         |"

def grid_edge_multi(columns):
    for i in range(0,columns):
        print "+ - - - -",
    print "+"
    
def grid_middle_multi(columns):
    for i in range(0, columns):
        print "|        ",
    print "|"

def grid_row(rows):
    for i in range(0, rows):
        print "test"
        
def grid_column(column):
    grid_edge_multi(column)    
    do_four(grid_middle_multi, column)

def full_grid(columns, rows):
    for i in range(0, rows):
        grid_column(columns)
    grid_edge_multi(columns)
    
full_grid(4, 8)
    
# grid_edge()
# do_four_no_arguments(grid_middle)
# grid_edge()
# do_four_no_arguments(grid_middle)
# grid_edge()