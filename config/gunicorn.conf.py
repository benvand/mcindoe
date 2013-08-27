bind=["127.0.0.1:8000",]
workers=2
accesslog="/var/log/gunicorn.access.log" 
errorlog="/var/log/gunicorn.error.log" 
daemonize=True
