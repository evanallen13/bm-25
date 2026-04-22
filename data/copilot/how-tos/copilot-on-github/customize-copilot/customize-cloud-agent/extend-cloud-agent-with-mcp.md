# Connect agents to external tools

Connect Copilot cloud agent to external tools and data sources through the Model Context Protocol (MCP).

## Prerequisite

Before setting up an MCP server for Copilot cloud agent, read [Model Context Protocol (MCP) and GitHub Copilot cloud agent](/en/copilot/concepts/agents/cloud-agent/mcp-and-cloud-agent) to make sure you understand the concepts around MCP servers and Copilot cloud agent.

## Introduction

As a repository administrator, you can configure MCP servers for use within your repository. You do this using a JSON-formatted configuration that specifies the details of the MCP servers you want to use. You enter the JSON configuration directly into the settings for the repository on GitHub.com.

Organization and enterprise administrators can also configure MCP servers as part of custom agents using the YAML frontmatter. For more information, see [Custom agents configuration](/en/copilot/reference/custom-agents-configuration#mcp-server-configuration-details).

> \[!WARNING]
> Once you've configured an MCP server, Copilot will be able to use the tools provided by the server autonomously, and will not ask for your approval before using them.

> \[!NOTE]
>
> * Copilot cloud agent only supports tools provided by MCP servers. It does not support resources or prompts.
> * Copilot cloud agent does not currently support remote MCP servers that leverage OAuth for authentication and authorization.

## Adding an MCP configuration to your repository

Repository administrators can configure MCP servers by following these steps:

1. On GitHub, navigate to the main page of the repository.

2. Under your repository name, click **<svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-gear" aria-label="gear" role="img"><path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path></svg> Settings**. If you cannot see the "Settings" tab, select the **<svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-kebab-horizontal" aria-label="More" role="img"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg>** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)

3. In the "Code & automation" section of the sidebar, click **Copilot** then **Cloud agent**.

4. Add your configuration in the **MCP configuration** section.

   The following sections in this article explain how to write the JSON configuration that you need to enter here.

5. Click **Save**.

   Your configuration will be validated to ensure proper syntax.

