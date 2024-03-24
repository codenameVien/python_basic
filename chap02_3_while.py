#while문

#if문과 사용 방법이 똑같음


n=5
while n>0:
    print(n)
    n=n-1
    

print()


a= ['A','B','C']
while a:
    print(a.pop(-1)) # a List 맨뒤에서부터 하나씩 뺴면서 False가 될(List가 텅텅 빌)때까지 반복 
                     # (False가 된다면 반복 종료,, a, 즉 차있는 List는 True 상태임)
    
print()


#break와 continue
n=5
while n>0:
    n-=1
    if n==2:
        break
    print(n)
print("Loop Ended")

print()

m=5
while m>0:
    m-=1
    if m==2:
        continue
    print(m)
print("Loop Ended")

print()

#if문 중첩
i=1

while i<=10:
    print('i:', i)
    if i ==6:
        break
    i+=1

print()

#While-else 구문
n=10
while n>0:
    n-=1
    print(n)
    #if n==5:
    #    break
else:
    print('else out.')

print()
print()

a=['A','B','C']
s= 'D'

while i<len(a): # i가 4미만일 때 실행
    if a[i] ==s:
        break
    i+=1
else:
    print(s,'not found in list')

print()
print()

a=['A','B','C']

while True:
    if not a: #즉 False, a가 비어있을때
        break #무한루프를 방지하기 위한 작업
    print(a.pop())