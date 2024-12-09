from django.urls import path
from . import views

urlpatterns = [
    path('studentnotifications/',views.studentnotifications,name='studentnotifications'),
    path('generate_reports/', views.generate_reports, name='generate_reports'),
    # Other URL patterns...
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('change_password/', views.change_password, name='change_password'),
    path('notifications/', views.notifications, name='notifications'),
    path('send_overdue_notifications/', views.send_overdue_notifications, name='send_overdue_notifications'),

    # Other URL patterns...
    path('manage_borrowed_books/', views.manage_borrowed_books, name='manage_borrowed_books'),
    path('return_book/<int:borrow_id>/', views.return_book, name='return_book'),
    path('manage_users/', views.manage_users, name='manage_users'),
    path('add_user/', views.add_user, name='add_user'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('manage_books/', views.manage_books, name='manage_books'),
    path('', views.custom_login, name='login'),
    path('borrow_book/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('borrowed_books/', views.borrowed_books, name='borrowed_books'),
    path('library_catalogue/', views.library_catalogue, name='library_catalogue'),
    path('rules/', views.rules, name='rules'),
    path('librarian_dashboard/', views.library_dashboard, name='librarian_dashboard'),
    path('history/', views.history, name='history'),
]
