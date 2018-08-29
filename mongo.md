#### Quick Start

- install mongo client: `sudo apt install -y mongodb-org-shell`
- install motor:  `pip install motor`
- docker run: `docker run --name some-mongo -p 27017:27017 -v /home/user_name/mongo_db:/data/db -d mongo`

#### Base app (python)

    from motor.motor_asyncio import AsyncIOMotorClient
    _client = AsyncIOMotorClient()
    DB = _client.test_database
    collection = DB.test_collection

    async def f():
        result = await collection.insert({'_id': 1})
        print('result %s' % repr(result.inserted_id))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(f())


#### links:

[install](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)
[docker hub](https://hub.docker.com/_/mongo/)
[motor](https://motor.readthedocs.io/en/latest/examples/index.html)
[examples](https://github.com/mongodb/motor/blob/master/test/asyncio_tests/test_asyncio_collection.py)
[docs](https://docs.mongodb.com/manual/reference/method/db.collection.bulkWrite/#bulkwrite-write-operations-updateonemany)
