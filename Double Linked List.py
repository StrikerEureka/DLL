class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
        self.prev = None

class doublelinkedlist(object) :
    def __init__(self) :
        self.head = None
        self.tail = None

    def tambahbelakang(self, data) :
        if self.head is None :
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else :
            new_node = Node(data)
            current_node = self.head
            while current_node.next is not None :
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
            new_node.next = None
            self.tail = new_node

        print("Data ditambahkan.")
        print("")
        
    def tambahdepan(self, data) :
        if self.head is None :
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else :
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None
        
        print("Data ditambahkan.")
        print("")

    def tambahsetelah(self, key, data) :
        current_node = self.head
        while current_node is not None :
            if current_node.next is None and current_node.data == key :
                self.tambahbelakang(data)
                return
            elif current_node.data == key :
                new_node = Node(data)
                nxt = current_node.next
                current_node.next = new_node
                new_node.next = nxt
                new_node.prev = current_node
                nxt.prev = new_node
            current_node = current_node.next

        print("Data ditambahkan.")
        print("")

    def tambahsebelum(self, key, data) :
        current_node = self.head
        while current_node is not None :
            if current_node.prev is None and current_node.data == key :
                self.tambahdepan(data)
                return
            elif current_node.data == key :
                new_node = Node(data)
                prev = current_node.prev
                prev.next = new_node
                current_node.prev = new_node
                new_node.next = current_node
                new_node.prev = prev
            current_node = current_node.next
        
        print("Data ditambahkan.")
        print("")

    def hapusdepan(self) :
        if self.head is None :
            print ("Data masih kosong.")
        else :
            if self.head.next is not None :
                self.head.next.prev = None
            self.head = self.head.next
        
        print("Data dihapus.")
        print("")
    
    def hapusbelakang(self) :
        if self.tail is None :
            print ("Data masih kosong.")
        else :
            if self.tail.prev is not None :
                self.tail.prev.next = None
                self.tail = self.tail.prev
                return

        print("Data dihapus.")
        print("")

    def hapustarget (self, data) :
        if self.head is None :
            print ("Data masih kosong.")
            return
        current_node = self.head
        while current_node.data is not data and current_node.next is not None :
            current_node = current_node.next
        if current_node.data is not data :
            print ("Data tidak ditemukan.")
            return
        if current_node.prev is not None :
            current_node.prev.next = current_node.next
        else :
            self.head = current_node.next

        if current_node.next is not None :
            current_node.next.prev = current_node.prev
        else :
            self.tail = current_node.prev
        
        print("Data dihapus.")
        print("")

    def tampil(self) :
        print("Data : ")
        print("")

        current_node = self.head
        while current_node is not None :
            print (current_node.data, end=" -> ")
            current_node = current_node.next     

    def tampilreverse(self) :
        current_node = self.tail
        while current_node is not None :
            print (current_node.data, end=", ")
            current_node = current_node.prev

    def menuUmum(self):
        pilih = "y"
        while ((pilih == "y") or (pilih == "Y")):
            # os.system('clear')
            print('Pilih menu yang anda inginkan')
            print('==============================')
            print('1. Tambah data di belakang')
            print('2. Tambah data di depan')
            print('3. Tambah data setelah data')
            print('4. Tambah data sebelum data')
            print('5. Hapus data di depan')
            print('6. Hapus data di belakang')
            print('7. Hapus data pilihan')
            print('8. Tampilkan data')
            pilihan = str(input("Masukkan Menu yang anda pilih : "))
            if(pilihan == "1"):
                node = str(input("Masukkan data : "))
                self.tambahbelakang(node)
            elif(pilihan == "2"):
                node = str(input("Masukkan data : "))
                self.tambahdepan(node)
            elif(pilihan == "3"):
                node = str(input("Masukkan data : "))
                node2 = str(input("Masukkan setelah : "))
                self.tambahsetelah(node2, node)
            elif(pilihan == "4"):
                node = str(input("Masukkan data : "))
                node2 = str(input("Masukkan sebelum : "))
                self.tambahsebelum(node2, node)
            elif(pilihan == "5"):
                self.hapusdepan()
            elif(pilihan == "6"):
                self.hapusbelakang()
            elif(pilihan == "7"):
                node = str(input("Masukkan data yang ingin dihapus : "))
                self.hapustarget(node)
            elif(pilihan == "8"):
                self.tampil()
                x = input("")
            else :
                pilih ="n"

if __name__ == "__main__" :
    d = doublelinkedlist()
    d.menuUmum()
