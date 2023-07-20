

# 2217. hw_4_2

# # 보유 중인 도서 리스트
# list_of_book = ['장화홍련전','가락국 신화','온달 설화','금오신화','이생규장전','만복자서포기','수성지','백호집','원생몽유록','홍길동전','장생전','도문대작','옥루몽','옥련몽']

# # 대여 예정 도서 리스트
# rental_book = ['장생전','원생몽유록','이생규장전','장화홍련전','수성지','백호집','난중일기','홍길동전','만복자서포기']


# box = len(rental_book)
# for i in range(len(rental_book)):
#     if rental_book[i] not in list_of_book:
#         print(rental_book[i],'은/는 보유하고 있지 않습니다.')
#         break
#     elif rental_book[i] in list_of_book:
#         box -= 1
#         if box == 0:
#             print('모든 도서가 대여 가능한 상태입니다.')
#     else:
#        continue



# 2217. hw_4_4

# # 보유 중인 도서 리스트
# list_of_book = ['장화홍련전','가락국 신화','온달 설화','금오신화','이생규장전','만복자서포기','수성지','백호집','원생몽유록','홍길동전','장생전','도문대작','옥루몽','옥련몽']

# # 대여 예정 도서 리스트
# rental_book = ['장생전','위대한 개츠비', '원생몽유록','이생규장전', '데미안', '장화홍련전','수성지','백호집','난중일기','홍길동전','만복자서포기']
# missing_book = [rental_book[i] for i in range(len(rental_book)) if rental_book[i] not in list_of_book]

# if len(missing_book) == 0:
#         print('모든 도서가 대여 가능한 상태입니다.')

# for j in range(len(missing_book)):
#     print(missing_book[j] , '을/를 보충하여야 합니다.')



# 1687. ws_4_1 

# import requests
# from pprint import pprint as print

# # 무작위 유저 정보 요청 경로
# API_URL = 'https://jsonplaceholder.typicode.com/users/1'
# # API 요청
# response = requests.get(API_URL)
# # JSON -> dict 데이터 변환
# parsed_data = response.json()

# # 응답 데이터 출력
# print(response)

# # 변환 데이터 출력
# print(parsed_data)
# # 변환 데이터의 타입
# print(type(parsed_data))

# # 특정 데이터 출력
# print(parsed_data['name'])
# print(parsed_data['username'])
# print(parsed_data['company']['name'])



#1688. ws_4_2

import requests
from pprint import pprint as print


API_URL = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(API_URL)
parsed_data = response.json()



print(parsed_data[0])

#1689. ws_4_3


#1690. ws_4_4


#1691. ws_4_5