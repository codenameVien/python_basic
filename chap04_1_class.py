
#클래스는 설계도, 즉붕어빵틀 & 인스턴스는 코드에서 사용하는 객체, 즉 붕어빵
#  클래스 and 인스턴스의 차이를 이해 
# 클래스는 객체의 설계도 / 인스턴스는 그 설계도를 바탕으로 생성된 실제 객체
# namespace : 객체를 인스턴스화 할때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 하나의 값을 공유
# 인스턴스 변수 : 객체마다 별도 존재 (값들이 전부 다름)

#예제1

class Dog: # 모든 클래스는 object 상속 - Class Dog(object) but 생략가능

    #클래스 속성
    species = 'firstdog'  #클래스 변수 species

    # 인스턴스 변수 name과 age (self가 붙었으면 인스턴스 변수이다)
    #초기화/인스터스 속성 - init 메소드는 class 초기화시 반드시 호출
    def __init__(self, name, age):  #self는 반드시 넘어오고, 클래스를 가지고 사용할 변수와 속성들을 적어줌(name, age)
        self.dn= name #self의 dn에 name 집어넣음 dn을 name이라해도 되고 아무거나 해도 상관읎다
        self.da=age #여기서 dn과 da는 딕셔너리형태의 '키'인데, 아래 네임스페이스 출력시 확인 가능

#클래스 정보 프린트
print(Dog)

# 인스턴스화
a= Dog("kiki",2) # 클래스 이름(init 메소드에서 필요로 했던 name, age)
b = Dog("amy",4)
c= Dog("kiki",2)

#비교
print(a==b, id(a), id(b)) # a에 b를 넣어 값을 같게 해도 주소 id값은 다름 (객체 기준으로 판단)
print("a:", id(a), "c:", id(c)) # id 값이 다름 : 같은 값이 들어있으나 전혀 다른 객체임

# 네임스페이스 namespace : 나만의 공간
print('dog1', a.__dict__)
print('dog2', b.__dict__)


#인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.dn, a.da, b.dn, b.da)) #직접 접근 가능

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.da, a.species))

#하나의 값을 공유 & 직접 접근 가능
print(Dog.species) #클래스로 바로 접근 (
print(a.species) #인스턴스화된 변수로도 접근 가능
print(b.species)
#>>>firstdog



print()
print()
print()


#예제2
#self의 이해

class SelfTest:
    def func1(): # 클래스내의 매개변수가 없는 함수는 클래스메소드
        print('Funcs1 called')
    def func2(self):
        print(id(self)) # f의 id와 같음
        print("Func2 called")
    # 여기네 init 메소드가 없는 이유는 기본 self만 사용할 것이기 떄문에. 위 예제1은 name과 age라는 다른 인스턴스 변수들이 있었기에 init 사용

f= SelfTest()

#f.func1() # 예외 *에러 / 래스메소드이기 떄문에 이렇게 그냥 호출 불가, 반드시 클래스의 함수이다는 것을 적어줘야함
SelfTest.func1() #SelfTest 클래스의 func1함수 호출 (클래스로 직접 호출)

f.func2() #인스턴스화 시켜서 호출 가능!!!!
print(id(f))
#SelfTest.func2() # 예외 / 매개변수를 요구하지만 매개변수를 적어주지 않아서 오류남
SelfTest.func2(f)

print()
print()

#예제3
# 클래스 변수, 인스턴스 변수
class Warehouse: #창고..
    # 클래스 변수
    stock_num = 0 #재고

    def __init__(self,name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1 #재고를 1 더함
    
    def __del__(self): # 객체 소멸시 자동 호출 함수
        Warehouse.stock_num -= 1 #재고를 1 빼줌

#인스턴스화
user1= Warehouse('Lee')
user2= Warehouse('Cho')

print(Warehouse.stock_num)
print()
#Warehouse.stock_num = 0.0094
print(user1.name)
print(user2.name)
print(user1.__dict__) #user1의 namespace에 접근해보기 Lee만 나오는데
print(user2.__dict__)
print('before', Warehouse.__dict__)
print('>>>', user1.stock_num) #여기서는 또 2가 나오는게 위에 dict에서는 모두 공유하지만 굳이 써줄 필요가 없기 때문제 적이 않은것.. dict해서 나오는 건 위에서 인스턴스화 시킨 정보뿐
                              # 이렇게 user1의 stock_num을 출력하라는데 없으면 얘가 알아서 namespace에 들어가서 찾아서 들고나옴

print()
del user1
print('after', Warehouse.__dict__) #stock_num이 -1 당해서 1로 바뀌어 있음!!

print()
print()

#예재4
class Dog:

    #클래스 속성 ( ex. 자동차의 색상, 종류 등)
    species = 'first dog'

    #초기화/인스턴스 속성
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    #메소드 (ex. 자동차의 전진 후진, 좌회전 등)
    def info(self): #강아지의 정보를 보여주는 메소드
        return '{} is {} years old'.format(self.name, self.age)
    
    def speak(self, sound): #speak호출시 sound 입력받음
        return"{} says {}!".format(self.name,sound)
    

# 인스턴스 생성
c = Dog('july', 4)
d = Dog("Mary", 10)
#메소드 호출
print(c.info())
#메소드 호출
print(c.speak('Wal Wal')) #Wal Wal을 speak에 넘겨줌
print(d.speak('Mung Mung'))

