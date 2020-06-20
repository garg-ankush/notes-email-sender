# This script reads in the data from S3 and selects highlights
import numpy as np
from database import read_json_data


def increment_has_chosen_before(item):
    count_now = int(item['has_been_chosen_before'])
    item['has_been_chosen_before'] = count_now + 1


class SelectorService:
    def __init__(self):
        self.raw_response = read_json_data()
        self.sampled_object = None
        self.sheet_name_to_sample_by = 'Sheet1'
        self.num_of_entries_to_sample = 3

    def select_random_entries(self):
        # Randomly choose entries from the dataset
        self.sampled_object = np.random.choice(self.raw_response[self.sheet_name_to_sample_by],
                                               self.num_of_entries_to_sample)

        # For each selection increment the field "has_been_chosen_before"
        # In the future can use probability to make selections to notes that haven't gotten selected
        for note in self.sampled_object:
            increment_has_chosen_before(note)
        return self.sampled_object
