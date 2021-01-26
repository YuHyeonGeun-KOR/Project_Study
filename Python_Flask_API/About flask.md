# Flask 기초다지기  

## 웹 프레임워크 

- 웹 프레임워크는 우리가 웹 어플리케이션을 만들고자 할 때 필요한 설정이나 기능들을 보다 쉽고 간편하게 다룰 수 있도록 해준다.
- 파이썬을 기반으로 하는 웹 프레임워크  : Flask , Django 
<br><br>

# Flask 설치

>pip install flask

위의 명령어를 terminal에 입력하여 falsk를 설치한다. 

입력한 결과 이미 설치가 되어있었기에 버전만 업데이트 해주기로 하였다.  

![](\img\1.png)

# Flask 패키지 이해하기

![](\img\2.png)

위의 코드는 Hello World 라는 문구를 출력하는 웹페이지를 완성한 모습이다.  
위의 코드를 한줄씩 이해해보기로 하였다.

1. from flask import Flask  
- 위에서 설치한 flask라는 패키지를 가져와서 사용하겠다는 의미이다.<br><br>  
2. app = Flask(__name__)  
- flask를 실행하는 의미이다.
- app이라는 변수에 flask 프로젝트를 초기화 시켜서 실행한다.
<br><br>  

3. @app.route('/')  
- 위에서 생성한 app에 대하여 route, 즉 경로를 설정한다.  

4. if __name__ == '__main__':
    app.run()  
- 설정한 경로에서 사용자가 요청을 보냈을 때 실행된다.



