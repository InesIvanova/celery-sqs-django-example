1. Install requirements
```
pip install -r requirements.txt
```
2. Migrate
```
python manage.py makemigrations
python manage.py migrate
```
3. Start project

If you want to run with celery you need to install:
```
python -m pip install celery
```
Install redis on your local machine OR use docker image. Once installed locally we need to install it for python venv as well:
```
python -m pip install redis
```

Start redis locally 
```
redis-server
```

Start celery workers:
```
python -m celery -A {your_project_name_here} worker
```



If you want to work with SQS + lambda instead for async tasks
1. Create AWS account
2. Create SES sandbox account
3. Register identities
4. Create SQS
5. Create lambda
6. Add policy to lambda for SQS and SES - SESFullAccess, SQSFullAccess
7. Follow the video for the respective lambda code and triggering sqs configuration