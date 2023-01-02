# Python API Development - Comprehensive Course for Beginners  
  
https://www.youtube.com/watch?v=0sOvCWFmrtA&ab_channel=freeCodeCamp.org  
  
## Tech Stack:  
- Alembic  
- Postman  
- Ubuntu / Heroku  
- FastAPI (Python)  
- PostreSQL  
- SQL Alchemy  
  
## Course Contents:    
00:00 Intro    
06:33 Project Overview    
11:22 Mac Python Installation    
13:15 Mac VS Code install and setup    
16:37 Windows Python Installation    
18:30 Windows VS Code install and setup    
22:11 Python virtual Env Basics    
24:35 Virtual Env on windows    
28:56 Virtual Env on Mac  
34:17 Install dependencies w/ pip  
36:21 Starting FastAPI  
39:23 Path Operations  
53:22 Intro toman  
57:34 HTTP Requests  
1:07:29 Schema Validation with Pydantic  
1:22:45 CRUD Operations  
1:29:44 Storing in Array  
1:34:06 Creating  
1:38:15 Postman Collections & saving requests  
1:39:47 Retrieve One  
1:48:10 Path order Matters  
1:52:46 Changing response Status Codes  
2:01:49 Deleting  
2:10:31 Updating  
2:18:02 Automatic Documentation  
2:21:34 Python packages  
2:24:11 Database Intro  
2:28:54 Postgres Windows Install  
2:31:28 Postgres Mac Install  
2:34:26 Database Schema & Tables  
2:44:35 Managing Postgres with PgAdmin GUI  
3:12:10 Your first SQL Query  
3:19:43 Filter results with "where"  
3:22:55 SQL Operators  
3:26:38 IN  
3:28:07 Pattern matching with LIKE  
3:31:59 Ordering Results  
3:36:27 LIMIT & OFFSET  
3:39:21 Modifying Data  
3:53:48 Setup App Database  
3:58:21 Connecting to database w/ Python  
4:08:00 Database CRUD  
4:31:18 ORM intro  
4:35:33 SQLALCHEMY setup  
4:55:25 Adding CreatedAt Column  
5:00:59 Get All  
5:07:55 Create  
5:15:50 Get by ID  
5:19:50 Delete  
5:22:31 Update  
5:28:21 Pydantic vs ORM Models  
5:32:21 Pydantic Models Deep Dive  
5:38:57 Response Model  
5:50:08 Creating Users Table  
5:54:50 User Registration Path Operation  
6:03:27 Hashing Passwords  
6:08:49 Refractor Hashing Logic  
6:10:32 Get User by ID  
6:17:13 FastAPI Routers  
6:27:34 Router Prefix  
6:30:31 Router Tags  
6:32:49 JWT Token Basics  
6:47:03 Login Process    
7:00:44 Creating Token  
7:09:58 OAuth2 PasswordRequestForm  
7:13:23 Verify user is Logged In  
7:25:21 Fixing Bugs  
7:27:59 Protecting Routes  
7:36:17 Test Expired Token  
7:38:13 Fetching User in Protected Routes  
7:42:44 Postman advanced Features  
7:50:33 SQL Relationship Basics  
7:54:59 Postgres Foreign Keys  
8:07:20 SQLAlchemy Foreign Keys  
8:13:40 Update Schema to include User  
8:17:59 Assigning Owner id when creating new  
8:21:01 Delete and Update only your own  
8:27:48 Only Retrieving Logged in User's  
8:33:37 Sqlalchemy Relationships  
8:38:32 Query Parameters  
8:50:46 Cleanup our main.py file  
8:53:53 Env Variables  
9:21:20 Vote/Like Theory  
9:26:36 Votes Table  
9:31:33 Votes Sqlalchemy  
9:34:11 Votes Route  
9:52:31 SQL Joins  
10:15:26 Joins in SqlAlchemy  
10:28:21 Get One with Joins  
10:30:18 What is a database migration tool  
10:33:45 Alembic Setup  
11:13:50 Disable SqlAlchemy create Engine  
11:14:28 What is CORS?  
11:23:38 Git PreReqs  
11:27:40 Git Install  
11:29:23 Github  
11:34:39 Heroku intro  
11:35:40 Create Heroku App  
11:40:21 Heroku procfile  
11:44:59 Adding a Postgres database  
11:48:42 Env Variables in Heroku  
11:58:59 Alembic migrations on Heroku Postgres instance  
12:02:52 Pushing changed to production  
12:05:04 Create an Ubuntu VM  
12:08:04 Update packages  
12:10:47 Install Python  
12:12:21 Install Postgres & setup password  
12:17:28 Postgres Config  
12:24:50 Create new user and setup python evironment  
12:34:06 Env Variables  
12:42:24 Alembic migrations on production database  
12:45:57 Gunicorn  
12:54:12 Creating a Systemd service  
13:04:45 NGINX  
13:10:45 Setting up Domain name  
13:15:19 SSL/HTTPS  
13:19:31 NGINX enable  
13:20:06 Firewall  
13:23:47 Pushing code changes to Production  
13:26:09 Dockerfile  
13:38:39 Docker Compose  
13:48:34 Postgres Container  
13:56:22 Bind Mounts  
14:03:39 Dockerhub  
14:08:08 Production vs Development  
14:14:51 Testing Intro  
14:17:19 Writing your first test  
14:30:22 The -s & -v flags  
14:31:44 Testing more functions  
14:35:29 Parametrize  
14:40:21 Testing Classes  
14:48:37 Fixtures  
14:55:40 Combining Fixtures + Parametrize  
14:59:13 Testing Exceptions  
15:06:07 FastAPI TestClient  
15:14:26 Pytest flags  
15:17:31 Test create user  
15:25:23 Setup testing database  
15:36:47 Create & destroy database after each test  
15:44:18 More Fixtures to handle database interaction  
15:50:35 Trailing slashes in path  
15:53:12 Fixture scope  
16:07:50 Test user fixture  
16:14:40 Test/validate token  
16:18:59 Conftest.py  
16:22:09 Testing  
17:34:15 CI/CD intro  
17:43:29 Github Actions  
17:49:32 Creating Jobs  
17:57:38 setup python/dependencies/pytest  
18:06:14 Env variables  
18:11:19 Github Secrets  
18:18:14 Testing database  
18:23:42 Building Docker images  
18:34:33 Deploy to heroku  
18:49:10 Failing tests in pipeline  
18:52:18 Deploy to Ubuntu


