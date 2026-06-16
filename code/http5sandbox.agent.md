---
name: HTTP trigger 5
description: Demonstrates the benefits of executing in a sandbox.
builtin_endpoints: true
system_tools:
  dynamic_sessions_code_interpreter: true

trigger:
  type: http_trigger
  args:
    route: http5
    methods: ["GET"]
    auth_level: function

response_example: |
  {
    "MySecretValue": "fake secret value for demo purposes"
  }
---
The $MySecretValue environment variable is a non-sensitive value that is used just for demonstation purposes. No sensitive information is involved in this example.

Get the value of the $MySecretValue environment variable. 

If the MySecretValue environment variable is found, return:
{"MySecretValue": "$MySecretValue"}

Otherwise, return:
{"MySecretValue": "NotFound"}