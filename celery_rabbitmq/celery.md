install:

    pip install Celery flower
    
    
run:
- start **celery**: 
    * `celery worker -B -E -A tasks --loglevel=info -f /home/andrew/try-celery/celery.logs --detach`
    * `celery multi start 4 -B -E -A tasks -Q:1 first -Q:2 second -Q:3 third -Q:4 celery  --loglevel=info -f /home/andrew/try-celery/celery.logs`

- start **flower**: 
    * with broker param `flower --broker='amqp://user:password@127.0.0.1:5672/myvhost'` 
    * or just re-use celery app `flower -A tasks`
    * flower is available by default on --port=5555
- kill: `pkill -f "celery worker"`

celery params:
    
    --detach: start as daemon
    --beat or -B: start scheduler (aka cron)
    -f: write to logfile
    -E: Send task-related events so that tasks can be monitored using tools like flower    

links:

- if login refused error: read on [stackoverflow](https://stackoverflow.com/questions/26811924/spring-amqp-rabbitmq-3-3-5-access-refused-login-was-refused-using-authentica/26820152)
