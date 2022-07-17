from math import ceil


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] * 3 for i in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label):

        for page in range(len(self.photos)):
            if len(self.photos[page]) < 4:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"
        return "No more free slots"

    def display(self):
        result = ''
        result += f"{'-' * 11}\n"
        for page in self.photos:
            result += f"{('[] ' * len(page)).rstrip()}\n"
            result += f"{'-' * 11}\n"

        return result.strip()

