# # def calcnum(n):
# #     initial = 1
# #     for i in range(1, n):
# #         initial = initial + i + 1
# #     return initial
# def cal(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum += i
#     return sum


# def print_pattern(n):
#     ch = chr(64 + cal(n))
#     for i in range(1, n + 1):
#         for j in range(1, n + 2 - i):
#             print(ch, end=" ")
#             ch = chr(ord(ch) - 1)
#         print()

# def main():
#     n = int(input())
#     print_pattern(n)

# if __name__ == "__main__":
#     main()




# rows = 5
# for i in range(rows):
#     if i <= 2:
#         print(' ' * (2 - i) + '*' * (2 * i + 1))
#     else:
#         print(' ' * (i - 2) + '*' * (2 * (4 - i) + 1))


rows = 6
mid = rows // 2

for i in range(rows):
    if i <= mid:
        stars = 2 * i + 1
    else:
        stars = 2 * (rows - i - 1) + 1
    spaces = (2 * mid + 1 - stars) // 2
    print(' ' * spaces + '*' * stars)
