from django.contrib import admin
from .models import Booking, Outpass, Payment, Notice, UserComplaint, RoomAllocation
# from .models import Outpass
# from .models import Payment
# from .models import Notice
# from .models import UserComplaint
from .models import VisitorEntry
from .models import Student, Attendance

admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(Notice)
admin.site.register(Booking)
admin.site.register(UserComplaint)
# Register your models here.
admin.site.register(Outpass)
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_id', 'payment_type', 'get_payment_for', 'bank', 'upi_method', 'payment_date')
    search_fields = ('student_name', 'student_id')
    list_filter = ('payment_type', 'bank')  # Removed payment_for from list_filter as it's now a list (JSON)

    def get_payment_for(self, obj):
        return ", ".join(obj.payment_for) if isinstance(obj.payment_for, list) else obj.payment_for
    get_payment_for.short_description = 'Payment For'

# from .models import RoomAllocation

@admin.register(RoomAllocation)
class RoomAllocationAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_id', 'room_number', 'allocation_date')
    search_fields = ('student_name', 'student_id', 'room_number')
    list_filter = ('allocation_date',)
    ordering = ('-allocation_date',)

@admin.register(VisitorEntry)
class VisitorEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'purpose', 'contact_number', 'entry_time')
    search_fields = ('name', 'user__username', 'purpose')
    list_filter = ('entry_time',)
