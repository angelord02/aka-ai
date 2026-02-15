from .mining_agent import MiningDataAgent
import json

class SportDataAgent(MiningDataAgent):
    """Specialized agent for the Sport industry APK (hosted on Firebase)."""

    def __init__(self, name="AKA_SPORT_AGENT_01"):
        super().__init__(name)

    def fetch_raw_data(self):
        """Simulates fetching sports performance and industry data."""
        return [
            {"source": "Firebase_Sport_APK", "content": "Athlete performance metrics in Lagos stadium.", "value": 0.9},
            {"source": "Sport_News", "content": "Investment in African football academies rising.", "value": 0.85},
            {"source": "General_News", "content": "Weather is sunny.", "value": 0.2}
        ]

if __name__ == "__main__":
    # Import adjustment for standalone run
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from data_agents.mining_agent import MiningDataAgent

    agent = SportDataAgent()
    results = agent.run_cycle()
    print("\n--- Sport Processed Data ---")
    print(json.dumps(results, indent=2))
