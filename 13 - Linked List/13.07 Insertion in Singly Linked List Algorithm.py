class Linked_List:
    '''
    Insertion algorithm
      (Node value,location)  -> create a node and assign value -> head = None? -Yes-> head = node tail = node -> Terminate
      -No-> Location = first -No-> location=last -No-> Find location(loop) current.next = node node.next = nextNode -> Terminate
      location = first -Yes-> node.next = head head = node -> Terminate
      location=lat -Yes-> node.next = null last.next = node tail = node -> Terminate
    '''


if __name__ == "__main__":
    print(Linked_List().__doc__)