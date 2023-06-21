class Trie:
    '''
    Common Operations on trie data structure
    - Creation of trie
    - Insertion in trie
    - Search for a string in trie
    - Deletion from trie


       Creation of trie
    Blank logical node
    Physically
              Map
    Characters | Link to trie node
               |
               |
               |
          End of string Yes/No
    Timr O(1) Space O(1)

    Insert a string in a Trie:
    Case 1: A Trie is Blank
    APP -
        Dict                          Dict                      Dict                     Dict
    char    Link to trie         char    Link to trie      char    Link to trie     char    Link to trie
     A           ------->         p           ------->     p           ------->


     End of string - No           End of string - No       End of string - No       End of string - Yes
    Case 2: new String's prefix is common to another strings prefix
     - API
    Case 3: New string's prefix is already present as complete string
    - APIS
    case 4: String to be inserted is already present in Trie
    - APIS
    Time O(n) Space - O(n)

    Search for a string in Trie
    Case 1: String does not exist in Trie
    Return : The string does not exist in Trie
    Case 2: String exits in the Trie
    Return: True
    Case 3: String is a prefix of another string, but it does not exist in Trie
    Return: False
    Time O(n) Space - O(1)

    Delete a string from Trie
    Case 1: Some other prefix of string is same as the one that we want to delete(API,APPLE)
    Case 2: The string is a prefix of another string(API,APIS)
    case 3: Other string is a prefix of the string(APIs,AP)
    case 4: Not any node depends on this string
    '''


if __name__ == "__main__":
    print(Trie().__doc__)
