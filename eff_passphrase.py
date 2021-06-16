import requests
from random import randint

ENDPOINT = 'https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt'

def get_wordlist():
    r = requests.get(ENDPOINT)
    lines = list(filter(None, r.text.split('\n')))
    wordlist = {}
    for line in lines:
        idx, ele = line.split('\t')
        wordlist[idx] = ele
        
    return wordlist
            

def generate_word_numbers():
    word_value = ''
    for p in range(0, 5):
        number = randint(1, 6)
        word_value = word_value+str(number)
    
    return word_value

def get_word_by_index(word_id):
    wordlist = get_wordlist()
    
    return wordlist[word_id]
    
def build_pasphrase(count):
    passphrase = ''
    if count is 0:
        count = 6
    for p in range(count):
        idx = generate_word_numbers()
        passphrase = passphrase+get_word_by_index(idx)  
    
    return passphrase

def main():
    print(build_pasphrase(6))


if __name__ == "__main__":
    main()