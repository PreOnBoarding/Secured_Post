# Secured_Post

비밀번호를 사용하여 비밀 게시글 작성 서비스
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
<br>

## 기술 스택

<div style='flex'>
<img src="https://img.shields.io/badge/Python3.9.0-3776AB?style=for-the-badge&logo=Python&logoColor=white" >
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">
<img src="https://img.shields.io/badge/Django REST framework-092E20?style=for-the-badge&logo=Django REST framework&logoColor=white">
</div>
<br>
<br>

## ERD

<img width="500" src="https://user-images.githubusercontent.com/101394490/188778444-95b9ce69-697b-4d75-bab7-2880f605a994.png" />
<br>
<br>

## API 명세서

 <img width="785" src="https://user-images.githubusercontent.com/101394490/188778870-c50b268f-013e-4bdc-b1b2-87aae520afc8.png" />

<details>
<summary>&nbsp; API 상세보기 : 게시글 조회</summary> <br>
<div markdown="1">
<img width="500" src="https://user-images.githubusercontent.com/104303285/190635411-6cf8772e-532a-4e6c-868e-50777854f068.png" />
</div>
</details>
<details>
<summary>&nbsp; API 상세보기 : 게시글 작성</summary> <br>
<div markdown="1">
<img width="500" src="https://user-images.githubusercontent.com/104303285/190635389-50985e0a-a760-4015-99b9-d9bb1a49bf5c.png" />
</div>
</details>
<details>
<summary>&nbsp; API 상세보기 : 게시글 수정</summary> <br>
<div markdown="1">
<img width="500" src="https://user-images.githubusercontent.com/104303285/190635406-998a549e-daff-43b6-9ef3-a2adde09e281.png" />
</div>
</details>
<details>
<summary>&nbsp; API 상세보기 : 게시글 삭제</summary> <br>
<div markdown="1">
<img width="500" src="https://user-images.githubusercontent.com/104303285/190635413-9de019bd-6914-41b0-a852-ecf34e05c06f.png" />
</div>
</details>
<br>

## 컨벤션

### Commit Message

- feat/ : 새로운 기능 추가/수정/삭제
- enhan/ : 기존 코드에 기능을 추가하거나 기능을 강화할 때
- refac/ : 코드 리팩토링,버그 수정
- test/ : 테스트 코드/기능 추가
- edit/ : 파일을 수정한 경우(파일위치변경, 파일이름 변경, 삭제)

### Naming

- Class : Pascal
- Variable : Snake
- Function : Snake
- Constant : Pascal + Snake

### 주석

- Docstring을 활용하여 클래스와 함수단위에 설명을 적어주도록 하자.
- input/output을 명시하여 문서 없이 코드만으로 어떠한 결과가 나오는지 알 수 있도록 하자.

### 벼락치기의 규칙

- 컨벤션 지키기
- Commit 단위 지키기
- 말 이쁘게하기
- 문제를 마주하여 트러블을 겪었다면, 어떻게 해결을 했는지 공유를 해주기
- 각자의 작업을 미리 작성을 하여서 각자의 작업을 공유하기
<br>
<br>

## 트러블슈팅
<br>
<details>
<summary>&nbsp; 1. 게시글의 해시화된 비밀번호를 생성함 </summary><br>

- 상황 : 비밀번호 생성시 `set_password`를 사용했었으나 상속받을 모델이 없기 때문에 사용할 수 없었음
- 해결 : 찾아보니 Django 내장 함수 중 같은 역할을 하는 `make_password`를 알게 되어 `import` 후 함수를 사용함

</details>
<img width="650" src="https://user-images.githubusercontent.com/104303285/188866809-a3213550-21d9-4c09-a33d-28aaf01f487e.png" />

<br>
<details>
<summary>&nbsp; 2. 예외처리를 필드별로 나타냄</summary><br>

- 상황 : validation에서의 에러메세지를 각각 설정해주어 입력값이 틀렸을 경우 각각의 필드별로 메세지를 띄우고 싶었음
- 해결 : 처음에 validate함수에서 각 필드에 대한 값과 메세지를 지정해주었으나, Django에서 validation의 값(key, value)을 받을 수 있다는 것을 확인하여 `join`문과 `keys()`를 사용하여 ValidationError 처리를 함

</details>
<img width="650" src="https://user-images.githubusercontent.com/104303285/188866842-4eaba61e-c8ef-471a-872b-46dffe79816c.png" />


<br>
<details>
<summary>&nbsp; 3. Pagination 구현</summary><br>

- 상황 : 이전에 페이지네이션 구현시 `request.query_params.get('page', '1')`을 사용하였고, 총 개수와 보여주고 싶은 개수를 계산하는 함수를 작성한 경험이 있어 다른 방식으로 진행해보고자 함 
- 설명 : 추가 로드를 20개 단위
    - `first_index`값이 전체 게시글의 길이보다 작거나
페이지가 0보다 작을때 빈 값(쿼리셋)을 도출함
    - page값이 3이 될 경우, (fist)3*20=60, (end)60+20=80 으로 첫 시작이 0보다 큼으로 `[60:80]`을 사용해 데이터의 리스트의 범위를 설정해 데이터를 보여줌
- 보완필요 : 게시글의 양이 방대해질 것을 생각한다면, 게시글을 불러올때 `all()`을 사용하는 점이 보여주고자 하는 게시글의 비해 많아 불필요해보임
</details>

<img width="650" src="https://user-images.githubusercontent.com/104303285/188866886-e003cd53-68bd-4150-82da-e070dee14c45.png" />
<img width="650" src="https://user-images.githubusercontent.com/104303285/188866868-dccf83b1-f8ec-4bad-9cad-b38bd331bba6.png" />
