# This script reads in the data from S3 and selects highlights
import boto3
import os
import sys
import pandas as pd
import json
import csv
import numpy as np


class SelectorService:
    def __init__(self):
        self.decoded_object = None
        self.sampled_object = None
        self.bucket = None
        self.key = None
        self.sheet_name_to_sample_by = 'Sheet1'
        self.num_of_entries_to_sample = 3

    def read_json_data(self):
        with open('/Users/ankushgarg/Desktop/email-reading-highlights/notes-email-sender/data/data.json') as json_file:
            response = json.load(json_file)
        return response

    def increment_has_chosen_before(self, item):
        count_now = int(item['has_been_chosen_before'])
        item['has_been_chosen_before'] = count_now + 1

    def select_random_entries(self):
        response = self.read_json_data()
        self.sampled_object = np.random.choice(response[self.sheet_name_to_sample_by], self.num_of_entries_to_sample)

        for note in self.sampled_object:
            self.increment_has_chosen_before(note)
        return self.sampled_object