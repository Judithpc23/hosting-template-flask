# Template 3 – Aplicación Flask (Python + Gunicorn)

Este repositorio es parte de la plataforma de hosting basada en contenedores para **Estructura del Computador II**.  
Está configurado como **Template Repository**, permitiendo que cada estudiante genere su propio backend Flask.

---

## 🌐 ¿Qué contiene este template?

Una aplicación básica en **Flask**, que incluye:

- Ruta principal `/` rendereando una plantilla HTML
- Ruta dinámica `/saludo/<nombre>`
- Soporte de plantillas con **Jinja2**
- `Dockerfile` con Gunicorn como servidor de producción
- Puerto interno: **8000**

Ideal para:
- APIs simples
- Backends ligeros
- Ejemplos de vistas dinámicas
- Prototipos tipo MVC

---

## 🚀 Cómo usar este repositorio como Template

1. En la parte superior, haz clic en **“Use this template”**.
2. Selecciona **“Create a new repository”**.
3. Crea un repo en tu cuenta personal.
4. Clónalo:
    ```bash
    git clone https://github.com/<tuUsuario>/<tuNuevoRepo>.git
    cd <tuNuevoRepo>
    
5. (Opcional) Instala dependencias localmente:

        pip install -r requirements.txt
        python app.py

6. Personaliza rutas y plantillas:

    Edita `app.py`
    Edita `templates/index.html`

7. Sube los cambios:
   
        git add .
        git commit -m "Personalizo el template Flask"
        git push
8. Luego registra la URL del repositorio en la plataforma de hosting.
