from Crypto.Cipher import AES
from Crypto.Util import Counter

key = bytes.fromhex("36f18357be4dbd77f050515c73fcf9f2")
c0 = bytes.fromhex("0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329")
IV0 = int("69dda8455c7dd4254bf353b773304eec", 16)
c1 = bytes.fromhex("e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451")
IV1 = int("770b80259ec33beb2561358a9f2dc617", 16)

if __name__ == "__main__":
	ctr0 = Counter.new(128, initial_value=IV0)
	encrypter0 = AES.new(key, AES.MODE_CTR, counter=ctr0)
	m0 = encrypter0.decrypt(c0)
	print(m0)
	ctr1 = Counter.new(128, initial_value=IV1)
	encrypter1 = AES.new(key, AES.MODE_CTR, counter=ctr1)
	m1 = encrypter1.decrypt(c1)
	print(m1)