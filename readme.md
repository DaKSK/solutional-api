## The Solution

I chose to solve the provided problem with Django Rest Framework. The reasons for this are that
DRF provides all the necessary tools for doing this, plus has the benefit of being executed to
run from ports like this:
python manage.py runserver 7000
While solving the issue I first needed to use the solution to understand the logic. Playing around
with the API I saw some key characteristics like the UUID requirement and also the need for a
table which seems a little "hidden" due the to naming of OrderItem to products.
From there I focused on getting the data models right. I landed on Product, Order, OrderItem as
my models. With the OrderItem being the child of both Product and Order.
Serializers and REST class based views took some looking into to find the proper tools to
recreate the provided API.
An issue emerged which I noticed prior to providing an estimation was that the replaced_with field
endpoint doesn't work as intended. The instructions were to copy exactly, but I did provide in the
comments a possible solution that would fix the issue, depending on how it's actually meant to work.
It's not too obvious what is that field representing or how it should behave, so further specification is needed.
After testing all the endpoints, I found an issue with the provided solution. The Order status, should be an
choice field instead of just a varchar. Unfortunately I ran out of time to make the fix.

## Running the solution:

At the moment only development version of Django is ready to run. Not ready to deploy to production.

1. Download the code and database file
2. Django 4.0 requires at least Python 3.9
3. Install dependencies with pip install based on requirements.txt
4. Run server with python manage.py runserver
5. API now available on localhost

## THE TASK:

1. It has a list of products;- DONE - available in database file
2. Products can be added to the order; - DONE
3. Products can be modified within the order; - DONE
4. Products can be replaced when assembled. - Replacement product operation unknown


## API Endpoints

Here's all the API endpoints with usage examples you need to implement:
https://homework.solutional.ee/api/
* GET /api/products - list of all available products
    curl https://homework.solutional.ee/api/products
* POST /api/orders - create new order
    curl -X POST https://homework.solutional.ee/api/orders
* GET /api/orders/:order_id - get order details
    curl https://homework.solutional.ee/api/orders/:order_id
* PATCH /api/orders/:order_id - update order
    curl -X PATCH --data '{"status": "PAID"}' \
      https://homework.solutional.ee/api/orders/:order_id
* GET /api/orders/:order_id/products - get order products
    curl https://homework.solutional.ee/api/orders/:order_id/products
* POST /api/orders/:order_id/products - add products to order
    curl --data '[123]' -H "Content-Type: application/json" \
      https://homework.solutional.ee/api/orders/:order_id/products
* PATCH /api/orders/:order_id/products/:product_id - update product quantity
    curl -X PATCH --data '{"quantity": 33}' -H "Content-Type: application/json" \
      https://homework.solutional.ee/api/orders/:order_id/products/:product_id
* PATCH /api/orders/:order_id/products/:product_id - add a replacement product
    curl -X PATCH --data '{"replaced_with": {"product_id": 123, "quantity": 6}}' -H "Content-Type: application/json" \
      https://homework.solutional.ee/api/orders/:order_id/products/:product_id

## Goals

1. Implement all API endpoints described above; - DONE
2. For `GET /api/products` endpoint keep products list exactly the same as is
   done in the reference API - same products with same attributes (even `id`); - DONE-> database file included
3. Make it possible to configure listening port number of the application without any need to change the code; - DONE by default when using Django
4. Before starting actual development, provide us with an estimation of when this task is going to be ready. - DONE estimation for 10.01.22 provided 03.01.22