def fibonacci(n): 
    #check for edge cases
    if isinstance(n, int) == False: 
        print("ERROR")
        return("Error")
    #declare variables
    a = 0
    b = 1
    x = range(n+1)
    # if statements for 0 & 1 edge cases (o(1))
    if n == 0: 
        return(a)
    elif n == 1:
        return (b)
    else:
    # Loop through math & get the desired digit in the fib seq
        for i in x:
            if i != (n-2): 
                c = a + b
                a = b
                b = c
                continue
            else:
                c = a + b
                print(c)
                return c
                

def lucas(n): 
    #check for edge cases
    if isinstance(n, int) == False: 
        return("Error")
        #isinstance(object, classinfo)
    #declare variables
    a = 2
    b = 1
    x = range(n+1)
    # if statements for 0 & 1 edge cases (o(1))
    if n == 0: 
        return(a)
    elif n == 1:
        return (b)
    else:
    # Loop through math & get the desired digit in the fib seq
        for i in x:
            if i != (n-2): 
                c = a + b
                a = b
                b = c
                continue
            else:
                c = a + b
                print(c)
                return(c)

def sum_series(n, a=0, b=1):
        #check for edge cases
    if isinstance(n, int) == False: 
        print("ERROR")
        return("Error")
    x = range(n+1)
    # if statements for 0 & 1 edge cases (o(1))
    if n == 0: 
        return(a)
    elif n == 1:
        return (b)
    else:
    # Loop through math & get the desired digit in the fib seq
        for i in x:
            if i != (n-2): 
                c = a + b
                a = b
                b = c
                continue
            else:
                c = a + b
                print(c)
                return c

fibonacci(8)
lucas(8)
sum_series(8)
sum_series(5, 6, 7)