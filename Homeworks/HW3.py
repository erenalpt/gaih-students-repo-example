def prime_first(num):
    if num<501:
        if not num<2:
            for i in range(2, num):
                if num%i == 0:
                    break
            else:
                print(num)


def prime_second(num):
    if num>500 and num <1001:
        if not num<2:
            for i in range(2, num):
                if num%i == 0:
                    break
            else:
                print(num)
        

for i in range(1,1000):
    prime_first(i)
    prime_second(i)
