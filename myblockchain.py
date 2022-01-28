import datetime
import hashlib

class myBlock:
    
    index = None
    chain = None

    def __init__(self):
        self.index = 0
        self.chain = []
        self.createBlock() #Create first block in chain
    
    def createBlock(self):
        
        #Proof always equals 1
        proof = 1

        #Date and Time
        time = datetime.datetime.now()
        time = time.strftime("%m/%d/%Y %H:%M:%S:%f")

        #Check if this is the first block in the chain for previous hash
        if self.index > 0:
            prev_hash = self.get_prev_block()
        else:
            prev_hash = 0

        block = {
            'index': self.index + 1,
            'timestamp': time,
            'proof': proof,
            'previous_hash': prev_hash
        }

        #Increase Index
        self.index += 1

        #Get new hash and append it to the block
        block['hash'] = (self.getHash(block))

        #print the whole block before appending it to the chain
        print("Dic:", block)

        #Append the blockChain
        self.chain.append(block)

    #Get the previous block in the chain
    def get_prev_block(self):
        last_block = self.chain[-1]
        last_block = last_block['hash']
        return last_block

    def getHash(self, data):
        status = False
        while status is False:
            hash = hashlib.sha256(str(data).encode()).hexdigest()
            if hash[:4] != '0000':
                data['proof'] += 1
            else:
                status = True

        return hash

b1  = myBlock()
x = 0
while x < 9:
    b1.createBlock()
    x += 1
