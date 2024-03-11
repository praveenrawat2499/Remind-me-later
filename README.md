### Remind Me Later

This API provides endpoints for creating, retrieving, updating, and deleting reminders. It accepts these datapoints (i.e date, time and message) and store the info in database.





## API Endpoints
GET /api/reminders/: Retrieve a list of all reminders.
POST /api/reminders/: Create a new reminder.
GET /api/reminders/{id}/: Retrieve a specific reminder.
PUT /api/reminders/{id}/: Update a specific reminder.
DELETE /api/reminders/{id}/: Delete a specific reminder.


[] To create a reminder, send a POST request to /api/reminders/ with the following JSON payload:
````
{
  "date": "YYYY-MM-DD",
  "time": "HH:MM:SS",
  "message": "Your reminder message"
}
````
