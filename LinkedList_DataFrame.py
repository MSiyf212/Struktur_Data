import pandas as pd
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/Mif212/dokumen/main/data_set_test.csv')
print(df)
print(df.columns)

class LinkedQueue:
  def __init__(self, data):
    self.data = data
    self.kolom = []
    for i in self.data:
      self.kolom.append(i)
  def __len__(self):
    return f"{len(list(self.data[self.kolom[0]]))} rows × {len(self.kolom)} columns"
  def is_empty(self):
    return len(list(self.data[self.kolom[0]])) == 0
  def add(self, index, data_item):
    if self.is_empty():
      raise Exception('List is empty')
    else:
      kol = {}
      j = 0
      for i in self.kolom:
        kol[j] = list(self.data[i])
        j += 1
      k = 0
      data = {}
      for j in data_item:
        kol[k].insert(index, j)
        k += 1
      p = 0
      for m in self.kolom:
        data[m] = kol[p]
        p += 1
      self.data = pd.DataFrame(data)
  def add_first(self, item):
    self.add(0, item)
  def add_last(self, item):
    last = len(list(self.data[self.kolom[0]]))
    print(last)
    self.add(last, item)
  def view(self):
    return self.data
  def first(self):
    if self.is_empty():
      raise Exception('List kosong')
    return self.data.head(1)
  def last(self):
    if self.is_empty():
      raise Exception('Stack kosong')
    return self.data.tail(1)
  def delete_first(self):
    if self.is_empty():
      raise Exception('List Kosong')
    else:
      data = {}
      for i in self.kolom:
        data[i] = list(self.data[i])
        del data[i][0]
      self.data = pd.DataFrame(data)
  def delete_last(self):
    if self.is_empty():
      raise Exception('List Kosong')
    else:
      data = {}
      for i in self.kolom:
        data[i] = list(self.data[i])
        data[i].pop()
      self.data = pd.DataFrame(data)
      
pandra = LinkedQueue(df)
print(pandra.view())
pandra.add_first(["Sastra Jawa", 90, 90, 90, 2, 3])
print(pandra.view())
print(pandra.__len__())
pandra.add_first(["Sastra Jepang", 100, 80, 100, 1, 1])
print(pandra.view())
pandra.add_last(["Sastra Jepang", 100, 80, 100, 1, 1])
print(pandra.view())
print(pandra.is_empty())
print(pandra.first())
print(pandra.last())
pandra.delete_first()
print(pandra.view())
pandra.delete_last()
print(pandra.view())
