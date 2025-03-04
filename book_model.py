

class BookModel : 

    #define constructor

    def __init__(self,isbn,title,genre,author ,price,quantity,publisher,yearofpub) :
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.quantity = quantity
        self.publisher=publisher
        self.yearofpub=yearofpub

    def con_to_dict(self) :
        return {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "price": self.price,
            "quantity": self.quantity,
            "publisher":self.publisher,
            "year of publication":self.yearofpub

        }    