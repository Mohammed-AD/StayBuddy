from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserComplaint(models.Model):
    name = models.CharField(max_length=100)
    room_no = models.CharField(max_length=10)
    complaint = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.room_no}"

class Booking(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    birth_date = models.DateField()
    address = models.TextField()
    floor = models.CharField(max_length=20)
    booking_date = models.DateField()

    def __str__(self):
        return f"{self.student.username} - {self.student_name} - {self.booking_date}"


class Outpass(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    out_time = models.TimeField()
    out_date = models.DateField()
    out_tdate = models.DateField()
    in_time = models.TimeField()
    place_going = models.CharField(max_length=200)
    purpose_going = models.TextField()

    def __str__(self):
        return f"{self.student.username} - {self.out_date} to {self.out_tdate}"


class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Payment(models.Model):
    PAYMENT_TYPE_CHOICES = [
        ('Online', 'Online'),
        ('Offline', 'Offline'),
    ]

    BANK_CHOICES = [
        ('SBI', 'State Bank of India'),
        ('HDFC', 'HDFC Bank'),
        ('ICICI', 'ICICI Bank'),
        ('Axis', 'Axis Bank'),
        ('PNB', 'Punjab National Bank'),
        ('Other', 'Other'),
    ]

    UPI_METHOD_CHOICES = [
        ('GPay', 'Google Pay'),
        ('PhonePe', 'PhonePe'),
        ('Paytm', 'Paytm'),
        ('NetBanking', 'Net Banking'),
        ('Other', 'Other'),
    ]

    PAYMENT_FOR_CHOICES = [
        ('Room', 'Room'),
        ('Mess', 'Mess'),
    ]

    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    payment_type = models.CharField(max_length=10, choices=PAYMENT_TYPE_CHOICES)
    payment_for = models.JSONField()  # allows storing multiple selections as a list
    bank = models.CharField(max_length=20, choices=BANK_CHOICES, blank=True, null=True)
    upi_method = models.CharField(max_length=20, choices=UPI_METHOD_CHOICES, blank=True, null=True)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} ({self.student_id}) - {self.payment_type}"


class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.name} - {self.date} - {'Present' if self.is_present else 'Absent'}"
class MessRegistration(models.Model):
    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=50)
    room_number = models.CharField(max_length=20)
    subscription_type = models.CharField(max_length=10)
    start_date = models.DateField()

    def __str__(self):
        return self.student_name
class RoomAllocation(models.Model):
    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=50)
    room_number = models.CharField(max_length=10)
    allocation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - Room {self.room_number}"

class VisitorEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    purpose = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    entry_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.entry_time.strftime('%Y-%m-%d %H:%M')}"
