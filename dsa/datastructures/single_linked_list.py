class Node:
    def __init__(self, ele):
        self.data = ele
        self.next = None

    
    def __repr__(self):
        return f'{self.data} -> {self.next}'
    
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
        while curr and curr.data!=prev:
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
        '''delete all occurrences of the key'''
        curr = self.head
        prev = None
        found = False

        # Remove matching head nodes
        while curr and curr.data == ele:
            self.head = curr.next
            curr = self.head
            found = True

        # Traverse and remove matching nodes
        while curr:
            if curr.data == ele:
                prev.next = curr.next
                curr = curr.next
                found = True
            else:
                prev = curr
                curr = curr.next

        if not found:
            print(f'No {ele} to delete')
    
    def deleteNodeAtIndex(self, i):
        if not self.head:
            return 'No Single linked list to delete any element'
        current=self.head
        
        if current.next is None and i==0:
            self.head = None
            return current.data
        if i > len(self)-1:
            return 'Index value is higher than length'
        prev=current
        index=0
        while current:
            if i==0:
                return self.deleteAtBeginning()
            else:
                if index==i:
                    t=current.data
                    print(prev.data)
                    print(current.data)
                    print(current.next)
                    prev.next=current.next
                    
                    return t
            index+=1
            prev=current
            current=current.next
    def search(self, ele):
        if self.head is None:
            return 'Empty sl'
        curr=self.head
        while curr:
            if curr.data==ele:
                return f'{ele} found'
                
            curr=curr.next
        if curr is None:
            return f'No {ele} found'
    
    
    def fetchElementFromIndex(self, index):
        len_sl = len(self)
        if index > len_sl or index < 0 :
            return f"Can't fetch {index}>{len_sl}"
        
        placeholder=1
        curr=self.head

        while curr:
            if placeholder == index:
                return curr.data

            placeholder+=1
            curr = curr.next

    def __repr__(self):
        
        if self.head is None:
            return 'None -> None Empty linked list'
        l=[]
        curr = self.head
        
        while curr:
            l.append(curr.data)
            
            curr=curr.next
            
        return f"{'->'.join(map(str, l))}" + '->None'  
    
    def __len__(self):
        count=0
        curr=self.head
        
        while curr:
            curr=curr.next
            count+=1
        return count
    
    def __eq__(self, other):
        if not isinstance(other, SingleLinkedlist):
            return False
        curr1 = self.head
        curr2 = other.head
        while curr1 and curr2:
            if curr1.data != curr2.data:
                return False
            curr1 = curr1.next
            curr2 = curr2.next
        return curr1 is None and curr2 is None
    
def main():

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

    sl1=SingleLinkedlist()
    sl1.append(1)
    sl1.append(2)
    sl1.append(1)
    sl1.deleteNodeValue(1)
    print(sl1)
if __name__ == '__main__':
    main()