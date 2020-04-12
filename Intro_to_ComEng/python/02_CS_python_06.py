'''
calculator 모듈을 만들려 하면,
class calculator 에 여러 함수를 저장한 다음
그 파일을 calculator.py 로 저장하기만 하면 된다.
이후 모두 다 쓸때는
import calculator을 쓴 뒤 쓰고
일부만 쓸 때는
from calculator import 함수이름 이라고 써주고 쓴다.
'''

import calculator

# . 은 calculator module 안의 것을 쓴다는 것을 말한다.
print(calculator.plus(10, 5))
print(calculator.minus(10, 5))
print(calculator.multiply(10, 5))
print(calculator.divide(10, 5))
