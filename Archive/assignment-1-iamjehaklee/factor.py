factor_list = []

def factor(n):
    for i in range(2,n+1):
        while n % i == 0:
            factor_list.append(i)
            n = n / i
    print('The factors are:', factor_list)
