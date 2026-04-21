# Managing GitHub Copilot cloud agent in your enterprise

Enable members of your enterprise to use Copilot cloud agent and control the repositories where it is available.

> \[!NOTE]
> For an introduction to Copilot cloud agent, see [About GitHub Copilot cloud agent](/en/copilot/concepts/agents/cloud-agent/about-cloud-agent).

## Prerequisites

* For general information, see [Piloting GitHub Copilot cloud agent in your organization](/en/copilot/tutorials/cloud-agent/pilot-cloud-agent).
* For information on premium requests and Actions minutes, see [Allowance usage for Copilot cloud agent](/en/billing/managing-billing-for-your-products/managing-billing-for-github-copilot/about-billing-for-github-copilot#allowance-usage-for-copilot-cloud-agent).
* For information on MCP servers, see [Extending GitHub Copilot cloud agent with the Model Context Protocol (MCP)](/en/copilot/how-tos/use-copilot-agents/cloud-agent/extend-cloud-agent-with-mcp).

## Enabling Copilot cloud agent for your Copilot subscribers

Copilot cloud agent and use of third-party MCP servers are blocked by default for users to whom you have assigned a Copilot license. You can allow members to use these features from the AI Controls tab for your enterprise. See [Managing policies and features for GitHub Copilot in your enterprise](/en/copilot/managing-copilot/managing-copilot-for-your-enterprise/managing-policies-and-features-for-copilot-in-your-enterprise#configuring-policies-for-github-copilot).

* On the "Agents" page, click **Copilot cloud agent**, then select **Enabled everywhere** or **Let organizations decide**.
* On the "MCP" page, for the "MCP servers in Copilot" policy, select **Enabled everywhere** or **Let organizations decide**.

### Next steps

* If you selected **Enabled everywhere**, tell organization owners that Copilot cloud agent is enabled for all members. By default, the agent will be available in all repositories, but it is possible to opt out some or all repositories.
* If you selected **Let organizations decide**, discuss member enablement with organization owners.

For more information, see [Adding GitHub Copilot cloud agent to your organization](/en/copilot/how-tos/administer-copilot/manage-for-organization/add-copilot-cloud-agent).

## Disabling Copilot cloud agent in your repositories

Copilot policies, like the "Copilot cloud agent" and "MCP servers on GitHub.com" policies described above, affect only the users you assign a Copilot license to.

If there are GitHub Copilot Pro+ users with access to your enterprise's repositories, they will be able to use Copilot cloud agent and will not be restricted by your policies.

You can choose to stop anyone using the agent in some or all of your repositories using organization-level settings. For more information, see [Adding GitHub Copilot cloud agent to your organization](/en/copilot/how-tos/administer-copilot/manage-for-organization/add-copilot-cloud-agent).

Alternatively, you can disable the agent for all repositories owned by your enterprise.

1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec\&ref_type=engagement\&ref_style=text) page on GitHub.com.
2. At the top of the page, click **<svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-copilot" aria-label="copilot" role="img"><path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path></svg> AI controls**.
3. In the "Installed Agents" section, click **Copilot cloud agent**.
4. In the "Copilot cloud agent" section, next to "Block Copilot cloud agent in all repositories owned by ENTERPRISE-NAME", click the toggle.