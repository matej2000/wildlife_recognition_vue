# Wildlife_recognition_django

Extension of my master's thesis, which enables easy use of models trained during my research. This repository contains the backend in Django. It provides user authentication and an endpoint for image upload. The rest of the project is available here:
- [Frontend](https://github.com/matej2000/wildlife_recognition_vue)
- [WS-DETR model](https://github.com/matej2000/rtdetr_pytorch_wsdetr)

## Prerequisites

Ensure you have the following installed:

- Python (>= 3.8)
- pip
- virtualenv (optional but recommended)
- PostgreSQL or SQLite (default)

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/matej2000/wildlife_recognition_django.git
cd wildlife_recognition_django
```

### 2. Create and Activate Virtual Environment (Recommended)
```sh
conda create --name myenv python=3.8
conda activate myenv 
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Apply Migrations
```sh
python manage.py migrate
```

### 5. Create a Superuser (Optional)
```sh
python manage.py createsuperuser
```

### 6. Run the Server
```sh
python manage.py runserver