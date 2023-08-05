Sure, here is the README.md file:

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
git clone https://github.com/<>/Myproduct.git
```

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


## Usage

The API is documented using Swagger. You can access the documentation at `http://localhost:8000/docs/`.

## Examples

Here are some examples of how to use the API:

* Get all products:


curl http://localhost:8000/product/products/
```

* Create a new product:

```
curl -X POST -H "Content-Type: application/json" -d '{
  "name": "Product 1",
  "description": "This is a product."
}' http://localhost:8000/product/products/
```

* Update a product:

```
curl -X PUT -H "Content-Type: application/json" -d '{
  "name": "Product 1 (updated)",
  "description": "This is a product (updated)."
}' http://localhost:8000/product/products/1/
```

* Delete a product:

```
curl -X DELETE http://localhost:8000/product/products/1/
```

## License

This project is licensed under the MIT License.
```

I hope this is helpful! Let me know if you have any other questions.