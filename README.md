# IDC5602_Cyber
Cybersecurity a Multidisciplinary Approach.

This repo contains exercises and resources for the course.

# Exercise 1: Zip Password Cracking
In this exercise, we will use zip_password_cracker, protected_zips, and common_passwords to crack the passwords of encrypted zip files. Inside each zip file is a secret.txt file that contains a protected phrase. The goal is to learn how to run the password cracker python script, crack the target zip file's password, and decrypt the contains of the secret text file.

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
