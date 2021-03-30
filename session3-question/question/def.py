#입력받은 문자열의 역순을 출력하는 함수를 작성하세요.
#ex) python -> nohtyp

def reverse_string(a) :
    length = len(a)    
    for i in range(length) :
        print(a[length-1-i], end="")


reverse_string("happy")
