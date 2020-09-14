# Example of Hash Data Structure Implementation in python

class Hash:
    def __init__(self):
        self.MAX = 10
        self.hash_table = [None for i in range(0, self.MAX)]

    def hash_function(self, key):
        count = 0
        for character in key:
            count += ord(character)
        return(count%self.MAX)

    def __setitem__(self, key, value):
        position = self.hash_function(key)
        self.hash_table[position] = value
        print("Successfully added value to hash table")

    def __getitem__(self, item):
        position = self.hash_function(item)
        print(self.hash_table[position])

    def __delitem__(self, key):
        position = self.hash_function(key)
        self.hash_table[position] = None
        print("Successfully deleted value to hash table")

if __name__ == "__main__":
    h_obj = Hash()
    h_obj["march 6"] = 5
    h_obj["march 7"] = 10
    h_obj["march 9"] = 15
    print(h_obj["march 6"])
    print(h_obj.hash_table)
    del h_obj["march 7"]
    print(h_obj.hash_table)
