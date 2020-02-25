from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        # self.size = 0
        self.storage = {}
        self.cache = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # * If the key exists in storage
        if key in self.storage:
            # * Find the item in the DLL and move to the head
            current_node = self.cache.head
            for i in range(0, self.cache.length):
                if key in current_node.value:
                    self.cache.move_to_front(current_node)
                i += 1
                current_node = current_node.next
            # * Return the value
            return self.storage[key]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # * Create new variable representing the entry
        entry = {key: value}
        # * If the size of the DLL is equal to limit, identify the Tail in a variable, remove it from the DLL and remove it from Storage dict
        # * Check if key already exists in dict
        if key in self.storage.keys():
            self.storage.update(entry)
            # * Update in cache by finding its location and updating
            current_node = self.cache.head
            for i in range(0, self.cache.length):
                if key in current_node.value:
                    current_node.value = entry
                    return entry
                i += 1

        else:
            if self.cache.length == self.limit:
                # * delete tail
                tail = self.cache.remove_from_tail()
                tail_key = next(iter(tail))
                # * find tail reference in dict and remove
                del self.storage[tail_key]
                # * Add to the dict
            self.storage.update(entry)
            # * Add to head of DLL
            self.cache.add_to_head(entry)
