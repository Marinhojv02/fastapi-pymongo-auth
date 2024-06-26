﻿# fastapi-pymongo-auth
## How to use the project

To install dependencies, run:
`pip install -r requirements.txt`

To run the application, execute the following command:
`uvicorn main:app --reload`

## Accessing Swagger UI

Once the app is running, you can access the Swagger documentation at:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Project Structure

The main components of this project are:

-   `main.py`: Entry point of the FastAPI application.
-   `app/`: Directory containing the FastAPI application.
	-   `models/`: Directory for data models used in the application.
	-   `controllers/`:Directory for controller modules handling API logic.
	-  	 `services/`: Directory for service modules handling business logic.
	-   `routes/`: Directory for route modules defining API endpoints.
	-  `utils/`: Directory for handling validations, constants and configs.
-   `requirements.txt`: List of Python dependencies.
