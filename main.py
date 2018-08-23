from mobi import Mobi

collins = "C:/Users/Anchpop/Google Drive/book/Calibre library/HarperCollins Publishers/Collins French to English (One Way) (115)/Collins French to English (One - HarperCollins Publishers.mobi"
potter = "C:/Users/Anchpop/Google Drive/book/Calibre library/J.K. Rowling/Harry Potter et la Coupe de Feu (La (110)/Harry Potter et la Coupe de Feu - J.K. Rowling.mobi"

book = Mobi(potter)
book.parse()

for record in book:
    if record:
        print(record)
