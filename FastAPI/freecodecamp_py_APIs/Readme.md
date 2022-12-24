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