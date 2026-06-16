---
description: seatable-html-page-sdk reference for uploading files and images from an HTML Page into file and image columns of a base.
---

# Files & Images

Upload files and images from an HTML Page. The returned data is used to populate a file or image column — typically by passing it into `updateRow` or `addRow` (see [Rows](rows.md)). The `sdk` instance below is created and initialized as shown in [Initialization](initialization.md).

!!! note "Return value"

    Unlike the row methods, the upload methods resolve to the result object **directly** — there is no `.data` wrapper.

!!! abstract "uploadFile"

    Upload a file for use in a **file** column.

    ```js
    sdk.uploadFile({ file });
    ```

    __Parameters__

    `file`
    :   object — the file to upload (for example, a `File` from an `<input type="file">`)

    __Returns__ `{ name, size, type, url }` — pass this object as the value of a file column.

    __Example__
    ```js
    fileInput.addEventListener("change", async (e) => {
      const file = e.target.files[0];
      const { name, size, type, url } = await sdk.uploadFile({ file });

      await sdk.updateRow({
        tableName: "Documents",
        rowId: "fcHIocncTsOygA3FjL-toQ",
        rowData: { Attachment: [{ name, size, type, url }] },
      });
    });
    ```

!!! abstract "uploadImage"

    Upload an image for use in an **image** column.

    ```js
    sdk.uploadImage({ file });
    ```

    __Parameters__

    `file`
    :   object — the image file to upload

    __Returns__ `{ name, size, type, url }` — same shape as `uploadFile`, with `type` set to `"image"`. Pass the URL as the value of an image column.

    __Example__
    ```js
    fileInput.addEventListener("change", async (e) => {
      const file = e.target.files[0];
      const { url } = await sdk.uploadImage({ file });

      await sdk.updateRow({
        tableName: "Products",
        rowId: "fcHIocncTsOygA3FjL-toQ",
        rowData: { Photo: [url] },
      });
    });
    ```
