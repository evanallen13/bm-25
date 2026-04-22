# Collaborating with others using GitHub Copilot Spaces

Share Copilot Spaces to support collaboration and knowledge sharing.

Copilot Spaces let you organize the context that Copilot uses to answer your questions. Sharing Copilot Spaces helps others:

* Avoid repeated explanations and handoffs.
* Stay aligned on how a system works or what’s expected.
* Learn from past work, documentation, and examples.
* Get better help from Copilot with grounded, curated context.

## Use cases for collaboration

* **Onboarding**: Share a space with code, documentation, diagrams, and checklists to help new developers get started faster. Make other people editors so anyone can update the included resources.
* **System knowledge**: Create a space for a complex system or workflow (like authentication or CI pipelines) that other people can reference.
* **Style guides or review checklists**: Document standards and examples in a space that Copilot can reference when suggesting changes.

For example, a subject matter expert creates a space called "Accessibility Reviews" that includes your team's internal accessibility checklist, product guidelines, and WCAG documentation. Developers can ask Copilot questions directly in the space to ensure they're following the latest guidelines in their work.

## Sharing Spaces

Spaces can belong to a personal account or to an organization, and the sharing options differ depending on who the space belongs to.

### Organization-owned spaces

Organization-owned spaces can be shared with other organization members, and you decide which level of access you want to grant other members (admin, editor, viewer).

Alternatively, you can choose to grant "No access" to organization members, and keep the space hidden.

To share an organization-owned space with others:

1. In the top right corner of the space, click **<svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-share" aria-label="share" role="img"><path d="M3.75 6.5a.25.25 0 0 0-.25.25v6.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-6.5a.25.25 0 0 0-.25-.25h-1a.75.75 0 0 1 0-1.5h1c.966 0 1.75.784 1.75 1.75v6.5A1.75 1.75 0 0 1 12.25 15h-8.5A1.75 1.75 0 0 1 2 13.25v-6.5C2 5.784 2.784 5 3.75 5h1a.75.75 0 0 1 0 1.5ZM7.823.177a.25.25 0 0 1 .354 0l2.896 2.896a.25.25 0 0 1-.177.427H8.75v5.75a.75.75 0 0 1-1.5 0V3.5H5.104a.25.25 0 0 1-.177-.427Z"></path></svg>**.

2. To add specific users or teams, search for them with the search bar, then choose a role for the people you added.

3. Optionally, next to your organization's name, choose a base role for all other organization members.

   * **Viewers** can use the space to ask questions and view the included attachments and instructions.
   * **Editors** can update the space's attachments, description, name, and instructions, in addition to having all the permissions of viewers. However, editors can't update sharing settings or delete the space.
   * **Admins** can update sharing settings or delete the space, in addition to having all the permissions of viewers and editors.
   * **No access** means the space will be hidden from other organization members.

4. Optionally, click **<svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-link" aria-label="the link" role="img"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg> Copy link** to copy the link to the space and share it with others.

### Individual-owned spaces

Spaces belonging to a personal account can be shared publicly, shared with specific GitHub users, or kept private to the person who created the space.

To share an individual-owned space with others:

1. In the top right corner of the space, click **<svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-share" aria-label="share" role="img"><path d="M3.75 6.5a.25.25 0 0 0-.25.25v6.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-6.5a.25.25 0 0 0-.25-.25h-1a.75.75 0 0 1 0-1.5h1c.966 0 1.75.784 1.75 1.75v6.5A1.75 1.75 0 0 1 12.25 15h-8.5A1.75 1.75 0 0 1 2 13.25v-6.5C2 5.784 2.784 5 3.75 5h1a.75.75 0 0 1 0 1.5ZM7.823.177a.25.25 0 0 1 .354 0l2.896 2.896a.25.25 0 0 1-.177.427H8.75v5.75a.75.75 0 0 1-1.5 0V3.5H5.104a.25.25 0 0 1-.177-.427Z"></path></svg>**.
2. To add specific GitHub users, search for them with the search bar, then choose a role for the people you added.
3. Optionally, to make the space public, under "General access", select **Anyone with link**. Then, copy the link to the space and share it with others.

   > \[!NOTE] Publicly shared spaces are view-only by default, and viewers can only see sources that they have access to.

## Accessing shared Spaces

If you’re part of an organization that has shared spaces, you can access them in the **Organizations** tab on [https://github.com/copilot/spaces](https://github.com/copilot/spaces?ref_product=copilot\&ref_type=engagement\&ref_style=text).

You can also use organization spaces directly in your IDE by specifying the organization as the owner when accessing the space. For more information, see [Using GitHub Copilot Spaces](/en/copilot/how-tos/provide-context/use-copilot-spaces/use-copilot-spaces#using-copilot-spaces-in-your-ide).