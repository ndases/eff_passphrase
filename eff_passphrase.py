import os
import urllib.request
from random import randint

ENDPOINT = 'https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt'

def download_wordlist():
    urllib.request.urlretrieve(ENDPOINT, 'wordlist.txt')

def get_wordlist():
    with open('wordlist.txt') as f:
        lines = f.read().splitlines()
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
    if count == 0:
        count = 6
    for p in range(count):
        idx = generate_word_numbers()
        passphrase = passphrase+get_word_by_index(idx)  
    
    return passphrase

def main():
    if not os.path.exists('wordlist.txt'):
        download_wordlist()
        print(build_pasphrase(6))
    else:
        print(build_pasphrase(6))

if __name__ == "__main__":
    main()