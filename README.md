# Operations solver microservice
This is a microservice that exposes an API to solve different mathematical operations:
- the pow function
- the n-th fibbonaci number
- the factorial of the number

It was built with:
- ```PostgreSQL``` as the relational database to store the data about performed operations. I created the database operations_db and then, a table called operations. The table contains the following columns:
    - id - the identifier of an operation;
    - type - what kind of operation needs to be computed;
    - operand_a - the first operand that appears in every type of permitted operation;
    - operand_b - the second operand that can appear just in pow function;
    - result - to store the result of a computed operation;
    - timestamp - this is the time when the operation was performed.

- ```Python with Flask``` as the app server that processes the user requests and interacts with the database to store every computed operation. To communicate with the interface, I created the routes:
    - ROUTE: /api, method: GET -  This route is used to land the initial page, which means generating the JWT token and rendering the template;
    - ROUTE: /api/solve, method: POST - This route was created to make the request for solving a certain operation with the chosen parameters and for inserting the operation data in the database.

- ```Docker Compose``` as the tool used for managing and running the multi-container Docker app. It creates 2 containers: the first one is for the backend and the second one is for the database. The frontend did not require a container, because I used a Jinja template rendered server-side in Flask.


### Important additions:
- Packages:
    - flask_monitoringdashboard - for monitoring and performance dashboards;
    - psycopg2 - PostgreSQL driver used for database connection;
    - jwt - for handling JSON Web Token-based authorization;
    - flask_caching - to enable and manage caching.
- Blueprints:
    - Added ```solving_bp``` blueprint for encapsulating all routes and logic for the solving of the required math operations.

## Running this app:
You will need to have Docker installed. If you are using Windows, it is needed to follow along inside of WSL or WSL2, where you are going to run shell commands.

__Step 1__: Clone this repo anywhere you want and move into the directory:
```
git clone https://github.com/beth23eli/Teme_python.git

cd tema_project/math_operations_service
```

__Step 2__: Copy an example .env file because the real one is git ignored:
```
cp .env.example .env
```

__Step 3__: Start **wsl**:
```
wsl
```
__Step 4__: Open **Docker Desktop**.
 

__Step 5__: Run the **docker-compose** file to build the images and to run the containers:
```
docker-compose up --build 
```

__Step 6__: You can check it out in a browser by visiting <a href="http://localhost:5000/api">http://localhost:5000/api</a>

__Step 7__: If you want to view the monitoring dashboard, you need to visit <a href="http://localhost:5000/dashboard/overview">http://localhost:5000/dashboard/overview</a> and then log in with the credentials from the config.cfg file.



### Cleanup
To close the app, run:
```
docker-compose down
```
To also delete the volumes, run:
```
docker-compose down -v
```