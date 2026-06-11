---
name: HTTP trigger 3
description: Call the animals skill

logger: true
trigger:
  type: http_trigger
  args:
    route: http3
    methods: ["POST"]
    auth_level: function

response_example: |
  {
    "result": "impact"
  }
---

Accept a request body that has the following json format:
{"animal": "animal_type"}

Use the animals skill to return a response.
