from Crypto.Cipher import AES

key = bytes.fromhex("140b41b22a29beb4061bda66b6747e14")
c0 = bytes.fromhex("28a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81")
IV0 = bytes.fromhex("4ca00ff4c898d61e1edbf1800618fb28")
c1 = bytes.fromhex("b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253")
IV1 = bytes.fromhex("5b68629feb8606f9a6667670b75b38a5")

if __name__ == "__main__":
	encrypter0 = AES.new(key, AES.MODE_CBC, IV0)
	m0 = encrypter0.decrypt(c0)
	print("Ciphertext 0 length is " + str(len(c0)))
	print(m0)
	encrypter1 = AES.new(key, AES.MODE_CBC, IV1)
	m1 = encrypter1.decrypt(c1)
	print("Ciphertext 1 length is " + str(len(c1)))
	print(m1)