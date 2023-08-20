# Madde22_Backend_Challenge  
# Brewery Project  

Welcome to the Brewery Project! This project is a Django web application that allows users to interact with breweries and perform various actions.  
It includes user registration, login, and interaction with brewery data through RESTful APIs.  
## API Endpoints  

### User Registration  

Register a new user.  

- **URL:** `/api/register/`  
- **Method:** `POST`  
- **Request Body:**  
  ```json  
  {  
    "username": "your_username",  
    "password": "your_password"  
  }  
Response: User registration successful  
User Login  
Log in as an existing user.  

URL: /api/login/  
Method: POST  
Request Body:  
{  
  "username": "your_username",  
  "password": "your_password"  
}  
Response: Login successful, returns an authentication token  
Breweries List   
Retrieve a list of breweries.  

URL: /api/breweries/  
Method: GET  
Response: List of breweries  

Getting Started  
Clone this repository: git clone https://github.com/your-username/brewery-project.git  
Change into the project directory: cd brewery-project  
Create a virtual environment: python -m venv venv  
Activate the virtual environment:  
On Windows: venv\Scripts\activate  
On macOS/Linux: source venv/bin/activate  
Install dependencies: pip install -r requirements.txt  
Run migrations: python manage.py migrate  
Start the development server: python manage.py runserver  
Access the application in your web browser at http://127.0.0.1:8000  

## Urls  
Registration: http://127.0.0.1:8000/api/register/  
Login: http://127.0.0.1:8000/api/login/  
Breweries API: http://127.0.0.1:8000/api/breweries/  
Swagger UI: http://127.0.0.1:8000/swagger/  
