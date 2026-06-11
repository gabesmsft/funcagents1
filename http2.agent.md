---
name: HTTP trigger 2
description: Call the food or drink recommendation tool
builtin_endpoints: true
system_tools:
  dynamic_sessions_code_interpreter: true

trigger:
  type: http_trigger
  args:
    route: http2
    methods: ["POST"]
    auth_level: function

response_example: |
  {
    "recommendation": "food_or_drink_recommendation"
  }
---

Accept a request body that has the following json format:
{"food_or_drink": "taste_or_texture"}

 Log the message "I like cornflakes", with "http2 agent" as the source.

If the key contains "food", call the food_recommendation tool.
If the key contains "drink", call the drink_recommendation tool.

Before returning the HTTP response to the client, log "http2 code wrote something! ", followed by the response from the tool.

Using "http2 agent" as the source in the logger:
- If an ACA session was called, log the message "ACA session called: ", followed by the session ID and the session's response.
Else if an ACA session was not called, , log "http2 ACA session was not called".
Else log "What is an ACA session?".

If there is an issue when trying to call the tool, do the following:
1. Log "No joy in http2: ", followed by the inner exception or summary of the issue. For security reasons, do not return this information in the HTTP response.
2. Return the following response:
{"responseText": "There was an issue with fulfilling this request."}
