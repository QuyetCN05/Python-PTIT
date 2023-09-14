
if __name__ == '__main__':
    for i in range(int(input())):
        s = input()
        a = list(s)
        str = ''
        for i in range(len(a)):
            if a[i].isdigit():
                str += a[i-1]*int(a[i])
        print(str)
