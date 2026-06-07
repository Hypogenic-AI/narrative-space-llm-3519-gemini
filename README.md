# Narrative Space in LLMs

## Project Overview
This project investigates whether Large Language Models (LLMs) exhibit a unique, artificial "spatial grammar" when generating narratives about spatial navigation. By comparing default LLM outputs against "human-prompted" generations across different models, we aim to quantify the structural and vocabulary biases inherent in how LLMs textually represent physical space.

## Key Findings
- **Vocabulary Constraint:** Default LLM prompts yield very low spatial preposition entropy (3.41 bits for `gpt-4o`), relying heavily on a small set of generic spatial terms.
- **Structural Rigidity:** LLM-generated spatial stories exhibit highly formulaic sentence lengths (variance of ~5.5) compared to explicit human-like prompts (variance of 8.98).
- **Lack of Sensory Detail:** The default POS structure of LLM spatial narratives heavily favors pure topological movements `(PRON, VERB)` and `(ADP, DET)` without utilizing descriptive adjectives, unless explicitly prompted.

## File Structure
- `datasets/babi_task19/`: Cached dataset for environment layouts.
- `src/experiment.py`: Main generation script calling OpenAI APIs.
- `src/analyze.py`: NLP feature extraction and plotting script.
- `results/`: Contains generated JSON data and summary CSVs.
- `figures/`: Contains data visualizations for entropy and variance.
- `REPORT.md`: Comprehensive research report detailing the methodology, results, and discussion.
- `planning.md`: The research design and hypothesis decomposition.

## How to Reproduce
1. Ensure you have an `OPENAI_API_KEY` set in your environment.
2. Set up the Python virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate
   uv pip install -r requirements.txt # (or install dependencies manually as listed in src/experiment.py)
   python -m spacy download en_core_web_sm
   ```
3. Run the generation script:
   ```bash
   python src/experiment.py
   ```
4. Run the analysis and generate figures:
   ```bash
   python src/analyze.py
   ```

For full details, please refer to [REPORT.md](./REPORT.md).