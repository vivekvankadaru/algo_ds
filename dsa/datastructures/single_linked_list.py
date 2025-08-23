class Node:
    def __init__(self, ele):
        self.head = ele
        self.next = None

    
    def __repr__(self):
        return f'{self.head} -> {self.next}'
    
class SingleLinkedlist:
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
    def InsertAtIndex(self, i, ele):
        if i == 0 and self.head is None:
            self.head = Node(ele)
            return
        if i > len(self)-1:
            print(f'Index {i} > {len(self)}. So cant insert')
            return
        index=0
        current=self.head
        prev=self.head
        while current:
            if i==0:
                self.InsertAtBeginning(ele)
                return
            if index==i:
                
                new_node=Node(ele)
                new_node.next=current
                prev.next=new_node
                return
            index+=1
            prev=current
            current=current.next
    def deleteAtBeginning(self):
        if self.head is None:
            print('Nothing to delete')
            return
        curr=self.head
        self.head=curr.next
    def deleteNodeValue(self, ele):
        '''delete the first occurence of the key'''
        curr=self.head
        if self.head is None:
            print('No elements to delete')
            return
        prev=self.head
        if self.head==ele and curr.next is None:
            self.deleteAtBeginning()
            return self.head
        l=[]
        while curr:
            print(f'curr.head: {curr.head}')
            print(f'prev:{prev}')
            print(f'curr:{curr}')
            if curr.head==ele:
                temp=curr.next
                prev.next=temp
                print(f'new prev: {prev}')
                l.append(curr.head)
            else:
                prev=curr
                print(f'new prev: {prev}')
            print(f'sl: {self}')
            #prev=curr
            curr=curr.next
        print(l)
        if not l:
            print(f'No {ele} to delete')
    
    def deleteNodeAtIndex(self, i):
        if not self.head:
            return 'No Single linked list to delete any element'
        current=self.head
        
        if current.next is None and i==0:
            self.head = None
            return current.head
        if i > len(self)-1:
            return 'Index value is higher than length'
        prev=current
        index=0
        while current:
            if i==0:
                return self.deleteAtBeginning()
            else:
                if index==i:
                    t=current.head
                    print(prev.head)
                    print(current.head)
                    print(current.next)
                    prev.next=current.next
                    
                    return t
            index+=1
            prev=current
            current=current.next
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
    
    
    def __repr__(self):
        
        if self.head is None:
            return 'None -> None Empty linked list'
        l=[]
        curr = self.head
        
        while curr:
            l.append(curr.head)
            
            curr=curr.next
            
        return f"{'->'.join(map(str, l))}" + '->None'  
    
    def __len__(self):
        count=0
        curr=self.head
        
        while curr:
            curr=curr.next
            count+=1
        return count
    
    

l=SingleLinkedlist()
l.append(2)
l.append(1)
l.append(3)
l.InsertAtBeginning(4)
l.insertAfter(5,3)
l.insertAfter(7,9)
l.deleteAtBeginning()
l.deleteNodeValue(3)
l.deleteNodeValue(5)
l.deleteNodeValue(10)
l.insertAfter(2,7)
l.search(2)
l.search(10)
l.append(0)
l.append(5)

print(len(l))
#print(l._bubble_sort())

l.deleteNodeAtIndex(3)
l.deleteNodeAtIndex(3)

l.InsertAtIndex(2,10)
l.InsertAtIndex(4,10)
l.append(10)
l.append(10)
print(l)
l.deleteNodeValue(10)
print(l)