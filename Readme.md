# Serverless Agents runtime for Azure Functions example

This sample application uses [Serverless Agents runtime](https://learn.microsoft.com/azure/azure-functions/functions-serverless-agents-runtime) for Azure Functions.

This application demonstrates very simple examples of using the markdown function agents, skills, custom tools, Container Apps dynamic sessions, and remote MCP servers in Serverless Agents. These are not meant to to be real-world examples, but clear, simple examples that demonstrate the functionality.

## Prerequisites

- [Azure Functions Core Tools](https://learn.microsoft.com/azure/azure-functions/functions-run-local?tabs=windows%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-csharp#install-the-azure-functions-core-tools) 4.12.0 or later for local testing and deployment to Azure Functions.
- Python and Pip for building the app locally. Am using Python 3.13 and Pip 26.1.1, but these aren't necessarily the earliest versions required.
- A Function App in Flex Consumption, with Python selected as the language runtime.
- Enable system-managed identity on the Function App. You can also use a user-assigned managed identity, but this example references system-managed identity for simplicity.
- A Microsoft Foundry project, with a deployed gpt-4o model. You can use a different model, and can also use an Azure Open AI project, but the references in this example are specific to Foundry and gpt-4o for simplicity.
  - Grant the Function App's managed identity the **Foundry User** role on the Foundry project resource.
- Deploy the Functions MCP server example found [here](https://github.com/gabesmsft/MCPFunctions). This will act as the remote MCP server for the Serverless Agents example.
- A [Container Apps code interpretter session pool](https://learn.microsoft.com/azure/container-apps/sessions-code-interpreter). This is optional and will be used to test the sandboxed execution functionality. You can deploy a Container Apps Session Pool via the Azure portal. Select platform built-in container (wording might differ) rather than custom container, and select Python.
  - Grant the Function App's managed identity the **Azure ContainerApps Session Executor** role on the Container Apps Session Pool resource.
- A Storage queue named **fakeq1**, in the same account used by AzureWebJobsStorage for simplicity. This will be used for the queue trigger agent function. If you don't want to test this, you can delete the storageqtrigger1.agent.md.
- Set the following environment variables on the Function App and/or in your local.settings.json (replace fields in <>, including the <>):
  - ACA_SESSION_POOL_ENDPOINT:  https://<region>.dynamicsessions.io/subscriptions/<subscriptionId>/resourceGroups/<resourceGroupName>/sessionPools/<sessionPoolName>
  - FOUNDRY_MODEL: gpt-4o
  - FOUNDRY_PROJECT_ENDPOINT: https://<FoundryProjectResource>.services.ai.azure.com/api/projects/<projectName>
  - MCP_URL_1: https://<FunctionAppHostPrefix of the MCP Function App you deployed>.azurewebsites.net/runtime/webhooks/mcp
  - FUNCTIONS_MCP_EXTENSION_SYSTEM_KEY_1: <mcp_extension app key from the MCP Function App you deployed>




## Test locally
### Preparation
1. Download the repository, and change to the **code** directory.
2. Run **pip install -r requirements.txt**


## Test the agent functions and features

### Hello world and invoking a custom tool
- Inspect the http1.agent.md, and then trigger it via http://localhost:7071/http1

  Verify that the following occurs:
  - The returned response is **{"Greeting": "Howdy", "Name": "World"}**

    The returned response demonstrates using declarative instructions for the AI model via the md file, rather than programatically writing code.

  - The following is logged to the console: **[custom-logger-tool][http1 agent] I like cornflakes** is logged to the console.
  
    The logged message demonstrates invoking a custom python tool (tools/log_to_console.py) via the md file. At the time of this writing, Serverless Agents doesn't include a logger, so nothing would have been logged via the md instructions if we hadn't included a custom tool to peform the logging.

### Using a remote MCP server

- Inspect the http2.agent.md, and then make a POST request to it to ask for a food or drink recommendation based on taste or texture. E.g.:

  ```
  curl -X POST "http://localhost:7071/http2" -H "Content-Type: application/json" -d "{"food_or_drink":"savory"}"
  ```
The above request should invoke the food_recommendation MCP tool on the remote endpoint, and return the response of {"recommendation": "grits with butter"}

- Open the chat UI at http://localhost:7071/agents/http2 , and then ask the agent a couple more food and drink recommendation questions:
  - "What is a good drink that is fizzy?"
  - "What is a good food that is bitter?"

### Using skills

- Inspect the SKILL.md and linked files under the skills folder. These contents consist of some simple declarative instructions and markdown tables to associate animals to items and costs.

- Inspect the http3animal.agent.md. This file references the animals skill and contains instructions for how to consume the skill.

- Open the chat UI at http://localhost:7071/agents/http3animal , and then ask the agent some questions about the impact of certain pets:
  - "What is the impact if I get a dog?"
  - "What is the impact if I get a cat?"
  - "What is the impact if I get a gorilla?"
  - "What pet would you recommend if I don't like my house but I like my city?"

You can also invoke the agent via REST. E.g.:

 ```
  curl -X POST "http://localhost:7071/http3" -H "Content-Type: application/json" -d "{"animal":"dog"}"
  ```

### Using the sandbox (Container Apps Dynamic Sessions)

- Add an environment variable named MySecret. Give it a **non-sensitive** value. Do <u>not</u> use a sensitive value for this test.

- Note that the http4nosandbox.agent.md has dynamic_sessions_code_interpreter: false. Make a request to http://localhost:7071/http4

  This should return the value that you set for the MySecret environment variable. 

- Note that the http4sandbox.agent.md has dynamic_sessions_code_interpreter: true. This is the default value for dynamic_sessions_code_interpreter, and you do not need to explicitly set it. Make a request to http://localhost:7071/http5

  This should return NotFound, because the execution happens in a Dynamic Sessions sandbox rather than on your machine or in the Function App. The MySecret environment variable is not present in the sandbox. This demonstrates a security benefit of executing code in Dynamic Sessions / sandboxes.

### Test an event trigger
Test the storageqtrigger1.agent.md by putting a message in the fakeq1 Storage queue. A Storage queue trigger is generated in the Functions host, which triggers the instructions in the md file. In this case, the instructions log the contents of the queue message.

    > Note: the custom python tool (tools/log_to_console.py) is invoked to do the logging since at the time of this writing, Serverless Agents doesn't include a logger.

### Test in the Function App

When testing in the Function App, replace http://localhost:7071 with https://<YourFunctionsHostPrefix>.azurewebsites.net in the above examples. Additionally:

- If invoking an HTTP trigger, add ?code=<FunctionKey> to the end of the URL.
- If using the agent chat, you will be prompted for a key after you enter input into the chat for the first time. Use the default host key. At the time of this writing, the key you enter gets saved to the browser cookies or cache. If you enter a wrong key or want to clear the saved key, clear your browser cookies and/or cache.