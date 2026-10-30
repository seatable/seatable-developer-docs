---
description: Generate, preview, and package a SeaTable HTML page with ChatGPT Codex. Includes setup, permissions, example prompts, and upload steps.
---

# Build an HTML page with ChatGPT Codex

This guide shows how to use the SeaTable HTML Page skill in the ChatGPT client to build an HTML page. It uses a customer registration form as an example.

The example uses two linked tables for customer management: a customer registration table and a sales personnel table.

When creating a customer record, users enter basic customer information and link one or more sales personnel records.

## Prepare for page generation

### Set up the app and HTML page

In the relevant base, create an app and add an HTML page to it.

![](../media/build-page-with-chatgpt-codex/01-create-html-page.jpg)

### Configure permissions

Configure page access permissions according to the page's intended use, as shown below.

![](../media/build-page-with-chatgpt-codex/02-configure-page-permissions.jpg)

Configure table permissions as shown below.

![](../media/build-page-with-chatgpt-codex/03-configure-table-permissions.jpg)

**Table 1: Customer Registration**

The page needs to add customer records to this table and update linked records. Enable the "Can add records" and "Can modify records" permissions for this table.

!!! warning "Review field permissions"

    For testing, this example enables adding values to all fields. Adjust the field permissions to suit your needs, especially before using the page in production.

![](../media/build-page-with-chatgpt-codex/04-customer-table-permissions.jpg)

**Table 2: Sales Personnel**

When adding a customer record, users select one or more records from this table to link. Enable the table's "Can list records" permission so the page can display the available records.

!!! warning "Review field permissions"

    For testing, this example also enables access to all fields. Adjust the field permissions to suit your needs, especially before using the page in production.

![](../media/build-page-with-chatgpt-codex/05-sales-personnel-table-permissions.jpg)



### Install the skill

If you have not used the skill before, install it first. This guide assumes that the ChatGPT client is already installed on your computer.

You can install the skill in either of the following ways.

**Method 1**: Send an installation command

In a conversation with the ChatGPT client, send the following command:

```plaintext
npx skills add seatable/skills@seatable-html-page
```

!!! note "GitHub connection required"

    If the ChatGPT client cannot connect to GitHub, this method may fail. Resolve the connection issue and try again, or use Method 2.

**Method 2 (recommended)**: Copy the skill to your local AI tool's skills directory

