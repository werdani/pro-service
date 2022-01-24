<h1>pro-service</h1>
<p>This project is used to add a user to create one or more products. In each product, there is a user name, product price, product name and seller name . </p>

<h3>technologies I used :</h3>
<ul style="list-style-type:circle">
  <li>Python framework Django .</li>
  <li>Django Rest framework .</li>
  <li>PostgreSQL database .</li>
  <li>linter flake8 .</li>
  <li>Docker .</li>
</ul>

<h3>API documentation </h3>
<p>https://documenter.getpostman.com/view/13014200/UVXjJvrZ</p>

<h3>How to Install and Run the Project in windows :</h3>
<ul style="list-style-type:circle">
  <li>Create a virtual environment on the desktop, for example 'env' .</li>
  <li>write this command in CMD to create it :- ' virtualenv env ' .</li>
  <li>open folder 'env' and acvtivate virtualenv using this command : '.\Scripts\activate' .</li>
  <li>clone my project using this command : git clone "https://github.com/werdani/pro-service.git" .</li>
  <li>cd 'pro-service' and install requirments using this command : pip install requirment.txt .</li>
  <li>now need to create database in PostgreSQL using this name 'productss' .</li>
  <li>'USER': 'postgres', 'PASSWORD': 'postgres', 'HOST': 'localhost', 'PORT': '5432' .</li>
  <li>need to makemigrations using this command in CMD : 'python manage.py makemigrations' .</li>
  <li>need to migrate using this command in CMD : 'python manage.py migrate' .</li>
  <li>now database is ready to add products, but now you need to create a superuser .</li>
  <li>to create superuser write this command in CMD: 'python mange.py createsuperuser' . </li>
</ul>
