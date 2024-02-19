import os
import sys
from datetime import date


programPath = os.path.abspath(__file__)
programDirectory = os.path.dirname(programPath)
#programın çalıştığı yeri belirtiyor. (bende direkt D) diskimde oluşturuyordu) soruna olacak en iyi çözüm buydu

class Library:
    def __init__(self):
        self.DB = open("{}\\books.txt".format(programDirectory),"+a")
        self.time = date.today()
        
    def Menu(self):         #menü
        print("""
            ======== Menu ========
            1) List Books
            2) Add Book
            3) Remove Book
            4) Delete DataBase (need restart...)
            q) Exit
            """)
        answer = input("Choice: ")
        if answer == "1":
            self.ListBook()
        elif answer == "2":
            self.AddBook()
        elif answer == "3":
            self.RemoveBook()
        elif answer == "4":
            self.delDB()
        elif answer.lower() == "q":
            self.Exit()
        else:
            self.Menu()
            
    def ListBook(self):         #kitapları listeleme
        self.DB.seek(0)
        x = 0
        for book in self.DB:
            bInfo = book.strip().split(',')
            print(f"{x}) Name: {bInfo[0]}, Author: {bInfo[1]}, Save Time: {bInfo[4]}")
            x += 1
    
    def AddBook(self):          #kitap ekleme
        self.DB.seek(0)
        BookName = input("Book Name: ")
        AuthorName = input("Author: ")
        Release_year = input("Release Year: ")
        PageNumber = input("Page: ")
        book = f"{BookName},{AuthorName},{PageNumber},{Release_year},{self.time} \n"
        self.DB.write(book)
        self.DB.seek(0)
        
    def RemoveBook(self):       #kitap silme kısmı
        titleCheck = input("Enter Title of the book to remove: ")
        CleanList = []
        flg = False
        self.DB.seek(0)
        for title in self.DB:
            check = title.strip().split(',')
            if check[0] != titleCheck:
                CleanList.append(title)
            else:
                flg = True
        if flg:
            self.DB.seek(0)
            self.DB.truncate()
            self.DB.writelines(CleanList)
            print(f"{titleCheck} removed")
        else:
            print(f"{titleCheck} not found")
        
    def delDB(self):    #books.txt dosyasını silmekte (sorun yaşanmaması için programı kapatmakta o yüzden tekrar açmanız gerekiyor)
        ans = input("Are you sure? (y/n): ")
        if ans.lower() == "y":
            self.DB.close()
            if os.path.exists(programDirectory+"\\books.txt"):
                os.remove(programDirectory+"\\books.txt")
                self.Exit()
            else:
                print("DataBase not Found")
        else:
            self.Menu()
    
    
    def Exit(self):     #kapatma kısmı
        print("Shut Down...")
        self.DB.close()
        sys.exit()
    
 
lib = Library()

while True:
    lib.Menu()