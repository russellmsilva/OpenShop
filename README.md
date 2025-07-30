# OpenShop

OpenShop is a Django-powered e-commerce platform supporting user-generated listings, admin-managed categorization, and robust cart logic. Though the frontend is currently in development, the backend includes authentication, form validation, media handling, and CI/CD workflows.

Screenshots of rendered HTML templates can be found in the "project_images" directory of this repository.

## Quick Project Setup

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

## Superuser Setup

To manage product categories and access admin-only features:

```bash
python manage.py createsuperuser
```

Log in at http://127.0.0.1:8000/admin/ and navigate to Category to create one-to-one category mappings for products.

## Media Storage

Product images uploaded by users are stored in media/, configured via Django’s MEDIA_URL and MEDIA_ROOT settings. Make sure the folder exists and is configured correctly in settings.py.

## SQLite Database

OpenShop uses SQLite for local development. Database migrations handle schema evolution and are tracked under migrations/ folders within each app.

## CI/CD and Testing

The GitHub Actions YAML file (.github/workflows/ci.yml) automates:

- Python dependency installation
- Synchronizing python versions between GitHub hosted runners and the project's Pipfile
- Running tests located in products/tests.py

This ensures consistent code quality across pushes and pull requests.

## User Features

- Users can sign up, log in, and post products through self-service flows
- Users can add items to carts, including products from different sellers
- Cart logic enforces single ownership rules (users cannot add products they have posted for sale to their cart)
- Authentication is handled in the account app, with session-based login/logout views

## Django App Architecture

| App      | Description                                 |
| -------- | ------------------------------------------- |
| products | Product models, gallery views, and listings |
| shipping | Buyer address validation                    |
| home     | Homepage and general views                  |
| account  | User authentication and session controls    |
| cart     | Cart logic, single-owner enforcement        |
| category | Admin-controlled product categorization     |

## Future Roadmap

Future Roadmap

- Cryptocurrency integration for transactions and wallet management
- User purchase/sale history for profile-based audit trails
- Finalize checkout logic, including quantity deduction and sold-out status