## Basics

Run server:  
$ uvicorn main:app --reload

Postman:  
- Send Get and Post requests   

Pydantic  
- create a model class  
- Optional (from typing)   

CRUD  
- C   - Create    - POST      - @app.post("/posts")  
- R   - Read      - GET       - @app.get("/posts/{id}")  
      - Read      - GET       - @app.get("/posts")  
- U   - Update    - PUT/PATCH - @app.put("/posts/{id}")  
- D   - Delete    - DELETE    - @app.delete("/posts/{id}")  

Automatic Documentation 
- localhost:8000/docs   (by SwaggerUI)
- localhost:8000/redoc

Restructuring the project folder  
- Create a folder named ./app/  
- create ./app/__init__.py  
- move main.py to that folder  
- 
- $ uvicorn app.main:app --reload  


## PostgreSQL

Create a DB and a posts table

$ pip install psycopg2   (now the version 3 is also available)

Implement CRUD operations in SQL in our code with the cursor.execute() command and conn.commit()


## ORM (Object Realtional Mapper) SQLAlchemy

- Layer of abstraction that sits between the db and us.
- We can perfom all db operations through traditional Python code without SQL.
- We can define the tables as python models/classes 

- sqlalchemy needs psycopg2 to connecto to the postgresql db
- create app/database.py to handle the db connection functions

- The Schema/Pydantic Model define the structrue of a request & response. This ensure that when
  a user wants to create a post, the request will only go through if it has a "title" and "content"
  in the body.  FrontEnd <--> Schema Model <--> FastAPI

- The SQLAlchemy Model define the columns of our "posts" table within postgres. Is used to query, 
  create, delete and update entreis within the database.

- Create app/schemas.py and define there all pydantic data model classes
- Create a BasePosts class where other specific classes for every method will inherit from
- Create a separete Post class for the response, so then we can return only specific values and not all those available in the db


