from azure.storage.blob import BlobServiceClient
class BlobDownloader:
    def __init__(self, account_name, account_key, container_name, directory_name):
        self.account_name = account_name
        self.account_key = account_key
        self.container_name = container_name
        self.directory_name = directory_name
        self.connection_string = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.usgovcloudapi.net"
        self.blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)
        self.container_client = self.blob_service_client.get_container_client(self.container_name)

    def download_blobs(self, destination_directory):
        try:
            i = 0
            blobs = self.container_client.list_blobs(name_starts_with=self.directory_name)
            for blob in blobs:
                blob_client = self.blob_service_client.get_blob_client(
                     container=self.container_name,
                     blob=blob.name
                 )
                 destination_path = f"{destination_directory}/{blob.name}"
                 with open(destination_path, "wb") as file:
                     file.write(blob_client.download_blob().readall())
                print(f"Blob downloaded: {blob.name}")
                i=i+1
            print("Total File Downloaded = " + str(i))
        except Exception as e:
            print(f"An error occurred while downloading blobs: {e}")

# Create an instance of BlobDownloader
downloader = BlobDownloader(
    account_name="My Account Name",
    account_key="My Account Key",
    container_name="My Account Name",
    directory_name="My dir-1/My-Dir-2"
)

# Download blobs to the specified directory
downloader.download_blobs(destination_directory="/path/to/destination")
