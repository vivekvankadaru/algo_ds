class Node:
    def __init__(self, ele):
        self.head = ele
        self.next = None

    
    def __repr__(self):
        return f'{self.head} -> {self.next}'
    
class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, ele):
        if self.head is None:
            self.head = Node(ele)
            
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(ele)
    
    def __repr__(self):
        
        if self.head is None:
            return 'None -> None Empty linked list'
        l=[]
        curr = self.head
        
        while curr:
            l.append(curr.head)
            print(l)
            curr=curr.next
            
        return f"{'->'.join(map(str, l))}" + '->None'  
    
    def InsertAtBeginning(self, ele):
        if self.head is None:
            self.head = Node(ele)
            return 
        temp = self.head
        new_node = Node(ele)
        new_node.next = temp
        self.head = new_node

    def insertAfter(self, ele, prev):
        curr = self.head
        if self.head is None:
            print('Empty Linked list.')
            return
        while curr and curr.head!=prev:
            curr=curr.next
        if curr is None:
            print(f'No {prev} found')
            return
        temp=curr.next
        new_node=Node(ele)
        new_node.next=temp
        curr.next=new_node
    def deleteAtBeginning(self):
        if self.head is None:
            print('Nothing to delete')
            return
        curr=self.head
        self.head=curr.next
    def deleteNode(self, ele):
        '''delete the first occurence of the key'''
        curr=self.head
        if self.head is None:
            print('No elements to delete')
            return
        prev=self.head
        if self.head==ele and curr.next is None:
            self.deleteAtBeginning()
            return self.head
        while curr:
            if curr.head==ele:
                temp=curr.next
                prev.next=temp
                return curr.head
            
            prev=curr
            curr=curr.next
        if curr is None:
            print(f'No {ele} to delete')
    def search(self, ele):
        if self.head is None:
            print('Empty sl')
        curr=self.head
        while curr:
            if curr.head==ele:
                print(f'{ele} found')
                return
            curr=curr.next
        if curr is None:
            print(f'No {ele} found')
    
    def __len__(self):
        count=0
        curr=self.head
        
        while curr:
            curr=curr.next
            count+=1
        return count
    
    

l=Linkedlist()
l.append(2)
l.append(1)
l.append(3)
l.InsertAtBeginning(4)
l.insertAfter(5,3)
l.insertAfter(7,9)
l.deleteAtBeginning()
l.deleteNode(3)
l.deleteNode(5)
l.deleteNode(10)
l.insertAfter(2,7)
l.search(2)
l.search(10)
l.append(0)
l.append(5)
print(len(l))
print(l._bubble_sort())
print(l)