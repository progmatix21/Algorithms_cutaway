#!/usr/bin/env python3

'''
A module that defines a Node class that can implement a linked list and a
function to reverse a linked list.
'''

class Node():
    '''
    A class that implements a linked list node.
    Node(val = None, nxt = None) returns Node
    '''
    def __init__(self, val = None, nxt = None):
        # Input: value for the node. Default: None
        self.val = val
        self.nxt = nxt
    
    def tail(self):
        # Return last node reachable from here
        cur = self   # get a pointer to this node
        while(cur.nxt != None):
            cur = cur.nxt
        return cur # Return terminal node
            
    def __str__(self):
        # print current node upto last reachable node for user
        return f"{self.val}->{self.nxt}"
        
    def __repr__(self):
        # print current node for debugging
        class_name = type(self).__name__
        if self.nxt != None:
            nxt_id = f"{id(self.nxt):x}"
        else:
            nxt_id = 'None'
        return f"{class_name}(val={self.val}) at {id(self):0x} linked to {nxt_id}"


def revll(head,cutaway=False):
    # Reverse linked list
    # Input: head of linked list to be reversed
    # Returns: head of reversed linked list
    '''
    Statement of recursion: given head, append head to reverse of rest of list.
    '''
    _cutaway = cutaway
    
    if head.nxt == None:   # At last node
        if cutaway:
            print("Cutaway view --------")
            print(f"[{head}], at terminal node of original list")
        return head

    else:
        last = head       # This node will become the tail of the reverse list
        rol = head.nxt    # Separate head and rest of list
        # Append last to reverse of rol or make it next node to tail of rol
        rhead = revll(rol, cutaway = _cutaway)
        last.nxt = None
        if cutaway: 
            print(f"Append [{last}] to part of reversed list [{rhead}]")
        rhead.tail().nxt = last
        return rhead

     
if __name__ == "__main__":
    '''Test the node class by creating a linked list.'''
    head = cur = None   # Initialize head and current pointer
    
    for i in range(10):   # Create a linked list of a series
        if head == None:  # First element
            head = Node(val = i)
            cur = head    # The current node is head node
        else:
            cur.nxt = Node(val = i)
            cur = cur.nxt
    
    ''' 
    # Print each node individually for debugging. Requires a do-while loop,
    # not available in Python, instead we use a while-else loop.
    cur = head
    while cur.nxt != None:
        print(repr(cur))
        cur = cur.nxt
    else:
        print(repr(cur))
    '''
        
    # Print entire list for user.
    print(f"Original linked list:\n{head}")
    print(f"Reversed linked list:\n{revll(head,cutaway = True)}")
    
