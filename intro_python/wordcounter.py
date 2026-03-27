#wordcounter

##example speech, this should work for every body of text
speech = """
The computer is something extraordinary.
It's going to probably take over our lives.
That's probably the new industry.
The computer will shape our lives.
It's already doing it quietly ... slowly. We're unaware of it.
We've talked to a great many of these experts, computer experts, for building it. They are not concerned with what happens to the human brain. You understand? They are concerned with creating it. Ah! Not creating it, building it. That's better word.
When the computer takes over ... our lives ... what happens to our brains?
They are better, far quicker, so rapid.
In a second they'll tell you a thousand memories. 
So when they take off, what's going to happen to our brains? Gradually wither? 
Or, be thoroughly employed in amusement ... in entertainment?
Please face all this, for God's sake, this is happening.
"""

##splits up text into a list containing each word
word_list = speech.split
##prints how many words there are in total
print(len(word_list()))

#creates empty list to fill
number_of_words = {}

##for loop that will go through each word to see how many times it is in the text
for word in word_list():
    if word in number_of_words:
        number_of_words[word] += 1
    else:
        number_of_words[word]=1


print(number_of_words)
