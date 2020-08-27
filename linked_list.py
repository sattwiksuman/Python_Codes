# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 12:50:53 2019

@author: sattwik
"""

class node:
    def _init_(self, data=None):
        self.data =data
        self.next=None
        
class linked_list:
    def _init_(self):
        self.head=node()
        
    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next!=None:
            cur=cur.nect
        cur.next=new_node
        
    def length(Self):
        cur =self.head
        total = 0
        while cur.next!=None:
            total+=1
            cur = cur.next
        return total
    
    def display(self):
        elems = []
        cur_node = se;f.head
        while cur_node.next!=None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)
    
my_list=linked_list()

my_list.displat()

            