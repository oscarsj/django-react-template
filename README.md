# README #

### Django + React skeleton ###

This code allows to bootstrapping an app based on django rest framework as backend, a react app as frontend, with a development environment based on docker-compose and mysql
The target of this is deploying to a service such as heroku.

Clone this repo and search&&replace for MYAPPNAME, then follow your favorite django tutorial to start adding apps, models and views, for example [this post](https://www.valentinog.com/blog/drf/)

### Dev env set up ###

- Add to your /etc/hosts:
```
127.0.0.1 mysql
```
- Create a database in the docker volume:
```
docker-compose run mysql
mysql -h mysql -u root
create database MYAPPNAME;
```
- Populate it with django models
```
docker-compose run MYAPPNAME python MYAPPNAME/manage.py migrate
```
Create super-user to be able to log in into admin, and provision regular users
```
docker-compose run MYAPPNAME python MYAPPNAME/manage.py createsuperuser
```
- Install frontend dependencies
```
cd frontend
npm install 
```
- Transpile React code:
```
npm run dev
```

- Run the app:
```
docker-compose up -d
```

- Connect to localhost:8080


* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact
