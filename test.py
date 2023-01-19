def test(a,b,*args,**kwargs):
    print(a+b)
    print(args) # 빈 튜플 출력
    print(kwargs) # 빈 딕셔너리 출력

test(10,30)
# test()
# test(b=50)


# print() # 가변인자가 들어온다


test(10,20,30,40,50) # 30 부터는 튜플로 args에 들어간다

 
test(10,20,30,40,50,pk=123) # 변수명과 함께 넣은 data는 kwargs에 들어간다


# post 함수를 장고가 알아서 호출해줌. 어떤 값이 들어올지 예측할수 없음. 안전장치를 만들어준 것임. 만약 안 쓰면 에러나니까