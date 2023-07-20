

# 조건문

# num = int(input('숫자를 입력하세요 : '))

# if num % 2 == 1:
#     print (num,'은 홀수 입니다.')
# else:
#     print (num,'은 짝수 입니다.')



# 반복문 1

# items = ['apple', 'banana', 'coconut']

# for item in items:
#     print(item)

# """
# apple
# banana
# coconut
# """



# 반복문 2

# for i in range(5):
#     print(i)


"""
0
1
2
3
4
"""

# 반복문 3




# [8, 12, 20, -16, 10]



# 중첩된 반복문 1

# outers = ['A', 'B']
# inners = ['c', 'd']

# for outer in outers:
#     for inner in inners:
#         print(outer, inner)

"""
A c
A d
B c
B d

"""

# 중첩된 반복문 2

# elements = [['A', 'B'], ['c', 'd']]

# for elem in elements:
#     print(elem) # 이해 테스트용
#     for item in elem:
#         print(item)
"""
A
B
c
d

"""



# while 반복문

# a = 0

# while a < 3:
#     print(a)
#     a += 1

# print('끝')

# number = int(input('양의 정수를 입력해주세요.: '))

# while number <= 0:
#     if number < 0:
#         print('음수를 입력했습니다.')
#     else:
#         print('0은 양의 정수가 아닙니다.')

#     number = int(input('양의 정수를 입력해주세요.: '))

# print ('잘했습니다!')



# break 예시

# number = int(input('양의 정수를 입력해주세요.: '))

# while number <= 0:
#     if number == -9999:
#         print('프로그램을 종료합니다.')
#         break
#     if number < 0:
#         print('음수를 입력했습니다.')
#     else:
#         print('0은 양의 정수가 아닙니다.')

#     number = int(input('양의 정수를 입력해주세요.: '))

#     print ('잘했습니다!')    



# continue 예시 - 홀수만 출력하기

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for num in numbers:
#     if num % 2 == 0:
#         continue
#     print(num)



# # 일반적인 방법으로 0~9 요소를 가지는 리스트 만들기

# new_list = []
# for i in range(10):
#     if i % 2 == 1:
#         new_list.append(i)
# print(new_list) #[1, 3, 5, 7, 9]

# # list comprehension으로 0~9 요소를 가지는 리스트 만들기

# new_list_2 = [i for i in range(10) if i % 2 == 1]
# print(new_list_2) #[1, 3, 5, 7, 9]



# 리스트를 생성하는 3가지 방법을 비교
# 어떤게 제일 빠른가??
# 정수 1,2,3을 가지는 새로운 리스트 만들기

# numbers = ['1', '2', '3']

# # 1. for loop

# new_numbers = []
# for number in numbers:
#     new_numbers.append(int(number))

# print(new_numbers)

# # 2. map

# new_numbers_2 = list(map(int,numbers))

# print(new_numbers_2)

# # 3. list comprehension

# new_numbers_3 = [int(number) for number in numbers]

# print(new_numbers_3)



# enumerate
# result = ['a', 'b', 'c']

# print(list(enumerate(result)))   #[(0, 'a'), (1, 'b'), (2, 'c')]

# for index, elem in enumerate(result):
#     print(index, elem)
#     """  
#     0 a
#     1 b
#     2 c
#     """

