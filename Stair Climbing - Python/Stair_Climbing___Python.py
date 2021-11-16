def reco_ways(num):
    '''Calculate number of ways to climb staircase (Iteration)'''

    if (num <= 1):
        return(num)
    return(reco_ways(num-1) + reco_ways(num-2))


def memo_ways(num, known_paths={}):
    '''Fibonacci function, recursion with memoization

    Similar to fib function, however
    this will memorise step paths previosly
    taken so when the same path is encountered
    in the search no need to recalculate
    '''
    if (num<=1):
        return(num)
    if(num not in known_paths):
        known_paths[num] = memo_ways(num-1, known_paths) + memo_ways(num-2, known_paths)
    return known_paths[num]


def main():
    '''Main function that runs program

    Asks for number of steps input from the user,
    and then uses the fibonacci function to return
    the number of possible outcomes to climb the staircase.
    '''

    try:
        while(True):
            num_steps = int(input("Enter number of steps: "))
            if (num_steps <= 0):
                print("Please be sure number of steps is a positive integer")
                main()
            print(f"Number of ways to reach the top (recursion): {reco_ways(num_steps + 1)}")
            print(f"Number of ways to reach the top (recursion w/ memoization): {memo_ways(num_steps + 1)}\n")
    except:
       print("Exception, Please be sure number of steps is a positive integer")
       main()


main()