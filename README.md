## Remind Me Later

This API provides endpoints for creating, retrieving, updating, and deleting reminders. It accepts these datapoints (i.e date, time and message) and store the info in database.


- Run the development server:

```` $ python manage.py runserver ````


### API Endpoints

GET /alert/: Retrieve a list of all reminders.
POST /alert/: Create a new reminder.
GET /alert/:id/: Retrieve a specific reminder.
PUT /alert/:id/: Update a specific reminder.
DELETE /alert/:id/: Delete a specific reminder.



- To create a reminder, send a POST request to /alert/ with the following JSON payload:
````
{
  "date": "YYYY-MM-DD",
  "time": "HH:MM:SS",
  "message": "Your reminder message"
}
````
- To retrieve all reminders, send a GET request to /alert/.
- To retrieve a specific reminder, send a GET request to /alert/:id.
- To update a specific reminder, send a PUT request to /alert/:id/ with the updated JSON payload.
- To delete a specific reminder, send a DELETE request to /alert/:id/.


### Technologies Used
Python 3.10.4
Django==4.1.6
djangorestframework==3.14.0