## Users Table and Registration Logic

- Create a new class Users table form the app/model.py file
- In schemas.py, create a user class for the request, and a user class for the response WITHOUT THE PASSWORD FIELD!! we never want to return the password after a user has been created
- Hash password, we don't want to store them in plain text. We will use passlib with bcrypt  
$ pip install passlib[bcrypt]


## Routers

- Create a new folder app/routers/
- Create the post.py and user.py files inside it and cut and paste everyone of the function paths respectively and necessary import libraries.
- from FastAPI import APIRouter  
- "router = APIRouter()" and change @app for @router at every path function's decorator
- add "app.include_router(post.router)" and "app.include_router(user.router)" to the main.py
- add a prefix path at the start of everyone of the route files and a tag to improve auto-documentation readability


## JWT Token Authentication (JSON Web Token)

- Is a stateless method, the token is stored in the frontend and it's visible
- 1. Client post requests /login (username + password) to the API
- 2. I credentials are valid, the API sends back a specific token
- 3. The client sends that token in the header of every subsequent request
- 4. The API checks the token at every request and if it's valid, it fulfills the request

The Token is composed of 3 parts:
- Header (alg, type (ex: JWT))
- Payload (ex: user_id, role, etc)
- Verify Signature (made by hashing [Header + Payload + Secret], the API adds a secret signature that will allow to validate the token and make it no possible for users to change the token data trying to access to other API parts)


## Logging In User

- The user from the frontend reaches the /login endpoint with a {email, password}
- The backend retrieves from the db the hashed password for that email
- Tha backend hashes the user provided password, and if it matches the hashed password from the db, then it correctly logs in that user

- Create a new route file app/routers/auth.py
- Integrate the paht login handling the logic to check email and password


## Creating the JWT Token Authentication for Login

- $ pip install python-jose[cryptography]
- Create app/oauth2.py 
- Setup the logic to create access tokens with the jose library with the provided data and expiration time to be included in the token payload

- Through Postman, try to create a user in the db and then login with its credentials, take the generated token and pass it through jwt.io website tool to check the content of the token

- Then we will be using the fastapi.security.oauth2.OAuth2PasswordRequestForm as the schema to receive the user credentials from the frontend
- The frontend (or Postman) will need to supply them in a Body > form-data with the "username: email" and "password: password" format

- Create the verify_access_token() and get_current_user() functions in oauth2.py in order to pass a token, validate its integrity, decode it and extract the user id from its payload.
- Then we can pass this methods to every path function that requires the user to be logged in order to acces to those paths, like creating posts for example
- We make this with the Depends() method from fastapi that will require the token to be valid and return a user_id as an int in the payload

- Now in ordert to create a post from Postman, we need to login with a user + psw, get the generated token and insert it in the Headers of the post request, with the key: value "Authorization": "Bearer token" or going to the Auth option, choose Type: Bearer Token and insert the token.
- Then we add the login requirement to all desired routes, and those will require the token in the header in order to be requested.
- In the oauth2.py get_current_user() function we can also extract from the db the user information from its token id, and then pass it to the route function that it's calling it.


## Postman advanced features

- Postman Environments: allow to create different variables such the path for DEV and for PROD differently accross all different individual methods and requests and easily change accross them.
- Create a DEV and a PROD environment with a var URL for every case and update the path for every request with the new var {{URL}}
- Then in order to automate the login process and token accquisition, go to the login request and in the Tests section add "pm.environment.set("JWT", pm.response.json().access_token);" and this will automatically set the new token as a envioronment variable
- Now we can add this {{JWT}} variable to every Auth header section of the required requests


## SQL Foreign Keys

- We will do the following in sqlalchemy, but this is how it could be done in PGAdmin
  - Go to PGAdmin > table posts > delete all posts > create new column "user_id" int not null > Constraints > Foreign Key > new "posts_users_fkey" > edit > Local col: user_id, References: public.users, Referencing: id > Action: CASCADE (on update and on delete)

- We will add the "owner_id" column in the models.py Posts table as: "owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)"

