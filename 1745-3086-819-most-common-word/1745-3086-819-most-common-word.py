class Solution:
    def mostCommonWord(self, paragraph, banned):
        # Step 1: Handling Banned Words
        ban = set(banned)

        # Step 2: Word Frequency Count
        word_frequency = defaultdict(int)
        # Process the paragraph
        paragraph = paragraph.lower()
        paragraph = re.sub(r'[^a-zA-Z]', ' ', paragraph)
        
        words = paragraph.split()
        for word in words:
            # Check if the word is not in the banned set
            if word not in ban:
                # Update the frequency in the dictionary
                word_frequency[word] += 1

        # Step 3: Remove Empty String Entry
        word_frequency.pop("", None)

        # Step 4: Finding Most Common Word
        result = ""
        max_frequency = 0
        for word, frequency in word_frequency.items():
            # Update result if the current word has a higher frequency
            if not result or frequency > word_frequency[result]:
                result = word

        # Return the most common word
        return result