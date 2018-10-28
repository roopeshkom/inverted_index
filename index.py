from os import listdir

def collect_words(file_dir):
    files = listdir(file_dir)
    words = []

    for file in files:
        with open(f'{file_dir}/{file}', 'r') as f:
            text = f.read()
            words += list(map(lambda x: (x[1], file, x[0]), enumerate(text.split(' '))))
    
    return words

def get_contiguous_substrings(word):
    return [word[start : start+len(word)+1-num] for num in range(1, 1+len(word))[::-1] for start in range(num)] 


print(get_contiguous_substrings('hello'))

#words = collect_words(file_dir='lorem_ipsum')
#print(*words, sep='\n')
