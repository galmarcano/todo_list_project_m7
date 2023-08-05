from django.shortcuts import render
from django.http import HttpResponseRedirect
from administrar.models import Tarea #Importar el modelo
from .forms import TareaForm #Para validar

# Create your views here.
def v_index(request):
  if request.method == 'POST':
    #POST voy a crear un registro
    _titulo = request.POST["titulo"]

    datos = request.POST.copy()
    
    form = TareaForm(datos) #Para validaciones
    if form.is_valid():
      #Validaciones extras, usando el lenguaje Python
      #Si es válido
      form.save() #En este punto guardo en DB
    else:
      #No es válido que redirija, form tiene errores
      return HttpResponseRedirect("/")

    if False: #Solo en caso de que se desea guardar datos sin validar, no caerá aquí nunca, no debería ejecutarse
      tarea = Tarea() #Instancio un modelo
      tarea.titulo = _titulo #Asigno titulo a la tarea
  
      #Antes de *.save no se guarda nada en DB
      tarea.save() #Guardo en DB
    

    return HttpResponseRedirect("/")
  else:
    #Peticiones method=get
    consulta = Tarea.objects.filter(titulo__icontains = request.GET.get("titulo", ""))
    
    if request.GET.get("estado", "") != "":
      consulta = consulta.filter(estado = request.GET.get("estado", ""))
      
    #Listar
    context = {
      'var1': 'valor1',
      'var2': 'valorrr',
      'lista': consulta
    }
    return render(request, 'pagina_x.html', context)

def v_eliminar(request, tarea_id):
  Tarea.objects.filter(id= tarea_id).delete()
  return HttpResponseRedirect("/") #Redirigir

def v_completado(request, tarea_id):
  task = Tarea.objects.get(id = tarea_id)
  task.estado = 1 #Completado
  task.save()
  return HttpResponseRedirect("/")