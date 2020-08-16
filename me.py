class check:
    def chechme(numcheck):
        if numcheck % 2 == 0:
            print('this is an even number')
        else:
            print('this is an odd number')
        return 0

num1 = int(input('enter a number to check'))
check.chechme(num1)
