from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import Booking
from .models import Outpass
from .models import Notice
from .models import Payment
from .models import Student, Attendance
from django.utils import timezone
from .forms import AttendanceForm
from .models import MessRegistration
from .models import UserComplaint
from .models import RoomAllocation
import datetime
from .forms import VisitorEntryForm
from .models import VisitorEntry


def index(request):
    return render(request,'index.html')

def mainnavbar(request):
    return render(request,'navbar.html')

def navbar(request):
    return render(request,'mainnavbar.html')

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admindash')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'adminlogin.html')

    return render(request, 'adminlogin.html')

def admin_dashboard(request):
    registrations = MessRegistration.objects.all()
    return render(request, 'admin_dashboard.html', {'registrations': registrations})

@login_required
def admindash(request):
    return render(request, 'admindash.html')  # Create this template

# @login_required
# def roomalloc(request):
#     return render(requests,'roomalloc.html')
# def is_admin(user):
#     return user.is_staff


def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin)
def roomalloc(request):
    if request.method == 'POST':
        form = RoomAllocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('roomalloc')  # Redirect to the same page to refresh list
    else:
        form = RoomAllocationForm()

    allocations = RoomAllocation.objects.all().order_by('-allocation_date')
    return render(request, 'roomalloc.html', {'form': form, 'allocations': allocations})

@user_passes_test(is_admin)
def mark_attendance(request):
    students = Student.objects.all()
    today = datetime.date.today()
    if request.method == 'POST':
        form = AttendanceForm(request.POST, students=students)
        if form.is_valid():
            for student in students:
                present = form.cleaned_data.get(f'student_{student.id}', False)
                Attendance.objects.update_or_create(
                    student=student, date=today,
                    defaults={'is_present': present}
                )
            return redirect('mark_attendance')
    else:
        form = AttendanceForm(students=students)
    return render(request, 'mark_attendance.html', {'form': form})

def attendance(request):
    students = Student.objects.all()

    if request.method == 'POST':
        today = timezone.now().date()

        # Clear previous attendance for today
        Attendance.objects.filter(date=today).delete()

        for student in student:
            is_present = f'attendance_{student.id}' in request.POST
            Attendance.objects.create(
                student=student,
                date=today,
                is_present=is_present
            )
        return redirect('attendance')  # Redirect to avoid re-submission

    return render(request, 'attendance.html', {'students': students})

@login_required
def visitor_entry(request):
    if request.method == 'POST':
        form = VisitorEntryForm(request.POST)
        if form.is_valid():
            visitor = form.save(commit=False)
            visitor.user = request.user
            visitor.save()
            return redirect('visitor_success')
    else:
        form = VisitorEntryForm()
    return render(request, 'visitor_entry.html', {'form': form})
def visitor_success(request):
    return render(request, 'visitor_success.html')
def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('userdash')
        else:
            return HttpResponse ("Username or Password is incorrect, Please Cheak your Username or Password otherwise Create a New Account?")
    return render(request,'userlogin.html')

def userdash(request):
    return render(request, 'userdash.html')


def LogoutPage(request):
    logout(request)
    return redirect('userlogin')

@login_required(login_url='userlogin')

def roombook(request):
     if request.method == 'POST':
        student = request.user
        student_name = request.POST.get('student_name')
        phone = request.POST.get('phone')
        birth_date = request.POST.get('birth_date')
        address = request.POST.get('address')
        floor = request.POST.get('floor')
        booking_date = request.POST.get('booking_date')

        Booking.objects.create(
            student=student,
            student_name=student_name,
            phone=phone,
            birth_date=birth_date,
            address=address,
            floor=floor,
            booking_date=booking_date
        )

        return redirect('userdash')  # or to a success page

     return render(request, 'roombook.html')

def user_complaints(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        room_no = request.POST.get('room_no')
        complaint = request.POST.get('complaint')

        UserComplaint.objects.create(name=name, room_no=room_no, complaint=complaint)
        return redirect('complaint_success')  # Redirect after successful submission

    return render(request, 'usercomplaints.html')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_complaint_dashboard(request):
    complaints = UserComplaint.objects.all().order_by('-submitted_at')
    return render(request, 'admin_complaint_dashboard.html', {'complaints': complaints})
def complaint_success(request):
    return render(request, 'complaint_success.html')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_room_allocation(request):
    allocations = RoomAllocation.objects.all().order_by('-allocation_date')
    return render(request, 'admin_room_allocation.html', {'allocations': allocations})
def outpass(request):
    if request.method == 'POST':
        student = request.user
        student_name = request.POST.get('student_name')
        out_time = request.POST.get('out_time')
        out_date = request.POST.get('out_date')
        out_tdate = request.POST.get('out_tdate')
        in_time = request.POST.get('in_time')
        place_going = request.POST.get('place_going')
        purpose_going = request.POST.get('purpose_going')

        Outpass.objects.create(
            student=student,
            student_name=student_name,
            out_time=out_time,
            out_date=out_date,
            out_tdate=out_tdate,
            in_time=in_time,
            place_going=place_going,
            purpose_going=purpose_going
        )

        return redirect('userdash')  # Or redirect to a success page

    return render(request, 'outpass.html')

def mess(request):
    return render(request,'mess.html')
def notices(request):
    return render(request,'notices.html')
def student_notices(request):
    notices = Notice.objects.all().order_by('-created_at')
    return render(request, 'student_notices.html', {'notices': notices})
def payment_page(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_id = request.POST.get('student_id')
        payment_type = request.POST.get('payment_type')
        payment_for_list = request.POST.getlist('payment_for')  # Checkbox selections
        bank = request.POST.get('bank')
        upi_method = request.POST.get('upi_method')

        # Save one Payment object with the selected payment_for list
        Payment.objects.create(
            student_name=student_name,
            student_id=student_id,
            payment_type=payment_type,
            payment_for=payment_for_list,  # Stored as a list in JSONField
            bank=bank if payment_type == 'Offline' else '',
            upi_method=upi_method if payment_type == 'Online' else '',
        )

        messages.success(request, "Payment recorded successfully!")
        return redirect('payment_success')

    return render(request, 'payment.html')


def payment_success(request):
    return render(request, 'payment_success.html')
def profile(request):
    return render(request,'profile.html')


def usersignup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('userlogin')
    return render(request,'usersignup.html')
