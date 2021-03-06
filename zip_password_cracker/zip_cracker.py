# Zip file password cracker.
# Requirements: pip3 install tqdm
# Requirements: Word list: https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
# Usage: python zip_cracker.py <zip_file> <word_list>
# Source: https://www.thepythoncode.com/code/crack-zip-file-password-in-python
# Details: https://www.thepythoncode.com/article/crack-zip-file-password-in-python

# Import libraries
from tqdm import tqdm
import zipfile
import sys

# the password list path you want to use
wordlist = sys.argv[2]

# the zip file you want to crack its password
zip_file = sys.argv[1]

# initialize the Zip File object
zip_file = zipfile.ZipFile(zip_file)

# count the number of words in this wordlist
n_words = len(list(open(wordlist, "rb")))

# print the total number of passwords
print("Total passwords to test:", n_words)

# Use the wordlist to attempt to open the zip
with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("[+] Password found:", word.decode().strip())
            exit(0)

print("[!] Password not found, try other wordlist.")
