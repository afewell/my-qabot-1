import os
import urllib.request
import tarfile

# Function to download and extract the tar.gz file
def download_and_extract_files(file_url, destination_directory):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
   
    # Download the tar.gz file
    urllib.request.urlretrieve(file_url, 'archive.tar.gz')
   
    # Extract the contents of the tar.gz file to the destination directory
    with tarfile.open('archive.tar.gz', 'r:gz') as tar:
        tar.extractall(destination_directory)
   
    # Remove the tar.gz file
    os.remove('archive.tar.gz')

# Define the URL of the tar.gz file and the destination directory
file_url = 'https://scrapyfarm.blob.core.windows.net/scrapyfarm/tanzubot_storage-0_2.tar.gz'
destination_directory = '.'

# Download and extract the files
download_and_extract_files(file_url, destination_directory)

# Call app.py
os.system('python web.py')