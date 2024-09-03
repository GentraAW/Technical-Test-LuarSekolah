# Technical-Test-LuarSekolah
python3 -m venv venv
source venv/bin/activate

cd Technical-Test-LuarSekolah
pip install django djangorestframework psycopg2-binary djangorestframework-simplejwt

django-admin startproject training_system

python manage.py startapp users

python manage.py makemigrations users
python manage.py migrate

python manage.py runserver 8000

--Logic agar postgre 12 berjalan--
venv/lob/python3.10/site-packages/django/db/backends/postgresql/base.py
def check_database_version_supported(self):
        if self.get_database_version() < (12, 0):
            raise NotSupportedError("PostgreSQL 12 or later is required.")


python manage.py loaddata users/fixtures/initial_data.json
python manage.py loaddata users/fixtures/user_training_data.json
