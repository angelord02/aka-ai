import json
import hashlib

class DataFilter:
    """Filters and classifies massive industrial data for targeted training."""

    def __init__(self):
        self.categories = {
            "DEFENSE": 0.8,
            "MINING": 0.7,
            "FINANCE": 0.75,
            "SPORT": 0.5 # Added for multi-industry expansion
        }

    def score_content(self, content):
        """Simple scoring logic based on keywords."""
        content = content.lower()
        scores = {}

        keywords = {
            "DEFENSE": ["security", "defense", "intelligence", "border", "sahel"],
            "MINING": ["lithium", "cobalt", "geology", "mine", "rare earth"],
            "FINANCE": ["defi", "finance", "payment", "bank", "currency"],
            "SPORT": ["sport", "football", "athlete", "stadium", "performance"]
        }

        for cat, kw_list in keywords.items():
            count = sum(1 for kw in kw_list if kw in content)
            scores[cat] = count / len(kw_list) if kw_list else 0

        return scores

    def classify(self, data_item):
        """Classifies a data item based on the highest score."""
        scores = self.score_content(data_item.get('content', ''))
        best_cat = max(scores, key=scores.get)

        if scores[best_cat] > 0:
            data_item['classification'] = best_cat
            data_item['relevance_score'] = scores[best_cat]
            return data_item
        else:
            data_item['classification'] = "UNCATEGORIZED"
            data_item['relevance_score'] = 0
            return data_item

if __name__ == "__main__":
    filter_sys = DataFilter()
    sample_data = {"content": "New lithium exploration in the Sahel region for mineral security."}
    result = filter_sys.classify(sample_data)
    print(json.dumps(result, indent=2))
