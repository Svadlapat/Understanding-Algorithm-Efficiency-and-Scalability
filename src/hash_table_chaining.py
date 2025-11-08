class HashTable:
    def __init__(self, initial_capacity=10, load_factor_threshold=0.75):
        self.capacity = initial_capacity        # number of buckets
        self.size = 0                           # number of key-value pairs stored
        self.table = [[] for _ in range(self.capacity)]
        self.load_factor_threshold = load_factor_threshold

    def hash_function(self, key):
        """Universal hashing (good for strings & numbers)"""
        return hash(key) % self.capacity

    def _rehash(self):
        """Double the table capacity and reinsert all keys"""
        old_table = self.table
        self.capacity *= 2
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0  # reset size and reinsert to count again

        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

    def insert(self, key, value):
        index = self.hash_function(key)
        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value  # update existing key
                return

        bucket.append([key, value])
        self.size += 1

        if self.get_load_factor() > self.load_factor_threshold:
            self._rehash()

    def search(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[i]
                self.size -= 1
                return True
        return False

    def get_load_factor(self):
        return self.size / self.capacity

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")


if __name__ == "__main__":
        h = HashTable(initial_capacity=5)

        print("\n--- Inserting Elements ---")
        h.insert("apple", 100)
        h.insert("banana", 200)
        h.insert("grape", 300)
        h.insert("orange", 400)
        h.insert("melon", 500)
        h.insert("lemon", 600)  # will trigger resize

        h.display()
        print("\nLoad Factor:", h.get_load_factor())

        print("\n--- Searching ---")
        print("Search apple:", h.search("apple"))
        print("Search banana:", h.search("banana"))
        print("Search mango:", h.search("mango"))

        print("\n--- Deleting ---")
        print("Delete banana:", h.delete("banana"))
        print("Search banana:", h.search("banana"))

        print("\nFinal Hash Table:")
        h.display()