The skill is available in the [seatable/skills repository](https://github.com/seatable/skills). Download the repository using your preferred method, then copy `seatable-html-page` from its `skills` directory to the directory where your AI tool stores skills.

The following screenshots show where the `seatable-html-page` skill is installed on a local computer.

![](../media/build-page-with-chatgpt-codex/06-skill-installation-path.jpg)

![](../media/build-page-with-chatgpt-codex/07-skill-files.jpg)

In ChatGPT, open **Plugins -> Skills** and check that "SeaTable HTML Page" appears in the list.

![](../media/build-page-with-chatgpt-codex/08-verify-skill-installation.jpg)

You can also enter `/seatable` in a conversation. If "SeaTable HTML Page" appears in the list of available skills, the skill is installed.

![](../media/build-page-with-chatgpt-codex/09-find-html-page-skill.jpg)

### Create a ChatGPT project

To keep your work organized, create a ChatGPT project for each HTML page. You will create a local folder for the page and link it to the project in the following steps.

![](../media/build-page-with-chatgpt-codex/10-create-chatgpt-project.jpg)



Create a folder for the page in a convenient location, using any method you prefer.

![](../media/build-page-with-chatgpt-codex/11-create-project-folder.jpg)

The project name is optional. If you leave it blank, ChatGPT uses the folder name by default.

![](../media/build-page-with-chatgpt-codex/12-link-folder-to-project.jpg)

Once the project has been created, a new conversation for it starts automatically.

![](../media/build-page-with-chatgpt-codex/13-project-conversation.jpg)



## Generate a page with ChatGPT Codex

### Select the skill and configure the local development environment

Enter `/seatable` and select the page-generation skill from the pop-up list.

![](../media/build-page-with-chatgpt-codex/14-select-html-page-skill.jpg)

![](../media/build-page-with-chatgpt-codex/15-start-skill-conversation.jpg)



After selecting the skill, ask it to set up the local development environment.

![](../media/build-page-with-chatgpt-codex/16-configure-local-environment.jpg)



In the configuration file, enter the server address, `appUuid`, and `pageId` shown for the blank HTML page you created during setup.

!!! warning "Keep your account token private"

    Find your `accountToken` under **Personal Settings -> Personal Information -> Account Token**. Do not share it in the conversation, because it could give others access to your account.

![](../media/build-page-with-chatgpt-codex/17-verify-local-configuration.jpg)



### Describe the page and data structure

Describe the page you want to generate, including its functionality, workflow, and visual style. Providing detailed requirements can reduce the amount of revision needed later. For example:

![](../media/build-page-with-chatgpt-codex/18-customer-registration-prompt.jpg)

!!! example "Example prompt"

    ```plaintext
    Create a customer registration page.

    Functions:
    - Validate required fields
    - Allow multiple sales personnel to be linked
    - After successful submission, display a confirmation message and clear the form

    Process:
    1. Enter the customer's basic information in the registration form.
    2. Link one or more sales personnel records.
    3. When the form is submitted, first create a customer record, then link it to the selected sales personnel records.
    4. Select sales personnel from the existing records in the Sales Personnel table.
    5. Style the "Submit" button with a purple gradient.
    ```

The skill may ask for details about the tables, fields, and other data structures the page needs. If you have not already provided this information, the AI will prompt you for it.

You can also include these details in your initial request. If the AI detects that you have already specified the data structure, it will proceed directly to generating the page.

**Example of additional data structure details:**

![](../media/build-page-with-chatgpt-codex/19-provide-table-schema.jpg)

!!! example "Example data structure"

    ```plaintext
    Table 1: Customer Registration. Relevant fields:
    - Customer Name, text
    - Contact Phone Number, text
    - Customer Type, single select; options: Individual / Corporate
    - Remarks, long text
    - Sales Personnel, linked to the "Sales Personnel" table; allows each customer record to be associated with multiple sales personnel records. This is the key part of this example.

    Table 2: Sales Personnel. Relevant fields:
    - Name, text; used as the display name
    - Department, single select; options for distinguishing departments: Sales Department I / Sales Department II
    - Employee ID, text
    - Mobile Number, number
    - Email, email
    - Date of Joining, date
    - Customer, linked to the "Customer Registration" table; establishes the relationship between sales personnel and customers and is the key field in this table.
    ```


### Generate and refine the page

After you provide the requirements and data structure, the AI begins generating the page.

If a confirmation prompt like the one below appears, select "Allow once."

![](../media/build-page-with-chatgpt-codex/20-allow-sdk-download.jpg)

![](../media/build-page-with-chatgpt-codex/21-allow-api-docs-access.jpg)

The AI then completes the generation process.

When generation is complete, the AI displays a summary similar to the following:

![](../media/build-page-with-chatgpt-codex/22-page-generation-summary.jpg)

Generated page:

![](../media/build-page-with-chatgpt-codex/23-generated-customer-form.jpg)

The generated files are also saved in the corresponding local folder:

![](../media/build-page-with-chatgpt-codex/24-generated-project-files.jpg)



Choose **Preview Page** to preview the result. After making any needed changes, package the page for upload.

If the page does not meet your requirements, ask the AI to revise it. For example, you can correct field definitions, as shown below.

![](../media/build-page-with-chatgpt-codex/25-request-page-changes.jpg)



## Preview page

When the preview service starts, the page opens automatically in ChatGPT. You can also open the service address in your preferred browser. By default, the address is [http://127.0.0.1:3005](http://127.0.0.1:3005/).

![](../media/build-page-with-chatgpt-codex/26-preview-customer-form.jpg)

When you finish testing, send the **Cancel Preview** command to stop the preview service.

Test features such as input validation and form submission.

![](../media/build-page-with-chatgpt-codex/27-test-form-validation.jpg)

Check the data submitted to the base.

## Package and upload the page

After testing the page and confirming that it works as expected, send the instruction "Package as an upload ZIP". The AI will then run the packaging script.

![](../media/build-page-with-chatgpt-codex/30-package-upload-zip.jpg)

Upload the ZIP file to the HTML page in the app.

![](../media/build-page-with-chatgpt-codex/31-upload-package-files.jpg)

The uploaded page appears in the app as follows:

![](../media/build-page-with-chatgpt-codex/32-uploaded-html-page.jpg)
