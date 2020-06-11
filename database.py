import boto3
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import json
import csv

csv.register_dialect('piper', delimiter='|', quoting=csv.QUOTE_NONE)


# Ended up using http://beautifytools.com/excel-to-json-converter.php to convert Excel to Json
class Database:
    def __init__(self, bucket, key):
        self.bucket = bucket
        self.key = key
        self.data = None

    def read_json_file_from_local(self):
        url = '/Users/ankushgarg/Desktop/email-reading-highlights/data/sample_dataset_test.json'

        with open(url) as file:
            self.data = file.read()

    def write_data_to_S3(self):
        boto3.setup_default_session(profile_name='dev-account')
        client = boto3.client('s3')
        response = client.put_object(
            ACL='private',
            Body=self.data,
            Bucket=self.bucket,
            Key=self.key
        )
