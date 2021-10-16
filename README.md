# IDC5602_Cyber
Cybersecurity a Multidisciplinary Approach.

This repo contains exercises and resources for the course.

# Exercise 1: Zip Password Cracking
In this exercise, we will use zip_password_cracker, protected_zips, and common_passwords to crack the passwords of encrypted zip files. Inside each zip file is a secret.txt file that contains a protected phrase. The goal is to learn how to run the password cracker python script, crack the target zip file's password, and decrypt the contents of the secret text file.

## Assignment Details
In Google Colab's Linux environment, crack the following zip file's password to uncover the contents of the secret.txt file. In the field below, type and submit secret.txt's text.

Encrypted Zip: https://bit.ly/protected1zip

Password Cracker Script: https://bit.ly/zip_password_cracker

**NOTE:** Save file with .py extension: zip_password_cracker.py

Common Password Dictionaries:
* https://bit.ly/common_passwords1
* https://bit.ly/common_passwords2
* https://bit.ly/common_passwords3
* https://bit.ly/common_passwords4
* https://bit.ly/common_passwords5

## Zip Password Cracker
Usage: python zip_cracker.py <zip_file> <word_list>

ex: python zip_cracker.py protected1.zip common_passwords1.txt

## Linux Commands
### Split Files into Partitions
Split by 10 MB (-b is bytes). Use m, k, or b:
split -b 10m common_passwords.txt split_prefix

Split by lines (-l is lines):
split -l 500 common_passwords.txt split_prefix

## WGET
Use -O to rename the incoming file:
wget -O new_file_name http://your_url.com

## All Commands
* sudo apt install unzip
* sudo apt install python3-pip
* pip install tqdm
* wget –O protected2.zip https://bit.ly/protected2zip
* wget –O zip_password_cracker.py https://bit.ly/zip_password_cracker
* wget –O common_passwords1.txt https://bit.ly/common_passwords1
* wget –O common_passwords2.txt https://bit.ly/common_passwords2
