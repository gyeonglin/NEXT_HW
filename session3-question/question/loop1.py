# 문제1. for문을 활용해서 1부터 10까지 숫자를 출력해주세요.
for i in range(1,11) :
    print(i)

# 문제2. for문을 활용해서 1부터 10까지 숫자 중 3의 배수는 제외하고 출력해주세요. (단, continue이용)
for i in range(1, 11) :
    if i % 3 == 0 :
        continue
    print(i)