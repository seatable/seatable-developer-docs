---
description: seatable-html-page-sdk reference for reading the signed-in user, page collaborators, and user profiles in an HTML page.
---

# Users

User operations on the `seatable-html-page-sdk`. Use them to personalize a page and to resolve the user identifiers stored by collaborator-related fields. All methods are asynchronous — `await` them. The `sdk` instance below is created and initialized as shown in [Initialization](initialization.md).

!!! warning "Response format"

    User methods resolve to the underlying HTTP response. Read the payload from `.data`.

## Current user

!!! abstract "getCurrentUser"

    Get the signed-in user of the current Universal App. This method takes no parameters and does not require a `tableName`.

    **Note:** This was added in SDK version 1.0-latest.

    ```js
    sdk.getCurrentUser();
    ```

    __Returns__ `.data` holds the current user's identity and profile fields, for example `{ username, name, user_id, avatar_url, role_id }`.

    __Example__
    ```js
    const res = await sdk.getCurrentUser();
    const currentUser = res.data;
    const displayName = currentUser.name || currentUser.username;
    const avatarUrl = currentUser.avatar_url;
    ```

    Use `name` and `avatar_url` to personalize the page UI, and fall back to `username` when `name` is empty. `user_id` identifies a user; it is not a table row ID.

## Collaborators

!!! abstract "listCollaborators"

    List the collaborators available to the HTML page. Use this method to load the initial choices for a collaborator control.

    **Note:** This was added in SDK version 1.0-latest.

    ```js
    sdk.listCollaborators();
    ```

    __Returns__ `.data` holds `{ collaborator_list }`. Each entry provides user profile information such as `email`, `name`, and `avatar_url`.

    __Example__
    ```js
    const res = await sdk.listCollaborators();
    const collaborators = res.data.collaborator_list || [];
    ```

!!! abstract "resolveUsers"

    Resolve user identifiers found in loaded row data that are not already present in the collaborator list.

    **Note:** This was added in SDK version 1.0-latest.

    ```js
    sdk.resolveUsers({ userIds });
    ```

    __Parameters__

    `userIds`
    :   array — user identifiers to resolve

    __Returns__ `.data` holds `{ user_list }`. Each entry provides user profile information such as `email`, `name`, and `avatar_url`.

    __Example__
    ```js
    const res = await sdk.resolveUsers({
      userIds: ["user@example.com", "former-user@example.com"],
    });
    const users = res.data.user_list || [];
    ```

## Resolve user values in rows

Collaborator, creator, and last-modifier fields store user identifiers rather than display names. Load collaborators first, then resolve only the identifiers from your loaded rows that are missing from that list. Merge both results before rendering names or building collaborator choices.

```js
function addUsersToMap(users, userMap) {
  (users || []).forEach((user) => {
    if (user.email) userMap.set(user.email, user);
  });
}

const userMap = new Map();

const collaboratorsRes = await sdk.listCollaborators();
addUsersToMap(collaboratorsRes.data.collaborator_list, userMap);

const missingUserIds = userIdsFromRows.filter((userId) => !userMap.has(userId));
if (missingUserIds.length > 0) {
  const usersRes = await sdk.resolveUsers({ userIds: missingUserIds });
  addUsersToMap(usersRes.data.user_list, userMap);
}

const collaboratorOptions = [...userMap.values()];
```

