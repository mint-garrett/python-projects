import collections
import itertools

#scan in dictionary as a list
word_list = []
for word in open("words.txt", mode = "r"):
    word_list.append(word.strip().lower())

#turn any word into a list of alphabetized strings
def signature(word):
    return ''.join(sorted(word))
#print(signature("kayak"))

#create a list of signatures
words_by_signature = collections.defaultdict(set)
for word in word_list:
    words_by_signature[signature(word)].add(word)

anagrams_by_signature = {sig: wordset for sig, wordset in words_by_signature.items() if len(wordset) >1}

#finds the anagram for any word by using the signature of the dict key
def find_anagram(word):
    try:
        return anagrams_by_signature[signature(word)]
    except KeyError:
        print("no anagrams for this word! sorry!")
#print(find_anagram("tac"))

#finds possible palindrome pairs
palindromes = []
def list_palindromes(dict):
    for anagram in dict.values():
        for word1, word2 in itertools.combinations(anagram, 2):
            if word1 == word2[::-1] and len(word1) == len(word2):
                words_oneandtwo = [word1, word2]
                palindromes.append(words_oneandtwo)
    return palindromes

def find_palindromes(word):
    possible_pal = list(word)
    if possible_pal == possible_pal[::-1]:
        print(f"{word} is a palindrome!")
    else:
        print(f"{word} is not a palindrome")
    

def main():
    
    print("welcome to the dictionary toy!\nPlease enter a word:")
    inp = input()
    print(f"you entered: {inp}. What would you like to learn about this word?")
    while(True):
        option = int(input("Options:\n1: Find this word's signature\n2: Find any anagrams of this word\n3: Find any palindromes of this word\n4: Show all palindromes\n5: Exit\n"))
        match(option):
            case 1:
                print(signature(inp))
            case 2:
                print(find_anagram(inp))
            case 3:
                print(find_palindromes(inp))
            case 4:
                print(list_palindromes(anagrams_by_signature))
            case 5:
                break

main()
