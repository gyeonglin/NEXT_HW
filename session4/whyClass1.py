naver = {
    "name" : "Naver",
    "location" : "경기도 성남시 분당구",
    "salary" : 5000,
    "employee" : 3978,
}

coupang = {
    "name" : "Coupang",
    "location" : "서울특별시 송파구 송파대로",
    "salary" : 6000,
    "employee" : 49915,
}

def naver_hire():
    naver["salary"] += 500
    naver["employee"] += 1000

def coupang_hire():
    coupang["salary"] += 500
    coupang["employee"] += 1000

# 결과
print(naver)
print(coupang)
naver_hire()
coupang_hire()
print('-----상반기 공채 진행-----')
print(naver)
print(coupang)