from django.urls import path
from . import views

# url patterns here
app_name = 'bloodmanagement'
urlpatterns = [
    path('',views.index,name='index'),
    path('create-doctor/', views.doctor_create,name='doctor-create'),
    path('list-doctor/',views.doctor_list,name='doctor-list'),
    path('<int:pk>/detail-doctor/',views.doctor_detail,name='doctor-detail'),
    path('<int:pk>/update-doctor/',views.doctor_update,name='doctor-update'),
    path('<int:pk>/delete-doctor/',views.doctor_delete,name='doctor-delete'),
    path('create-department/',views.department_create,name='department-create'),
    path('list-department/',views.department_list,name='department-list'),
    path('<int:pk>/detail-department/',views.department_detail,name = 'department-detail'),
    path('<int:pk>/update-department/',views.department_update,name= 'department-update'),
    path('<int:pk>/department-delete/',views.department_delete,name = 'department-delete'),
    path('create-patient/', views.patient_create, name='patient-create'),
    path('list-patient/',views.patient_list,name='patient-list'),
    path('<int:pk>/detail-patient/',views.patient_detail,name='patient-detail'),
    path('<int:pk>/update-patient/',views.patient_update,name='patient-update'),
    path('<int:pk>/delete-patient/',views.patient_delete,name='patient-delete'),
    path('create-blood/', views.blood_create,name='blood-create'),
    path('list-blood/',views.blood_list,name='blood-list'),
    path('<int:pk>/detail-blood/',views.blood_detail,name='blood-detail'),
    path('<int:pk>/update-blood/',views.blood_update,name='blood-update'),
    path('<int:pk>/delete-blood/',views.blood_delete,name='blood-delete'),
    path('create-staff/',views.staff_create,name='staff-create'),
    path('list-staff/',views.staff_list,name='staff-list'),
    path('<int:pk>/detail-staff/',views.staff_detail,name='staff-detail'),
    path('<int:pk>/delete-staff/',views.staff_delete,name='staff-delete'),
    path('<int:pk>/update-staff/',views.staff_update,name='staff-update'),
]
