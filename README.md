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
docker-compose run escuela python MYAPPNAME/manage.py migrate
```
- Install frontend dependencies
```
cd frontend
npm i webpack webpack-cli --save-dev
npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
npm i react react-dom --save-dev
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
