# 띄어쓰기, 들여쓰기 꼭 확인하세요!

list1 = ["갈비탕", "비빔밥", "냉면"]
list2 = ["짜장", "짬뽕", "꿔바로우", "깐풍기"]
list3 = ["파스타", "스테이크", "감바스"]

food = input("음식을 입력해주세요: ")

# 여기서부터 음식이 한식, 중식, 양식 중 어느 곳에 속하는지 판단하는 코드를 작성해주세요. 단, 조건식으로 list1, list2, list3에 포함되는지 여부를 이용하셔야 합니다!

if food in list1:
    print("한식")
elif food in list2:
    print("중식")
elif food in list3:
    print("양식")
else :
    print("몰라요")