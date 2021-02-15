# Longest palindrome API

This is an Palindrome API, where you can send it an string, And it returns the longest palindrome if exist
#### Capabilities:
* Log Up
* Log In
* Get the longest palindrome given one string

#### Requirements for deployment:
* Linux os 
* Docker
* Docker Compose

#### Requirements for testing:
* Linux os 
* Python 3.7

#### Steps to deploy it:
* Clone the repository in your machine, It doesn't matter the path
```
- git clone https://github.com/jalondono/palindrome-API
- cd API_grupoD
```
* Once there, you need to execute the docker command, to build the image and the run it
```
- docker-compose build
- docker-compose up
```
#### Steps to run tests:
* Clone the repository in your machine, It doesn't matter the path
```
- git clone https://github.com/jalondono/palindrome-API
- cd API_grupoD
```
* Install the requirements file using this command
```
- pip install -r requirements.txt
```
* Checkout to test branch using this command:
```
- git checkout test
```
* Once done this, just run it using the next command
```
- python manage.py tests --settings=grupo_d.settings.test_sqlite
```

### Endpoints
**For documentation.**
It is a simple endpoint where you can see the documentation of the API through SWAGGER OpenAPI, **Where you can explore the models, payloads and responses**
```
GET: http://0.0.0.0:8000/ 
```
.<img align="center" src="https://i.imgur.com/XbAE4fp.png" height="80%" width="80%"/>

**For User register.**
```
POST: http://0.0.0.0:8000/register/
```

 In order make use of palindrome Endpoint, you need to be authenticated, so first you must to create one user, using the register endpoint as follow. The user will be saved in a **sqlite db**
 
 .<img align="center" src="https://i.imgur.com/ueCDc1w.png" height="80%" width="80%"/>


**For Get Token.**
```
POST: http://0.0.0.0:8000/token/
```
At the time of make request to palindrome endpoint, you will need pass in the headers a valid token, You can get your token making use of this endpoint as follow

 .<img align="center" src="https://i.imgur.com/8UTEH85.png" height="80%" width="80%"/>
 
**For Refresh Token.**
```
POST: http://0.0.0.0:8000/token/refresh/
```

By default the token will have a duration of 6 hours, once passed this time you have to refresh it, using this endpoint as follow

.<img align="center" src="https://i.imgur.com/lR2Sqx0.png" height="80%" width="80%"/>

**For Palindrome.**
```
POST: http://0.0.0.0:8000/palindrome/
```
Well... The palindrome endpoint needs two things, A valid token on headers and the string from which you will get the palindrome.
* Headers

.<img align="center" src="https://i.imgur.com/RyXnBRx.png" height="40%" width="90%"/>

After put the token on the headers like in the image above. You just need insert the string and that's all

.<img align="center" src="https://i.imgur.com/pntZywH.png" height="80%" width="90%"/>

 # Authors:
* **Juan Alberto Londoño H.** - [jalondono](https://github.com/jalondono)