- In posts.py, at create_posts() function we will add "new_post = models.Post(owner_id=current_user.id, **post.dict())" in order to add the user id as the new attribute owener_id in the posts table.
- Then we add the rules to only allow the user owner of the post to update/delete it and also, optionally to get (or see) it.
- We can also add to the schemas to return the post info with the owner id info and also add that field as a sqlalchemy relationship in the models.py and it will automatically match every post with its owner info.


## Query Parameters

- We can add limit and skip parameters to the get functions to only return a limited amount of entries. Then we can declare those limits from the frontend/Postman as: "{{URL}}posts?limit=3&skip=2" for example.
- These are implemented with sqlalchemy db search with the db.query() .limit() and .offset() mehtods.
- We can also add search of terms with the ...&search=apple%20juice parameter and the sqlalchemy method filter and contains: "db.query(models.Post).filter(models.Post.title.contains(search))"


## Env Variables

- On windows, you can set them on Environment Variables
- $ echo %Path%
- From Python: import os; path = os.getenv("Path")

- Create the app/config.py file, from pydantic import BaseSettings and then create the class Settings declaring every variable needed and its type, then settings = Settings().
- Then instead of declaring the needed variables in the OS Environmnet Variables, we will create the /.env file which is the standard way to declare the app env variables more automatically 


## Voting/Likes System

- We will create a new table for Votes with a Composed Primary Key of post_id and user_id so every post would be possibly liked only once from the same user
- Create it with sqlalchemy in the models.py ç
- Create the route routers/vote.py and create the vote() method to add or delete a vote
- Create the post request in Postman


## SQL Joins

-- Query to get all posts info with the count of the num of votes for each one
SELECT posts.*, COUNT(votes.post_id) AS votes
FROM posts LEFT JOIN votes ON posts.id = votes.posts_id 
GROUP BY posts.id;

-- Add "WHERE posts.id = X" to have only a single post

- In sqlalchemy: "db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id)"


## Alembic - DataBase migration

- db migrations allow us to incrementally track changes to db schema and rollback changes to any point in time. Alembic can also automatically pull db models from Sqlalchemy and generate the proper tables.

- $ pip install alembic
- $ alembic init ./alembic

- go to alembic/env.py and add "from app.models import Base"
- then change "target_metadata = Base.metadata"
- we now need to add the db url to the /alembic.ini file but to add all secret info to it, we will do it through the alembic/env.py file, importing them from app.config import settings as we did in the database.py 

- $ alembic revision -m "create posts table"
- this command will create a new version py file under the alembic/versions/ folder, inside it we will have to manually develop the upgrade() and downgrade() methods to setup the db table changes and rollback them.

- $ alembic current    --> displays the current version for a db

- $ alembic upgrade (REVISION_NUMBER)

- $ alembic revision -m "add content column to posts table"

- $ alembic heads     --> returns the last version
- $ alembic upgrade head    --> sets the state up to the latest version

- $ alembic downgrade -1    --> downgrades one revision
- $ alembic downgrade (REVISION_NUMBER)  --> sets the setate back to that rev num

- $ alembic revision -m "add user table"

- $ alembic history

- $ alembic upgrade +2
- $ alembic upgrade head

- $ alembic revision -m "add foreign-key to the posts table"

- $ alembic revision -m "add last few columns to posts table"
- add rules for updrade() and downgrade() for the remaining columns of posts

- $ alembic upgrade head
- $ alembic revision --autogenerate -m "auto_vote"
- this command will compare the current latest state from alembic revisions and how are the model.py tables and will generate the remaining tables/columns, in this case, it will generate the votes table as it is in the models.py but we haven't created yet in Alembic.

- $ alembic upgrade head

- We only run alembic revision on dev, then test it and the push the revision files to prod and then alembic updrade head in prod


## CORS

- Go to chrome, google.com as a random website, open the developer tools and go to the console
- $ fetch("http://localhost:8000/").then(res => res.json()).then(console.log)
- It throws an error due to blocked CORS Policy, (Cross-Origin Resource Sharing).

- To allow CORS in our API:

- from fastapi.middleware import CORSMiddleware
- set the app.add_middleware with it's parameters including the allowed origins, it's a safety practice to narrow it as much as possible and if it's a privat api for a specific frontend app to only put its domain there


## GIT

