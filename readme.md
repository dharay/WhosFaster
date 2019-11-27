This repo contains various frameworks for backend which support the following 2 endpoints:

http://127.0.0.1:8000/fib/35  (...fib/Int)

http://127.0.0.1:8000/  (hello world)

The fib endpoint calculates and returns the nth term of fibonacci series and all have the same algo for calculation: 
eg: In python

```python
def calulateFib(n):
    if n==0 or n == 1:
        return n
    else:
        return calulateFib(n-1)+calulateFib(n-2) 
```

Load testing parameters: Transactions,Availability
    calculated using siege: 100 concurrent calls for 5 sec

# Django python:
prerequisites: django, python3

 run: 

 python3 manage.py runserver

port: 8000

response time for 35th term ~3.5 sec

Transactions:                3963 hits

Availability:               84.39 %

# FastApi python:
prerequisites: fastApi, uvicorn , python3

 run: 
 
 python3 main.py 

port: 8090

response time for 35th term ~3.5 sec

Transactions:               10335 hits

Availability:              100.00 %


# Kitura swift:
run:

swift build

swift run

port : 8080

response time for 35th term ~200 msec

Transactions:               16463 hits

Availability:              100.00 %

# NodeJS(express):


run:

node server.js

port :3000

response time for 35th term ~255 msec

Transactions:               16472 hits

Availability:              100.00 %

# SpringJava:


run:

mvn package

java -jar /target/fibonacci-0.0.1-SNAPSHOT.jar 

port :8080

response time for 35th term ~42 msec 😱 #fastest

Transactions:               16452 hits

Availability:              100.00 %
