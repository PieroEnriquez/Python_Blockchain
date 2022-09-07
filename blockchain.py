import datetime
from block import Block

block_chain = [Block.create_genesis_block()]

print("The genesis block has been created!")
print(f"Hash {block_chain[-1].hash}")

num_blocks_to_add = 10

for i in range(1, num_blocks_to_add + 1):
    block_chain.append(Block(block_chain[-1].hash, "Data", datetime.datetime.now()))
    
    print(f"Block {i} has been created.")
    print(f"Block hash: {block_chain[i].hash}")


