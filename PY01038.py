
if __name__ == '__main__':
    for i in range(int(input())):
        s = input()
        if int(s) % 7 == 0:
            print(s)
        else:
            sum = 0
            ok = 0
            for i in range(1000):
                sum = int(s)+int(s[::-1])
                if sum % 7 == 0:
                    ok = 1
                    print(sum)
                    break
                s = str(sum)

            if ok == 0:
                print(-1)
