# Files

## Download

!!! question "Download (simple method)"

    Download a file to a local path.

    ``` python
    base.download_file(file_url, save_path)
    ```

    __Example__

    ``` python
    file_url = "https://cloud.seatable.io/workspace/74/asset-preview/41cd05da-b29a-4428-bc31-bd66f4600817/files/2020-10/invoice.pdf"
    save_path = "/tmp/invoice.pdf"
    base.download_file(file_url, save_path)
    ```

!!! question "Download (detailed method)"

    This detailed method is for handling complex situations where the file is extremly large or the internet connection is slow. In this example I assume that there exist a file like `https://cloud.seatable.io/dtable-web/workspace/74/asset-preview/41cd05da-b29a-4428-bc31-bd66f4600817/files/2020-10/invoice.pdf`.

    ``` python
    download_link = base.get_file_download_link(file_url)
    ```

    __Example__

    ``` python
    import requests
    download_link = base.get_file_download_link('files/2020-10/invoice.pdf')
    response = requests.get(download_link)
    ```

!!! question "Download file to local"

    ``` python
    base.download_custom_file(path, save_path)
    ```

    __Example__

    ``` python
    custom_file_path = "/Main/sky.png"
    local_path = "/Users/Desktop/sky.png"
    base.download_custom_file(custom_file_path, local_path)
    ```

## Upload

!!! question "Upload (simple method)"

    Upload a file from your local drive, memory or a website.

    ``` python
    base.upload_local_file(file_path, name=None, file_type='file', replace=False)
    # or
    base.upload_bytes_file(name, content, file_type='file', replace=False)
    ```

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
    info_dict = base.upload_bytes_file = ('seatable-logo.png', content, file_type='image')
    ```

    __Example: Upload a file from a website__

    ``` python
    import requests
    file_url = 'https://seatable.io/wp-content/uploads/2021/09/seatable-logo.png'
    response = requests.get(file_url)
    info_dict = base.upload_bytes_file = ('seatable-logo.png', response.content)
    ```

!!! question "Upload (detailed method)"

    Get a file upload link.

    ``` python
    base.get_file_upload_link()
    ```

    __Example__

    ``` python
    # Get the upload link and file path allocated by server
    upload_link_dict = base.get_file_upload_link()
    parent_dir = upload_link_dict['parent_path']
    upload_link = upload_link_dict['upload_link'] + '?ret-json=1'

    # Upload the file
    upload_file_name = "file_uploaded.txt"
    replace = 1
    response = requests.post(upload_link, data={
        'parent_dir': parent_dir,
        'replace': 1 if replace else 0
    }, files={
        'file': (upload_file_name, open('/User/Desktop/file.txt', 'rb'))
    })
    ```

!!! question "Upload local file to custom folders"

    ``` python
    base.upload_local_file_to_custom_folder(self, local_path, custom_folder_path=None, name=None)
    ```

    __Example__

    ``` python
    local_path = "/Users/Desktop/sky.png"
    custom_path = "/Main/"

    info_dict = base.upload_local_file_to_custom_folder(local_path， custom_path)
    row_id = "xxxx"
    file_col_name = "File"
    base.update_row('Table1', row_id, {"File": [info_dict]})
    ```

## List files

!!! question "List files"

    List files in custom folders.

    ``` python
    base.list_custom_assets(path)
    ```

    __Example__

    ``` python
    folder_dir = "/Main/photos"
    base.list_custom_assets(folder_dir)
    # A dict will be returned including dir and file
    {
    "dir": [{'name': "MyDir"}, ...]
    "file":[{'name': "sky.png"}, ....]
    }
    ```

## Get file info

!!! question "Get file info"

    The data structure returned can be used to updated cells of file column.

    ``` python
    base.get_custom_file_info(path, name)
    ```

    __Example__

    ``` python
    folder_dir = "/Main/"
    file_name = "sky.png"
    info_dict = base.get_custom_file_info(path, name)
    row_id = "xxxx"
    file_col_name = "File"
    base.update_row('Table1', row_id, {"File": [info_dict]})
    ```
