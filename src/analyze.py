import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
import json

def calculate_entropy(counts):
    total = sum(counts.values())
    if total == 0:
        return 0
    probs = [c/total for c in counts.values()]
    return -sum(p * np.log2(p) for p in probs)

def main():
    print("Loading data...")
    df = pd.read_json("results/generated_narratives.json")
    
    results_summary = []
    
    conditions = df['model_condition'].unique()
    
    # Vocabulary & Entropy Analysis
    for cond in conditions:
        cond_data = df[df['model_condition'] == cond]
        
        all_preps = []
        for preps in cond_data['prepositions']:
            all_preps.extend(preps)
        
        prep_counts = Counter(all_preps)
        entropy = calculate_entropy(prep_counts)
        
        avg_sent_len = cond_data['avg_sent_length'].mean()
        avg_sent_var = cond_data['var_sent_length'].mean()
        
        results_summary.append({
            "Condition": cond,
            "Prep_Entropy": entropy,
            "Avg_Sent_Length": avg_sent_len,
            "Avg_Sent_Variance": avg_sent_var,
            "Total_Preps": len(all_preps),
            "Unique_Preps": len(prep_counts)
        })
    
    summary_df = pd.DataFrame(results_summary)
    print("\n--- Summary Statistics ---")
    print(summary_df.to_string(index=False))
    
    summary_df.to_csv("results/summary_statistics.csv", index=False)
    
    # Plotting
    sns.set_theme(style="whitegrid")
    
    # 1. Preposition Entropy
    plt.figure(figsize=(10, 6))
    sns.barplot(data=summary_df, x="Condition", y="Prep_Entropy")
    plt.title("Spatial Preposition Entropy (Vocabulary Diversity)")
    plt.ylabel("Entropy (bits)")
    plt.savefig("figures/prep_entropy.png")
    plt.close()
    
    # 2. Sentence Variance
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x="model_condition", y="var_sent_length")
    plt.title("Sentence Length Variance Distribution")
    plt.ylabel("Variance in Sentence Length")
    plt.savefig("figures/sent_variance.png")
    plt.close()
    
    # 3. Pos N-grams
    # Find most common bigrams of POS tags
    print("\n--- Top POS Bigrams ---")
    for cond in conditions:
        cond_data = df[df['model_condition'] == cond]
        bigrams = []
        for tags in cond_data['pos_tags']:
            bigrams.extend([(tags[i], tags[i+1]) for i in range(len(tags)-1)])
        
        bigram_counts = Counter(bigrams)
        print(f"\nCondition: {cond}")
        for bg, count in bigram_counts.most_common(5):
            print(f"  {bg}: {count}")

    # Generate a brief markdown report of the stats to use in the final REPORT.md
    with open("results/stats_report.md", "w") as f:
        f.write("## Statistical Analysis Results\n\n")
        f.write(summary_df.to_markdown(index=False))

if __name__ == "__main__":
    main()