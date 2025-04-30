from django.urls import path
from .views import(
    Interview_list_view,Interview_Detail_view,Interview_Delete_view,mock_interview_view,
    interview_setup_view, redo_interivew_view
)
# from .views import interview_setup_view, mock_interview_view

urlpatterns = [
    path('setup/', interview_setup_view, name='interview_setup'),
    path('mock/', mock_interview_view, name='mock_interview'),
    path('list/', Interview_list_view.as_view(), name='interview_list'),
    path('<int:pk>/', Interview_Detail_view.as_view(), name='interview_detail'),
    path('delete/<int:pk>/', Interview_Delete_view.as_view(), name='interview_delete'),
    path('restart/<int:pk>', redo_interivew_view, name='redo'),
]
