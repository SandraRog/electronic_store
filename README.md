**Parts Warehouse REST API**
This is a simple REST API for managing parts in a warehouse, designed to be used in electronic repair workshops. The API is connected to a PostgreSQL database and provides CRUD functionality for managing parts and categories. Additionally, it includes an endpoint for searching parts.<br>

__Setup__<br>

__Requirements__<br>
- Python 3.x
- Docker
- Django
- djangorestframework<br>
  
__Installation__<br>
1. Clone this repository to your local machine:<br>
bash<br>
Copy code<br>
```
git clone <repository_url>
```
2. Navigate to the project directory:<br>
bash<br>
Copy code<br>
```
cd parts-warehouse-api
```
3. Create a virtual environment:<br>
bash<br>
Copy code<br>
```
python3 -m venv venv
```
4. Activate the virtual environment:<br>
bash<br>
Copy code<br>
```
source venv/bin/activate
```
5. Install dependencies:<br>
bash<br>
Copy code<br>
```
pip install -r requirements.txt
```
6. PostgreSQL Configuration:<br>
Install PostgreSQL on your local machine or use a PostgreSQL instance provided by a cloud service.
Update the PostgreSQL connection settings in the settings.py file to point to your PostgreSQL instance.<br>
bash<br>
Copy code<br>
```
python manage.py runserver
```

**API Endpoints**<br>
__Parts__<br>
GET /parts/: Get all parts.<br>
POST /parts/: Create a new part.<br>
GET /parts/{id}/: Get a specific part.<br>
PUT /parts/{id}/: Update a specific part.<br>
DELETE /parts/{id}/: Delete a specific part.<br>
GET /parts/search/?query={query}: Search for parts by name or description.<br><br>
__Categories__<br>
GET /categories/: Get all categories.<br>
POST /categories/: Create a new category.<br>
GET /categories/{id}/: Get a specific category.<br>
PUT /categories/{id}/: Update a specific category.<br>
DELETE /categories/{id}/: Delete a specific category.<br><br>
__Locations__<br>
GET /locations/: Get all parts.<br>
POST /locations/: Create a new part.<br>
GET /locations/{id}/: Get a specific part.<br>
PUT /locations/{id}/: Update a specific part.<br>
DELETE /locations/{id}/: Delete a specific part.<br>

**Docker**<br>
This application is containerized using Docker. To run the application in a Docker container, follow these steps:<br>

1. Build the Docker image:<br>
bash<br>
Copy code<br>
```
docker build -t parts-warehouse-api .
```
2. Run the Docker container:<br>
bash<br>
Copy code<br>
```
docker run -p 8000:8000 parts-warehouse-api
```
The API will be accessible at http://localhost:8000/.<br>

**Data Format**<br>
The API returns results in JSON format.
