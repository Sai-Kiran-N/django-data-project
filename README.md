# Instructions To Run Django version of Data Project

## Getting Started

These instructions will get you how to run this Project on your local machine.

### Introduction

In this project, we will use the same datasets as the previous Data Projects.

### Requirements

* Clone this project from gitlab using the below command.
  * **$ git clone git@gitlab.com:sai-kiran-nalamothu/django-data-project-saikiran.git**
* Create a virtual environment in your system and install the dependency libraries.
* The required libraries are listed in **requirements.txt** text file.
* Postgresql database server should be installed in the system.

### Execution of project

* Start postgresql server by using below command in linux terminal.
  * **$ sudo service postgresql start**
* Activate the virtual environment.
* Install the dependency libraries by using below command.
  * **$ pip install -r requirements.txt**
* If you got any errors related to psycopg2 package installation, then please run the below command otherwise ignore it.
  * **$ sudo apt install python3-dev libpq-dev**
* Locate to the file location of cloned git repository.

step-1 : Configuring the essential details.
* open **.env** file.
* Replace the **username** and **password** values with your postgres credentials.


step-2 : Creating Database
* Run **create_database.py** file by using below command.
  * **$ python create_database.py**
* It creates a database named **un_saikiran**

step-3 : Migrations
* Open terminal and perform the following commands.
  * **$ python manage.py migrate**
* It performs the migrations.

step-4 : Loading csv data to database
  * Run the following command in the terminal.
    * **$ python manage.py populate_data_to_db**

step-5 : Accessing website
  * Execute the following command in the terminal.
    * **$ python manage.py runserver**
  * Copy the localhost server address displayed in the terminal and paste it in the web browser address bar field.
  * The localhost server address will look like below one.
    * **$  [http://127.0.0.1:8000/]( http://127.0.0.1:8000/)**
  * It will display the plots.


  step-6 : Dropping database
  * Run **drop_database.py** file by using below command.
  * **$ python drop_database.py**
* It drops the database named **un_saikiran**.

# Note : 
* open **.env** file.
* Replace the **username** and **password** values with your postgres credentials.

*ThankYou!*
