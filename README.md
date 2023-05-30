# OpenAPI Vehicle Tester
This Django project provides an API for managing vehicle information. It provides endpoints for **creating**, **retrieving**, **updating**, and **deleting** vehicle records. Follow the instructions below to set up and run the project on your local computer.

## **Prerequisites**
Make sure you have the following software installed on your computer:
1.  Python
2.  Virtual environment
3.  Django
4.  Django REST Framework

## **Installation and Setup**
1.  Download the project files and extract them to a directory of your choice.
2.  Open a terminal or command prompt and navigate to the project directory using the **`cd`** command. For example:
```bash
cd Desktop/hellofleet-candidate
```
3.  Activate a virtual environment to isolate the project's dependencies. Run the following commands:
```bash
vehicles\venv\Scripts\activate
```
4. Change the directory to the `vehicles` folder by running the following command:
```bash
cd vehicles
```
5. Start the Django development server by running the following command:
```bash
python manage.py runserver 8080
```
The server should start running on http://localhost:8080/.

## **Testing the API**
You can test the API using the provided URLs or cURL commands.
1. Open web browser to access the following URLs:
	-   [http://localhost:8080/heartbeat](http://localhost:8080/heartbeat)
	-   [http://localhost:8080/vehicles](http://localhost:8080/vehicles)
	-   [http://localhost:8080/vehicle/1](http://localhost:8080/vehicle/1)
	-   [http://localhost:8080/vehicle](http://localhost:8080/vehicle)
	-   [http://localhost:8080/vehicle/7/create-or-update](http://localhost:8080/vehicle/7/create-or-update)
	-   [http://localhost:8080/vehicle/5/update](http://localhost:8080/vehicle/5/update)
	-   [http://localhost:8080/vehicle/7/delete](http://localhost:8080/vehicle/7/delete)
2. Alternatively, you can use cURL commands to interact with the API. Open a terminal or command prompt and run the following commands: 
	```bash
	curl -X GET http://localhost:8080/heartbeat
	curl -X GET http://localhost:8080/vehicles
	curl -X GET http://localhost:8080/vehicle/1
	curl -X POST -H "Content-Type: application/json" -d "{\"name\": \"AV9\", \"description\": \"Auto Vehicle 9\"}" http://localhost:8080/vehicle
	curl -X PUT -H "Content-Type: application/json" -d "{\"passenger\": 2}" http://localhost:8080/vehicle/9/create-or-update
	curl -X PATCH -H "Content-Type: application/json" -d "{\"passenger\": 0}" http://localhost:8080/vehicle/1/update
	curl -X DELETE http://localhost:8080/vehicle/8/delete
	```
## **Explaination**
1. **Assumption make:**
	- The instructions set the column name to "detail," but the OpenAPI specification set the column name to "passenger," so I thought the column should be called "passenger" instead. Therefore, the modification was made to align with the OpenAPI specification, and the column name in the Vehicle model was created as "passenger." The column is defined as an IntegerField with a default value of 0.
2. **Thinking process:**
	- I use the Django and Django REST Framework to implement the defined open API specification as a server-side REST endpoint and follow the RESTful principles for CRUD operations on vehicle information. To successfully implement the REST endpoint, there have several processes need to be involved:
		- Defining a model with the required fields.
		- Create serializers to serialize the data in order to read, create, update, and delete vehicle information.
		- Implementing view functions for each endpoint handles the request processing and returns appropriate responses.
		- Handling potential errors and exceptions and returning meaningful error messages.
3. **Design and implementation:**
	- The project consists of the following components:
		- models.py: Defines the model called "Vehicle". The Vehicle model includes id, name, description, and passenger.
		- serializers.py: Defines two serializers, VehicleListSerializer and VehicleCreateSerializer, for the Vehicle model. VehicleListSerializer is used to serialize the list of vehicles with selected fields, while VehicleCreateSerializer is used for creating and updating new vehicles with all fields.
		- views.py: Implements the API views corresponding to the defined URL patterns. The views include functions for getting the heartbeat, retrieving the vehicle list, retrieving specific vehicle information, creating vehicles, creating or updating vehicles, updating vehicles, and deleting vehicles. The functions also handle request processing and return appropriate responses.
		- urls.py: Contains URL patterns for different API endpoints, such as heartbeat, all vehicles, vehicle details, create a vehicle, create or update vehicle information, update vehicle information, and delete the vehicle.
4. **Limitation:**
	- Due to my lack of knowledge, I can't implement the authentication or authorization methods in some APIs such as retrieving the vehicle list, retrieving specific vehicle information, creating or updating vehicles, and deleting vehicles.
	- I did not include more error handling and may not cover all possible scenarios or responses.
5. **Improvements:**
	- In the future, I will add authentication and authorization ways to secure the API endpoints and control who can use the resources.
	- Enhanced error handling to provide more specific error information and handle a wider range of exceptions.
