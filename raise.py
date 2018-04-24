# Raise
#  사용자가 직접 에러를 발생 시키는 기능
# 많이 사용하면 코드가 읽기 어려워진다. 필요한 곳에만 사용하자
# def rsp(mine,yours):
#     allowed = ['가위','바위','보']
#     if mine not in allowed:
#         raise ValueError
#     if yours not in allowed:
#         raise ValueError

# try:
#     rsp('가위','야')
# except ValueError:
#     print('잘못 된 값 입력')

# # 각 반에 190 넘는 아이 찾기
# school = {'1반': [172,188,174,167,198,150],'2반':[146,168,185,168,197,186]}
# try:
#     for class_number, students in school.items():
#         for student in students:
#             if student>190:
#                 print(class_number,'반에 190 넘는 학생 있다')
#                 raise StopIteration
# except StopIteration:
#     print('2반은 검색 안함')

shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}
try:
    for shop, products in shops.items():
        for product, price in products.items():
    	    if product == '풀':
                raise StopIteration
except StopIteration:
	print("{}: {}원".format(shop, price))
