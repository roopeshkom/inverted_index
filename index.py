from os import listdir

# Grabs words from files in given folder, and tracks their file and location in file
def collect_words(file_dir):
    files = listdir(file_dir)
    words = []

    for file in files:
        with open(f'{file_dir}/{file}', 'r') as f:
            text = f.read()
            words += map(lambda x: (x[1], file, x[0]),
                enumerate(text.split(' ')))
    
    return words

# Takes a word and returns list of contiguous substrings in the word
def get_contiguous_substrings(word):
    return [word[start : start+len(word)+1-num]
            for num in range(1, 1+len(word))[::-1]
            for start in range(num)] 


words = collect_words(file_dir='lorem_ipsum')
print(*words, sep='\n')
