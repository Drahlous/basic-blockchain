import time
import hashlib
import string
import random

########################
#   HELPER FUNCTIONS   #
########################

def get_prev_hash(block):
  return block[0]

def get_transaction_list(block):
  return block[1]

def get_self_hash(block):
  return block[2].hexdigest()

# Blocks are stored as tuples
# (previous_hash, transaction_list, self_hash)

# Create a new block
def create_block(hasher, transactions, prev_hash):
  prev_data = str(prev_hash) + transactions 
  hasher.update(prev_data.encode())
  return (prev_hash, transactions, hasher)

# Create the Genesis block
def create_genesis_block(hasher,transactions):
  return create_block(hasher, transactions, 0)



#############
#   START   #
#############

hasher = hashlib.sha256()

# Genesis
genesis_block = create_genesis_block( hasher, "Hello world :)")

# Print hash of the genesis block
genesis_block_hash = get_self_hash(genesis_block)
print("genesis_block_hash: ", genesis_block_hash)

# Initialize previous_block data
previous_block = genesis_block

# Loop Forever
while True:

  # Let transactions be a 100-character string of random letters and numbers
  new_transactions = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(100))

  # Create a new block
  new_block = create_block(hasher, new_transactions, get_self_hash(previous_block))

  # Print block data
  print("\n\n\n" + "-"*100)
  print("previous_hash:     ", get_prev_hash(new_block))
  print("new_transactions:  ", get_transaction_list(new_block))
  print("new_hash:          ", get_self_hash(new_block))
  print("-"*100)

  # Update with new block information
  previous_block = new_block 
  time.sleep(1)
