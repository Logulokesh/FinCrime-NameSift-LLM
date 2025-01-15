import ollama
import logging

logger = logging.getLogger(__name__)

class LLMAnalyzer:
    def __init__(self):
        self.model = "gemma3:12b"  # Ollama model
        self.host = "http://localhost:11434"  # Default Ollama host

    def analyze(self, name: str, matched_entity: dict) -> str:
        try:
            prompt = (
                f"Analyze the risk of an individual named '{name}' who matches a watchlist entry: "
                f"Unique ID: {matched_entity['unique_id']}, "
                f"Name: {matched_entity['name']}, "
                f"Date of Birth: {matched_entity['date_of_birth']}, "
                f"Risk Category: {matched_entity['risk_category']}. "
                f"Provide a brief explanation of why this match might indicate a risk."
            )
            response = ollama.generate(
                model=self.model,
                prompt=prompt,
                options={"temperature": 0.7}
            )
            explanation = response["response"].strip()
            logger.info(f"LLM analysis completed for {name}")
            return explanation
        except Exception as e:
            logger.error(f"LLM analysis failed: {str(e)}")
            return f"LLM analysis failed: {str(e)}"