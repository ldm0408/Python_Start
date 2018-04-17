def random_rsp():
    import random
    return random.choice(['가위','바위','보'])


paper = '보'
scisors = '가위'
rock ='바위'

"""모듈 만들기
사용할 함수, 메소드 코드를 작성한 모듈 파일을 생성
모듈이 쓰일 파일에 import를 사용하여 모듈을 호출
사용 방법은 기존의 모듈과 동일
주의할 점은 사용자가 만든 모듈과 모듈을 쓸 파일이 같은 폴더에 있어야 한다.
"""