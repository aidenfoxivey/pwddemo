from backports.pbkdf2 import pbkdf2_hmac, compare_digest
import os
import getpass

salt = os.urandom(32)
iterations = 100000

def main():
	# create the existing password
	existing_pwd()

	newpwd = getpass.getpass("Please input your password.\t")
	new_hash = hash_new(newpwd, salt)
			   
		# test for equality of the passwords
	if (compare_digest(new_hash, existing_pwd())):
		print("Excellent, passwords match!")
	else:
		print("Unfortunately, passwords don't match... :(")

def existing_pwd():
	password = 'password123'
	# num of times we run the algorithm
	
	# the hash is stored somewhere from here
	return pbkdf2_hmac(
			'sha256',
			password.encode('utf-8'),
			salt,
			iterations,
			)

def hash_new(password, salt):
	return pbkdf2_hmac(
			'sha256',
			password.encode('utf-8'),
			salt,
			iterations,
			)

main()