6. If your MCP server requires a variable, key, or secret, add a variable or secret to your Copilot environment. Only variables and secrets with names prefixed with `COPILOT_MCP_` will be available to your MCP configuration. See [Setting up a Copilot environment for Copilot cloud agent](#setting-up-a-copilot-environment-for-copilot-cloud-agent).

## Writing a JSON configuration for MCP servers

You configure MCP servers using a special JSON format. The JSON must contain an `mcpServers` object, where the key is the name of the MCP server (for example, `sentry`), and the value is an object with the configuration for that MCP server.

```json copy
{
  "mcpServers": {
    "MCP SERVER 1": {
      "command": "VALUE",
      "args": [ VALUES ],
      ...
    },
    "MCP SERVER 2": {
      "command": "VALUE",
      "args": [ VALUES ],
      ...
    },
    ...
  }
}
```

The configuration object can contain the following keys:

**Required keys for local and remote MCP servers**

* `tools` (`string[]`): The tools from the MCP server to enable. You may be able to find a list of tools in the server's documentation, or in its code. We strongly recommend that you allowlist specific read-only tools, since the agent will be able to use these tools autonomously and will not ask you for approval first. You can also enable all tools by including `*` in the array.
* `type` (`string`): Copilot cloud agent accepts `"local"`, `"stdio"`, `"http"`, or `"sse"`.

**Local MCP specific keys**

* `command` (`string`): Required. The command to run to start the MCP server.
* `args` (`string[]`): Required. The arguments to pass to the `command`.
* `env` (`object`): Optional. The environment variables to pass to the server. This object should map the name of the environment variable that should be exposed to your MCP server to one of the following:
  * A substitution reference to a secret or variable in your Copilot environment, such as `$COPILOT_MCP_API_KEY` or `${COPILOT_MCP_API_KEY}`. Referenced names must start with `COPILOT_MCP_`.
  * A literal string value.

**Remote MCP specific keys**

* `url` (`string`): Required. The MCP server's URL.
* `headers` (`object`): Optional. The headers to attach to requests to the server. This object should map the name of header keys to one of the following:
  * A substitution reference to a secret or variable in your Copilot environment, such as `$COPILOT_MCP_API_KEY` or `${COPILOT_MCP_API_KEY}`. Referenced names must start with `COPILOT_MCP_`.
  * A literal string value.

Note that all `string` and `string[]` fields besides `tools` and `type` support substitution with a variable or secret you have configured in your Copilot environment.

### Variable substitution

The following syntax patterns are supported for referencing environment variables configured in your Copilot environment:

| Syntax            | Example                                  |
| ----------------- | ---------------------------------------- |
| `$VAR`            | `$COPILOT_MCP_API_KEY`                   |
| `${VAR}`          | `${COPILOT_MCP_API_KEY}`                 |
| `${VAR:-default}` | `${COPILOT_MCP_API_KEY:-fallback_value}` |

## Example configurations

The examples below show MCP server configurations for different providers.

* [Sentry](#example-sentry)
* [Notion](#example-notion)
* [Azure](#example-azure)
* [Cloudflare](#example-cloudflare)
* [Azure DevOps](#example-azure-devops)
* [Atlassian](#example-atlassian)

### Example: Sentry

The [Sentry MCP server](https://github.com/getsentry/sentry-mcp) gives Copilot authenticated access to exceptions recorded in [Sentry](https://sentry.io).

```javascript copy
// If you copy and paste this example, you will need to remove the comments prefixed with `//`, which are not valid JSON.
{
  "mcpServers": {
    "sentry": {
      "type": "local",
      "command": "npx",
      // We can use the $SENTRY_HOST environment variable which is passed to
      // the server because of the `env` value below.
      "args": ["@sentry/mcp-server@latest", "--host=$SENTRY_HOST"],
      "env": {
        // We can specify an environment variable value as a string...
        "SENTRY_HOST": "https://contoso.sentry.io",
        // or refer to a variable or secret in your Copilot environment
        // with a name starting with `COPILOT_MCP_`
        "SENTRY_ACCESS_TOKEN": "$COPILOT_MCP_SENTRY_ACCESS_TOKEN"
      }
    }
  }
}
```

### Example: Notion

The [Notion MCP server](https://github.com/makenotion/notion-mcp-server) gives Copilot authenticated access to notes and other content from [Notion](https://notion.so).

```javascript copy
// If you copy and paste this example, you will need to remove the comments prefixed with `//`, which are not valid JSON.
{
  "mcpServers": {
    "notionApi": {
      "type": "local",
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "-e",
        // We can use the $NOTION_API_KEY environment variable which is passed to
        // the server because of the `env` value below.
        "OPENAPI_MCP_HEADERS={\"Authorization\": \"Bearer $NOTION_API_KEY\", \"Notion-Version\": \"2022-06-28\"}",
       "mcp/notion"
      ],
      "env": {
        // The value of the `COPILOT_MCP_NOTION_API_KEY` secret will be passed to the
        // server command as an environment variable called `NOTION_API_KEY`
        "NOTION_API_KEY": "$COPILOT_MCP_NOTION_API_KEY"
      },
      "tools": ["*"]
    }
  }
}
```

### Example: Azure

The [Microsoft MCP repository](https://github.com/microsoft/mcp) includes the Azure MCP server, which allows Copilot to understand your Azure-specific files and Azure resources within your subscription when making code changes.

To automatically configure your repository with a `copilot-setup-steps.yml` file to authenticate with Azure, plus secrets for authentication, clone the repository locally then run the [Azure Developer CLI](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/?ref_product=copilot\&ref_type=engagement\&ref_style=button)'s `azd cloud-agent config` command in the root of the repository.

Once you've run the command and merged the created pull request, you can add the MCP configuration to your repository.

```json copy
 {
   "mcpServers": {
     "Azure": {
      "type": "local",
      "command": "npx",
      "args": [
        "-y",
        "@azure/mcp@latest",
        "server",
        "start"
       ],
      "tools": ["*"]
     }
   }
 }
```

### Example: Cloudflare

The [Cloudflare MCP server](https://github.com/cloudflare/mcp-server-cloudflare) creates connections between your Cloudflare services, including processing documentation and data analysis.

```json copy
{
  "mcpServers": {
    "cloudflare": {
      "type": "sse",
      "url": "https://docs.mcp.cloudflare.com/sse",
      "tools": ["*"]
    }
  }
}
```

### Example: Azure DevOps

The [Azure DevOps MCP server](https://github.com/microsoft/azure-devops-mcp) creates a seamless connection between Copilot and your Azure DevOps services, including work items, pipelines or documentation.

To use the Azure DevOps MCP server with Copilot cloud agent, you must update the repository's copilot-setup-steps.yml file to include an Azure login workflow step.

1. Configure OIDC in a Microsoft Entra application, trusting GitHub. See [Use the Azure Login action with OpenID Connect](https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure-openid-connect).
2. Setup access to Azure DevOps organization and projects for the application identity. See [Add organization users and manage access](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/add-organization-users).
3. Add a `.github/workflows/copilot-setup-steps.yml` Actions workflow file in your repository if you do not already have one.
4. Add an Azure login step to the `copilot-setup-steps` workflow job.

   ```yaml copy
   # This workflow uses actions that are not certified by GitHub.
   # They are provided by a third-party and are governed by
   # separate terms of service, privacy policy, and support
   # documentation.
   on:
     workflow_dispatch:
   permissions:
     id-token: write
     contents: read
   jobs:
     copilot-setup-steps:
       runs-on: ubuntu-latest
       permissions:
         id-token: write
         contents: read
       environment: copilot
       steps:
         - name: Azure login
           uses: azure/login@a457da9ea143d694b1b9c7c869ebb04ebe844ef5
           with:
             client-id: ${{ secrets.AZURE_CLIENT_ID }}
             tenant-id: ${{ secrets.AZURE_TENANT_ID }}
             allow-no-subscriptions: true
   ```

   This configuration ensures the `azure/login` action is executed when Copilot cloud agent runs.
5. In your repository’s Copilot environment, add secrets for your `AZURE_CLIENT_ID` and `AZURE_TENANT_ID`.
6. Configure the Azure DevOps MCP server by adding an `ado` object to your MCP configuration with defined tools you want Copilot cloud agent to use.

```json copy
{
  "mcpServers": {
    "ado": {
      "type": "local",
      "command": "npx",
      "args": ["-y", "@azure-devops/mcp", "<your-azure-devops-organization>", "-a", "azcli"],
      "tools": ["wit_get_work_item", "wit_get_work_items_batch_by_ids", ...]
    }
  }
}
```

### Example: Atlassian

The [Atlassian MCP server](https://github.com/atlassian/atlassian-mcp-server) gives Copilot authenticated access to your Atlassian apps, including Jira, Compass, and Confluence.

For more information about authenticating to the Atlassian MCP server using an API key, see [Configuring authentication via API token](https://support.atlassian.com/atlassian-rovo-mcp-server/docs/configuring-authentication-via-api-token/) in the Atlassian documentation.

```javascript copy
// If you copy and paste this example, you will need to remove the comments prefixed with `//`, which are not valid JSON.
{
  "mcpServers": {
    "atlassian-rovo-mcp": {
      "command": "npx",
      "type": "local",
      "tools": ["*"],
      "args": [
        "mcp-remote@latest",
        "https://mcp.atlassian.com/v1/mcp",
        // We can use the $ATLASSIAN_API_KEY environment variable which is passed
        // to the server because of the `env` value below.
        "--header",
        "Authorization: Basic $ATLASSIAN_API_KEY"
      ],
      "env": {
        // The value of the `COPILOT_MCP_ATLASSIAN_API_KEY` secret will be passed
        // to the server command as an environment variable
        // called `ATLASSIAN_API_KEY`.
        "ATLASSIAN_API_KEY": "$COPILOT_MCP_ATLASSIAN_API_KEY"
      }
    }
  }
}
```

## Reusing your MCP configuration from Visual Studio Code

If you have already configured MCP servers in VS Code, you can leverage a similar configuration for Copilot cloud agent.

Depending on how VS Code is configured, you may be able to find your MCP settings in your repository's `.vscode/mcp.json` file, or in your machine's private `settings.json` file.

To adapt the configuration for Copilot cloud agent, you will need to:

1. Add a `tools` key for each MCP server, specifying which tools will be available to Copilot.
2. If you've configured `inputs`, switch to using `env` directly.
3. If you've configured an `envFile`, switch to using `env` directly.
4. Update any references to `inputs` in your `args` configuration to refer to environment variables from `env` instead.

For more information on MCP in VS Code, see the [VS Code docs](https://code.visualstudio.com/docs/copilot/chat/mcp-servers).

## Setting up a Copilot environment for Copilot cloud agent

Some MCP servers will require keys or secrets. To leverage those servers in Copilot cloud agent, you can add secrets to an environment for Copilot. This ensures the secrets are properly recognized and passed to the applicable MCP server that you have configured.

You must be a repository administrator to configure a Copilot environment for your repository.

1. On GitHub, navigate to the main page of the repository.
2. Under your repository name, click **<svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-gear" aria-label="gear" role="img"><path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path></svg> Settings**. If you cannot see the "Settings" tab, select the **<svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-kebab-horizontal" aria-label="More" role="img"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg>** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)
3. In the left sidebar, click **Environments**.
4. Click **New environment**.
5. Call the new environment `copilot` and click **Configure environment**.
6. Under "Environment secrets", click **Add environment secret**.
7. Give the secret a name beginning `COPILOT_MCP_`, add the secret value, then click **Add secret**.

## Validating your MCP configuration

Once you've set up your MCP configuration, you should test it to make sure it is set up correctly.

1. Create an issue in the repository, then assign it to Copilot.
2. Wait a few seconds, and Copilot will leave an 👀 reaction on the issue.
3. Wait a few more seconds, and Copilot will create a pull request, which will appear in the issue's timeline.
4. Click the created pull request in the timeline, and wait until a "Copilot started work" timeline event appears.
5. Click **View session** to open the Copilot cloud agent logs.
6. Click the ellipsis button (**...**) at the top right of the log viewer, then click **Copilot** in the sidebar.
7. Click the **Start MCP Servers** step to expand the logs.
8. If your MCP servers have been started successfully, you will see their tools listed at the bottom of the logs.

If your MCP servers require any dependencies that are not installed on the GitHub Actions runner by default, such as `uv` and `pipx`, or that need special setup steps, you may need to create a `copilot-setup-steps.yml` Actions workflow file to install them. For more information, see [Configure the development environment](/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment).

## Customizing the built-in GitHub MCP server

The GitHub MCP server is enabled by default and connects to GitHub with a specially scoped token that only has read-only access to the current repository.

If you want to allow Copilot to access data outside the current repository, you can give it a personal access token with wider access.

1. Create a personal access token with the appropriate permissions. We recommend using a fine-grained personal access token, where you can limit the token's access to read-only permissions on specific repositories. For more information on personal access tokens, see [Managing your personal access tokens](/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

2. On GitHub, navigate to the main page of the repository.

3. Under your repository name, click **<svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-gear" aria-label="gear" role="img"><path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path></svg> Settings**. If you cannot see the "Settings" tab, select the **<svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-kebab-horizontal" aria-label="More" role="img"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg>** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)

4. In the "Code & automation" section of the sidebar, click **Copilot** then **Cloud agent**.

5. Add your configuration in the **MCP configuration** section. For example, you can add the following:

   ```javascript copy
    // If you copy and paste this example, you will need to remove the comments prefixed with `//`, which are not valid JSON.
    {
      "mcpServers": {
        "github-mcp-server": {
          "type": "http",
          // Remove "/readonly" to enable wider access to all tools.
          // Then, use the "X-MCP-Toolsets" header to specify which toolsets you'd like to include.
          // Use the "tools" field to select individual tools from the toolsets.
          "url": "https://api.githubcopilot.com/mcp/readonly",
          "tools": ["*"],
          "headers": {
            "X-MCP-Toolsets": "repos,issues,users,pull_requests,code_security,secret_protection,actions,web_search"
          }
        }
      }
    }
   ```

   For more information on toolsets, refer to the [README](https://github.com/github/github-mcp-server?tab=readme-ov-file#available-toolsets) in the GitHub Remote MCP Server documentation.

6. Click **Save**.

7. In the left sidebar, click **Environments**.

8. Click the `copilot` environment.

9. Under "Environment secrets", click **Add environment secret**.

10. Call the secret `COPILOT_MCP_GITHUB_PERSONAL_ACCESS_TOKEN`, enter your personal access token in the "Value" field, then click **Add secret**.

For information on using the GitHub MCP server in other environments, see [Using the GitHub MCP Server in your IDE](/en/copilot/customizing-copilot/using-model-context-protocol/using-the-github-mcp-server).

## Next steps

* [Adding MCP servers for GitHub Copilot CLI](/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers)
* [Creating custom agents for Copilot cloud agent](/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-custom-agents)
* [Configure the development environment](/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment)
* [Extending GitHub Copilot Chat with Model Context Protocol (MCP) servers](/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp)