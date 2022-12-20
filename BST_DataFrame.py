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
