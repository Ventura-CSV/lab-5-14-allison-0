def fibo(N):
    a, b = 0, 1 # initialize first two fibo numbers
    count = 0 # counter to keep track of number of terms generated
    while count < N:
        yield a # yield current fibo number
        a, b = b, a + b # update fibo sequence
        count += 1 # add to counter



def main():
    N = 16
    gen = fibo(N)
    # for v in gen:
    #     print(v, end=' ')
    print(list(gen))


if __name__ == '__main__':
    main()
