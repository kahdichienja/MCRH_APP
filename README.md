# MCRH_APP
## Installation

 #### Environment Set Up
 Make a folder in your development env.
```python
mkdir test
cd test
[~/Desktop/test/]
git clone https://github.com/kahdichienja/MCRH_APP.git

```
## Creating a vitualenv
```python
$ virtualenv env

# activate the env
$ source env/bin/activate
$ (env)/Desktop/test/ cd MCRH_APP


```
### Installing Packages
```python

$ source env/bin/activate
$ (env)/Desktop/test/ cd MCRH_APP
$ (env)/Desktop/test/MCRH_APP pip install -r requirements.txt

# run migrations
$ python manage.py migrate


# create super user
$ python manage.py createsuperuser

# run server
$ python manage.py runserver


```
