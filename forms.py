from django import forms
from .models import Student
from .models import VisitorEntry

class AttendanceForm(forms.Form):
    def __init__(self, *args, **kwargs):
        students = kwargs.pop('students')
        super().__init__(*args, **kwargs)
        for student in students:
            self.fields[f'student_{student.id}'] = forms.BooleanField(
                label=student.user.get_full_name(), required=False
            )

from .models import RoomAllocation

class RoomAllocationForm(forms.ModelForm):
    class Meta:
        model = RoomAllocation
        fields = ['student_name', 'student_id', 'room_number']

class VisitorEntryForm(forms.ModelForm):
    class Meta:
        model = VisitorEntry
        fields = ['name', 'purpose', 'contact_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'purpose': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
        }
