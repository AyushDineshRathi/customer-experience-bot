import sys
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

# 1. Initialize the Engines
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

def mask_pii(text: str):
    # Define EXACTLY what we want to catch.
    # This prevents it from guessing "UK_NHS" or "US_DRIVER_LICENSE"
    target_entities = ["PERSON", "PHONE_NUMBER", "EMAIL_ADDRESS"]
    
    # Step A: Analyze with restrictions
    results = analyzer.analyze(
        text=text, 
        language='en',
        entities=target_entities  # <--- This is the fix
    )

    # Step B: Anonymize
    anonymized_result = anonymizer.anonymize(
        text=text,
        analyzer_results=results
    )

    return anonymized_result.text

# --- TESTING BLOCK ---
if __name__ == "__main__":
    user_input = "Hi, I'm Deepak. My number is 987-654-3210 and email is deepak@gmail.com. I'm cold."
    
    print(f"Original: {user_input}")
    print("-" * 50)
    
    clean_text = mask_pii(user_input)
    
    print(f"Sanitized: {clean_text}")
    print("-" * 50)
    
    # Verification Logic
    # We check if the real data is gone AND if the correct tags are present
    if "987-654-3210" not in clean_text and "<PHONE_NUMBER>" in clean_text:
        print("✅ SUCCESS: PII successfully masked and correctly labeled.")
    else:
        print(f"❌ FAILURE: Output was: {clean_text}")