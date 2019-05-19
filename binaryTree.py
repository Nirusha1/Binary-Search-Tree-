class BinarySearchTree:
    def __init__(self):
        self._size=0
        self._root=None
        
    class _BSTNode:
        def __init__(self,key,value):
            self.key=key
            self.value=value
            self.left=None
            self.right=None


    def add(self,key,value):
        z=self._BSTNode(key,value)
        y=None
        x=self._root
        while(x!=None):
            y=x
            if(key<x.key):
                x=x.left
            else:
                x=x.right

        if(y==None):
            self._root=z
        elif (z.key<y.key):
            y.left=z

        else:
            y.right=z
        self._size +=1

    def search(self, v):
        if self._root.key == v:
            return True
        elif self._root.key > v:
            if self._root.left == v:
                return True
            else:
                return self._root.left.search(v)
        elif self._root.key < v:
            if self._root.right ==v:
                return True
        return None
            

    def searche(x,k):
        if x==None | x.key==k:
            return x
        if x<x.key:
            return searche(x.left, k)
        else:
            return searche(x.right, k)







    def smallest(self):
        if self._root is not None:
            current = self._root
            while current.left is not None:
                current = current.left
            return current.key
 
    def largest(self):
        if self._root is not None:
            current = self._root
            while current.right is not None:
                current = current.right
            return current.key

    
 
                
           

    def is_empty(self):
        return self._size==0
           
    def size(self):
        return self._size

    def inorder_walk(self):
        nodes=[]
        self._inorder_walk(self._root, nodes)
        return nodes
                
    def _inorder_walk(self, subtree, nodes):
        if subtree:
            self._inorder_walk(subtree.left,nodes)
            nodes.append(subtree.key)
            self._inorder_walk(subtree.right, nodes)
               
    def preorder_walk(self):
        nodes=[]
        self._preorder_walk(self._root, nodes)
        return nodes
                
    def _preorder_walk(self, subtree, nodes):
        if subtree:
            nodes.append(subtree.key)
            self._preorder_walk(subtree.left,nodes)
            
            self._preorder_walk(subtree.right, nodes)

    def postorder_walk(self):
        nodes=[]
        self._postorder_walk(self._root, nodes)
        return nodes
                
    def _postorder_walk(self, subtree, nodes):
        if subtree:
            self._postorder_walk(subtree.left,nodes)
            self._postorder_walk(subtree.right, nodes)
            nodes.append(subtree.key)   
            
                

        
      
