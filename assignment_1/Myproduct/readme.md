```
# Myproduct

This is a simple REST API for managing products.

## Requirements

* Python 3.8+
* Django 4.1+
* Django REST Framework 3.13+
* Simple JWT 4.6.0+

## Installation

1. Clone the repository:

```
https://github.com/vr-vinayak/Python-Django-Assingments.git```

2. Install the requirements:

```
pip install -r requirements.txt
```

3. Create a `.env` file and add the following environment variables:

```
SECRET_KEY=your_secret_key
```

4. Run the development server:

```
python manage.py runserver


## Examples

Here are some examples of how to use the API:


* Get Authentication Token for user:

1. Create superuser: 
```
python manage.py createsuperuser
```

2. Get user token:
```
curl --location 'http://127.0.0.1:8000/product/user-login/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "<email>",
    "password": "<passsword>"
}'
```

* Get all products:

```
curl --location 'http://127.0.0.1:8000/product/products/' \
--header 'Authorization: Bearer <token>'```

* Create a new product:

```
curl --location 'http://127.0.0.1:8000/product/products/add-product/' \
--header 'Authorization: Bearer <token>' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Milk4",
    "description": "Milk6",
    "price": 34.99,
    "quantity": 9
}'
```

* Update a product:

```
curl --location --request PUT 'http://127.0.0.1:8000/product/products/63c954f5-f7a6-4e2e-94a2-9744f5d89f1d/update-product/' \
--header 'Authorization: Bearer <token>' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Milk",
    "description": "Milk6",
    "price": 34.99,
    "quantity": 9
}'
```

* Delete a product:

```
curl --location --request DELETE 'http://127.0.0.1:8000/product/products/63c954f5-f7a6-4e2e-94a2-9744f5d89f1d/delete-product/' \
--header 'Authorization: Bearer <token>'
```

## License

This project is licensed under the MIT License.
```

I hope this is helpful! Let me know if you have any other questions.
