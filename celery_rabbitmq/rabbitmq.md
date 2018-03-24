start docker container:
    
    docker run -d --restart=always --hostname my-rabbit --name some-rabbit -p 8081:15672 -p 5672:5672 -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password -e RABBITMQ_DEFAULT_VHOST=myvhost rabbitmq:3-management

setup:

- RabbitMQ container listening on the default port of `5672`
- **Management Plugin** of rabbitmq is running on host: `http://container-ip:15672`, outside the host: `http://container-ip:8081`
- (from the host computer, after first logon to Managment Plugin) check that credentionals are verified: `curl -i -u user:password http://127.0.0.1:8081/api/whoami`
- create second user from Managment Plugin?

