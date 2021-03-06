from django.urls import path
from django.contrib import admin

from expenses import views

admin.autodiscover()

app_name = 'expenses'

urlpatterns = [
    path(
        'create/', views.ExpenseCreateView.as_view(),
        name='expense_create'
    ),
    path(
        '<int:pk>/update/',
        views.ExpenseUpdateView.as_view(),
        name='expense_update'
    ),
    path(
        '<int:pk>/delete/',
        views.ExpenseDeleteView.as_view(),
        name='expense_delete'
    ),
    path(
        'all/', views.ExpenseListView.as_view(),
        name='expenses_all'
    )
]
