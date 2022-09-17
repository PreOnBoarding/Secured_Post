# Secured_Post

비밀번호를 이용한 게시글 서비스
<br>
<br>

## MVP Service
유저가 이모지, 비밀번호를 포함한 게시글을 작성하는 서비스로 아래와 같은 기능을 제공한다.

- 유저 : 구현하지 않음 ( 분석된 요구사항에서 필요로 하지 않음 )
- 게시글
    - **R**ead : All
    - **C**reate : All (이모지, 작성하는 게시글의 비밀번호 포함하여 작성한다.)
        - 이모지 적용 방법 : (제목, 내용에)정규표현식을 적용
    - **U**pdate : C에서 입력한 비밀번호를 통과해야만 가능
    - **D**elete : C에서 입력한 비밀번호를 통과해야만 가능
<br>

## 💻 기술 스택

<div style='flex'>
<img src="https://img.shields.io/badge/Python3.9.5-3776AB?style=for-the-badge&logo=Python&logoColor=white" >
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">
<img src="https://img.shields.io/badge/Django REST framework-092E20?style=for-the-badge&logo=Django REST framework&logoColor=white">
</div>
<br>
<br>

## 👉 ERD

<img width="500" src="https://user-images.githubusercontent.com/101394490/188778444-95b9ce69-697b-4d75-bab7-2880f605a994.png" />
<br>

## 🙏 API 명세서

### [API 링크](https://www.notion.so/617c8233819e4cc58a47979f609ac178) 

### **API 이미지 (예시)**
 <img width="785" src="https://user-images.githubusercontent.com/101394490/188778870-c50b268f-013e-4bdc-b1b2-87aae520afc8.png" />

<details>
<summary>API 상세보기 이미지</summary> <br>
<div markdown="1">
 <img width="500" src="https://user-images.githubusercontent.com/101394490/188778490-1ad715ab-cad5-48cd-ae29-1e15da7d2498.png" />
</div>
</details>
<br>

## 📌 컨벤션

### ❓ Commit Message

- feat/ : 새로운 기능 추가/수정/삭제
- enhan/ : 기존 코드에 기능을 추가하거나 기능을 강화할 때
- refac/ : 코드 리팩토링,버그 수정
- test/ : 테스트 코드/기능 추가
- edit/ : 파일을 수정한 경우(파일위치변경, 파일이름 변경, 삭제)

### ❓ Naming

- Class : Pascal
- Variable : Snake
- Function : Snake
- Constant : Pascal + Snake

### ❓ 주석

- Docstring을 활용하여 클래스와 함수단위에 설명을 적어주도록 하자.
- input/output을 명시하여 문서 없이 코드만으로 어떠한 결과가 나오는지 알 수 있도록 하자.

### 🚷 벼락치기의 규칙

- 컨벤션 지키기
- Commit 단위 지키기
- 말 이쁘게하기
- 문제를 마주하여 트러블을 겪었다면, 어떻게 해결을 했는지 공유를 해주기
- 각자의 작업을 미리 작성을 하여서 각자의 작업을 공유하기
<br>

## 💻 트러블슈팅
- 문제1
    - User에서만 password 세팅을 하다보니 set_password 말고 어떻게 적용을 해야할지 몰랐음
    - set_password와 유사한 make_password를 이용해 해쉬화에 성공
    - But 같은 문자열이더라도 hash화가 되어있는 문자열과, 새로 해쉬한 문자는 다른값을 내뱉기에 체크에 어려움을 겪음
- 해결1
    - django의 내장함수인 check_password를 사용
    - check_password (기본 문자열, 해쉬된 기본문자열)를 사용하여서 해쉬된 비밀번호의 일치 여부를 알게 되었음
    
- 문제2
    - 게시물을 생성할 때에는 Serializer를 사용하여 진행함
    - 비밀번호 valid 검증을 위한 validation 함수를 생성
    - Create때는 정상작동을 하지만, Update와 Delete시에는 Validation 함수를 통과하지 못하는 문제 발생
- 해결2
    - Create에는 그대로 validaion이 적용된 Serializer를 사용
    - Update와 Delete시에는 같은 모델을 사용하지만, Validation이 없는 새로운 Serializer를 만들어서 사용
    - 같은 기능을 사용하지만, 비밀번호 정규식을 체크하냐 안하냐로 구분하여서 분리사용을 하였음

## 추후에 서비스 개선을 하고자 한다면

- 미처 검증하지 못한 Service와 API에 대한 Unit Test 코드 진행
- 아직 발견하지 못한 Error들을 적용하여 예외처리 구체화

- User기능을 만들어서 자신의 게시글을 찾을 수 있도록 구현
- 게시글을 찾았다면, 해당 게시글의 비밀번호를 재설정 할 수 있도록 추가 구현

- 관리자 계정을 추가로 구현하여 게시글 서비스가 원할하게 이용이 될 수 있도록 구현
