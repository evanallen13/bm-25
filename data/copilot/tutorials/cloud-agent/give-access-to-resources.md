# Giving GitHub Copilot cloud agent access to resources in your organization

Get more out of Copilot by giving it access to approved MCP servers and internal packages.

Copilot cloud agent can connect to MCP servers, use private packages, and access external services, but only if your organization's repositories are configured to allow it.

Although much of the configuration below is done at the repository level, organization owners have control over which resources are in scope and who can configure access to them.

## Example scenario

Your organization uses Sentry to track bugs in your Node app. New exceptions are raised as issues on GitHub, and your developers want to assign these issues to Copilot.

You want Copilot to:

* Connect to the Sentry MCP server so it can access details on your Sentry instance
* Install dependencies, including private packages hosted on GitHub, to build your app and run tests
* Follow your organization's conventions for error-handling

## Storing secrets securely

By default, the scope of Copilot's authentication token is limited to the repository where it's running. This means that Copilot won't be able to authenticate to external systems or access private, organization-scoped packages.

Repository administrators should add variables and secrets that Copilot requires to a dedicated `copilot` GitHub Actions environment. Copilot can access this data in its setup and task execution. It won't be able to access variables or secrets outside this environment, such as organization-wide GitHub Actions secrets.

### Example: Save a secret

A repository administrator saves an authentication token for the organization's Sentry instance.

1. Go to the **Environments** section of the repository settings.
2. Create a new environment called `copilot`.
3. Save an access token for your Sentry instance in an environment secret called `COPILOT_MCP_SENTRY_ACCESS_TOKEN`.

> \[!TIP] We don't need to save a token for our private GitHub Packages registry, which we'll access using the standard GitHub Actions `GITHUB_TOKEN`. However, you would want to save an authentication token if you were using an external package registry.

## Configuring access to MCP servers

Organization and enterprise owners can set a policy to allow users to configure access to MCP servers. If this policy is enabled, users can configure MCP servers for Copilot cloud agent in repository settings or in custom agent profiles. For organization-wide consistency, we recommend creating **custom agent profiles** at the organization or enterprise level.

A session using a custom agent has access to MCP servers configured in **both** the repository settings and the agent profile. However, the more use cases you cover with organization-wide custom agents, the less users will need to configure ad hoc access to MCP servers in repository settings.

We recommend browsing the [GitHub MCP Registry](https://github.com/mcp) to find trusted, highly rated options.

### Example: Create a custom agent

An organization owner creates a custom agent profile for the Sentry agent. It has access to the Sentry MCP server and custom instructions for the organization's error-handling conventions.

1. Create a repository called `.github-private` in your organization. Optionally, an enterprise owner can set this repository as the source for all custom agents in the enterprise.

2. In the repository, add an `agent.md` file with a profile like the following. This includes configuration for the MCP server, which references the secret we saved.

   ```text
   ---
   name: sentry-error-fixer
   description: Proposed fixes for exception issues raised from Sentry
   mcp-servers:
     sentry:
       type: 'local'
       command: 'npx'
       args: ['@sentry/mcp-server@latest']
       env:
         SENTRY_ACCESS_TOKEN: ${{ secrets.COPILOT_MCP_SENTRY_ACCESS_TOKEN }}
   ---

   You are an error resolution specialist. When you're assigned an issue created by our Sentry integration, check for error details and stack traces using the MCP server, then propose a fix.

   Make sure you check that your proposed fix works by building the site with `npm run build` and running the test suite in `npm test`.
   ```

3. When developers assign an issue to Copilot, they can select the custom agent from a dropdown.

## Installing private packages

The best way to give Copilot access to a project's dependencies is to install them in a `copilot-setup-steps.yml` workflow file. This file defines how the environment is set up before Copilot starts working.

To allow the workflow to pull your private, organization-scoped packages, you will update the package settings to make sure that the repository's `GITHUB_TOKEN` has access to the package. This is more secure than using a long-lived personal access token with organization permissions.

### Example: Install Node dependencies

A developer creates a workflow to install the Node dependencies defined in a repository's `package-lock.json` file. This includes private, organization-scoped packages hosted on GitHub.

1. The developer creates a `copilot-setup-steps.yml` file in the repository.

2. They add steps for installing the project's dependencies. For example:

   ```yaml
   # ...

   jobs:
     copilot-setup-steps:
       # ...

       # You can define any steps you want, and they will run before the agent starts.
       # If you do not check out your code, Copilot will do this for you.
       steps:
         - name: Checkout code
           uses: actions/checkout@v6

         - name: Set up Node.js
           uses: actions/setup-node@v4
           with:
             node-version: "20"
             cache: "npm"

         - name: Install JavaScript dependencies
           run: npm ci
   ```

3. An organization administrator ensures that the repository has access to the organization's private packages by granting access to the repository in each package's settings. See [Configuring a package's access control and visibility](/en/packages/learn-github-packages/configuring-a-packages-access-control-and-visibility#github-actions-access-for-packages-scoped-to-organizations).

> \[!TIP] If you need to access packages that are hosted internally within your corporate network, you may need to run Copilot cloud agent on self-hosted GitHub Actions runners.

## Controlling who can configure these settings

Now you have seen how access to resources is controlled at the repository and organization levels, consider how much scope you want to give users to manage these settings.

1. **Choose which repositories have access** to Copilot cloud agent. If you're concerned about a specific repository, you can block it for all users.
2. **Consider who gets admin access** to these repositories. You can control this at the organization level by creating a team with the **All-repository admin** custom role. These users will be able to manage configuration *settings*, such as MCP configuration and `copilot` environments, in every repository.
3. **Use rulesets and CODEOWNERS files** to control edits of configuration *files*, such as `copilot-setup-steps.yml`, which anyone with write access can edit by default.
4. **Review the default firewall**. The firewall doesn't affect connections to MCP servers or setup steps in `copilot-setup-steps.yml`, but it does limit Copilot's access to the Internet during task execution. See [Customizing or disabling the firewall for GitHub Copilot cloud agent](/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall).