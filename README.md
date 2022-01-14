<h1>pro-service</h1>
<p>This project is used to add a user to choose one or more products. In each product, there is a user name, product price, and seller name . </p>

<h3>technologies I used :</h3>
<ul style="list-style-type:circle">
  <li>Python framework Django .</li>
  <li>Django Rest framework .</li>
  <li>PostgreSQL database .</li>
  <li>linter flake8 .</li>
</ul>
<h3>How to Install and Run the Project in windows :</h3>
<h4>Create a virtual environment on the desktop, for example 'env' .</h4>
<h4>write this command in CMD to create it :- ' virtualenv env ' .</h4>
<h4>open folder 'env' and acvtivate virtualenv using this command : '.\Scripts\activate' .</h4>
<h4>clone my project using this command : git clone "https://github.com/werdani/pro-service.git" .</h4>
<h4>cd 'pro-service' and install requirments using this command : pip install requirment.txt .</h4>
<h4>now need to create database in PostgreSQL using this name 'productss' .</h4>
<h4>'USER': 'postgres', 'PASSWORD': 'postgres', 'HOST': 'localhost', 'PORT': '5432' .</h4>
<h4>need to makemigrations using this command in CMD : 'python manage.py makemigrations' .</h4>
<h4>need to migrate using this command in CMD : 'python manage.py migrate' .</h4>
<h4>now database is ready to add products, but now you need to create a superuser .</h4>
<h4>to create superuser write this command in CMD: 'python mange.py createsuperuser' . </h4>
