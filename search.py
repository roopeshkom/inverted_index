from helpers.index import create_dictionary 

file_dir = input('Please enter a directory to search: ')
dictionary = create_dictionary(file_dir)
print(f'Creating search engine from files in {file_dir}...')

while True:
    results = []
    query = input('Please enter search: ')

    if query in dictionary:
        results = dictionary[query]
        print(f'{len(results)} results found containing "{query}":')
    else:
        print(f'No results found for "{query}".')

    for word, source, location in results:
        print(f'Word {location} in file {source}: {word}')

