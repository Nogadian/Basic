'''"\"를 이용해서 문자열 안에 따옴표 표기 가능'''
# print("python\'s favorite food is perl")
# print("\"python is very easy.\" he says.")

''' \n 대신 여러줄 개행하는 방법'''
# multiline = """
# Life is too short
# You need python
# """
# print(multiline)

'''은근히 자주 쓰는 format함수'''
# print("i ate {0} apples. so I was sick for {1} days.".format(10, "three"))
# ''' 변수 명으로 넣어쓰는 것도 씹가능'''
# print("I ate {number} apples. so I was sick for {day} days.".format(number = 10, day = "three"))
# '''이제는 걍 이렇게 씁니다 f 문자열 포매팅. python 3.6 기준임'''
# name = '홍길동'
# age = 30
# print(f"나의 이름은 {name}입니다. 나이는 {age}입니다.")
'''집합(set) 복습'''
# s1 = set("Hello")
# print(s1)

'''replace함수 사용'''
# a = "a#b#c#d"
# print(a.replace("#", ":"))
'''딕셔너리 pop'''
# a = {'A':90, 'B':80, 'C':70}
# print(a.pop('B'))

'''함수 사용시 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?'''
'''매개변수로 *args를 사용하면 됨!'''

def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

print(add_many(1,2,3,4,5,6,7,8,9,10))