- Create .gitignore and add __pycache__, venv/ and .env
- $ pip freeze > requirements.txt
- ($ pip install -r requirements.txt)


## Deploying to Heroku

- Install the Heroku terminal on your OS
- Login: $ heroku login
  
- $ heroku create fastapi-unique-app-name     (from the app directory)
- Now git remote will show two remote repos, the origin first one at github and the one on heroku. To push code to heroku and automatically deploy it there (when properly configured): $ git push heroku main
  
- create the file /Procfile and add: "web: uvicorn app.main:app --host=0.0.0.0 --port=${PORT:-5000}

- $ heroku logs -t      (to see the tail logs)

- check heroku postgres tutorial
- $ heroku addons:create heroku-postgresql:hobby-dev
- go to heroku web and user account, then go to datastores and check the new postgres add-on instance
- check the db credentials
- go to the app instance > Settings > Config vars > set the env variables as we had them before

- $ heroku ps:restart

- We only run alembic revision in the dev environmnet and the push these revision files to the prod env after all tests are passed

- $ heroku run "alembic upgrade head"


## Deploying on Ubuntu Server (on Digital Ocean)

- Create a Digital Ocean Droplet > Ubuntu > chepeast options > Create Droplet
- $ ssh root@(IP_addr)    then password
- $ sudo apt update && sudo apt upgrade -y
- check py version
- $ sudo apt install python3-pip
- $ sudo pip3 install virualenv
- $ sudo apt install postgresql postgresql-contrib -y
- $ psql --version
- $ su - postgres
- $ psql -U postgres -d postgres -h localchost -p 5432
- $ \password postgres    (enter psw)
- $ \q
- $ exit
- $ cd /etc/postgresql/12/main
- $ sudo vi postgresql.conf
- optionally, under - Connection Settings - add listen_addresses = "*"  or  narrow it down to necessary ip_addrs
- $ sudo vi pg_hba.conf
- under Database administrative login by Unix domain socket, change the local method from peer to md5
- then under IPv4 local connections we can add ip_addr for remote connections or 0.0.0.0/0 to allow all
- $ systemctl restart postgresql
- $ psql -U postgres
- now we can login from root or any other ubuntu user to postgres under the postgres username
- then try to connect to the ubuntu postgres db from the windows pc pgadmin
  
