# web 강의 자료

> 본 강의 자료는 3/23(월), 3/24(화)에 진행된 내용입니다.

* bootstrap 강의 자료는 에듀싸피에 e-book 형태로 제공되고 있습니다. 참고 바랍니다.
* bootstrap 활용시에는 반드시 CDN을 적용하셔야 합니다.
  * https://getbootstrap.com/docs/4.4/getting-started/introduction/



## Github pages

> Github에서 무료로 정적 사이트를 호스팅을 해주는 기능

git을 모르시는 분들을 위하여 간단하게 작성하였습니다.

### 준비 사항

#### 1. 소스코드

* HTML/CSS, JS로 구성되어 있는 코드만 활용 가능
* https://startbootstrap.com/ 에 있는 resume를 활용하였습니다.
  * https://startbootstrap.com/themes/resume/

#### 2. Github 저장소

* `username`.github.io 로 저장소 이름을 만들어주셔야 합니다.

  

### 최초 업로드

* 아래의 명령어를 통해 업로드 하시면 됩니다.
* 명령어는 반드시 `index.html` 이 있는 폴더에서 `git add .`
* git 내용은 내일 프로젝트를 진행하면서 설명 드리겠습니다.

```bash
# ls를 하고 index.html이 있는지 반드시 확인합니다.
$ ls
css/         img/        js/      package.json       README.md  vendor/      gulpfile.js  index.html  LICENSE  package-lock.json  scss/

$ git init
(master) $ git add . 
(master) $ git commit -m 'init'
```

* github 저장소에서 아래의 두 명령어를 복사하여 붙여넣기
  * 주의 : gitbash 에서는 복사 붙여넣기 명령어가 다릅니다. 우클릭해서 참고 해주세요.

<img src="images/Screen Shot 2020-03-24 at 오전 11.14.png" alt="Screen Shot 2020-03-24 at 오전 11.14" style="zoom:60%;" />

### 이후 수정시

* 수정을 하고 나서는 아래의 명령어들을 통해 커밋 및 업로드를 합니다.

  ```bash
  $ git add .
  $ git commit -m 'Update XXX'
  $ git push origin master
  ```

  

### resume 관련

* fontawesome
  * https://fontawesome.com/
  * 현재 프로젝트에는 vendor에 파일이 저장되어 있어, 여러분들이 위의 url에서 찾아보고 가져다 쓰셔도 무방합니다.
  * 다만, 향후 본인 프로젝트에 적용하기 위해서는 회원가입 후 mail을 통해 받은 CDN 등을 활용하셔야 합니다.
* 주의 사항
  * index.html과 resume.css를 중심으로 수정 하시면 됩니다.
  * resume.min.css가 불러와져있어, index.html에서 수정을 하시면 됩니다.