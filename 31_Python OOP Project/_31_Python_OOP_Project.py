class Library:
	def __init__(self, list, name):
		self.bookList = list
		self.name = name
		self.lenDict = {}

	def displayBooks(self):
		print(f"{self.name}, We have follwong books in our library")
		sno = 1
		for book in self.bookList:
			print(f"{sno}. {book}")
			sno += 1

	def lendBook(self, book, name):
		if book in self.bookList:
			if book not in self.lenDict:
				self.lenDict.update({book : name})
				print("Lender-Book database has been updated. You can take the book now")
			else:
				print(f"Book is already being used by {self.lenDict[book]}")
		else:
			print("Book is not available in our library")
			
	def addBook(self, book):
		if book not in self.bookList:
			self.bookList.append(book)
			print("Book has been added to the book list")
		else:
			print("Book is already in the book list")
			
	def returnBook(self, book):
		if book in self.lenDict:
			self.lenDict.pop(book)
			print("Lender-Book database has been updated")
		else:
			print("Book is not being used by anyone")
			
myLibrary = Library(['Python', 'C++', 'Java', 'C', 'C#'], "CodeWithHarry Library")
print(myLibrary.__dict__)

# Display books
myLibrary.displayBooks()

# Add a book
myLibrary.addBook('Django')
print(myLibrary.__dict__)
myLibrary.addBook('Python')

# Lend a book
myLibrary.lendBook('C++', 'Harry')
print(myLibrary.__dict__)
myLibrary.lendBook('C++', 'Harry')
myLibrary.lendBook('C', 'Harry Poster')
print(myLibrary.__dict__)

# Return a book
myLibrary.returnBook('C++')
print(myLibrary.__dict__)
myLibrary.returnBook('C++')



