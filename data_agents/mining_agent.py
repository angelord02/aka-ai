import hashlib
import json
import datetime
import random

class MiningDataAgent:
    def __init__(self, name="AKA_MINING_AGENT_01"):
        self.name = name
        self.collected_data = []

    def fetch_raw_data(self):
        """Simulates fetching data from various industrial sources."""
        raw_sources = [
            {"source": "Geology_Feed", "content": "New lithium deposit found in Manono, DRC.", "value": 0.95},
            {"source": "Market_API", "content": "Price of Cobalt increased by 5% today.", "value": 0.8},
            {"source": "Sensor_Net", "content": "Operational efficiency at Mine X is at 88%.", "value": 0.6},
            {"source": "Spam_Source", "content": "Buy cheap gold now!", "value": 0.1},
        ]
        return raw_sources

    def filter_and_classify(self, raw_data):
        """Filters out low-relevance data and classifies it."""
        filtered = []
        for item in raw_data:
            if item['value'] > 0.5: # Threshold for industrial relevance
                item['timestamp'] = datetime.datetime.now().isoformat()
                item['classification'] = "INDUSTRIAL_INTELLIGENCE"
                filtered.append(item)
        return filtered

    def hash_data(self, data_item):
        """Creates a SHA-256 hash of the data item for blockchain verification."""
        data_string = json.dumps(data_item, sort_keys=True)
        return hashlib.sha256(data_string.encode()).hexdigest()

    def run_cycle(self):
        print(f"[{self.name}] Starting data collection cycle...")
        raw = self.fetch_raw_data()
        print(f"[{self.name}] Fetched {len(raw)} raw items.")

        filtered = self.filter_and_classify(raw)
        print(f"[{self.name}] Retained {len(filtered)} relevant items after filtering.")

        for item in filtered:
            data_hash = self.hash_data(item)
            item['hash'] = data_hash
            self.collected_data.append(item)
            print(f"[{self.name}] Processed item: {item['source']} | Hash: {data_hash[:10]}...")

        return filtered

if __name__ == "__main__":
    agent = MiningDataAgent()
    results = agent.run_cycle()
    print("\n--- Final Processed Data ---")
    print(json.dumps(results, indent=2))
