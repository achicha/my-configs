# quick start
1. init containers and DB: `./sentry-init.sh`
2. create superuser: `docker-compose exec sentry-base sentry createuser --email YOUR_EMAIL --password YOUR_NEW_PASSWORD --superuser --no-input`
3. login to `0.0.0.0:9000` with `YOUR_EMAIL\YOUR_NEW_PASSWORD`

# Links
### with docker-compose
Docker-compose is **NOT** work when OpenVPN is turned on!

- [guide](https://mikedombrowski.com/2018/03/self-hosting-sentry-with-docker-and-docker-compose/)
- [official](https://github.com/getsentry/onpremise)
- [example](https://gist.github.com/denji/b801f19d95b7d7910982c22bb1478f96)

### python
- [sentry quick start with python](https://docs.sentry.io/clients/python/integrations/logging/)
- [logging](https://docs.sentry.io/clients/python/integrations/logging/)

### docker 
- [docker sentry link](https://github.com/docker-library/docs/tree/master/sentry)
