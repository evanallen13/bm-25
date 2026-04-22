# Customize Copilot for your project

Set up custom instructions, create a specialized agent, and organize project context on GitHub.

This quickstart walks you through customizing GitHub Copilot for a repository. By the end, Copilot will know your project's conventions, have a specialized agent for common tasks, and have curated project context.

**Scenario:** You work on a team's web application repository with an established test suite, coding conventions, and active issues. You want Copilot to work effectively with the codebase from day one.

## Prerequisites

* A Copilot plan that includes Copilot cloud agent (GitHub Copilot Pro+, Copilot Business, or Copilot Enterprise). For more information, see [Plans for GitHub Copilot](/en/copilot/about-github-copilot/subscription-plans-for-github-copilot).
* Cloud agent enabled for your organization or account. For more information, see [Managing access to GitHub Copilot cloud agent](/en/copilot/concepts/agents/cloud-agent/access-management).
* Write access to a GitHub repository.

## Step 1: Teach Copilot your project's conventions

Repository custom instructions give Copilot persistent context about your project—its structure, coding standards, and how to build and test code. Every Copilot interaction in the repository uses these instructions automatically.

Ask Copilot cloud agent to generate a `copilot-instructions.md` file:

1. Go to [github.com/copilot/agents](https://github.com/copilot/agents?ref_product=copilot\&ref_type=engagement\&ref_style=text).

2. Select your repository from the dropdown menu in the prompt field.

3. Enter the following prompt:

   ```text copy
   Onboard this repository to Copilot cloud agent by adding a
   .github/copilot-instructions.md file. Include information about project
   structure, coding conventions, the test framework, and how to build and
   run the project.
   ```

4. Review the generated file and merge the pull request.

Copilot now understands your project's conventions across chat, code review, and agent sessions. See [Adding repository custom instructions for GitHub Copilot](/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions).

## Step 2: Create a specialized agent

Custom agents let you create focused assistants for recurring tasks. In this example, create an agent that diagnoses and fixes bugs.

1. Go to [github.com/copilot/agents](https://github.com/copilot/agents?ref_product=copilot\&ref_type=engagement\&ref_style=text) and select your repository.

2. In the prompt field, click <svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-copilot" aria-label="Select a custom agent" role="img"><path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path></svg>. Then click **<svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-plus" aria-label="Plus button" role="img"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg> Create a custom agent**.

3. Rename the file to `bug-fixer.agent.md`.

4. Replace the template content with:

   ```yaml copy
   ---
   name: Bug Fixer
   description: Diagnoses and fixes bugs reported in GitHub issues.
   tools:
     - read
     - edit
     - terminal
     - search
   ---

   You are a bug-fixing specialist. When given a bug report or issue:

   1. Reproduce the bug by writing a failing test.
   2. Identify the root cause.
   3. Fix the code.
   4. Verify the fix passes the test and doesn't break existing tests.

   Always follow the project's testing conventions and coding standards.
   ```

5. Commit the file and merge it into the default branch.

Your bug-fixer agent now appears in the agents dropdown on the agents tab. Select it before pasting an issue URL to start a focused debugging session. See [Creating custom agents for Copilot cloud agent](/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/create-custom-agents).

## Step 3: Organize project context with a space

Copilot Spaces let you curate the exact context Copilot needs for a specific area of your project. Answers are grounded in relevant files, issues, and documentation.

1. Go to [github.com/copilot/spaces](https://github.com/copilot/spaces?ref_product=copilot\&ref_type=engagement\&ref_style=text) and click **Create space**.
2. Name the space (for example, "API Architecture") and choose an owner.
3. Click **<svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-plus" aria-label="plus" role="img"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg> Add sources**, then add context that's relevant to your project:
   * **<svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-file-code" aria-label="file-code" role="img"><path d="M4 1.75C4 .784 4.784 0 5.75 0h5.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v8.586A1.75 1.75 0 0 1 14.25 15h-9a.75.75 0 0 1 0-1.5h9a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 10 4.25V1.5H5.75a.25.25 0 0 0-.25.25v2.5a.75.75 0 0 1-1.5 0Zm1.72 4.97a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734l1.47-1.47-1.47-1.47a.75.75 0 0 1 0-1.06ZM3.28 7.78 1.81 9.25l1.47 1.47a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018l-2-2a.75.75 0 0 1 0-1.06l2-2a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Zm8.22-6.218V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg> Add files and repositories** — Add architecture docs, API schemas, or key configuration files.
   * **<svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-link" aria-label="link" role="img"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg> Link files, pull requests, and issues** — Paste URLs for active issues or design discussions.
4. In the space's chat, ask a question like: "What patterns does our API use for error handling?"

Copilot answers using only the context you've curated. See [Creating GitHub Copilot Spaces](/en/copilot/how-tos/copilot-on-github/customize-copilot/copilot-spaces/create-copilot-spaces).

## Next steps

* **[Adding personal custom instructions for GitHub Copilot](/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-personal-instructions)** — Set personal preferences that apply across all your repositories.
* **[Adding agent skills for GitHub Copilot](/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)** — Add new capabilities to your agents.
* **[Connect agents to external tools](/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/extend-cloud-agent-with-mcp)** — Connect agents to external tools and services.
* **[Collaborating with others using GitHub Copilot Spaces](/en/copilot/how-tos/copilot-on-github/customize-copilot/copilot-spaces/collaborate-with-others)** — Share your spaces with teammates.