# 🛒 API de Productos - Django REST Framework

Este proyecto es una API REST construida con **Django** y **Django REST Framework (DRF)** que permite gestionar productos y categorías.

Incluye operaciones CRUD completas, relaciones entre entidades y una estructura base lista para escalar a un backend profesional.

---

## 🚀 Tecnologías utilizadas

* Python 3.x
* Django
* Django REST Framework
* PostgreSQL en Docker

---

## 📁 Estructura del proyecto

```
findit/
│── findit/          # Configuración principal del proyecto
│── api/             # App principal
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│── manage.py
│── requirements.txt
```

---

## ⚙️ Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/sebas0040/bk_findIt.git

```

---

### 2. Crear entorno virtual

```bash
python -m venv venv
```

Activar entorno:

* Windows:

```bash
venv\Scripts\activate
```

* Linux / Mac:

```bash
source venv/bin/activate
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 4. Levantar la base de datos con Docker

```bash
docker compose up -d db
```

El contenedor crea automaticamente la base de datos `findit_db`.

Variables usadas por defecto:

```env
DB_NAME=findit_db
DB_USER=postgres
DB_PASSWORD=POSTGRES1
DB_HOST=localhost
DB_PORT=5432
```

Si necesitas cambiarlas, copia `.env.example` como `.env` y ajusta los valores.

---

### 5. Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Ejecutar servidor

```bash
python manage.py runserver
```

Servidor disponible en:

👉 http://127.0.0.1:8000/

---

## 📦 Archivo requirements.txt

Ejemplo de contenido:

```
Django>=4.0
djangorestframework>=3.14
```

---

## 📚 Endpoints disponibles

### 🔹 Productos

| Método | Endpoint             | Descripción        |
| ------ | -------------------- | ------------------ |
| GET    | /api/productos/      | Listar productos   |
| POST   | /api/productos/      | Crear producto     |
| GET    | /api/productos/{id}/ | Obtener producto   |
| PATCH  | /api/productos/{id}/ | Actualizar parcial |
| DELETE | /api/productos/{id}/ | Eliminar producto  |

---

### 🔹 Categorías

| Método | Endpoint         | Descripción       |
| ------ | ---------------- | ----------------- |
| GET    | /api/categorias/ | Listar categorías |
| POST   | /api/categorias/ | Crear categoría   |

---

## 🧪 Casos de uso (Ejemplos)


---

### ✅ 1. Crear un producto

```http
POST /api/productos/
Content-Type: application/json

{
  "nombre": "Laptop",
  "precio": 2500,
  "categoria": 1
}
```

---

### ✅ 2. Listar productos

```http
GET /api/productos/
```

---

### ✅ 3. Actualizar precio (PATCH)

```http
PATCH /api/productos/1/
Content-Type: application/json

{
  "precio": 3000
}
```

---

### ✅ 4. Eliminar producto

```http
DELETE /api/productos/1/
```

---



---

## 🔥 Funcionalidades actuales

* CRUD completo de productos
* API navegable de Django REST Framework

---

## 🚀 Mejoras futuras

* Autenticación con JWT
* Permisos por usuario
* Filtros y paginación
* Soft delete
* Documentación con Swagger

---

## 👨‍💻 Autor

Proyecto desarrollado como práctica de backend con Django REST Framework.
Deivid Sebastian Armero Gualguan
Julián Alejandro Flórez Morán
Marlon Jesus Hernandez Gomez

---

## 📄 Licencia

Este proyecto es de uso libre para aprendizaje.
