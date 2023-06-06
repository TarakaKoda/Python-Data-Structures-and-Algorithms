class Linked_List:
    '''
    Insertion algorithm
      (Node value,location)  -> create a node and assign value -> head = None? -Yes-> node.next = node, head = node, tail = node -> Terminate
      -No-> Location = first -No-> location=last -No-> Find location(loop) current.next = node node.next = nextNode -> Terminate
      location = first -Yes-> node.next = head, head = node, tail.next = node -> Terminate
      location = last -Yes-> last.next = node, tail = node, node.next = head -> Terminate
    '''


if __name__ == "__main__":
    print(Linked_List().__doc__)