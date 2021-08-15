#!/usr/bin/env python
# coding: utf-8

# # PREFIX TO POSTFIX
# 

# In[1]:


priority_dic = {
    "(" : 1,
    ")" : 1,
    "+" : 3,
    "-" : 2,
    "*" : 4,
    "/" : 5
}


# In[19]:

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None


class Stack:
    def __init__(self,first_node,max_items):
        self.head = Node(first_node)
        self.max_items = max_items
        self.len = 1
        
    def push(self,node):
        if self.head == None:
            self.head = Node(node)
            self.len +=1
        elif self.len < self.max_items:
            current = self.head
            self.head = Node(node)
            self.head.next = current
            self.len+=1
        else:
            raise Exception("Stack Memory is Full")
            
    def pop(self):
        if self.len == 0:
            return None
        else:
            self.len -=1
            deleted_node = self.head
            self.head = self.head.next
            current = self.head
            return deleted_node
            
    def __len__(self):
        return self.len
# stack = Stack(1,6)


# In[6]:


# In[33]:


class PtoPConvertor:
    def _postfix(self,stack,expression):
        postfix = ""
        for arg in expression:
            if arg == "(":
                stack.push("(")
            elif arg == ")":
                while(1):
                    pop_item = stack.pop()
                    if pop_item != None:
                        if pop_item.data == "(":
                            break
                        else:
                            postfix += pop_item.data
                    else:
                        break
            elif priority_dic.get(arg,0):
                if stack.head.data != "(":
                    if priority_dic.get(stack.head.data,0) < priority_dic.get(arg,0):
                        stack.push(arg)
                    elif priority_dic.get(stack.head.data,0) == priority_dic.get(arg,0):
                        pop_item = stack.pop()
                        stack.push(arg)
                        postfix +=pop_item.data
                    else:
                        stack.push(arg)
                else:
                    stack.push(arg)
            else:
                postfix += arg
        return postfix
    
    def postfix(self,expression):
        exp_len = len(expression)
        stack = Stack("(",exp_len)
        expression += ")"
        return self._postfix(stack,expression)
        
        
        
        


# In[ ]:




