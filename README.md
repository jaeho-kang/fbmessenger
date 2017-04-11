# fbmessenger<br>
페이스북 챗봇 
version 0.1

참조 git 
https://github.com/hult/facebook-chatbot-python
https://github.com/davidchua/pymessenger

설정
./config/config.json 수정

설정값 

|메인키|서브키|의미|
|---|---|---|
|SSL|crt|crt파일 경로, server/enc/ 경로에 직접 복사하거나 링크를 걸어둠|
|SSL|key|ssl key 파일 경로, server/enc/ 경로에 직접 복사하거나 링크를 걸어둠|
|FB_TOKEN|ACCESS_TOKEN|페이스북 개발자페이지, 어플 설정의 메신저 설정에 나오는 페이지 액세스 코드,시스템에 의해서 주어진 코드|
|FB_TOKEN|VERIFY_TOKEN|페이스북 개발자페이지, 어플 설정의 webhook 설정시 콜백 url 설정 창에서 나오는 확인 토큰, 사용자가 정의|


실행 방법 
<code>$/foo/fbmessenger/pytyhon3 ./server/server.py</code>

실행 환경 
python3 
SSL (콜백 url이 주어졌을때 https를 제공하기 위한 root ca 인증 필요)
Facebook graph 2.6 api 사용 

dependency 
konlpy(한국어 형태소분석기)
requirements.txt 참조

Release Note
0.1
facebook 연동
한국어 형태소 분석기 연동 

