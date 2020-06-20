from selector_service import SelectorService


class ContentParser:
    def __init__(self):
        self.sample_entries = SelectorService().select_random_entries()
        self.content = None

    def parse_selected_entries(self):
        content = ''
        for item_index in range(len(self.sample_entries)):
            item = "DATE-ADDED: " + self.sample_entries[item_index]['date_added']
            content = content + item + "\n"
            item = "HIGHLIGHT: " + self.sample_entries[item_index]['highlight']
            content = content + item + "\n"
            item = "TITLE: " + self.sample_entries[item_index]['title']
            content = content + item + "\n"
            item = "CHAPTER: " + self.sample_entries[item_index]['chapter']
            content = content + item + "\n"
            item = "SOURCE: " + self.sample_entries[item_index]['source']
            content = content + item + "\n"
            item = "PAGE-NUMBER: " + self.sample_entries[item_index]['page_number']
            content = content + item + "\n" + "------------" + "\n"
        self.content = content
        return self.content
