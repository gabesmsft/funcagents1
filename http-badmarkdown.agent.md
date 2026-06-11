\---

name: Missing markdown format

description: Missing markdown format - including this file for testing purposes.



trigger:

&#x20; type: http\_trigger

&#x20; args:

&#x20;   route: http1

&#x20;   methods: \["POST"]

&#x20;   auth\_level: function



response\_example: |

&#x20; {

&#x20;   "accountName": "account\_name", "containerName": "container\_name"

&#x20; }

\---



Accept a request body that has the following json schema, where account\_name and container\_name are placeholders for the actual variables:

{"accountName": "account\_name", "containerName": "container\_name"}



Send a message to the sbq1 queue in the service bus namespace that is specified in the $sbconn1 connection. If there is an exception when trying to put the message in the queue, return a human-understandable response with the reason, if the reason does not compromise security according to general best practices. Otherwise return a human-friendly response that generally indicates that there was an issue with fulfilling the request.

