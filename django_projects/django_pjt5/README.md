1. json 파일 데이터 로드하는 것. (loaddata)

   fixtures template 같은것. 

   ```django
   movies/fixtures/movies/moviedata.json 
   # json 파일 읽기
   $ python manage.py loaddata movies/moviedata.json
   ```

   

2. user custom 작업

   1) 1차본

   - 저번 프로젝트4에서 user custom 작업을 진행한 코드를 다시 사용해서 수정중

   ```python
   from django.db import models
   from django.conf import settings
   from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
   
   class UserManager(BaseUserManager):
   
       use_in_migrations = True
   
       def create_user(self, email, username, gender, age, password=None):
           if not email :
               raise ValueError('must have user email')
           user = self.model(
               email = self.normalize_email(email),
               username = username,
               gender = gender,
               age = age,
   
           )
           user.set_password(password)
           user.save(using=self._db)
           return user
   
       def create_superuser(self, email, username, gender, age, password ):
   
           user = self.create_user(
               email = self.normalize_email(email),
               username = username,
               password=password,
               gender = gender,
               age = age,
           )
           user.is_admin = True
           user.is_superuser = True
           user.is_staff = True
           user.save(using=self._db)
           return user
   
   
   
   class User(AbstractBaseUser,PermissionsMixin):
   
       objects = UserManager()
   
       email = models.EmailField(
           max_length=255,
           unique=True,
       )
       username = models.CharField(
           max_length=20,
           null=False,
           unique=True
       )
   
       GENDER_CHOICES = {
         ('male','남성'), #오른쪽에 있는 것이 화면에 보인다.
         ('female', '여성'),
       }
       gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
       followers = models.ManyToManyField(
               settings.AUTH_USER_MODEL,
               related_name='followings'
           )
       age = models.IntegerField()
   
       is_active = models.BooleanField(default=True)
       is_admin = models.BooleanField(default=False)
       is_superuser = models.BooleanField(default=False)
       is_staff = models.BooleanField(default=False)
       date_joined = models.DateTimeField(auto_now_add=True)
       USERNAME_FIELD = 'username'
       REQUIRED_FIELDS = ['email','gender','age']
   
   ```

   - admin  사이트에 생성한 모델들 등록 

     1) movies/admin.py 에 movie의 model 등록

     ```
     admin.site.register(Movie)
     admin.site.register(Genre)
     ```

     2) accounts/admin.py 에 user만 등록

      UserManager를 등록하지 않은 이유 - 우리가 어드민 페이지에서 관리하는건 user고 usermaneger는 회원가입때 사용하는 폼같은 것. use class 에 다저장되서 user만 등록한다. 

     ```
     admin.site.register(User)
     ```

   - admin 을 깔끔하게 보여주기위해 ``MovieAdmin`` class 를 만들고 ``list_display`` 에있는 것만 보여준다.

     ```python
     from django.contrib import admin
     from blog.models import Post
     
     class MovieAdmin(admin.ModelAdmin):
         list_display = ['title', 'popularity', 'vote_count', 'vote_average']
     
     class GenreAdmin(admin.ModelAdmin):
         list_display = ['name']
     
     admin.site.register(Movie, MovieAdmin)
     admin.site.register(Genre, GenreAdmin)
     ```

     