# Django pjt 03

1. project 생성

2. app 생성 (accounts, community)

3. accounts url 설정 

   - 회원가입
   - 로그인 : get 방식으로 들어올때 폼을 띄우고 post 방식일 떄 폼을 저장한다.

4. project url에서 accounts, community url path를 include 하게 설정하게 한다. 

5. account view 생성

6. accounts, community, django_pjt3에 template 폴더를 생성하여 그 안에 html 파일을 생성하였다. 

7. settings 에서 다른 템플릿으로 [os.path.join(BASE_DIR, 'templates')], 로 설정한다. 

8. community model 생성

   1) Movie 모델 생성

   - 영화 제목 필드 생성

   - 포스터 필드 생성 (URL 필드)

   - 영화 평점 필드 생성

   - 영화 줄거리 필드 생성

     

   2) Review 모델 생성

   - 해당 review의 영화를 Movie 의 foriegnkey 로 받아온다.
   - 해당 review를 작성하는 user의 정보를   foriegnkey를 받아온다.
   - review image 업로드 필드 생성

   3) Comment 모델 생성

   - 해당 comment 작성 user field 생성

   - 해당 comment의 review foreignkey 로 불러옴

   - comment 내용 필드 생성

   - comment 생성, 수정 필드 생성

     

9. 느낀점 및 배운점

   1. django_pjt3 보다 명세의 자유성이 높아서 자유롭게 모델을 작성하고 뷰 파일을 작성하다보니 순서가 엉망이 되서 굉장히 어려움을 겪었다. 중간 중간 하나씩 만들면서 확인했었어야 했는데 전체 모델을 마이그레이트 한 상태에서 코드를 작성하다보니 하나 고치고 또 다른 오류가 나오고 등 어려움을 겪었다. 앞으로는 모델을 한꺼번에 마이그레이트를 하고 하기보다는 하나씩 해결해서 해야된다고 생각했다. 

   2. 또한 ImageField 모델을 지정해주는 과정에서 blank = True, 와 null = True의 차이점을 알 수 있었다. blank 경우에는 필드가 폼에서 빈 채로 저장되는 것을 허용하고 장고관리자 및 직접 정의한 폼에도 반영이된다. 반면 null 같은 경우 필드의 값이 null(정보없음)로 저장되는 것을 허용한다. 결국 데이터 베이스 열에 관한 설정이다. 추가적으로 ``BooleanField`` 에 NULL 을 입력할 수 있도록 하려면 ``null=True``  가 아닌 `NullBooleanField`를 사용해야 한다.

   3. user 모델에 is_superuser 라는 속성이 있어서 admin인지 판단할 수 있다. 

      ```
      is_superuser¶
      Boolean. Designates that this user has all permissions without explicitly assigning them.
      ```

      이를 활용해 superuser 권한을 가지고 있을 경우 moviecreate 와 movieupdate를 하는 것으로 html 과 view.py 에 추가하여

      구현하였다.

   4. `settings.py`에 `AUTH_USER_MODEL = 'accounts.User'`를 넣어 커스텀한 User를 사용할 수 있다.

      커스텀한 User를 사용 시,  UserCreationForm을 사용하려 하면 에러가 난다. 따라서 밑의 식을 통해 수정해야 한다.

      ```python
      from django.contrib.auth.forms import UserCreationForm
      from django.contrib.auth import get_user_model
      
      class CustomUserCreationForm(UserCreationForm):
          class Meta(UserCreationForm.Meta):
              model = get_user_model()
      ```

   5. ``include`` 하여 다른 html 파일에서 참조 할 수 있다.

      ```python
      {% include 'community/_like.html' %}
      ```

      













