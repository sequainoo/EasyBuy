# EasyBuy
---
EasyBuy is a phone shop. Is a translation of the way my brother operates his phone business.
The flow of the platform mimics a scenario where you visit a local phone shop.
You browse, with the option of selecting multiple items and then checking out.
Customers are not expected to login with the shop to make a purchase.

You are required to provide an email, name, and address for first time buyers and only email for subsequent shopping. it is neccessary to get these information to ship orders to the customer.
So the next time after the purchase is not going to be a hustle.
You get couple Payment options, by card, bank and mobile money.

### Click [Here](http:/easybuy.digital:8080) to shop with us.
<br>

## The Application Flow And Usage
---
- ### The front page allows browsing through a list of phones. Clicking on any takes you to the detail page of the phone.
- <img src="./readme_img/product_list.JPG" width="100%">
- ### On the detail page two options are presented, `Add a phone to the cart and continue browsing` or `order the phone as a singleton`. either options allows specification of quantity of phone to include.
- <img src="./readme_img/product_detail.JPG" width="100%">
- ### If first option is choosen you make your order on the `cart page`.
- ### An order is created for the customer once the `checkout` button is clicked and a page to collect your payment and address(first timers) is displayed.
- <img src="./readme_img/checkout.JPG" width="100%">
- ### Customer then fills in the address information and finally pay for the order.
- ### A page is displayed about the success or failure of the payment.
- ### After successful payment order is processed and shipped.

## Tech Stack
---
>- Ubuntu server 20.04
>- MySQL Server
>- nginx web server
>- gunicorn application server
>- Python 3
>- Flask Backend Framework
>- SQLAlchemy

## Installation
---
### Illustration on ubuntu 20.04.
> Python3 Setup
>- `sudo apt-get install -y python3 python3-pip`
>- `git clone https://github.com/sequainoo/EasyBuy.git easybuy`
>- `cd easybuy`
>- `pip3 install virtualenv`
>- `virtualenv venv .`
>- `source ./venv/bin/activate`
>- `pip install -r requirements.txt`
>- `export MYSQL_HOST=database_host`
>- `export EASYBUY_MYSQL_DB=database_name`
>- `export EASYBUY_MYSQL_USER=user_name`
>- `export EASYBUY_MYSQL_PWD=passwd`
>- `sudo --preserve-env gunicorn --bind 0.0.0.0:5000 web_app.app:app`

> NGINX Setup
>- `sudo apt-get install -y nginx`
>- start nginx as proxy to port 5000
>- `sudo nano /etc/nginx/sites-available/default`
>- Add `location /static/ {alias path_to_your_static_folder}`
>- Add `location /product-images/ {alias /var/easybuy/phone_image_uploads/;}`
>- `sudo nginx -t` to make sure server is right with config
>- `sudo service nginx start`

> MySQL Setup
>- `sudo apt-get install -y mysql-server`
>- `sudo service mysql start`
>- create database and user with the right privileges on all tables

<br>

## Contributing
---
> Comments and Improvements? Please create a Github issues.

<br>

## Author: [Gideon Quainoo](https://twitter.com/gideonme)
