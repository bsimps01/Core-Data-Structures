#need to start from the head
#go through each node, check the node after and
#see if there are duplicates
#set those duplicates to none
#we can print out the not duplicates

def remove_duplicates(self):
    current = self.head

    while current.next != None:

        if current.data == current.next.data:
            