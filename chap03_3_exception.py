#예외처리 try - except

#복습
#input의 기본 타입은 str

# 예제 1
# try:
#     n= int(input('Enter a number : '))
#     print("Ok. Your number is ",n)
# except ValueError: 
#     print("This is not a number.")

#예제2 -> 올바른 값 입력 완료까지 반복
while True:
    try:
        number = input("Enter a number: ")
        break
    except ValueError:
        print("This is not a number.")

print("Ok. Your number is ", number)
