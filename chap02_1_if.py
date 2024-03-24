#if문
##조건식 (True/ False)

if True:
    print('Good')
if 'a':
    print('Good')

# False 이기에 출력이 되지 않음!!!!!!
if False:
    print('Bad')
else:
    print('Good') #얜 트루이므로 실행됨!!

print()


x= 15
y=10
print(x==y)
print(x!=y)

print()

city = "" # 빈값이므로 False -> else 문 실행
if city: 
    print("You are in : ", city)
else: 
    print("Enter your city")


city = "Seoul" #값이 채워져 있으므로 True 이므로 if 문 실행
if city: 
    print("You are in : ", city)
else: 
    print("Enter your city")

print()
print()


# 반대로 출력해주는 not
a =75
b = 40
print(not a>b) #
#>>> False

print()
print() 


#뽁습!!
q= {10,20,30}
w= {70,80,90,100}
e= {"name" : "Lee", "city": "Seoul", "grade": "A"}
r= {10,12,14}

print(15 in q)
print(90 in w)
print(12 not in r) 
print("name" in e) # 키는 그냥 써주면 된다 
print("Seoul" in e.values()) # 해당'값'이 존재하는가 
                             ## '값'이 있는지 확인하려면 반드시 values 써야함
