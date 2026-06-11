---
name: HTTP trigger 1
description: Simple HTTP trigger and logger test
system_tools:
  dynamic_sessions_code_interpreter: false


logger: true
trigger:
  type: http_trigger
  args:
    route: http1
    methods: ["GET"]
    auth_level: function

response_example: |
  {
    "Greeting": "Name"
  }
---

Do the following:
1. Log the message "I like cornflakes", with "http1 agent" as the source.
2. In the response, enter "Howdy" as the Greeting, and enter "World" as the name. 
