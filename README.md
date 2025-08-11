# blog_app

blog_app es una aplicación web desarrollada con Django que permite gestionar publicaciones y categorías con control de acceso por roles. Está diseñada para ser modular, segura y fácilmente extensible, ideal para entornos educativos, técnicos o personales donde se requiere administración eficiente de contenido.

Características principales
- Autenticación de usuarios con roles diferenciados
- CRUD completo para posts, categorías y usuarios
- Post con texto enriquecido
- Roles: Admin (admin), Moderador (moderator), Editor (editor), Lector (reader)
- Estructura modular para escalar y adaptar fácilmente

⚙️ Tecnologías utilizadas
- Django 5.2.4
- HTML / CSS / JS básico
- Tailwind
- MySQL
- CKEditor-5


🚀 Instalación rápida
1. git clone https://github.com/tu_usuario/blog_app.git
2. cd blog_app
3. python -m venv venv
4. 
    source venv/bin/activate      # en Linux/macOS
    venv\Scripts\activate         # en Windows

5. pip install -r requirements.txt
6. python manage.py migrate
7. python manage.py runserver



⚠️ NOTA: Aplicación en fase de desarrollo.