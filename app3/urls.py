from django.urls import path,include
from.import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login_view/',views.login_view,name='login'),
    path('register/',views.register,name='register'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('form',views.form,name='form'),
    path('prediction',views.prediction,name='prediction'),
    path('chatbot',views.chatbot,name='chatbot'),
    path('dietplan',views.dietplan,name='dietplan'),
    path('terms',views.terms,name='terms'),
    path('question',views.question,name='question'),
    path('add/',views.add,name='add'),
    path('home/',views.home,name='home'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('filter_details/',views.filter_details,name='filter_details'),

]
