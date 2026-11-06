---
description: seatable-html-page-sdk reference for sending notifications and emails, and running configured Python scripts from an HTML page.
---

# Actions

Action operations on the `seatable-html-page-sdk`. They start asynchronous notification, email, or Python-script tasks. All methods are asynchronous — `await` them. The `sdk` instance below is created and initialized as shown in [Initialization](initialization.md).

!!! warning "Response format"

    Action methods resolve to the underlying HTTP response. Read the payload from `.data`. Methods that start a task return its identifier in `.data.task_id`; retain this ID when the page needs to query task progress or results.

## Notifications and email

!!! abstract "sendNotification"

    Create a notification task associated with one row.

    **Note:** This was added in SDK version 1.0-latest.

    ```js
    sdk.sendNotification({ tableName, rowId, emails, msg });
    ```

    __Parameters__

    `tableName`
    :   string — display name of the table containing the row

    `rowId`
    :   string — `_id` of the row associated with the notification

    `emails`
    :   array — non-empty list of recipient email addresses

    `msg`
    :   string — non-empty notification text. It can contain row-value template placeholders such as `{Order number}`.

    __Returns__ `.data` holds `{ task_id }` — use `task_id` with `getMessageStatus`.

    __Example__
    ```js
    const res = await sdk.sendNotification({
      tableName: "Orders",
      rowId: "fcHIocncTsOygA3FjL-toQ",
      emails: ["a7f34c91e2bd4d6b8a50f1c73e9d2a48@auth.local"],
      msg: "Your order {Order number} has been shipped.",
    });
    const taskId = res.data.task_id;
    ```

!!! abstract "sendEmail"

    Create an email task associated with one row.

    **Note:** This was added in SDK version 1.0-latest.

    ```js
    sdk.sendEmail({
      tableName,
      rowId,
      accountName,
      sendTo,
      copyTo,
      replyTo,
      subject,
      message,
      htmlMessage,
      attachmentColumnNames,
    });
    ```

    __Parameters__

    `tableName`
    :   string — display name of the table containing the row

    `rowId`
    :   string — `_id` of the row associated with the email

    `accountName`
    :   string — name of the configured email account

    `sendTo`
    :   array — non-empty list of recipient email addresses or row-value templates

    `copyTo`
    :   array — optional list of CC email addresses or row-value templates

    `replyTo`
    :   string — optional Reply-To email address or row-value template

    `subject`
    :   string — non-empty plain-text email subject

    `message`
    :   string — plain-text body template

    `htmlMessage`
    :   string — HTML body template

    `attachmentColumnNames`
    :   array — optional list of FILE column display names; do not use column keys

    `message` and `htmlMessage` must provide exactly one body: do not pass both, and do not omit both. Recipient values and the message body can use row-value template placeholders such as `{Customer email}` and `{Order number}`.

    __Returns__ `.data` holds `{ task_id }` — use `task_id` with `getMessageStatus`.

    __Example__
    ```js
    const res = await sdk.sendEmail({
      tableName: "Orders",
      rowId: "fcHIocncTsOygA3FjL-toQ",
      accountName: "Operations SMTP",
      sendTo: ["customer@example.com"],
      copyTo: ["orders-audit@example.com"],
      replyTo: "support@example.com",
      subject: "Order shipment notification",
      htmlMessage: "<p>Your order <strong>{Order number}</strong> has been shipped.</p>",
      attachmentColumnNames: ["Invoice"],
    });
    const taskId = res.data.task_id;
    ```

!!! abstract "getMessageStatus"

    Get the status of a notification or email task returned by `sendNotification` or `sendEmail`.

    **Note:** This was added in SDK version 1.0-latest.

    ```js
    sdk.getMessageStatus({ taskId });
    ```

    __Parameters__

    `taskId`
    :   string — task identifier returned in `response.data.task_id`

    __Example__
    ```js
    const res = await sdk.getMessageStatus({ taskId });
    if (res.data.is_finished) {
      // Stop polling and update the UI.
    }
    ```

    Do not query the status until the task-starting method has returned its `task_id`.

## Python scripts

!!! abstract "runScript"

    Start a configured Python script.

    **Note:** This was added in SDK version 1.0-latest.

    ```js
    sdk.runScript({ scriptName, tableName, rowId });
    ```

    __Parameters__

    `scriptName`
    :   string — displayed name of the configured script, not its internal ID or file name

    `tableName`
    :   string — optional display name of the table that supplies the row context

    `rowId`
    :   string — optional `_id` of the row that supplies the row context

    Provide `tableName` and `rowId` together when the script needs a row context, or omit both when it does not.

    __Returns__ `.data` holds `{ task_id }` — use `task_id` with `getScriptResult`.

    __Example__
    ```js
    const res = await sdk.runScript({
      scriptName: "Generate order report",
      tableName: "Orders",
      rowId: "fcHIocncTsOygA3FjL-toQ",
    });
    const taskId = res.data.task_id;
    ```

!!! abstract "getScriptResult"

    Get the result of a script started by `runScript`.

    **Note:** This was added in SDK version 1.0-latest.

    ```js
    sdk.getScriptResult({ scriptName, taskId });
    ```

    __Parameters__

    `scriptName`
    :   string — the same displayed script name used to start the task

    `taskId`
    :   string — task identifier returned in `runScript` response `.data.task_id`

    __Returns__ `.data` holds `{ script }`. The `script` object includes `state`, `success`, `output`, `return_code`, `started_at`, and `finished_at`.

    __Example__
    ```js
    const res = await sdk.getScriptResult({
      scriptName: "Generate order report",
      taskId,
    });
    const scriptResult = res.data.script;

    if (scriptResult.state === "finished") {
      if (scriptResult.success) {
        // The script completed successfully.
      } else {
        // Inspect scriptResult.return_code and scriptResult.output.
      }
    }
    ```

    Query the result only with the `taskId` returned by the corresponding `runScript` call. Treat `success: false` or a non-zero `return_code` as a failed execution, and render `output` as plain text rather than HTML.
