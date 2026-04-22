# Creating GitHub Copilot Spaces

Create spaces to organize and centralize relevant content that grounds Copilot's responses in the right context for a specific task.

## Creating a space

1. To create a space, go to [https://github.com/copilot/spaces](https://github.com/copilot/spaces?ref_product=copilot\&ref_type=engagement\&ref_style=text), and click **Create space**.
2. Give your space a name.
3. Choose whether the space is owned by you or by an organization you belong to. Organization-owned Spaces can be shared using GitHub’s built-in permission model.
4. Click **Create Space**.
5. Optionally, under the space name, add a description. The description does not affect Copilot's responses, but helps others understand the purpose of the space.

   > \[!NOTE] You can change the name and description of your space at any time by hovering over them and clicking **<svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-pencil" aria-label="pencil" role="img"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path></svg>**.

## Adding context to a space

You can add two types of context to your space:

* **Instructions**: Free text that describes what Copilot should focus on within this space. Include its areas of expertise, what kinds of tasks it should help with, and what it should avoid. This helps Copilot give more relevant responses based on your intent.

  For example:

  > You are a SQL generator. Your job is to take the sample queries and data schemas defined in the attached files and generate SQL queries based on the user's goals.

* **Sources**: This context will be used to provide more relevant answers to your questions. Additionally, Spaces will always refer to the latest version of the code on the `main` branch of the repository.

  To add sources, click **<svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-plus" aria-label="plus" role="img"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg> Add sources**, then choose one of the following options:

  * **<svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-file-code" aria-label="file-code" role="img"><path d="M4 1.75C4 .784 4.784 0 5.75 0h5.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v8.586A1.75 1.75 0 0 1 14.25 15h-9a.75.75 0 0 1 0-1.5h9a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 10 4.25V1.5H5.75a.25.25 0 0 0-.25.25v2.5a.75.75 0 0 1-1.5 0Zm1.72 4.97a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734l1.47-1.47-1.47-1.47a.75.75 0 0 1 0-1.06ZM3.28 7.78 1.81 9.25l1.47 1.47a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018l-2-2a.75.75 0 0 1 0-1.06l2-2a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Zm8.22-6.218V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg> Add files and repositories**: You can add files, folders, and entire GitHub repositories. When you add a repository, Copilot searches its contents to find relevant information, but adding specific files or folders that are most relevant to your work will give you the best results. This can include code files, documentation, and other content that helps Copilot understand the context of your space.
  * **<svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-link" aria-label="link" role="img"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg> Link files, pull requests, and issues**: You can paste the URLs of the GitHub content, including pull requests and issues.
  * **<svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-upload" aria-label="upload" role="img"><path d="M2.75 14A1.75 1.75 0 0 1 1 12.25v-2.5a.75.75 0 0 1 1.5 0v2.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 14Z"></path><path d="M11.78 4.72a.749.749 0 1 1-1.06 1.06L8.75 3.811V9.5a.75.75 0 0 1-1.5 0V3.811L5.28 5.78a.749.749 0 1 1-1.06-1.06l3.25-3.25a.749.749 0 0 1 1.06 0l3.25 3.25Z"></path></svg> Upload a file**: You can upload files directly from your local machine. This includes images, text files, rich documents, and spreadsheets.
  * **<svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-paste" aria-label="paste" role="img"><path d="M3.626 3.533a.249.249 0 0 0-.126.217v9.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-9.5a.249.249 0 0 0-.126-.217.75.75 0 0 1 .752-1.298c.541.313.874.89.874 1.515v9.5A1.75 1.75 0 0 1 12.25 15h-8.5A1.75 1.75 0 0 1 2 13.25v-9.5c0-.625.333-1.202.874-1.515a.75.75 0 0 1 .752 1.298ZM5.75 1h4.5a.75.75 0 0 1 .75.75v3a.75.75 0 0 1-.75.75h-4.5A.75.75 0 0 1 5 4.75v-3A.75.75 0 0 1 5.75 1Zm.75 3h3V2.5h-3Z"></path></svg> Add text content**: You can type or paste free-text content, such as transcripts, notes, or any other relevant information that can help Copilot understand the context of your space.

## Choosing repositories or files as context

When adding sources to your space, you can choose to attach entire repositories or individual files. Understanding how each option works can help you get the best results from Copilot.

* **Attach a repository**: When you attach a repository, Copilot doesn't load the entire project into memory. Instead, it searches the repository and retrieves only the most relevant content for your question. This is best for large-scale use cases, such as answering questions across all documentation in a repository.

* **Attach individual files**: When you attach a file, its full contents are loaded into Copilot's context window and considered for every query in that space. This is best when you want Copilot to consistently prioritize a specific document or a small set of files.

## Adding context as you're working

You can add files to a space directly from the code view on GitHub, so you don't need to break your flow when building context for your space.

1. At the top of any file in the code view, click **<svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-space" aria-label="Add to space" role="img"><path d="M0 13.25V2.75C0 1.784.784 1 1.75 1H5c.551 0 1.07.26 1.4.7l.9 1.2a.25.25 0 0 0 .2.1h6.75c.966 0 1.75.784 1.75 1.75v3.638a.75.75 0 0 1-1.5 0V4.75a.25.25 0 0 0-.25-.25H7.5a1.75 1.75 0 0 1-1.4-.7l-.9-1.2a.25.25 0 0 0-.2-.1H1.75a.25.25 0 0 0-.25.25v10.5c0 .138.112.25.25.25h5.663l.076.004a.75.75 0 0 1 0 1.492L7.413 15H1.75A1.75 1.75 0 0 1 0 13.25Z"></path><path d="M12.265 9.16a.248.248 0 0 1 .467 0l.237.649a3.726 3.726 0 0 0 2.219 2.218l.649.238a.249.249 0 0 1 0 .467l-.649.237a3.728 3.728 0 0 0-2.219 2.219l-.237.649a.249.249 0 0 1-.467 0l-.238-.649a3.726 3.726 0 0 0-2.218-2.219l-.649-.237a.248.248 0 0 1 0-.467l.649-.238a3.725 3.725 0 0 0 2.218-2.218l.238-.649Z"></path></svg>**.

   ![Screenshot of a file in the code view. The "Add to space" icon is highlighted in orange.](/assets/images/help/copilot/add-to-copilot-space.png)

2. From the dropdown, select the space you want to add the file to, or create a new space.

## Next steps

* For an overview of Copilot Spaces, see [About GitHub Copilot Spaces](/en/copilot/concepts/about-organizing-and-sharing-context-with-copilot-spaces).
* To use Spaces in GitHub and your IDE, see [Using GitHub Copilot Spaces](/en/copilot/how-tos/provide-context/use-copilot-spaces/use-copilot-spaces).
* To speed up development work with Spaces, see [Speeding up development work with GitHub Copilot Spaces](/en/copilot/using-github-copilot/copilot-spaces/speeding-up-development-work-with-copilot-spaces).
* To share your space with your team, see [Collaborating with others using GitHub Copilot Spaces](/en/copilot/using-github-copilot/copilot-spaces/collaborating-with-your-team-using-copilot-spaces).