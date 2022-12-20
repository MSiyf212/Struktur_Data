import pandas
data = pandas.read_csv("https://raw.githubusercontent.com/Mif212/dokumen/main/data_mhs.csv")
data.drop(["tahun_akademik", "nama_mk", "sks_matkul", "nilai_mutu"], axis = 1, inplace=True)
data

class Stack:
  def __init__(self, data):
    self.data = data
    self.kolom = []
    for i in self.data:
      self.kolom.append(i)

  def __len__(self):
    return f"{len(list(self.data[self.kolom[0]]))} rows × {len(self.kolom)} columns"

  def isempty(self):
    return len(list(self.data[self.kolom[0]])) == 0
  
  def view(self):
    return self.data

  def push(self, item):
    kol = {}
    j = 0
    for i in self.kolom:
      kol[j] = list(self.data[i])
      j += 1
    k = 0
    data = {}
    for j in item:
      kol[k].append(j)
      k += 1
    p = 0
    for m in self.kolom:
      data[m] = kol[p]
      p += 1
    self.data = pandas.DataFrame(data)

  def pop(self):
    if self.isempty():
      raise Exception('Stack kosong')
    else:
      data = {}
      df_a = self.data.tail(1)
      for i in self.kolom:
        data[i] = list(self.data[i])
        data[i].pop()
      self.data = pandas.DataFrame(data)
      return df_a

  def top(self):
    if self.isempty():
      raise Exception('Stack kosong')
    return self.data.tail(1)
  
sipa = Stack(data)
print(sipa.__len__())
print(sipa.isempty())
print(sipa.view())
sipa.push(["121450125", "Miftahul Huda", 3, "RC", 3.21, 3.11])
print(sipa.view())
print(sipa.pop())
print(sipa.view())
print(sipa.push(["121450113", "Syifa Fathonah", 3, "RC", 4.00, 4.00]))
print(sipa.view())
print(sipa.top())
print(sipa.push(["121450125", "Miftahul Huda", 3, "RC", 3.21, 3.11]))
print(sipa.top())
print(sipa.view())
print(sipa.__len__())
