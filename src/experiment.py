import os
import json
import random
import numpy as np
import pandas as pd
from datasets import load_from_disk
from openai import OpenAI
import spacy
import nltk
from tqdm import tqdm

# Reproducibility
random.seed(42)
np.random.seed(42)

def main():
    print("Loading NLP tools...")
    nlp = spacy.load("en_core_web_sm")
    
    print("Loading dataset...")
    ds = load_from_disk("datasets/babi_task19")
    test_data = ds['test']
    
    # Sample 50 examples
    sampled_indices = random.sample(range(len(test_data)), 50)
    sampled_data = [test_data[i] for i in sampled_indices]
    
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    
    def generate_story(model, passage, start, end, style="standard"):
        if style == "standard":
            prompt = f"Here is a spatial layout:\n{passage}\nWrite a short narrative (3-5 sentences) describing your journey from the {start} to the {end}. Focus on the movement."
        else:
            prompt = f"Here is a spatial layout:\n{passage}\nWrite a creative, highly varied, and human-like story (3-5 sentences) describing a character's journey from the {start} to the {end}. Avoid robotic, formulaic sentence structures."
            
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=150,
                seed=42
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error: {e}")
            return ""

    results = []
    models_to_test = [
        ("gpt-4o-mini", "standard"),
        ("gpt-4o-mini", "human_prompt"),
        ("gpt-4o", "standard")
    ]
    
    print("Generating stories...")
    for i, example in enumerate(tqdm(sampled_data)):
        passage = example['passage']
        q = example['question']
        
        parts = q.replace("How do you go from the ", "").replace("?", "").split(" to the ")
        if len(parts) == 2:
            start, end = parts
        else:
            start, end = "starting point", "destination"
            
        for model, style in models_to_test:
            story = generate_story(model, passage, start, end, style)
            
            # NLP feature extraction
            doc = nlp(story)
            pos_tags = [token.pos_ for token in doc]
            spatial_adps = [token.text.lower() for token in doc if token.pos_ == 'ADP']
            
            sents = nltk.sent_tokenize(story)
            sent_lengths = [len(s.split()) for s in sents]
            
            results.append({
                "example_id": i,
                "model_condition": f"{model}_{style}",
                "start": start,
                "end": end,
                "story": story,
                "pos_tags": pos_tags,
                "prepositions": spatial_adps,
                "num_sentences": len(sents),
                "avg_sent_length": np.mean(sent_lengths) if sent_lengths else 0,
                "var_sent_length": np.var(sent_lengths) if sent_lengths else 0
            })
            
    df = pd.DataFrame(results)
    df.to_json("results/generated_narratives.json", orient="records", indent=2)
    print("Saved generated narratives to results/generated_narratives.json")

if __name__ == "__main__":
    main()