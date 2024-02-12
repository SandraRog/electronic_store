**Parts Warehouse REST API**
This is a simple REST API for managing parts in a warehouse, designed to be used in electronic repair workshops. The API is connected to a MongoDB database and provides CRUD functionality for managing parts and categories. Additionally, it includes an endpoint for searching parts.

__Setup__

__Requirements__
- Python 3.x
- Docker
- pymongo 3.12.3
- Django
- djangorestframework
  
__Installation__
Clone this repository to your local machine:

bash
Copy code
git clone <repository_url>
Navigate to the project directory:

bash
Copy code
cd parts-warehouse-api
Create a virtual environment:

bash
Copy code
python3 -m venv venv
Activate the virtual environment:

bash
Copy code
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up MongoDB:

Install MongoDB on your local machine or use a MongoDB instance provided by a service like MongoDB Atlas.
Update the MongoDB connection settings in settings.py file to point to your MongoDB instance.
Run the API:

bash
Copy code
python manage.py runserver

**API Endpoints**
__Parts__
GET /parts/: Get all parts.
POST /parts/: Create a new part.
GET /parts/{id}/: Get a specific part.
PUT /parts/{id}/: Update a specific part.
DELETE /parts/{id}/: Delete a specific part.
GET /parts/search/?query={query}: Search for parts by name or description.
__Categories__
GET /categories/: Get all categories.
POST /categories/: Create a new category.
GET /categories/{id}/: Get a specific category.
PUT /categories/{id}/: Update a specific category.
DELETE /categories/{id}/: Delete a specific category.
__Locations__
GET /locations/: Get all parts.
POST /locations/: Create a new part.
GET /locations/{id}/: Get a specific part.
PUT /locations/{id}/: Update a specific part.
DELETE /locations/{id}/: Delete a specific part.

**Docker**
This application is containerized using Docker. To run the application in a Docker container, follow these steps:

Build the Docker image:

bash
Copy code
docker build -t parts-warehouse-api .
Run the Docker container:

bash
Copy code
docker run -p 8000:8000 parts-warehouse-api
The API will be accessible at http://localhost:8000/.

**Data Format**
The API returns results in JSON format.
