class Library:

    def __init__(self,listofBooks):
        self.availableBooks = listofBooks

    def displayAvailableBooks(self):
        print("Available books:")
        for book in self.availableBooks:
            print(book)

    def lendBook(self,requestedBook):
        if requestedBook in self.availableBooks:
            print("You have now borrowed this book")
            self.availableBooks.remove(requestedBook)
        else:
            print('Book is not available')

    def addBook(self,returnedBook):
        self.availableBooks.append(returnedBook)
        print("You have returned the book thankyou")


class Customer:
    def requestBook(self):
        print("Enter a name of book you want to borrow")
        self.book=input()
        return self.book

    def returnBook(self):
        print("Enter the book which you want to return")
        self.book=input()
        return  self.book

library= Library(["think","who will","for one more"])
customer= Customer()
while True:

    print("Enter 1 to display books")
    print("Enter 2 to request a book")
    print("Enter 3 to return a book")
    print("Enter 4 to Exit")

    userchoice=int(input())

    if userchoice is 1:
        library.displayAvailableBooks()
    elif userchoice is 2:
        requestedBook=customer.requestBook()
        library.lendBook(requestedBook)
    elif userchoice is 3:
        returnBook=customer.returnBook()
        library.addBook(returnBook)
    elif userchoice is 4 :
        quit()



