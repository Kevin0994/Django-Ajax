from django.shortcuts import render
from .forms import StudentRegistration
from .models import Usuario
from django.http import JsonResponse
#from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    form = StudentRegistration()
    stud = Usuario.objects.all()
    return render(request, 'home.html', {'form': form, 'stu': stud})

#@csrf_exempt
def save_data(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            sid = request.POST['stuid']
            nombre = request.POST['nombre']
            email = request.POST['email']
            password = request.POST['password']
            telefono = request.POST['telefono']
            fecha_nacimiento = request.POST['fecha_nacimiento']
            if(sid==''):
                usr = Usuario(nombre=nombre, email=email, password=password, telefono=telefono, fecha_nacimiento= fecha_nacimiento)
            else:
                usr = Usuario(id=sid, nombre=nombre, email=email, password=password, telefono=telefono, fecha_nacimiento= fecha_nacimiento)
            usr.save()
            stud = Usuario.objects.values()
            #print(stud)
            student_data = list(stud)
            return JsonResponse({'status': 'Save',
                                 'student_data': student_data})
        else:
            return JsonResponse({'status': 0})

#Delete Data
def delete_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        #print(id)
        pi = Usuario.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})

#Edit Data
def edit_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        student = Usuario.objects.get(pk=id)
        student_data = {"id": student.id, "nombre": student.nombre, "email": student.email, "password": student.password, "telefono": student.telefono, "fecha_nacimiento": student.fecha_nacimiento}
        return JsonResponse(student_data)