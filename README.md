# Job Application Form built with Python Django
This app allows users to get baby development information by submitting their week in pregnancy and choice. 
User data will be stored in our database and users will receive baby development info by email. 
A microservice is used to scrape baby development information from https://www.whattoexpect.com/pregnancy/week-by-week/.

<p align="center">
    <img src="https://github.com/bingyingchu/baby-dev/blob/main/baby_dev/static/baby-dev.png">
<p>

#### To run this app locally, you can
Run the project locally
```python 
git clone https://github.com/bingyingchu/baby-dev.git
```
Migrate for the project
```python 
python manage.py makemigrations 
python manage.py migrate
```
Run the project
```python 
python manage.py runserver
```
Get admin access to manage database
```python 
python manage.py createsuperuser
```
You also need to run the microservice separately
```python 
python scraper.py
```
 