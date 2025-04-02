# a=10
# b=20

# # a=a+b #30
# # b= a-b #10
# # a= a-b


# a,b = b,a
# print(f"a:{a} \nb:{b}")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_nums = [x for x in nums if(lambda x: x%2==0)(x)]
is_even = lambda x: x % 2 == 0
even_nums = [num for num in nums if is_even(num)]
print(even_nums)  # Output: [2, 4, 6, 8]
