from redis import Redis
from rq import Queue
from task import count_words_at_url

### Queue
queue = Queue(connection=Redis(host='redis-12411.c8.us-east-1-4.ec2.cloud.redislabs.com',
    port=12411,
    username="default",
    password="Kt6NhzlAkEUm7vfHQDG1TdAQVvzrdh8D"))


job = queue.enqueue(count_words_at_url, 'https://stamps.id')


print(queue.get_jobs())


### what are we doing ?
## Task Queue ----> running task in backgroud

### Understanding
## Docs ---> chatgpt
## redme, quickstart

### Test 1
## start redis server -----> cloud, docker

###. ---------


