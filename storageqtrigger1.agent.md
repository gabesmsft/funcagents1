---
name: Storage Q trigger 1
description: Returns the body contents of a queue message

trigger:
  type: queue_trigger
  args:
    queue_name: fakeq1
    connection: AzureWebJobsStorage
---
Log "Queue trigger test: " plus the body contents of the queue message in utf-8 format.
