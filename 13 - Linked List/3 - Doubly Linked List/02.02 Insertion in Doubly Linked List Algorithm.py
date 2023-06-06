class Linked_List:
    '''
    Insertion algorithm
      (Node value,location)  -> create a node and assign value -> head = None? -Yes-> node.next = None, node.previous = None head = node, tail = node -> Terminate
      -No-> Location = first -No-> location=last -No-> Find location(loop) current.next = node node.next = nextNode, node.previous = current, nextNode.previous = node-> Terminate
      location = first -Yes-> node.next = head,head.previous = node, head = node, node.previous = None -> Terminate
      location = last -Yes-> last.next = node, node.previous = last, tail = node, node.next = None-> Terminate
    '''


if __name__ == "__main__":
    print(Linked_List().__doc__)