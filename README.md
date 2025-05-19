# Employee Management System
A Dockerized Django + PostgreSQL application for managing employees, departments, attendance, and performance reviews with role-based access control.

## ✅ Features
- **Roles Supported** : admin, hr, employee
- **Session-Based Authentication** : For template views
- **JWT Authentication** : For DRF APIs
- **Analytics Dashboard** : View employee stats via Chart.js
- **Attendance Management** : HR/Admin can mark attendance directly
- **PostgreSQL Database**
- **Dockerized Setup** : Easy to deploy and test

## 📦 Requirements

- Docker & Docker Compose
- Python 3.12+
- PostgreSQL 16
- Git (optional)

## 🛠️ Setup Instructions
## 1. Clone the Repository
```bash
git clone https://github.com/yourusername/employee_project.git 
cd employee_project
```
## 2. Create .env File
Create a .env file in the root directory:
```bash
DATABASE_URL=postgres://django_user:django_password@db:5432/employee_db
DEBUG=True
```
## 3. Install Dependencies
Make sure requirements.txt contains:
```txt
Django>=4.2,<5.0
djangorestframework>=3.15,<4
psycopg2-binary>=2.9,<3.0
gunicorn>=21,<22
python-decouple>=3.8,<4
dj-database-url>=0.5,<1.0
djangorestframework-simplejwt>=5.3,<6
drf-spectacular>=0.27,<0.28
django-filter==23.2
```
## 🐳 Run Using Docker
Build and Start Containers
```powershell
docker-compose up -d --build
```
This will:

- Set up PostgreSQL database
- Install all dependencies
- Start Django development server at http://localhost:8000/

### Apply Migrations
```powershell
docker-compose exec web python manage.py migrate
```
### Seed Sample Data (HR, Employees, Departments, Attendance)
```powershell
docker-compose exec web python manage.py seed_data
```
## 🚀 Accessing the App
Template Views
| URL    | Description |
| -------- | ------- |
| http://localhost:8000/login/  | Login page    |
| http://localhost:8000/signup/ | Signup (if enabled)    |
|http://localhost:8000/home/  | Home dashboard  |
|http://localhost:8000/analytics/|View analytics (HR/Admin only)|
|http://localhost:8000/attendance/|	Mark attendance (HR/Admin only)|

## API Endpoints (JWT Auth Required)
| URL    | Description |
| -------- |---------|
| POST /api/token/ |Get JWT token |
| GET /api/employees/ | List employees   |
|GET /api/departments/|	Department stats|
|GET /api/attendance/|	Attendance records|
|GET /api/performance/|	Performance reviews |
#### Use headers:

```
Authorization: Bearer <your-access-token>
```

## 📊 Analytics Dashboard
#### HR and Admin users can access real-time charts:

- Bar chart: Employees per department
- Line chart: Monthly attendance trends
- Table view: Daily attendance report

## 🧾 Management Commands
To seed realistic data:
```bash
docker-compose exec web python manage.py seed_data
```
 ## Run Unit Tests
 ```bash
 docker-compose exec web python manage.py test
 ```
 #### Tests cover:

- Login flow
- Role-based access
- Attendance/performance models
- Custom manager logic

## 📄 Swagger/OpenAPI Docs
Visit:
👉 http://localhost:8000/api/swagger/

To see interactive documentation of all available API endpoints.

## 🧹 Clean Up
Stop containers:
```powershell
docker-compose down
```
Rebuild cleanly:
```powershell
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```
- 🧰 Optional: Use Without Docker
If not using Docker:
```Bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Then open:
👉 http://localhost:8000/login/
## 🛡️ Role-Based Access
| Role     | Can Access |
| -------- |---------|
| employee | /home/ , limited access   |
|hr|	/analytics/,  /attendance/|
|admin|	All features|

## 🧩 Technologies Used
- Backend : Django 4.2.x
- Database : PostgreSQL
- Authentication : JWT (djangorestframework-simplejwt)
- UI : Django Templates + Chart.js
- Filtering : django-filter==23.2
- Containerization : Docker + Docker Compose