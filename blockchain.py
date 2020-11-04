import hashlib
import json
from time import time 


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.cuurent_transactions = []
        # create the genesis block
        self.new_block(previous_hash = 1, proof = 100)

    def new_block(self, proof, previous_hash=None):
        """
        Create a new block in the BlockChain 
        :param proof: <str> Hash of previous Block
        :return: <dict> New Block
        """
        block = {'index': len(self.chain) + 1, 'timestamp': time(), 'transactions': self.current_transactions, 'proof': proof, 'previous_hash': previous_hash or self.hash(self.chain[-1]), }
        # reset the current list of transactions
        self.current_transactions  = []
        self.chain.append(block)
        return block 

    def new_transaction(self, sender, recipient, amount):
    
        """
        Creates as new transaction to go into the next mined block
        param sender : <str> Address of the sender 
        param recipient: <str> Address of the Recipient
        param amount: <int> Amount
        return: <int> The index of the block that will hold this transaction
        """
        self.cuurent_transactions.append[{'sender': sender , 'recipient' : recipient, 'amount': amount, }]
        return self.last_block['index'] + 1 

    @staticmethod 
    def has(block):
        #hashes a Block
        pass 

    @property
    def last_block(self):
        #returns the last block in the chain
        pass

        