# PythonCRUD

This app still has some bugs and it's not, by all means, complete. It's still under development.

## Creating the database

To create the database and table, just run the `users.sql` script. Since I used MySQL on my local machine, I navigated to the script folder and used:
```
$ mysql -u root -p
```
then typed my password to access the MySQL server. To run the script I used:
```
mysql> source users.sql
```

## Using the database in the app

In the file `database_connect.py`, edit the `connect_string` to match the desired host, user and password. For more information on this, check the SQLAlchemy engine documentation [here](https://docs.sqlalchemy.org/en/latest/core/engines.html).

Furthermore, if you change the name of the fields, table or database, you may have to edit the MySQL commands on file `print_sql.py`.

## Starting the app

To start the app, run:
```shell
$ python startApp.py
```
