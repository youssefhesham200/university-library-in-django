from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name="register"),
    path('StudentRegister', views.StudentRegister.as_view(), name="StudentRegister"),
    path('OwnerRegister', views.OwnerRegister.as_view(), name="OwnerRegister"),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('addbook/', views.addBook, name='addbook'),
    path('booksadmin/', views.booksadmin, name='booksadmin'),
    path('booksstudent/', views.booksstudent, name='booksstudent'),
    path('borrowing/<int:id>', views.borrowing, name='updateborrowing'),
    path('returning/<int:id>', views.returning, name='returning'),
    path('extend/<int:id>', views.extend, name='extend'),
    path('<int:id>', views.updateBook, name='updateBook'),
    path('updateUser', views.updateUser, name='updateUser'),
    path('updateStudent',views.updateStudent, name='updateStudent'),
]
