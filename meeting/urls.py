from meeting import views

from django.urls import path

urlpatterns = [
    path('',
         views.MeetingView.as_view(),), # /meeting/ 모임 글 작성, 목록
    path('<int:meeting_id>/',
         views.MeetingDetialView.as_view(),), # /meeting/<int:meeting_id>/ 모임 글 상세, 수정, 삭제
    path('<int:meeting_id>/bookmark/',
         views.MeetingBookmarkView.as_view(),), # /meeting/<int:meeting_id>/bookmark/ 모임 글 북마크
    path('<int:meeting_id>/comment/',
         views.MeetingCommentView.as_view(),), # /meeting/<int:meeting_id>/comment/ 모임 댓글 작성, 목록
    path('<int:meeting_id>/comment/<int:comment_id>/',
         views.MeetingCommentDetailView.as_view(),), # /meeting/<int:meeting_id>/comment/<int:comment_id>/ 모임 댓글 수정 삭제
    path('<int:meeting_id>/comment/<int:comment_id>/reply/',
         views.MeetingCommentReplyView.as_view(),), # /meeting/<int:meeting_id>/comment/<int:comment_id>/reply/ 모임 대댓글 작성, 목록
    path('<int:meeting_id>/comment/reply/<int:reply_id>/',
         views.MeetingCommentReplyDetailView.as_view(),), # /meeting/<int:meeting_id>/comment/reply/<int:reply_id>/ 모임 대댓글 수정 삭제 
    path('search_title/',
         views.MeetingTitleSearchView.as_view(),), #/meeting/search_api/?search=키워드 -모임 글에서 제목을 검색
     path('search_content/',
         views.MeetingContentSearchView.as_view(),), #/meeting/search_api/?search=키워드 -모임 글에서 내용을 검색
     path('search_user/',
         views.MeetingUserSearchView.as_view(),), #/meeting/search_api/?search=키워드 -모임 글에서 작성자를 검색
     path('bookmark_list/',
          views.MeetingBookmarkView.as_view(),), #/meeting/bookmark_list/ 북마크 한 모임 글 리스트 
     path('my_create_meeting/',
          views.MyCreateMeetingView.as_view(),), #/meeting/my_create_meeting/ 내가 작성한 모임 글 리스트
     path('<int:meeting_id>/meeting_image/<int:image_id>/',
          views.MeetingImageDetailView.as_view(),), #/meeting/<int:meeting_id>/meeting_image/<int:image_id> 이미지 삭제
]