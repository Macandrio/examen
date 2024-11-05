# examen

atributo

CharField, IntegerField, EmailField, DateField, DateTimeField,
BooleanField, DurationField, TextField, FloatField, DecimalField

parametros

1. max_length = 100  => maximo de caracteres 100
2. verbose_name="Aeropuerto" => como se ve en el administrador en el formulario
3. choices=CIUDADES  =>  es para que solo pueda elejir una opcion del array
4. default='ES'  => por defecto poge ES si no pone nada
5. blank=True  => puede dejar el campo en blanco
6. auto_now_add=True  => si no pones nada pone la hora actual
7. error_messages={'blank': 'Este campo no puede estar vacío.',}  =>  pone un mensaje de error
8. db_column='Volando' => te cambia el nombre de la columna de la base de datos
9. editable=False  => no se puede editar en el admin
10. validators=[ MaxValueValidator(999999999)] => valida si el numero es menor al puesto
11. unique=True => el valor es unico
12. max_digits=6 => solo puede poner 6 dijitos contando con los dos de decimales
13. decimal_places=2 => solo puede poner 2 decimales.

comandos 

python3 -m venv myvenv
source myvenv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt

python manage.py migrate
python manage.py makemigrations examen
python manage.py migrate examen
python manage.py seed examen --number=20
python manage.py dumpdata --indent 4 > examen/fixtures/datos.json
python manage.py loaddata examen/fixtures/datos.json

python manage.py createsuperuser
python manage.py runserver
--------------------------------------------------------


Las urls deben funcionar y mostrar resultados. En el caso de que de error o no muestre resultado alguno no será válida.


