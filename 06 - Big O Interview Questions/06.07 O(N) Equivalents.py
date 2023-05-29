# Which of the following are equivalent to O(N)?
class Big_O:
    '''
    1. O(N + P), where P < N/2  -> equivalent to O(N)
    2. O(2N)                    -> equivalent to O(N)
    3. O(N + log N)             -> equivalent to O(N)
    4. O(N + N log N)           -> equivalent to O(N log N)
    5. O(N + M)                 -> equivalent to O(N + M)
    '''

if __name__ == "__main__":
    print(Big_O().__doc__)