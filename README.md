# Jouni CV

Jouni CV is a small Django project that powers a personal curriculum vitae website. It stores profile information, work experience, education and skills and renders them through a simple web interface.

## Setup

1. **Clone the repository** and move into the project directory.
2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Create a `.env` file** with environment variables:
   ```env
   SECRET_KEY=your_django_secret_key    # required
   DEBUG=False                          # optional, defaults to False
   ALLOWED_HOSTS=localhost,127.0.0.1    # optional, comma-separated
   ```
5. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```
6. *(Optional)* create an admin user:
   ```bash
   python manage.py createsuperuser
   ```

## Usage

Run the development server:

```bash
python manage.py runserver
```

Visit `http://localhost:8000/` to view the CV site and `http://localhost:8000/admin/` to manage content.

## License

This project is provided as-is without a specific license.

