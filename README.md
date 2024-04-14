# Part1-ecommerce
E-commerce Backend System Development: A backend system for an e-commerce platform using Python and Django. The system should support product management, user orders, and an analytics dashboard.

## Description
* User Authentication
    1. Implement user authentication with email verification, password reset, and OAuth2 integration for third-party logins.
    2. Use JWT tokens for session management.

* Product Management
    1. Create a CRUD interface for admin users to manage products, including adding, updating, deleting, and listing products.
    2. Implement product categories and allow products to be associated with multiple categories.

* Shopping Cart and Order Processing
    1. Enable users to add products to a shopping cart and place orders.
    2. Update product stock quantities based on orders.
    3. Process orders and maintain order history for users.
* RESTful API and Documentation
    1. Develop RESTful API endpoints for all functionalities.
    2. Provide comprehensive API documentation using Swagger or a similar tool.
* Database Design
    1. Design a schema using MySQL, focusing on normalization and efficient data retrieval.


## Techs Used
* Python, Django, Django Rest Framework, MySQL


## Running The Project
1. Clone the project
2. Install Python (if not already installed)
3. Create and activate a virtual environment
4. Install Django (pip install django)
5. Install Django Rest Framework (pip install django djangorestframework djangorestframework-simplejwt django-rest-auth) 
6. Install Django allauth (pip install django-allauth)
7. Install MySQL client library (pip install pymysql)
8. Install library for image processing in Python: (python -m pip install Pillow)
9. Install any additional dependencies (python3 -m pip install --upgrade pip, pip install django-ratelimit, pip install ...)
10. Run requirements.txt (pip install -r requeriments.txt)
11. Start the development server (python manage.py runserver)
12. For Migrations: run these two commands("python manage.py makemigrations" & "python manage.py migrate")
13. Create superuser for Django Admin: (python manage.py createsuperuser)



## Usage
1. Create Super-User as an Admin for Django administration Panel Access
2. Login with your Admin credentials
3. Add Product by adding description, price, stock-quantity, categories, and product image
4. Admin can also create multiple category and can associate multiple categories to single product.

5. Go to the URL: http://127.0.0.1:8000/
6. Any User can signup, login or logout and can reset user password by using mailId
7. User can Add products to cart by clicking on "Add to cart" button 
8. User can checkout items after adding product into cart by cliecking on cart icon
9. During checkout user can increase and decrease the product quantity by using arrow_up and arrow_down buttons
10. Process Order by clicking on "Continue" button.
11. After Order Creation: It will redirect to the Order Listing Page.


## Postman Collection for the APIS
* Find the **Postman** collection for the apis [Here](https://api.postman.com/collections/3660213-14e822c6-bf99-4f84-a04b-1174f282b20e?access_key=PMAT-01HVFB8VBHNMT6KWAM2CP4RF2N)
  
## DB Schema:
Check the uploaded png fine named as **DB Schema.png** or 
