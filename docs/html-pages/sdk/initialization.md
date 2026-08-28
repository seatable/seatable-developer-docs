---
description: Install and initialize the seatable-html-page-sdk. Set up the SDK via npm or CDN and connect an HTML page to its SeaTable base.
---

# Initialization

The `seatable-html-page-sdk` is the bridge between an HTML page and its Universal App. It exposes APIs for data interaction and event subscription. This page covers installation and initialization. For data operations, see [Rows](rows.md) and [Files & Images](files.md).

## Installation

=== "Package manager"

    Install with npm or yarn — recommended for the [modular development style](../getting-started.md#2-choose-a-development-style).

    ```shell
    # npm
    npm install seatable-html-page-sdk --save

    # yarn
    yarn add seatable-html-page-sdk
    ```

    ```js
    import { HTMLPageSDK } from "seatable-html-page-sdk";
    ```

=== "CDN"

    Load the SDK via CDN — convenient for the non-modular style, where everything lives in `index.html`. `HTMLPageSDK` becomes available as a global.

    ```html
    <!-- unpkg -->
    <script src="https://unpkg.com/seatable-html-page-sdk@latest/dist/index.min.js"></script>

    <!-- or jsDelivr -->
    <!-- <script src="https://cdn.jsdelivr.net/npm/seatable-html-page-sdk@latest/dist/index.min.js"></script> -->

    <script>
      const sdk = new HTMLPageSDK();
    </script>
    ```

    !!! warning "Pin a version"

        `@latest` always resolves to the newest release. For production pages, pin an explicit version (for example `seatable-html-page-sdk@1.0.0`) so a new release cannot change behavior unexpectedly.

## Initialize the SDK

Create an instance, then call `init()` before making any data calls. Write the initialization **once** — the same code works in both development and production:

```js
const options = window.__HTML_PAGE_DEV_CONFIG__ || null;
const sdk = new HTMLPageSDK(options);
await sdk.init();
```

How `options` is resolved differs by environment, but your code does not change:

=== "Production"

    Inside the Universal App, `window.__HTML_PAGE_DEV_CONFIG__` is not defined, so `options` is `null`. The SDK derives the connection context from the host app automatically — no credentials in your code.

=== "Development"

    There is no host app locally, so the SDK needs connection details. You do **not** hardcode them: the Vite dev server reads [`src/setting.js`](../getting-started.md#3-configure-local-development) and injects the values into `window.__HTML_PAGE_DEV_CONFIG__` at serve time.

    The injected object has this shape:

    ```js
    {
      server: "your-html-page-server",
      accountToken: "your-account-token",
      appUuid: "your-app-uuid",
      pageId: "your-app-page-id",
    }
    ```

    Because `setting.js` is git-ignored and never bundled, your account token stays out of the build.

## Basic usage

Once initialized, call the data APIs on the instance:

```js
const sdk = new HTMLPageSDK(options);
await sdk.init();

const res = await sdk.listRows({
  tableName: "Employees",
  start: 0,
  limit: 100,
});
const rows = res.data.results;
```

All SDK methods are asynchronous and return promises — always `await` them. Row methods resolve to the HTTP response, so the payload is under `.data` (see [Rows](rows.md)). Upload methods are the exception and return the result object directly (see [Files & Images](files.md)).

## Next steps

- [Rows](rows.md) — list, add, update and delete rows, including batch operations.
- [Files & Images](files.md) — upload files and images for file and image columns.
