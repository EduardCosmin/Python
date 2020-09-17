#Special Methods

my_list = [1,2,3]
print(len(my_list))

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):  #special method for strings
        return f"{self.title} by {self.author}"

    def __len__(self):  #special method for length
        return self.pages

    def __del__(self):  #show a message when we delete a book
        print("A book object has been deleted")

b = Book('Python rocks', 'Jose', 200)
print(b)
print(len(b))

#If we want to delete a book we use 'del'
del b   #delete variable'b' from the computer memory (in our case: book b)
print(b)    #Output: name 'b' is not defined


#Another way to write the class above:
# class Book:
#     def __init__(self, title, author, pages):
#         print("A book is created")
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def __str__(self):
#         return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)

#     def __len__(self):
#         return self.pages

#     def __del__(self):
#         print("A book is destroyed")

# book = Book("Python Rocks!", "Jose Portilla", 159)

# #Special Methods
# print(book)
# print(len(book))
# del book