import random

doc = 'transphobia.txt'

try:
    with open(doc, 'r') as file:
        doc_contents = file.read()
        words = doc_contents.split()
        num_words = random.randint(1, 1000)
        num_words = min(num_words, len(words))
        random_words = random.sample(words, num_words)
        payload = ' '.join(random_words)
        
        print(payload)
            
except FileNotFoundError:
    print(f"The file '{doc}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")