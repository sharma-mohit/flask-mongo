# Flask-MongoDB
[![Build Status](https://travis-ci.org/sharma-mohit/flask-mongo.svg?branch=master)](https://travis-ci.org/sharma-mohit/flask-mongo)
A simple flask app that accepts json data and store in mongodb.

This Flask web application listens on port 8080 and has only 2 endpoints, supports two methods: **GET** and **POST**.

#####First endpoint
The first endpoint accept only **POST** requests which will have a json payload.

`http://hostname:8080/api/`

The JSON payload should be like:
```
{"date": "2015-05-12T14:36:00.451765", "uid": "1", "name": "John Doe", "md5checksum": "e8c83e232b64ce94fdd0e4539ad0d44f"}'

{"date": "2015-05-13T14:36:00.451765", "uid": "2", "name": "Jane Doe", "md5checksum": "13065eda9a6ab62be1e63276cc7c46b0"} 
```

The endpoint stores the data in a mongo data store.

Before storing the data it makes sure that the checksum for each JSON object (just fields: date, uid and name) is correct and matches the original checksum in the JSON payload.

**Ordered fields**

For instance for the first object in example above, checksum will be checked for json string:
`{"date": "2015-05-12T14:36:00.451765", "uid": "1", "name": "John Doe"}`

*Note: Order of fields only matter for checksum, you can enter data in any order, but checksum will be evaluated according to above order*
To verify checksum online, use this link: http://www.progs.be/md5.html
___

#####Second Endpoint
The second Endpoint accept only **GET** requests with an uid parameter and a date parameter. Like:
`http://hostname:8080/api/<uid>/<date>/` (date format: %Y-%m-%d)

This will return the number of occurrences of a given UID for that day.

***
## Deployment

To deploy in local environment with Vagrant:
### Dependencies
Vagrant 1.7.4

Ansible 1.9.4

VirtualBox 5.0.2

Git

###Steps
1. Install dependencies
2. Clone repo `git clone https://github.com/sharma-mohit/flask-mongo.git`
3. Go to directory `cd flask-mongo`
4. Start virtual machine `vagrant up`
5. Ready to use/test
  * Use api like: `http://localhost:8080/api/`.

