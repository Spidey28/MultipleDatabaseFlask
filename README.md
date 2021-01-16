Tech. Used:

1. Clever-cloud.com used to host mysql instance on cloud
2. ElephantSQL used to host postgresql instance on cloud

Core Libraries:

1. Flask (of course)
2. Flask-Restless: Used to create API
3. psycopg2-binary: Used for establishing connection with PostgreSQL
4. SQLAlchemy: Used for interacting database with the help of ORM
5. mysqlclient: Used for establishing connection with MySQL

To run the project:

Step:1 - Install requirements with command - $pip install -r requirement.txt

Step:2 - Go to directory where multiple_databases.py and run command - $python multiple_databases.py

Step:3 - Kudos! - Go to web browser or postman and write any of below URLs:
                    <localhost:<port-n0>/MySQL> or <<localhost:<port-n0>/PostgreSQL>>

                    For example: http://127.0.0.1:5000/MySQL
                                 http://127.0.0.1:5000/PostgreSQL
