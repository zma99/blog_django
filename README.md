# blog_app

blog_app es una aplicación web desarrollada con Django que permite gestionar publicaciones y categorías con control de acceso por roles. Está diseñada para ser modular, segura y fácilmente extensible, ideal para entornos educativos, técnicos o personales donde se requiere administración eficiente de contenido.

Características principales
- Autenticación de usuarios con roles diferenciados
- CRUD completo para posts, categorías y usuarios
- Roles: Admin (admin), Editor (editor), Lector (reader)
- Estructura modular para escalar y adaptar fácilmente

⚙️ Tecnologías utilizadas
- Django 4.x
- HTML / CSS / JS básico
- Tailwind
- MySQL


🚀 Instalación rápida
git clone https://github.com/tu_usuario/blog_app.git
cd blog_app
python -m venv venv
source venv/bin/activate      # en Linux/macOS
venv\Scripts\activate         # en Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver



