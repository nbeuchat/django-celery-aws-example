# django-celery-aws-example
Test project on how to use Django and Celery with AWS. This is a **work-in-progress**.

I followed the following articles to set this project up:

* http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html#django-first-steps
* http://docs.celeryproject.org/en/latest/getting-started/brokers/sqs.html

# Setup
## Project creation and setup
```
conda create -n djangocelery python=3.4
activate djangocelery
#Unix:
#source activate djangocelery
```

Install packages: 

```
pip install django celery boto3 django-celery
```

## AWS

On AWS, you need to do the following:

* Create a SQS queue
* Create an IAM user with full rights to AWS

**TODO**

* Setup elastic beanstalk

## Django settings

The project requires credentials to AWS. Create a `local_settings.py` file in the `app/app` folder with the following lines:

```
CELERY_BROKER_USER = '**aws_access_key_id**' 
CELERY_BROKER_PASSWORD = '**aws_secret_access_key**'
```

# Rununing
## Locally
In one terminal, run the django server:

```
cd app
python manage.py runserver
```

In another terminal, start the worker process:

```
celery -A proj worker -l info
```

## AWS

**TO-DO**

* How to deploy and run an app on AWS (Elastic Beanstalk) with `eb deploy`
* Troubleshooting
