def fac(n):
    if n <= 0:
        return 1
    else:
        return fac(n-1) * n


def main():
    for i in range(25):
        print(i, fac(i), ", ")


if __name__ == '__main__':
    main()
