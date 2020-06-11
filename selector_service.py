# This script reads in the data from S3 and selects highlights
import boto3
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import json
import csv
import numpy as np


class SelectorService:
    def __init__(self, bucket, key):
        self.decoded_object = None
        self.sampled_object = None
        self.bucket = bucket
        self.key = key

    def get_response(self):
        boto3.setup_default_session(profile_name='dev-account')
        client = boto3.client('s3')
        response = client.get_object(
            Bucket=self.bucket,
            Key=self.key
        )
        return response

    def read_json_data(self):
        response = self.get_response()
        load_object = json.loads(response['Body'].read().decode('utf-8'))
        self.decoded_object = load_object

    def select_random_entries(self):
        sheet_name_to_sample_by = 'Sheet1'
        self.sampled_object = np.random.choice(self.decoded_object[sheet_name_to_sample_by])
        self.increment_has_chosen_before()
        return self.sampled_object

    def increment_has_chosen_before(self):
        count_now = int(self.sampled_object['has_been_chosen_before'])
        self.sampled_object['has_been_chosen_before'] = count_now + 1
