# Django Blog Application with Django Rest Framework

This project is a Django-based blog application that utilizes Django Rest Framework (DRF) to provide a RESTful API for interacting with blog posts.

## Features

- **Blog Post Management:**
  - Create, read, update, and delete blog posts.
  - Categorize posts.
  - Implement user authentication and authorization for post management.
- **RESTful API:**
  - Expose blog posts and categories through a well-defined API.
  - Support JSON format for data exchange.
  - Implement API versioning (optional).
- **User Authentication:**
  - User registration and login.
  - Token-based authentication using DRF's `TokenAuthentication` or JWT.
  - Permission based access to create, update, and delete posts.
- **Search and Filtering:**
  - Search blog posts by title or content.
  - Filter posts by category or author.
- **Pagination:**
  - Implement pagination for listing blog posts to improve performance.
- **Testing:**
  - Includes unit and integration tests for both Django models and DRF API endpoints.

## Technologies Used

- **Django:** Web framework.
- **Django Rest Framework (DRF):** Toolkit for building Web APIs.
- **Python:** Programming language.
- **PostgreSQL:** Database.
- **Git:** Version control.
- **pip:** Package manager.

## Prerequisites

- Python 3.x
- pip
- Git

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd django-blog-drf
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure the database:**

    - Edit the `settings.py` file to configure your database settings.
    - if using SQLite, the default will create a db.sqlite3 file.

5.  **Run migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

8.  **Access the API:**

    - Open your browser or use a tool like Postman to access the API endpoints.
    - The API will be accessible at `http://127.0.0.1:8000/api/`.
    - The Django admin interface will be at `http://127.0.0.1:8000/admin/`.

## API Endpoints

- `/api/posts/`: List and create blog posts.
- `/api/posts/{id}/`: Retrieve, update, and delete a specific blog post.
- `/api/categories/`: List and create categories.
- `/api/categories/{id}/`: Retrieve, update, and delete a specific category.
- `/api/users/register/`: Register a new user.
- `/api/users/login/`: Login and obtain an authentication token.

## Running Tests

```bash
python manage.py test
```
