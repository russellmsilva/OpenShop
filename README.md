# OpenShop

A template for a web application that allows users to buy and sell products using cryptocurrency

Note: Stores media such as pictures in the media folder within the project base directory

## Project Setup

Follow these steps to get the OpenShop development environment up and running.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/OpenShop.git
cd OpenShop
```

### 2. Install Dependencies

Make sure you have Pipenv installed. Then run:

```bash
pipenv install --dev
```

This will install all dependencies listed in the Pipfile, including Django.

### 3. Activate the Virtual Environment

```bash
pipenv shell
```

### 4. Run the Development Server

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser to view the app.
