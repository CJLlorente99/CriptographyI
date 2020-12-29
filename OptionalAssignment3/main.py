from Crypto.Hash import SHA256

testPath = "./6.2.birthday.mp4_download"
assignmentPath = "./6.1.intro.mp4_download"

correcth0Test = "03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8"

def divideIntoChunks(path, CHUNK_SIZE=1024):
	res = []
	with open(path, 'rb') as f:
		chunk = f.read(CHUNK_SIZE)
		while chunk:
			res.append(chunk)
			chunk = f.read(CHUNK_SIZE)

		f.close()
	return res

if __name__ == "__main__":

	dividedTestData = divideIntoChunks(testPath)
	dividedAssignmentData = divideIntoChunks(assignmentPath)

	i = len(dividedTestData) - 1

	while i >= 0:
		hasher = SHA256.new()
		hasher.update(dividedTestData[i])
		if i != 0:
			dividedTestData[i-1] += hasher.digest()
		else:
			if int(hasher.hexdigest(),16) == int(correcth0Test,16):
				print("TEST PASSED h0Test was "  + correcth0Test)
			else:
				print("TEST FAILED")
				print("Calculated was " + hasher.hexdigest())
				print("but expected was " + correcth0Test + "\n")

		i -= 1

	i = len(dividedAssignmentData) - 1

	while i >= 0:
		hasher = SHA256.new()
		hasher.update(dividedAssignmentData[i])
		if i != 0:
			dividedAssignmentData[i-1] += hasher.digest()
		else:
			print("h0Assignment was "  + hasher.hexdigest())

		i -= 1
