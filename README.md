### Set up local environment
Create .env file in the project dir to store environment variable

Add following variables to above file:

 * ENV
 * DATABASE_NAME
 * DATABASE_USERNAME
 * DATABASE_PASSWORD
 * SECRET_KEY

**All docker commands should be run from project dir**

Build and run container:

```
docker-compose build
docker-compose up
```

Run migration, createsuperuser amd run command to create test data:

``` 
docker-compose exec web python /webapp/src/manage.py migrate
docker-compose exec web python /webapp/src/manage.py createsuperuser
docker-compose exec web python /webapp/src/manage.py create_initial_data
```


### Run test

```
docker-compose exec web python -m pytest
```

### Static checks
In this project the following packages are used for static checks:
  * Prospector: https://prospector.landscape.io/en/master/
  * Bandit: https://github.com/PyCQA/bandit

By default, prospector runs following tools: 

  * dodgy
  * mccabe 
  * pep8
  * profile-validator 
  * pyflakes
  * pylint

To run prospector: 

```
docker-compose exec web python -m prospector
```

To run bandit: 

```
docker-compose exec web python -m bandit -r .
```
