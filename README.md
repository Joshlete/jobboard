# Job Board

Job Board is a streamlined, Django-based web application designed to bridge the gap between job seekers and employers. It enables users to view and apply for job listings curated by various companies. The application emphasizes ease of use and functionality, incorporating full CRUD (Create, Read, Update, Delete) capabilities that allow job seekers to apply to their preferred listings and employers to manage their postings effortlessly.

## Usage

After launching the server, you can interact with the application via the following URLs:

- **Homepage**: Navigate to `http://127.0.0.1:8000/` to view and apply to the available job listings.
- **Admin Panel**: Access `http://127.0.0.1:8000/admin` to manage job postings.
  - Default admin credentials:
    - Username: `admin`
    - Password: `jobboard`

## Environment

These are the versions used for this application. Before you begin, ensure you have met the following requirements:

- Ubuntu 22.04 on WSL2
- python(3.12)
- pip(24.0)
- virtualenv(20.25.3) or venv

## Installation

1. Clone the repository to your local machine
```
git clone git@github.com:Joshlete/jobboard.git
```

2. Create your virtual environment
```
virtualenv env
```

3. Enter your virtual environment
```
source env/bin/activate
```

5. Navigate to the cloned directory
```
cd jobboard
```

6. Install Django Debug Toolbar
```
pip install django-debug-toolbar
```
## Local Deployment

1. Run the server
```
python manage.py runserver
```

2. Run migration (optional)
```
python manage.py migrate
```

## License

This project is licensed under the [MIT License](LICENSE).

