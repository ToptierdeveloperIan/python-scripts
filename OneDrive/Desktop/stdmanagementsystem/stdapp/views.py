from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .models import Book, BorrowRecord
from datetime import datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserForm, CreateUserForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BorrowRecord
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import BorrowRecord
from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Book, BorrowRecord
from datetime import datetime, timedelta
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomPasswordChangeForm

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('student_dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


@login_required
def generate_reports(request):
    # Borrowing trends
    one_month_ago = datetime.now() - timedelta(days=30)
    recent_borrows = BorrowRecord.objects.filter(borrowed_date__gte=one_month_ago)
    borrow_trends = recent_borrows.count()

    # Inventory status
    total_books = Book.objects.count()
    borrowed_books = BorrowRecord.objects.filter(returned=False).count()
    available_books = total_books - borrowed_books

    # Context to pass to the template
    context = {
        'borrow_trends': borrow_trends,
        'total_books': total_books,
        'borrowed_books': borrowed_books,
        'available_books': available_books,
        'recent_borrows': recent_borrows,
    }

    return render(request, 'generate_reports.html', context)

def studentnotifications(request):
    overdue_records = BorrowRecord.objects.filter(borrower=request.user, returned=False, due_date__lt=datetime.now())
    for record in overdue_records: messages.info(request,
   f"Overdue: {record.book.title} by {record.book.author} is overdue. Please return it.")
    return render(request, 'notificationstudents.html')
@login_required
def notifications(request):
    # Handling sending notifications logic here is optional.
    return render(request, 'notifications.html')

@login_required
def send_overdue_notifications(request):
    overdue_records = BorrowRecord.objects.filter(returned=False, due_date__lt=datetime.now())
    for record in overdue_records:
        user = record.borrower
        messages.info(request, f"Overdue: {record.book.title} by {record.book.author} is overdue. Please return it.")
        # Optionally send an email or another form of notification
    return redirect('notifications')


@login_required
def manage_borrowed_books(request):
    borrowed_books = BorrowRecord.objects.all()
    return render(request, 'manage_borrowed_books.html', {'borrowed_books': borrowed_books})

@login_required
def return_book(request, borrow_id):
    borrow_record = get_object_or_404(BorrowRecord, id=borrow_id)
    if request.method == 'POST':
        borrow_record.returned = True
        borrow_record.save()
        return redirect('manage_borrowed_books')
    return render(request, 'return_book.html', {'borrow_record': borrow_record})


@login_required
def manage_users(request):
    users = User.objects.all()
    return render(request, 'manage_users.html', {'users': users})

@login_required
def add_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('manage_users')
    else:
        form = CreateUserForm()
    return render(request, 'add_user.html', {'form': form})

@login_required
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('manage_users')
    else:
        form = UserForm(instance=user)
    return render(request, 'edit_user.html', {'form': form, 'user': user})

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('manage_users')


@login_required
def manage_books(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_books')
    else:
        form = BookForm()
    books = Book.objects.all()
    return render(request, 'manage_books.html', {'form': form, 'books': books})

@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('manage_books')
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('manage_books')
        else:
            form = BookForm( instance =book)
        return render(request, 'edit_book.html', {'form': form, 'book': book})
    else:
        form = BookForm(instance=book),
    return render(request, 'edit_book.html', {'form': form, 'book': book})



@csrf_protect
def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.groups.filter(name='librarians').exists():
                return redirect('librarian_dashboard')
            elif user.groups.filter(name='students').exists():
                return redirect('student_dashboard')
            else:
                messages.error(request, 'You are not authorized to access the system.')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'OSMS login page.html')

def student_dashboard(request):
    return render(request, 'studentdashboard.html')

@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.available:
        due_date = datetime.now() + timedelta(days=14)  # Set due date to 2 weeks from now
        BorrowRecord.objects.create(book=book, borrower=request.user, due_date=due_date)
        book.available = False
        book.save()
    return redirect('library_catalogue')

@login_required
def borrowed_books(request):
    borrowed_books = BorrowRecord.objects.filter(borrower=request.user, returned=False)

    return render(request, 'borrowedbooks.html', {'borrowed_books': borrowed_books})

def library_catalogue(request):
    books = Book.objects.all()
    return render(request, 'libarycatalogue.html', {'books': books})

def rules(request):
    return render(request, 'rules.html')

def library_dashboard(request):
    return render(request, 'libarydashboard.html')

def history(request):
    books = Book.objects.filter(category='History')
    return render(request, 'history.html', {'books': books})
