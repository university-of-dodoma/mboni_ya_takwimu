from django.urls import path

from . import views
app_name= 'taswira'
urlpatterns = [
    path('', views.index, name='upload'),
        # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('upload', views.simple_upload, name='upload'),
    path('<int:pk>/edit', views.question_edit, name='edit_question' ),
    path('post', views.post_add, name='post_edit'),
    path('<int:pk>/view', views.post_view, name='post_view'),
    path('graph',views.graph, name='graph')
]
