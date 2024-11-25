import time

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.memo = {}

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def can_form_word(self, word, is_original_word):
        # If we've already computed the result for this word, return it from the cache
        if word in self.memo:
            return self.memo[word]

        node = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in node.children:
                self.memo[word] = False
                return False
            node = node.children[char]
            # If we reach the end of a word, recursively check the rest of the string
            if node.is_end_of_word:
                if i == len(word) - 1:  # Entire word is a valid compound
                    return not is_original_word
                if self.can_form_word(word[i + 1:], False):
                    self.memo[word] = True
                    return True
        
        self.memo[word] = False
        return False

def find_longest_compound_words(words):
    trie = Trie()

    # Insert all words into the Trie
    for word in words:
        trie.insert(word)

    words.sort(key=len, reverse=True)

    longest = ""
    second_longest = ""
    for word in words:
        if trie.can_form_word(word, True):
            if not longest:
                longest = word
            elif not second_longest:
                second_longest = word
            if longest and second_longest:
                break

    return longest, second_longest

if __name__ == "__main__":
    start_time = time.time()

    input_file = "Input_01.txt"  # Change this for Input_01.txt
    with open(input_file, "r") as file:
        words = [line.strip() for line in file.readlines()]

    longest, second_longest = find_longest_compound_words(words)

    end_time = time.time()
    time_taken = int((end_time - start_time) * 1000)

    print(f"Longest Compound Word: {longest}")
    print(f"Second Longest Compound Word: {second_longest}")
    print(f"Time taken to process {input_file}: {time_taken} milliseconds")
