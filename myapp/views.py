import os
from django.conf import settings
from django.shortcuts import render, redirect

from .forms import ContactForm
from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        print("Form submitted")
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            contact_message = form.cleaned_data['contact_message']
            # Process the data (save to DB or send email)
            Contact.objects.create( contact_name=contact_name, contact_email=contact_email, contact_message=contact_message )
            # return render(request, 'success.html')  # Redirect to a success page
            return redirect("home")
    else:
        print("Form is not valid")
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})



# Create your views here.
def home(request):
    # Define the folder containing images
    img_folder = os.path.join(settings.BASE_DIR, 'static','myapp','img')
    img_folder_fotos2 = os.path.join(settings.BASE_DIR, 'static','myapp','fotos2')
    
    # List to hold the image URLs
    img_list_fA = []
    img_list_fB = []
    img_list_fC = []

    img_list_Aa = []
    img_list_Ab = []
    img_list_Ba = []
    img_list_Bb = []
    img_list_Ca = []
    img_list_Cb = []

    # Loop through the folder and get all image file paths
    for filename in os.listdir(img_folder):
        if (filename.endswith(('tn.jpg', 'tn.jpeg')) and filename.startswith("tm-img-0")):  # Filter image types
            
            img_list_Aa.append(f'myapp/img/{filename}')
            img_list_Ab.append(f'myapp/img/{filename.replace("-tn", "")}')
            img_list_Ca.append(f'myapp/img/{filename}')
            img_list_Cb.append(f'myapp/img/{filename.replace("-tn", "")}')
        elif (filename.endswith(('tn.jpg', 'tn.jpeg')) and filename.startswith("tm-img-1")):
            img_list_Ba.append(f'myapp/img/{filename}')
            img_list_Bb.append(f'myapp/img/{filename.replace("-tn", "")}')
    
    
    # Loop through the folder and get all image file paths
    for filename in os.listdir(img_folder_fotos2):
        if (filename.endswith('.png') and filename.startswith("fotosA")):  # Filter image types
            img_list_fA.append(f'myapp/fotos2/{filename}')
        elif (filename.endswith('.png') and filename.startswith("fotosB")):  # Filter image types
            img_list_fB.append(f'myapp/fotos2/{filename}')
        elif (filename.endswith('.png') and filename.startswith("fotosC")):  # Filter image types
            img_list_fC.append(f'myapp/fotos2/{filename}')
            

    # 'imagesA': zip(img_list_Aa, img_list_Ab),
    # 'imagesB': zip(img_list_Ba, img_list_Bb),
    # 'imagesC': zip(img_list_Ca, img_list_Cb),

    context = {
        'section_title' : 'Muebles tipo',
        'imagesA': zip(img_list_fA, img_list_fA),
        'imagesB': zip(img_list_fB, img_list_fB),
        'imagesC': zip(img_list_fC, img_list_fC),

        'about_us_title' : 'Acerca de nosotros',
        'about_us' : 'Con más de 50 años de experiencia en el arte de la ebanistería, nuestra empresa ha sido pionera en la creación de muebles únicos y personalizados. Nos dedicamos a transformar espacios con piezas de alta calidad y diseño a medida, cuidando cada detalle para lograr la satisfacción de nuestros clientes.',

        'mission_title' : 'Nuestra misión',
        'mission' : 'Convertimos la madera en arte, creando muebles duraderos y bellos que reflejan la esencia y visión de nuestros clientes. Nos esforzamos por mantener la tradición artesanal mientras incorporamos innovaciones que nos permitan entregar siempre lo mejor.',

        'story_title' : 'Historia',
        'story' : 'Fundada por Alonso hace más de cinco décadas, la empresa nació de una pasión por la ebanistería y un compromiso con la excelencia.',
        
        'team_title' : 'Equipo',
        'team' : 'Nuestro equipo está compuesto por artesanos dedicados y apasionados por su trabajo. Cada miembro aporta su experiencia y habilidad para asegurar que cada pieza supere las expectativas de cada cliente.',
        
        'quality_title' : 'Compromiso de calidad',
        'quality' : 'La calidad es nuestra prioridad. Desde la selección de los mejores materiales hasta los acabados más finos, nos aseguramos de que cada detalle cumpla con los más altos estándares, garantizando la satisfacción y durabilidad de nuestros productos.',
        
        'sustain_title' : 'Sostenibilidad',
        'sustain' : 'Nos comprometemos con la sostenibilidad y el respeto por el medio ambiente. Utilizamos madera de fuentes responsables y aplicamos prácticas ecológicas para reducir nuestro impacto ambiental, asegurando un futuro mejor para todos.',
        
        'contact_title' : '¡Hablemos de tus ideas!',
        'contact' : 'Estamos aquí para ayudarte a hacer realidad tus proyectos en madera. Completa el formulario con tu nombre, correo electrónico y un mensaje detallado sobre lo que necesitas. Nos pondremos en contacto contigo lo antes posible para discutir cómo podemos trabajar juntos.',

        'map_street' : ':)'
    }
    return render(request, 'myapp/index.html', context)
