---
name: Service Bus Q trigger 1
description: Returns a list of blobs in a container

trigger:
  type: service_bus_queue_trigger
  args:
    queue_name: sbq1
    connection: sbqconn1
---
Process queue messages that contain the following JSON format:
  {
    "food_or_drink": "recommendation"
  }


If the key contains "food", call the food_recommendation tool.
Else, if the key contains "drink", call the drink_recommendation tool.
Else, log "message rejected because it does not contain a food or drink recommendation-related request, and then return without taking further action.

Do one of the following:
- If the tool successfully returned data, log "sbqtrigger1 was triggered! " plus the tool response.
- If there is an exception: log "No joy in sbqtrigger1: " followed by the inner exception or summary of the issue to the console output. For security reasons, do not return this information in an HTTP response.

