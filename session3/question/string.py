# 띄어쓰기, 들여쓰기 꼭 확인하세요!

# answer와 같은 형태가 되도록 string1, string2, string3를 수정하고 조합해주세요!
answer = "3/29은 NEXT 세션하는 날!"

string1 = "2021-03-29은 "
string2 = "next"
string3 = "      세션하는 날!       "

string = string1[6:].replace('-', '/')+string2.upper()+' ' + string3.strip()

if answer == string:
    print("정답입니다!")
else:
    print("틀렸습니다.")
    print(f"정답 : {answer}")
    print(f'입력값 : {string}')



