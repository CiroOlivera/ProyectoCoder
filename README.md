# ProyectoCoder
Este es mi proyecto para coder house

es una aplicacion web de la que se espera pueda funcionar como foro para una comunidad de deportistas

contiene funciones para las cuales es necesario registrar un usuario, modelo para el cual he usado
el modelo de autenticacion personalizado abstractUser. Se encuentra en los modelos de la app "socios"
para un usuario admin:  luego de crear un socio llamado "admin"
utilice este metodo para otorgarle privilegios para acceder al panel admin de django
python manage.py shell
    from socios.models import Socio
    usuario = Socio.objects.get(username='admin')
    usuario.is_superuser=True
    usuario.is_staff = True

la web permite subir articulos y crear actividades para que otros usuarios se inscriban
podran buscar en los articulos por titulo y por contenido

deje un requerimientos.txt con los paquetes del venv
pip install -r requerimientos.txt