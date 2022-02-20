import numpy as np
class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        self.len_collection = len(self.collection)
        self.pages = []
        page = 0
        items_per_page = self.items_per_page
        for i in range(self.len_collection):
            self.pages.append(page)
            if  i == items_per_page-1:
                page += 1
                items_per_page += self.items_per_page

    def item_count(self):
        return len(self.collection )

    def page_count(self):
        return len(np.unique(self.pages))

    def page_item_count(self, page_index):
        return -1 if self.pages.count(page_index) <= 0 else self.pages.count(page_index)

    def page_index(self, item_index):
        return -1 if 0 > item_index or item_index >= self.len_collection else self.pages[item_index]

if __name__ == '__main__':
    # collection = range(1, 25)
    collection = ['a','b','c','d','e','f','g',"h"]
    helper = PaginationHelper(collection, 12)
    h1 = helper.page_count()
    h2 = helper.item_count()
    h3 = helper.page_item_count(5)
    h4 = helper.page_index(7)
    print(f'page_count {h1}')
    print(f'item_count {h2}')
    print(f'page_item_count {h3}')
    print(f'page_item_count {h4}')



