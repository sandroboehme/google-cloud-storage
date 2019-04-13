import os
import unittest
# Imports the Google Cloud client library
from random import randint

from google.cloud import storage

from definitions import ROOT_PATH


class TestCloudStorageAccess(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        auth_file_path = os.path.join(ROOT_PATH, 'auth.json')
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = auth_file_path

    def test_create_bucket(self):

        # Instantiates a client
        storage_client = storage.Client()

        # The name for the new bucket
        bucket_name = str(randint(0, 9))+'th-new-bucket'

        # Creates the new bucket
        bucket = storage_client.create_bucket(bucket_name)

        print('Bucket {} created.'.format(bucket.name))

    def test_upload_json_file(self):
        """Uploads a file to the bucket."""
        storage_client = storage.Client()
        bucket = storage_client.get_bucket('sandros-new-bucket')
        blob = bucket.blob('8.json')

        file_path = os.path.join(ROOT_PATH, 'test/8.json')
        blob.upload_from_filename(file_path)

        print('File uploaded.')

    def test_download_blob(self):
        """Downloads a blob from the bucket."""
        storage_client = storage.Client()
        bucket = storage_client.get_bucket('sandros-new-bucket')
        blob = bucket.blob('8.json')

        file_path = os.path.join(ROOT_PATH, 'test/8-downloaded.json')
        blob.download_to_filename(file_path)

        print('Blob downloaded.')


if __name__ == '__main__':
    unittest.main()
