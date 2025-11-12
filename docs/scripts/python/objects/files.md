# Files

## Download

For the following methods, you'll have to provide the URL of the file you want to download. The file URL structure is as follows: 

```js
{server_url}/workspace/{workspace_id}/asset-preview/{base_uuid}/{file location}
```

- `{server_url}` is the URL of your server, for example `https://cloud.seatable.io`

- You can find the `workspace_id` by looking at any of your database URL which will look like `{server_url}/workspace/{workspace_id}/dtable/{base_name}`, or by checking the [user manual](https://seatable.com/help/workspace-id-einer-gruppe-ermitteln/)

- You can find the base uuid in your Team administration (see the [User manual](https://seatable.com/help/bases-in-der-teamverwaltung/), it's displayed as `ID` in the base right panel) or by looking for `dtableUuid` in the source code of the web page while consulting any of your bases

- The file location is what you can find in the [file manager](https://seatable.com/help/file-management-in-a-base/) of your base and will always have the same structure:

    - if uploaded automatically, the file will be in the system folder `files` (if uploaded in a **file-type column**, even if it's an image) and in the subdirectory `YYYY-MM` (year and month of the upload), for example `https://cloud.seatable.io/dtable-web/workspace/74/asset-preview/41cd05da-b29a-4428-bc31-bd66f4600817/files/2020-10/invoice.pdf` is the URL of a file called invoice.pdf and downloaded in October 2020 (`2020-10`) in the base whose uuid is `41cd05da-b29a-4428-bc31-bd66f4600817` in the workspace whose id is `74` on `https://cloud.seatable.io`. It will be the same for an image, but in the `images` system folder instead of the `files` folder (if uploaded in an **image-type column only**)
    - if uploaded by yourself in a custom folder, the file will be in directory `custom` and in the eventual directory you created, for example:
`https://cloud.seatable.io/dtable-web/workspace/74/asset-preview/41cd05da-b29a-4428-bc31-bd66f4600817/custom/My Personal Folder/quote.pdf` is the URL of a file called quote.pdf that you stored in the folder `My Personal Folder` of the custom folders in the same database.

!!! info "Get easily the file URL"
    For files that need to open an external window to preview (almost all files except images), the URL of this new window will actually be the URL your looking for!

!!! abstract "Download (simple one-step method)"

    Download a file to a local path. The save path as naturally to ends with the same extension as the original file.

    ``` python
    base.download_file(file_url, save_path)
    ```
    __Output__ Nothing (throws an error if the URL is invalid or if the save path is wrong)

    __Example__
    
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    file_url = "https://cloud.seatable.io/workspace/74/asset-preview/41cd05da-b29a-4428-bc31-bd66f4600817/files/2020-10/invoice.pdf"
    save_path = "/tmp/invoice.pdf"
    base.download_file(file_url, save_path)
    ```

    Download every file from the *File* column of *Table1* table, providing the id of the row.

    ```python
    from seatable_api import Base

    server_url = 'https://cloud.seatable.io'
    api_token = '5e165f8b7af...98950b20b022083'

    base = Base(api_token, server_url)
    base.auth()

    target_row = base.get_row('Table1','Pd_pHLM8SgiEcnFW5I7HLA')

    save_directory = './tmp/' # (1)!

    files = target_row['File']
    print(f"{len(files)} files to download")
    for file in files :
        print(f"Downloading {file['url']}")
        base.download_file(file['url'], save_directory + file['name']) # (2)!
    ```

    1. Ensure that your target directory exists! Directory beginning with `.` are relative to the current working directory

    2. The download URL is found in the `url` key of each element of the file-type column. The `name` key is used so every files will keep their original names (and you don't have to bother with extensions)

!!! abstract "Download (detailed two-steps method)"

    This detailed method is for handling complex situations, for example when the file is extremely large or the internet connection is slow. In this example, we assume that a file with URL `https://cloud.seatable.io/dtable-web/workspace/74/asset-preview/41cd05da-b29a-4428-bc31-bd66f4600817/files/2020-10/invoice.pdf` exists (a file called invoice.pdf and downloaded in October 2020 (`2020-10`) in the base whose uuid is `41cd05da-b29a-4428-bc31-bd66f4600817`, located in the workspace whose id is `74`).

    This method actually relies on two different steps: first getting the file public download link and then downloading it using a `GET` request.

    Compared to the file URL from the `base.download_file` method, the file path needed here is just the "file location" part of the URL corresponding to the location of the file in the base file system (starting **with** `/files/`, `/images/` or `/custom/`).

    !!! info "Download link expires"

        The download link is only valid for some hours. After that the download link must be created again. That's why it's not possible to use permanent download links of files hosted on SeaTable in web pages. For such purpose, we recommend to store the files on public hosting services and to save only the links in SeaTable, which will allow direct use.

    ``` python
    base.get_file_download_link(file_path)
    ```

    __Output__ The public download link (looking like `{server_url}/seafhttp/files/{access_token}/{file_name}`). Keep in mind that it's not permanent as the token expires! (throws an error if the file path is wrong)

    __Example__
    
    ``` python
    from seatable_api import Base, context
    import requests

    base = Base(context.api_token, context.server_url)
    base.auth()
    
    download_link = base.get_file_download_link('files/2020-10/invoice.pdf')
    response = requests.get(download_link)
    if response.status_code in range(200,300) : # (1)!
        with open("invoice.pdf", "wb") as f: # (2)!
            f.write(response.content)
    ```

    1. `2xx` response status codes correspond to a successful request

    2. Open the file with write permission and write the response content into it

!!! abstract "Download file from a custom folder"

    This method is specific for files stored in a custom folder. Compared to the file URL from the `base.download_file` method, the custom path needed here is just the part of the URL corresponding to the location of the file in the custom folders file system (part of the URL starting **after** `/custom/`). In the following example, we consider the file quote.pdf described in the `base.download_file` section uploaded in the custom folder `My Personal Folder` whose URL is `https://cloud.seatable.io/dtable-web/workspace/74/asset-preview/41cd05da-b29a-4428-bc31-bd66f4600817/custom/My Personal Folder/quote.pdf`.


    ``` python
    base.download_custom_file(custom_path, save_path)
    ```

    __Output__ Nothing (throws an error if the URL is invalid or if the save path is wrong)

    __Example__
    
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    custom_file_path = "My Personal Folder/quote.pdf" # (1) !
    local_path = "/Users/Desktop/quote.pdf"
    base.download_custom_file(custom_file_path, local_path)
    ```

    1. Unlike the `get_file_download_link` method, `custom_file_part` **doesn't** include `/custom/`

## Upload

Please note that uploading a file *to a cell* will require two or three steps, depending on the method you use: you'll first need to upload the file to the base, and then you'll be able to update the row with the newly uploaded file details in the cell. You can learn more about this process in the [API Reference](https://api.seatable.com/reference/uploadfile). As for download, there are one simple (one-step) and one detailed (two-steps) process to upload a file: 

!!! abstract "Upload (simple ones-step method)"

    Upload a file from your local drive, memory or a website.

    ``` python
    base.upload_local_file(file_path, name=None, file_type='file', replace=False) # (1)!
    # or
    base.upload_bytes_file(name, content, file_type='file', replace=False) # (2)!
    ```

    1. - `name`: the name of the file once uploaded. If `name` is not provided, the uploaded file will keep the same name than the original

        - `file_type`:  can be either `file` or `image` (default is `file`)
        - `replace`: if set to `True`, uploading a new file with the same name as an existing one will overwrite it (default is `False`)

    2. When using `base.upload_bytes_file`, `name` is mandatory as their is no named attached to the `content`

    __Output__ File dict containing the same keys as every element in a file-type column: `type` (`file` or `image`), `size`, `name` and `url`

    __Example: Upload a file from local hard drive__

    ``` python
    local_file = '/Users/Markus/Downloads/seatable-logo.png'
    info_dict = base.upload_local_file(local_file, name='seatable-logo.png', file_type='image', replace=True)
    ```

    __Example: Upload a file from memory__

    ``` python
    local_file = '/Users/Markus/Downloads/seatable-logo.png'
    with open (local_file, 'rb') as f:
      content = f.read()
    info_dict = base.upload_bytes_file('seatable-logo.png', content, file_type='image')
    ```

    __Example: Upload a file from a website__

    ``` python
    import requests
    file_url = 'https://seatable.io/wp-content/uploads/2021/09/seatable-logo.png'
    response = requests.get(file_url)
    if response.status_code in range(200,300) :
        info_dict = base.upload_bytes_file('seatable-logo.png', response.content)
    ```

!!! abstract "Upload (detailed two-steps method)"

    As for the download detailed method, this method actually relies on two different steps: first getting a file upload link and then uploading it using a `POST` request. 

    ``` python
    base.get_file_upload_link()
    ```

    __Output__ - `base.get_file_upload_link` outputs a dict containing `upload_link`, `parent_path`, `img_relative_path` and `file_relative_path` keys

    - the `POST` request will return a `400` error `Parent dir doesn't exist.` if `parent_dir` is wrong or a `403` error `Access token not found.` if `upload_link` is wrong
    
    __Example__
    
    ``` python
    import requests
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    # Get the upload link and file path allocated by server
    upload_link_dict = base.get_file_upload_link()
    upload_link = upload_link_dict['upload_link'] # (1)!
    parent_dir = upload_link_dict['parent_path'] # (2)!
    file_relative_path = upload_link_dict['file_relative_path']
    img_relative_path = upload_link_dict['img_relative_path']

    # Upload the file
    upload_file_name = "file_uploaded.txt"
    replace = True
    response = requests.post(upload_link, data={
        'parent_dir': parent_dir,
        'replace': 1 if replace else 0  # (3)!
    }, files={
        'file': (upload_file_name, open('/User/Desktop/file.txt', 'rb')),
        'relative_path': file_relative_path # (4)!
    })
    ```

    1. `upload_link` will look like `{server_url}/seafhttp/upload-api/{temporary_upload_token}`

    2. `parent_path` will look like `/asset/{base_uuid}`. Please note that the name of the corresponding parameter for the upload `POST` request is `parent_dir`!
    
    3. `replace` requires `0` or `1`. You can use this syntax if you prefer to specify `True` or `False`

    4. Choose either the **file** relative path or the **image** relative path depending on the type of column you want to upload your file to

!!! abstract "Upload local file to a custom folder"

    This method is specific for files to store in a custom folder. It is the counterpart of the `base.download_custom_file` method. Please note that using this method, existing files will not be replaced (a new `My file(2)` will be created if `My file` already exists).

    ``` python
    base.upload_local_file_to_custom_folder(local_path, custom_folder_path=None, name=None) # (1)!
    ```

    1. - `custom_folder_path`: the path in the custom folders of the base where you want to upload the file
    - `name`: the name of the file once uploaded. If `name` is not provided, the uploaded file will keep the same name than the original

    __Output__ Single file dict containing `type`, `size`, `name` and `url` keys. This dict can be used to "assign" a file to a row.
    
    __Example__
    
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()

    #Step 1: Uploading a file to the base
    local_path = "/Users/Desktop/sky.png"
    custom_path = "/Main/"
    info_dict = base.upload_local_file_to_custom_folder(local_path, custom_path)

    #Step 2: Update a row with the uploaded file
    row_id = "xxxx"
    FILE_COL_NAME = "File" # (1)!
    base.update_row('Table1', row_id, {FILE_COL_NAME: [info_dict]})
    ```

    1. Get in the habit of storing column and/or table names in variables, this will make your scripts much easier to update if names change

## List files

!!! abstract "List files"

    List files in any folder of the custom folders file system (use `/` as path if you want to see the content of Custom folders). If you need to list the files present in a system (non-custom) folder, please refer to the [API Reference](https://api.seatable.com/reference/listbaseassets).

    ``` python
    base.list_custom_assets(path) # (1)!
    ```

    1. `path`: **Absolute** path of the directory you want to list the assets for (for example `/My Personal Folder/Photos` for a subdirectory `Photos` located in the directory `My Personal Folder`)

    __Output__ A dict containing a `dir` and a `file` key, each containing a list of respectively directories and files present in the `path` you specified (throws an error if the path is not valid)

    __Example__
    
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    folder_dir = "/Main/photos"
    main_photos_content = base.list_custom_assets(folder_dir)
    print(main_photos_content)
    ```

    __Example: display the whole Custom folders file structure__
    
    ``` python
    from seatable_api import Base, context

    def list_assets(path):
        global indent
        if path == "/" :
            print(f"📁 {path}")
        else :
            print(f"{indent}∟ 📁 {path.split('/')[-1]}")
        assets = base.list_custom_assets(path)
        if assets:
            indent += ' '
            for f in assets['file']:
                print(f"{indent}∟ 📄 {f['name']}")
            for d in assets['dir']: # (1)!
                if path == '/' :
                    list_assets(path+d['name'])
                else :
                    list_assets(path+'/'+d['name'])
            indent = indent[:-1]

    base = Base(context.api_token, context.server_url)
    base.auth()
    indent = ''
    list_assets('/') # (2)!
    ```

    1. Recursive function: for each directory of the current directory, the functions calls itself

    2. The `list_assets` function we created starts at the root level (`/`)

## Get file info

!!! abstract "Get file info"

    This methods allows you to get the file dict of any `name` file in any folder (`path`) of the custom folders file system.

    ``` python
    base.get_custom_file_info(path, name) # (1)!
    ```

    1. `path`: **Absolute** path of the directory you want to list the assets for (for example `/My Personal Folder/Photos` for a subdirectory `Photos` located in the directory `My Personal Folder`)

    __Output__ Single file dict containing `type`, `size`, `name` and `url` keys (throws an error if `path` or `name` is not valid). This dict can be used to "assign" a file to a row.

    __Example__

    === "Replace existing content"
    
        ``` python
        from seatable_api import Base, context

        base = Base(context.api_token, context.server_url)
        base.auth()
        #Step 1: Get file info
        folder_dir = "/Main/"
        file_name = "sky.png"
        file_dict = base.get_custom_file_info(folder_dir, file_name)
        print(file_dict)
        #Step 2: Update row content with file info (overwriting current content)
        row_id = "fDMHEdraSRuUMNPGEj-4kQ"
        FILE_COL_NAME = "File"
        base.update_row("Table1", row_id, {FILE_COL_NAME: [file_dict]})
        ```

    === "Append to content (detailed version)"

        ```python
        from seatable_api import Base, context

        base = Base(context.api_token, context.server_url)
        base.auth()
        #Step 1: Get file info
        folder_dir = "/Main/"
        file_name = "sky.png"
        file_dict = base.get_custom_file_info(folder_dir, file_name)
        print(file_dict)
        #Step 2: Update row content with file info (appending to current content)
        row_id = "fDMHEdraSRuUMNPGEj-4kQ"
        FILE_COL_NAME = "File"
        row = base.get_row("Table1", row_id)
        current_files = row[file_col_name]
        current_files.append(file_dict)
        print(base.update_row("Table1", row_id, {FILE_COL_NAME: current_files}))
        ```

    === "Append to content (short version)"

        ```python
        from seatable_api import Base, context

        base = Base(context.api_token, context.server_url)
        base.auth()
        #Step 1: Get file info
        folder_dir = "/Main/"
        file_name = "sky.png"
        file_dict = base.get_custom_file_info(folder_dir, file_name)
        print(file_dict)
        #Step 2: Update row content with file info (appending to current content)
        row_id = "fDMHEdraSRuUMNPGEj-4kQ"
        FILE_COL_NAME = "File"
        print(base.update_row("Table1", row_id, {FILE_COL_NAME: base.get_row("Table1",row_id)[FILE_COL_NAME] + [file_dict]}))
        ```
