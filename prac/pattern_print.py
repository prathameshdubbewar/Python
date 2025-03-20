# def calcnum(n):
#     initial = 1
#     for i in range(1, n):
#         initial = initial + i + 1
#     return initial
def cal(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum


def print_pattern(n):
    ch = chr(64 + cal(n))
    for i in range(1, n + 1):
        for j in range(1, n + 2 - i):
            print(ch, end=" ")
            ch = chr(ord(ch) - 1)
        print()

def main():
    n = int(input())
    print_pattern(n)

if __name__ == "__main__":
    main()

