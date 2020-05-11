# Django_project_3_READ.ME

1. 구현과정

   | 시간         | 내용                                                      | driver |
   | ------------ | --------------------------------------------------------- | ------ |
   | 12:30 - 1:00 | 프로젝트 생성 및 directory 구성                           | 김호연 |
   | 1:00 - 2:00  | community 앱 구성: Model 작성,admin,url 설정 및 migration | 나종석 |
   | 3:00 - 4:00  | community 앱 구성: views, template 작성                   | 김호연 |
   | 4:00 - 5:00  | accounts 앱 구성: Model 작성,admin,url 설정 및 migration  | 나종석 |
   | 5:00 - 6:00  | accounts 앱 구성: views, template 작성                    | 김호연 |
   | 7:00 - 12:00 | style 수정 및 보완, 이미지 업로드 구현, 이미지 크롭       | 김호연 |

   

2. 학습내용

   

   - 전체적인 flow를 이전보다 확실히 이해했다.

   - render, redirect : render 은 템플릿을 불러오고 파라미터들을 넘겨주는 것이고

     redirect는 정한 url로 페이지를 보내는 것이다. 이후 이동한 url view함수의 내용에 따라 수행한다

   - ``review_detail.html`` 에서 ``review.title`` 과 같은 값들이 어떠한 과정을 통해서 인자로 받아드려지는지에 대한 이해가 부족했다. 이는  review_detail뷰에서 return시  ``'community/review_detail.html'``로 렌더링 되는데 이때 뷰함수내부에서 넘겨주는 ``context ``내부에``'review':review``로 코드를 짜였기 때문에 가능한 것이다.

   - 또한 같은 맥락으로 ``{% if request.user == review.user %}`` 에서의 request.user 같은 경우 ``review_detail`` 뷰함수에서 ``request`` 파라미터를 return 하기에 가능한 것이다.

   - comment 작성 혹은 review 생성시 각각의 view 함수에서 ``comment.user = request.user`` 과  ``form.user = request.user`` 코드를 추가적으로 작성해야 했다.

     이는 model 에서 정한 user의 정보를 작성중인 유저로 넣기 위함이다. ``CommentForm`` 과 ``ReviewForm``에서 user에 대한 fields가 없기 때문에 user에 대한 선언이 꼭 필요하다.

   - 추가적으로 이후에 댓글에 대한 update 또한 구현하려고 시도했지만, 댓글 수정 버튼을 눌렀을때 html의 부분만 변화하는 작업 구현이 불가해 실패하였다. 이는 차후에 꼭 시도하길!

   - 사진업로드도 구현하였는데 업로드시 원본 파일로 올라가게되어 이를 해결하기 위해

     ``from imagekit.models import ProcessedImageField``
     ``from imagekit.processors import ResizeToFill`` 를 모델에 추가해주고 image의 세부항목을 정하여 재migrate를 해주었다.

   

   

3. 프로젝트 후기

   - 따라가기식 코드를 했다면 flow를 이해하면서 직접 구현해보니 공부가 많이 부족하다 생각했다.
   - 또한 프로젝트가 명세가 있어 협업시 파트를 나누는 것에 굉장히 수월하였지만 명세가 없을 경우 협업이 굉장히 힘들것으로 예상된다. 
   - 따라서 프로젝트 시작시, 최대한 자세하게 틀을 짜놓는 것이 중요하다는 것을 배웠다.

   - 주석처리가 협업시 상당히 중요한것같다. 내가 하다가 막히거나, 혹은 상대가 하다 막혔을 때 서로 코드 리뷰를 빠르게 하기 위해서 필요한 부분이다.

     

     

     

