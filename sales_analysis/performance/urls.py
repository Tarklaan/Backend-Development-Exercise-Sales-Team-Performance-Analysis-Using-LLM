from django.urls import path
from .views import performance_feedback, team_performance, performance_trends, load_sales_data

urlpatterns = [
    path('feedback/<int:employee_id>/', performance_feedback, name='performance_feedback'),
    path('team-performance/', team_performance, name='team_performance'),
    path('performance-trends/', performance_trends, name='performance_trends'),
    path('load-data/', load_sales_data, name='load_sales_data'),
]
