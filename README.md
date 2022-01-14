<h1>pro-service</h1>
<p>This project is used to add a user to create one or more products. In each product, there is a user name, product price, product name and seller name . </p>

<h3>technologies I used :</h3>
<ul style="list-style-type:circle">
  <li>Python framework Django .</li>
  <li>Django Rest framework .</li>
  <li>PostgreSQL database .</li>
  <li>linter flake8 .</li>
</ul>

<h3>API documentation </h3>
<p>https://documenter.getpostman.com/view/13014200/UVXjJvrZ</p>

<h3>How to Install and Run the Project in windows :</h3>
<p>Create a virtual environment on the desktop, for example 'env' .</p>
<p>write this command in CMD to create it :- ' virtualenv env ' .</p>
<p>open folder 'env' and acvtivate virtualenv using this command : '.\Scripts\activate' .</p>
<p>clone my project using this command : git clone "https://github.com/werdani/pro-service.git" .</p>
<p>cd 'pro-service' and install requirments using this command : pip install requirment.txt .</p>
<p>now need to create database in PostgreSQL using this name 'productss' .</p>
<p>'USER': 'postgres', 'PASSWORD': 'postgres', 'HOST': 'localhost', 'PORT': '5432' .</p>
<p>need to makemigrations using this command in CMD : 'python manage.py makemigrations' .</p>
<p>need to migrate using this command in CMD : 'python manage.py migrate' .</p>
<p>now database is ready to add products, but now you need to create a superuser .</p>
<p>to create superuser write this command in CMD: 'python mange.py createsuperuser' . </p>


