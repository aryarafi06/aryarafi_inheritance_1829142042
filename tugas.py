class Sekolah(object):
   def __init__(self, k, g, c):
      self.ruangkepsek = k
      self.ruangguru = g
      self.ruangkelas = c

   def cetakData(self):
      print("ruangkepsek\t: ", self.ruangkepsek)
      print("ruangguru\t: ", self.ruangguru)
      print("ruangkelas\t: ", self.ruangkelas)

# mendefinisikan kelas turunan (subclass)
class Ruangan(Sekolah):
   def __init__(self, k, g, c, j):
      self.ruangkepsek = k
      self.ruangguru = g
      self.ruangkelas = c
      self.kantin = j
      
   def cetakData(self):
      print("ruangkepsek\t: ", self.ruangkepsek)
      print("ruangguru\t: ", self.ruangguru)
      print("ruangkelas\t: ", self.ruangkelas)
      print("kantin\t        : ", self.kantin)

def main():
   # membuat objek ruangan
   Ruangan1 = Ruangan(1, 1, 9, 1)

   # menggunakan objek
   Ruangan1.cetakData()

if __name__ == "__main__":
   main()
