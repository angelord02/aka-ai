import hashlib
import json
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class MockIndustrialChain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block - Industrial AI Network", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        index = len(self.chain)
        timestamp = time.time()
        previous_hash = self.get_latest_block().hash
        new_block = Block(index, timestamp, data, previous_hash)
        self.chain.append(new_block)
        return new_block

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def display_chain(self):
        for block in self.chain:
            print(f"Block {block.index} [{block.hash[:10]}...]")
            print(f"  Timestamp: {block.timestamp}")
            print(f"  Data: {block.data}")
            print(f"  Previous Hash: {block.previous_hash[:10]}...")
            print("-" * 30)

if __name__ == "__main__":
    blockchain = MockIndustrialChain()

    print("Adding APK Metadata to blockchain...")
    blockchain.add_block({"type": "APK_REGISTRATION", "name": "AKA Mining Pro", "version": "1.0.0"})

    print("Adding Industrial Data Provenance to blockchain...")
    blockchain.add_block({
        "type": "DATA_PROVENANCE",
        "agent": "AKA_MINING_AGENT_01",
        "data_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    })

    blockchain.display_chain()
    print(f"Is Blockchain Valid? {blockchain.is_chain_valid()}")
