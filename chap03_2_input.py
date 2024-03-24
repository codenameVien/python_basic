#o 입력
#Input
#기본 타입 (str)


#에제1
name =input("Enter your name : ")
print(name)
#>>>Enter your name : Kim
#>>>Kim

#예제2
print("FirstName - {0}, LastName - {1}".format(input("Enter first name : "), input("Enter last name : ")))
#>>>Enter first name : ej
#>>>Enter last name : lee
#>>>FirstName - ej, LastName - lee

#형변환 예제
float_number = float(input("Enter a float num : "))
print(type(float_number),float_number)
#>>>Enter a float num : 3.14
#>>><class 'float'> 3.14

