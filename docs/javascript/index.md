---
description: Get started with the SeaTable JavaScript API. Use it inside SeaTable scripts or from Node.js — installation, authentication, and async usage.
---

# JavaScript

SeaTable provides a JavaScript API that works in two contexts: inside SeaTable as a script, or externally via Node.js or a frontend application. The core methods (tables, views, columns, rows, links, SQL) are the same in both contexts. Features that are only available in one context are clearly marked on the respective pages.

## Script vs. External Client

| | Script in SeaTable | External client |
|---|---|---|
| Installation | None | `npm install seatable-api` |
| Authentication | Not needed (user is already logged in) | API token required |
| Execution | In the browser | Node.js or frontend app |
| `await` required | Only for `query()` and `getLinkedRecords()` | For all calls |
| Exclusive features | [Context, Output, Utilities, Filter/QuerySet](scripting-features.md) | [Constants](constants.md) |

## Installation

```shell
npm install seatable-api
```

Not needed for scripts inside SeaTable.

## Authentication

External programs need an API token for authentication. API tokens can be [generated in the SeaTable web interface](https://seatable.com/help/create-api-tokens/). Scripts inside SeaTable require no authentication.

```js
import { Base } from "seatable-api";

const base = new Base({
  server: "https://cloud.seatable.io",
  APIToken: "your-api-token",
});
await base.auth();
```

## Async Operations

External API calls are asynchronous and return promises. Use `await` to wait for the result.

In scripting context, most methods are synchronous. The exceptions are `query()` and `getLinkedRecords()`, which also require `await`.

## API Limits

JavaScript calls are subject to [rate](https://api.seatable.com/reference/limits#general-rate-limits) and [size](https://api.seatable.com/reference/limits#size-limits) limits. Use batch operations (`batchAppendRows`, `batchUpdateRows`, `batchDeleteRows`) whenever possible to reduce the number of API calls.

!!! tip "Looking for examples?"

    Step-by-step JavaScript script examples are available in the [SeaTable User Manual](https://seatable.com/help/scripts/).
