install:

    pip install Celery flower
    

run:
- start celery: `celery worker -B -E -A tasks --loglevel=info -f /home/andrew/try-celery/celery.logs --detach`
- start flower: `flower --broker='amqp://user:password@127.0.0.1:5672/myvhost'`  
- kill: `pkill -f "celery worker"`
- if login refused error: read on (stackoverflow)[https://stackoverflow.com/questions/26811924/spring-amqp-rabbitmq-3-3-5-access-refused-login-was-refused-using-authentica/26820152]
- flower is available by default on --port=5555

params:
    
    --detach: start as daemon
    --beat or -B: start scheduler (aka cron)
    -f: write to logfile
    -E: Send task-related events so that tasks can be monitored using tools like flower    