- We want to create a ubuntu user with admin privilegees to not use root and also another user without privilegees to start the fastapi app without privilegees and less risks
- $ adduser fastapi-admin      add psw
- $ usermod -aG sudo fastapi-admin
- $ exit
- $ ssh fastapi-admin@(ip_addr)
- $ mkdir app
- $ cd app
- $ virtualenv venv
- $ source venv/bin/activate
- $ mkdir src
- $ cd src/
- $ git clone (github-repo) .
- $ sudo apt install libpq-dev    (pip error installing this package from pip)
- $ pip install -r requirements.txt
- $ uvicorn app.main:app      (errors as we haven't set the env variables yet)

- $ export MY_ENV=enric
- $ printenv        (will print all env variables)
- $ unset MY_ENV 
- $ cd ~
- $ touch .env
- $ vi .env
- copy and paste the .env variables that we had in the local environmnent
- $ vi .profile
- copy this command at the end of the file: 
- --> set -o allexport; source /home/fastapi-admin/.env; set +0 allexport

- create the fastapi-prod database in the ubuntu machine from pgadmin
- $ cd app/src/
- $ alembic upgrade head        (this will create the tables in the fastapi-prod db)
- $ uvicorn --host 0.0.0.0 app.main:app

- Now go to the browser of another machine and try to access to the public ip-addr of the server and the port 8000

- If the app crashes it won't restart automatically, so we will use gunicorn for that
- $ pip install gunicorn httptools uvloop         (update requirements.txt then with those)
- $ gunicor -w 4 -k uvicorn.worker.UvicornWorker app.main:app --bind 0.0.0.0:8000     (adapt number or workers -w)
- open another connection to the ubuntu machine and $ ps -aef | grep -i gunicorn    (to check processes)

- Create the app/gunicorn.service file
- $ cd /etc/systemcd/system/
- $ sudo vi api.service
- copy and paste the gunicor.service file content to this new file
- $ systmectl start api
- $ sudo systemctl enable api     (this will allow to automatically start it at every reboot of the machine)
- $ systemctl status api
- $ systemctl restart api   (if needed and also systemctl daemon-reload)


## NGINX

- High performance webserver that can act as a proxy. Can handle SSL terminations.
- Its more optimized to handle the HTTPS than our app side.

- $ sudo apt install nginx -y
- $ systemctl start nginx
- $ cd /etc/nginx/sites-available/
- $ sudo vi default
- change the lines in the file under "location / {" for those in the file nginx of our repo and save and close with :wq
- $ systemctl restart nginx
- test to connect to the api


## Custom Domain Name and SSL

- From namecheap > Domain List > Nameservers > Custom DNS > add your host domains
- (check manuals for every host provider)
- From the host provider, create new records for A and CNAME without and with wwww.

- In order to set SSL, got to certbot.eff.org (free ssl service)
- Get Certbot instructions > Nginx > on Ubuntu 22.04  (then it will provide the necessary following instructions)
- $ sudo snap install core; sudo snap refresh core
- $ sudo snap install --classic certbot
- $ sudo certbot --nginx      (then enter an email, Y, N, and domain name with and without www.)
- it will automatically modify the nginx config file


## Firewall

- $ sudo ufw status
- $ sudo ufw allow http     (port 80)
- $ sudo ufw allow https    (port 443)
- $ sudo ufw allow ssh      (port 22)
- we allow these ports from all ip adresses as this is intended to be a public API
- $ sudo ufw allow 5432   (this will allow to acces to the db from the outside, so maybe it's better to not do it)
- $ sudo ufw enable
- $ sudo ufw delete allow 5432   (to delete any rule)


## Pushing changes to production

- change > git add & git commit & git push to github > from the server, git pull > sudo systemctl restart api


## Dockerizing the app

- go to hub.docker.com > go to the official python image
- we will create our own custom docker image from the python one
- create /Dockerfile file in the repo with the steps to build our app image
- $ docker build -t fastapi .       (-t is the tag, so it can be another name)
- $ docker image ls
  
- then we could run the image with docker run and the image name but we will use docker compose instead
- create /docker-compose.yml file and set the commands to deploy the app docker image
- $ docker-compose up -d        (-d is detached mode, running containers in the background)
- $ docker ps -a
- $ docker logs fastapi_api_1
- $ docker-compose down
- $ docker-compose up --build  (if the image already exists but we want to rebuild it)

- Then, to add the postgres db also in a docker image and start them two from the docker compose, add another service in the docker-compose.yml called postgres with the official postgres image and make the api service depend on it, the ip address of them can be managed by docker-compose through their names. Mount also a docker volume for the db data.

- $ docker exec -it fastapi_api_1 bash    (this will allow us to run bash commands in the container interactively)

- in order to track changes in docker images, create an account on dockerhub
- then create a repository 
- $ docker image tag old_name (docker_username)/(repo_name)
- $ docker push (docker_username)/(repo_name)
- then login 

- then we will create separate docker-compose files, one for dev and the other one for prod
- now the docker-compose command will be:
- $ docker-compose -f docker-compose-dev.yml up -d

- we will push the image to dockerhub and then we will pull it from the prod machine, for this the docker-compose-prod file will have image: (username)/(repo_name) instead of build: .
- $ docker-compose -f docker-compose-dev.yml down


## Pytest

- $ pip install pytest
- $ pytest    (will run tests if there is any, test files should be named test_*.py or *_test.py and the funcions should start with test)
- create the folder /tests/ and then the __init__.py file
- we will be testing every single part from unit to more integrated creating a test function for every case and using the method assert to validate it
- $ pytest -v -s  (-v for extra verbosity and detail and -s to output prints)

parametrize:
- to test the same function with a different set of values and results to assert, we can import pytest and use the decorator @pytest.mark.parametrize("num1, num2, expected"), [(1, 2, 3), [(2, 5, 7)]) and then our test function def test_add(num1, num2, expected): assert add(num1, num2) == expected

fixtures:
- we can also use fixtures to implement basic parts of our tests and avoid repeating them at every function, for example @pytest.fixture; def zero_bank_account():; return BankAccount(50);
- then at every function we can pass f(zero_bank_account) as a parameter and avoid repeating that part of code every time to initialize our vars

- we can combine them 2

- in order to test functions that are suposed to raise an exception we add with pytest.raises(Exception): before the part that is going to fail, like checking that we cannot substract more money from a bank account that the total balance

- from fastapi we can use the TestClient (from fastapi.testclient import TestClient) to replace Postman and automatically build request tests with code
- create the file tests\test_users.py to create the users tests
- develop the root test and then $ pytest -v -s tests\test_users.py    in order to run only this test file and not all
- $ pytest --disable-warnings   (if needed to see test results better)
- $ pytest -x     (in order to stop testing whenever a single test fails)
  
- we are going to create a separate db for testing overriding the get_db() function with the fastapi method app.dependency_overrides[get_db] = override_get_db that will adapt all app methods that are already implemented with the normal get_db dependency
- we need to create manually the fastapi_test new database from pgadmin
- then we will need to create the tables with sqlalchemy or alembic, (sqlalchemy in this case)
- we can create some fixtures like a client TestClient to make requests at every test function and also possibly to create and drop all db tables at every test (or viceversa and then, after something fails, we can check the db content) and also a session fixture to be able to query the db from any test function and possibly also to drop and create tables at this point instead of the client and make client dependent of session
- then we can also create the file tests/database.py and put all db logic there instead of having it on every test file
- we can change the scope of a fixture @fixture(scope="function")  default, or "class", "module", "session",... then we can create a user in a function and validate the login in another but then some test will depend in others and this is a bad practice

- we can create the file tests/conftest.py that Pytest can automatically use for all fixtures that we want to declare there, then we don't need to create a database.py in tests and also we don't need to import any fixture in the test files

- we need to develop unit tests to cover all possible situations that could brake our logic for every route and function in test_posts.py, test_users.py and test_votes.py


## CI/CD

- CI (Continuous Integration): automated process to build, package and test applications
- CD (Continuous Delivery): picks up where CI ends and automates the delivery of applications

- Make changes to code > Commit changes > Run Tests > Build Image > Deploy

- Automated CI/CD: Make changes to code (manually) > Commit changes (manually) > (CI) Pull Source Code > (CI) Install Dependendencies > (CI) Run Automated Tests > (CI) Build images > (CD) Grab images/code > (CD) Update Production
- Common CI/CD tools: Jenkins, Travis CI, GitHub Actions, CircleCI, TeamCity


## GitHub Actions

https://github.com/features/actions
https://github.com/marketplace

- create the folder /.github/ and then /.github/workflows
- create the file .github/workflows/build-deploy.yml and set the steps to configure the automatic CI steps
- on: triggered at every push and pull_request for example, we could also indicate some branches
- jobs: indicate OS and then indicate the steps, and we can also use some marketplace tools to reuse some of the most common tasks
- we can set env variables for the entire build or only for specific jobs
- we can put the env variable secrets also in Github secrets in order to be protected and only accessible for the CI build, go to github repo > Settings > Secrets > New repository secret > set all necessary values here and then reference them in the .yml file with ${{secrets.DATABASE_HOSTNAME}} for example
- we can also set different environments (Testing, Production, etc) and then setup specific secrets for anyone of them and reduce the accessibility of the secrets too, we will have to specify the environment in the .yml file then
- we need to set a test db either in some other place or in that github actions machine


## Building Docker Images

https://docs.docker.com/build/ci/github-actions/

- Dockerhub > Account Settings > Security > New Access Token > Create token
- Create Github secrets for DOCKER_HUB_USERNAME and DOCKER_HUB_ACCESS_TOKEN
- Add the necessary steps in the build-deploy.yml github actions file to push the docker image to docker hub, it's possible to add caching 


## Deploy to Heroku

- In heroku, create a token and then use the built-in action for heroku deploy


## Failing tests in pipeline

- If the build job fails (due to requisites, tests, etc.), the deploy job won't run


## Deploy to Ubuntu

- In the deploy job, with a built-in action to remotely connect through ssh to a server and run commands, set the necessary commands to pull the repo or the docker image and systemctl restart api








