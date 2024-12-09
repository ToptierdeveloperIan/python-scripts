
from django.contrib import admin
from .models import Book, BorrowRecord, Notification

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'available')
    search_fields = ('title', 'author')

@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('book', 'borrower', 'borrowed_date', 'due_date', 'returned')
    search_fields = ('book__title', 'borrower__username')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'sent_date', 'read')
    search_fields = ('user__username', 'message')







