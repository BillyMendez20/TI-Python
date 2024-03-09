from django.shortcuts import render, redirect
from .models import Student
from .views import StudentForm
from django.db.models import Count
from datetime import datetime
from collections import Counter  # Agregar esta línea para importar Counter




from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.db.models import Count
from datetime import datetime

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})

def student_statistics(request):
    current_year = datetime.now().year
    birth_years = Student.objects.values_list('fecha_nacimiento__year', flat=True)
    age_distribution = {current_year - birth_year: count for birth_year, count in 
                        dict(Counter(birth_years)).items()}
    return render(request, 'students/student_statistics.html', {'age_distribution': age_distribution})
