import datetime
import hashlib

class Block:
    def __init__(self, previous_block_hash, transaction_list, timestamp):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        self.timestamp = timestamp
        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.hash = self.get_hash()
    
    @staticmethod
    def create_genesis_block():
        return Block("0", "0", datetime.datetime.now())

    def get_hash(self):
        header_bin = (str(self.previous_block_hash) + str(self.transaction_list) + str(self.timestamp)).encode()
        
        inner_hash = hashlib.sha256(header_bin).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest().encode()
        return outer_hash


