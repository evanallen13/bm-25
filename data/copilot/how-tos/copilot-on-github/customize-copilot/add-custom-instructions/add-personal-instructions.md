# Adding personal custom instructions for GitHub Copilot

Customize GitHub Copilot Chat responses to match your personal preferences.

> \[!NOTE] Personal custom instructions are only supported for GitHub Copilot Chat in GitHub.

You can layer multiple types of custom instructions to shape GitHub Copilot Chat responses. For an overview, see [About customizing GitHub Copilot responses](/en/copilot/concepts/about-customizing-github-copilot-chat-responses?tool=webui).

## About personal custom instructions for Copilot Chat

Personal custom instructions apply to every conversation you have on the GitHub website, so Copilot always responds in your preferred language, tone, and style.

Examples of instructions you can add:

* `Always respond in Spanish.`
* `Use a helpful, collegial tone. Keep explanations brief, but provide enough context to understand the code.`
* `Always provide examples in TypeScript.`

Multiple types of custom instructions can apply to a request sent to Copilot. Personal instructions take the highest priority. Repository instructions come next, and then organization instructions are prioritized last. However, all sets of relevant instructions are provided to Copilot.

Whenever possible, try to avoid providing conflicting sets of instructions. If you are concerned about response quality, you can temporarily disable repository instructions. See [Adding repository custom instructions for GitHub Copilot](/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot?tool=webui#enabling-or-disabling-repository-custom-instructions).

## Adding personal custom instructions

To add personal custom instructions on GitHub:

1. Open [Copilot Chat](https://github.com/copilot?ref_product=copilot\&ref_type=engagement\&ref_style=text).

2. In the bottom left corner, click your profile picture. Then click **<svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-note" aria-label="note" role="img"><path d="M0 3.75C0 2.784.784 2 1.75 2h12.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14H1.75A1.75 1.75 0 0 1 0 12.25Zm1.75-.25a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25ZM3.5 6.25a.75.75 0 0 1 .75-.75h7a.75.75 0 0 1 0 1.5h-7a.75.75 0 0 1-.75-.75Zm.75 2.25h4a.75.75 0 0 1 0 1.5h-4a.75.75 0 0 1 0-1.5Z"></path></svg> Personal instructions**.

3. Add natural language instructions to the text box.

   Use any format. For example, a single block of text, each instruction on a new line, or instructions separated by blank lines.

4. Optionally, use a template for common instructions. Click <svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-light-bulb" aria-label="The light-bulb icon" role="img"><path d="M8 1.5c-2.363 0-4 1.69-4 3.75 0 .984.424 1.625.984 2.304l.214.253c.223.264.47.556.673.848.284.411.537.896.621 1.49a.75.75 0 0 1-1.484.211c-.04-.282-.163-.547-.37-.847a8.456 8.456 0 0 0-.542-.68c-.084-.1-.173-.205-.268-.32C3.201 7.75 2.5 6.766 2.5 5.25 2.5 2.31 4.863 0 8 0s5.5 2.31 5.5 5.25c0 1.516-.701 2.5-1.328 3.259-.095.115-.184.22-.268.319-.207.245-.383.453-.541.681-.208.3-.33.565-.37.847a.751.751 0 0 1-1.485-.212c.084-.593.337-1.078.621-1.489.203-.292.45-.584.673-.848.075-.088.147-.173.213-.253.561-.679.985-1.32.985-2.304 0-2.06-1.637-3.75-4-3.75ZM5.75 12h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1 0-1.5ZM6 15.25a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 0 1.5h-2.5a.75.75 0 0 1-.75-.75Z"></path></svg> and select a template.

   When you select a template, placeholder text appears. Replace placeholders like `{format}` with your preferences.

5. Click **Save**.

Your instructions are now active and remain active until you change or remove them.

<div class="ghd-alert ghd-alert-accent ghd-spotlight-accent">

Did you successfully add personal custom instructions?

<a href="https://docs.github.io/success-test/yes.html" target="_blank" class="btn btn-outline mt-3 mr-3 no-underline"><span>Yes</span></a>  <a href="https://docs.github.io/success-test/no.html" target="_blank" class="btn btn-outline mt-3 mr-3 no-underline"><span>No</span></a>

</div>

## Further reading

* [Custom instructions](/en/copilot/tutorials/customization-library/custom-instructions)—a curated collection of examples