---
name: HTTP trigger 3
description: Call the animals skill

builtin_endpoints:
  debug_chat_ui: true
  chat_api: false
  mcp: false

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

Use the animals skill to return the following response (adjusted for grammar, based on {item}):
{"impact": "Your {item} is ruined! Impact: ${cost}"}