class Book:
    def __init__(self, pages):
        self.pages = pages

    def page_count(self):
        return len(self.pages)
    
    def remove_page(self, number):
        pass  # this method will be implemented in subclasses
      
    def show_remaining(self):
        print("Remaining pages:")
        for p in self.pages:
            print(p)


class Ebook(Book):
    def remove_page(self, number):
        if 1 <= number <= len(self.pages):
            removed = self.pages.pop(number - 1)
            print(f"{number}. page deleted: {removed}")
        else:
            print("No such page in the e-book.")


class PrintedBook(Book):
    def remove_page(self, number):
        if 1 <= number <= len(self.pages):
            print(f"{number}. page torn out: {self.pages[number - 1]}")
            # we do not delete the page from printed book
        else:
            print("No such page in the printed book.")


pages = [
    "Page 1: Introduction",
    "Page 2: Topic Nine",
    "Page 3: Topic Eleven",
    "Page 4: Topic Fifteen",
    "Page 5: Topic Twenty",
    "Page 6: Conclusion"
]

ebook = Ebook(pages.copy())
printed = PrintedBook(pages.copy())

print("E-Book:")
num = int(input("Enter the page number to delete: "))
ebook.remove_page(num)
ebook.show_remaining()

print("\nPrinted Book:")
num = int(input("Enter the page number to tear out: "))
printed.remove_page(num)
printed.show_remaining()
