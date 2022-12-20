import pandas
import numpy 
data = pandas.read_csv("https://raw.githubusercontent.com/Mif212/Struktur_Data/main/Cleaned_Laptop_data.csv")
data.drop(["processor_brand", "processor_gnrtn", "ram_type", "os", "os_bit", "graphic_card_gb", "weight", "display_size", "warranty", "Touchscreen", "msoffice", "old_price", "discount", "star_rating", "ratings", "reviews"], axis=1, inplace=True)
data = data.drop_duplicates()
data

# Searching data
class Search:
    def __init__(self, data):
        self.data = data
        self.col = []
        for i in self.data:
            self.col.append(i)
    def searching(self, column, item):
        if column in self.col:
            if item not in list(self.data[column]):
                return f"No {item} in Columns {column}"
            else:
                return self.data[self.data[column] == item]
        else:
            return f"No Columns {column} in Data Frame" 

# Mencari nilai yang paling dekat dengan mean
def closest_average(data):
    dt = numpy.array(data)
    mean = dt.mean()
    selisih = abs(dt[0] - mean)
    for i in dt:
        if abs(i - mean) <= selisih:
            selisih = abs(i - mean)
            root = i
    return root

# DataFrame ke list
def df_to_list(data):
    for i in data:
        kol = i
    list_data = []
    for j in range(len(list(data[kol]))):
        dic = {}
        for k in data:
            dic[k] = list(data[k])[j]
        list_data.append(dic)
    return list_data

class BST:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
    self.col = []
    self.display = []
    n = 0
    for i in self.key.keys():
      self.col.append(i)
      self.display.append(n)
      n+=1
    for j in self.display:
      self.display[j] = []

  # Inorder Traversal
  def inorder_display(self, root, kol, kol_ke):
    if root is not None:
      # Traverse Left
      self.inorder_display(root.left, kol, kol_ke)

      # Traverse Root
      self.display[kol_ke].append(root.key[kol])

      #Traverse right
      self.inorder_display(root.right, kol, kol_ke)

  def inorder(self, root):
    if root is not None:
      j = 0
      for i in self.col:
        self.inorder_display(root, i, j)
        j += 1
      l = 0
      dic_df = {}
      for k in self.col:
        dic_df[k] = self.display[l]
        self.display[l] = []
        l += 1
      return pandas.DataFrame(dic_df)
      

  # Insert a Node
  def insert(self, node, key):
    
    # Return a new node if the tree is empty
    if node is None:
      return BST(key)
    
    # Traverse to the right place and insert the node
    if int(key["latest_price"]) < int(node.key["latest_price"]):
      node.left = self.insert(node.left, key)
    else:
      node.right = self.insert(node.right, key)
    return node

  # Find the inorder successor
  def minValueNode(self, node):
    current = node
    #Find leftmost leaf
    while(current.left is not None):
      current = current.left
    return current

  # Deleting a Node
  def deleteNode(self, root, key):
    # Return if the tree is empty
    if root is None:
      return root

    # Find the node to be deleted
    if key["latest_price"] < root.key["latest_price"]:
      root.left = self.deleteNode(root.left, key)
    elif key["latest_price"] > root.key["latest_price"]:
      root.right = self.deleteNode(root.right, key)
    else:
      # If the node is with only child or no child
      if root.left is None or root.right is None:
        if root.left is None:
          temp = root.right
        if root.right is None:
          temp = root.left
        root = None
        return temp
      # If the node has two childern,
      # place the inorder sucessor in position of the node to be deleted
      temp = self.minValueNode(root.right)
      root.key = temp.key
      # Delete teh inorder successor
      root.right = self.deleteNode(root.right, temp.key)

    return root

  # Search a Node
  def searchNode(self, root, key):
    # Find the node to be search
    if root is None:
      return False
    elif key == root.key:
      return True
    else:
      if root.key["latest_price"] > key["latest_price"]:
        search = self.searchNode(root.left, key)
      elif root.key["latest_price"] < key["latest_price"]:
        search = self.searchNode(root.right, key)
    return search

  
  cari_root = Search(data)
ketemu = cari_root.searching("latest_price", closest_average(data["latest_price"]))
key = {}
for i in ketemu:
    key[i] = list(ketemu[i])[0]
list_data = df_to_list(data)

root = BST(key)
for j in list_data:
    root.insert(root, j)
root.inorder(root)

#tambah data 
amsiluman = {"brand" : "Amsiluman", "model" : "AXE", "processor_name" : "Core i20", "ram_gb" : "100 GB", "ssd" : "100 TB", "hdd" : "0 GB", "latest_price" : 300000}
root.insert(root, amsiluman)
laptop_2000_tahun_mendatang = {"brand" : "212XY", "model" : "ALIENFIRE", "processor_name" : "Hard Core", "ram_gb" : "100 TB", "ssd" : "10000 TB", "hdd" : "0 GB", "latest_price" : 308000}
root.insert(root, laptop_2000_tahun_mendatang)
root.inorder(root)

#search data
asus = {"brand":"ASUS", "model":"Zephyrus", "processor_name":"Core i9", "ram_gb":"16 GB GB", "ssd":"3072 GB", "hdd":"0 GB", "latest_price":441990}
print(root.searchNode(root, asus)) # True
print(root.searchNode(root, amsiluman)) # True
#delete asus
root.deleteNode(root, asus)
print(root.searchNode(root, asus)) # False

print(root.key) # cek root/akar pohon
print(root.right.left.right.key) # cek -> kanan -> kiri -> kanan (pada pohon)
print(root.left.left.right.right.key) # cek -> kiri -> kiri -> kanan -> kanan (pada pohon)
