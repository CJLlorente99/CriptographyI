import urllib.parse
import urllib.error
import urllib.request
import sys

toDecrypt = "f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4"

# CBC with random IV
# First 16 bytes are the unencrypted IV
# Then blocks are 16 bytes wide

TARGET = 'http://crypto-class.appspot.com/po?er='
#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib.parse.quote(q)    # Create query URL
        req = urllib.request.Request(target)         # Send HTTP request to server
        try:
            f = urllib.request.urlopen(req)          # Wait for response
        except urllib.error.HTTPError as e:          
            # print("We got: " + str(e.code))       # Print response code
            if e.code == 404:
                print("Good padding found!")
                return True # good padding
            return False # bad padding

def divide(something):
    
    res = []
    i = 0
    chunk = something[0:2*16 -1]

    while chunk:
        i += 2*16
        chunk = something[i:i+2*16] # all chunks must be the same size (for AES CBC compliance)
        res.append(chunk)

    return res

def stickTogether(nBlock, stringReplaced, strings, IV):
    res = IV
    for i in range(len(strings)):
        if i == nBlock:
            res += stringReplaced
        else:
            res += strings[i]
    return res

if __name__ == "__main__":
    
    po = PaddingOracle()

    IV = toDecrypt[0:2*16]

    blocks = divide(toDecrypt)

    guessedMessage = []

    for n in range(len(blocks)-1, -1,-1):

        block = blocks[n]
        guessedBlock = []
        print(block)
        padding = []

        for i in range(len(block)-1,-1,-2): # 2 hex digits per byte

            for j in range(256):

                gGuess = "{0:#0{1}x}".format(j,4)[2:]
                newTry = block[0:i-1] + gGuess + "".join(padding)
                if len(newTry) != 32:
                    print("new try size is " + str(len(newTry)))

                if po.query(stickTogether(n,newTry,blocks, IV)):
                    guessedBlock.insert(0,gGuess)
                    padding = []

                    for k in range(0, len(block)-i, 2):

                        padding.append("{0:#0{1}x}".format(len(block)-i,4)[2:])

                    block = block[0:i-1] + "".join(padding)
                    print(block)
                    print(len(block))
                    print("Guessed block is\n" + "".join(guessedBlock))
                    break

                else:

                    if j == 255:
                        print("Error guessing in position " + str(i) + " and " + str(i+1) + " in block num " + str(n))
                        exit()

        guessedMessage.insert(0,"".join(guessedBlock))

    # once every block is guessed. Deal with first block (brute force?)

    for i in range(2**(8*16)):

        if po.query(stickTogether(0, hex(i)[2:], blocks, IV)):

            guessedMessage[0] = hex(i)[2:]
            break

    print("".join(guessedMessage).decode("hex"))
