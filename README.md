# django-celery-aws-example
Test project on how to use Django and Celery with AWS.


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
