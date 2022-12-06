# locals()는 로컬 심볼 테이블 딕셔너리를 가져오는 메소드로 업데이트 또한 가능하다.
import pprint

x = 100
y = [1, 3, '1']
y.append(3)
pprint.pprint(locals())