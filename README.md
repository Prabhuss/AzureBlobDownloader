# AzureBlobDownloader

# Blob Downloader
This is a Python script that allows you to download blobs from Azure Blob Storage.

## Prerequisites
Before running this script, make sure you have the following:

- Python 3.x installed on your machine.
- The `azure-storage-blob` library installed. You can install it using pip:


## Usage
1. Import the `BlobDownloader` class from the `azure.storage.blob` module:

 ```python
 from azure.storage.blob import BlobServiceClient

2. Create an instance of the BlobDownloader class, providing the necessary parameters:
  downloader = BlobDownloader(
    account_name="My Account Name",
    account_key="My Account Key",
    container_name="My Container Name",
    directory_name="My Directory Name"
)
3. Replace "My Account Name", "My Account Key", "My Container Name", and "My Directory Name" with your own values.

Call the download_blobs method on the downloader instance, specifying the destination directory where the blobs should be downloaded:

 downloader.download_blobs(destination_directory="/path/to/destination")

Replace "/path/to/destination" with the actual path where you want the blobs to be downloaded.

4. Run the script, and the blobs will be downloaded to the specified directory.

Note: Make sure you have the necessary permissions and correct values for the account name, account key, container name, and directory name.

License
This project is licensed under the MIT License.

You can copy this content and save it as a `README.md` file in your GitHub repository. Feel free to modify the content according to your specific requirements.
