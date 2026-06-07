# Research Plan: Narrative Space in LLMs

## Motivation & Novelty Assessment

### Why This Research Matters
Understanding how Large Language Models (LLMs) conceptualize and describe spatial environments is critical as these models are increasingly integrated into robotics, virtual environments, and interactive storytelling. If LLMs exhibit a unique, artificial "spatial grammar," it could lead to navigation errors, unnatural human-computer interactions, and a lack of grounding in physical reality.

### Gap in Existing Work
Current research heavily focuses on evaluating LLMs' spatial reasoning through QA tasks like StepGame and bAbI, or via linear probing of internal representations (e.g., Martorell et al.). However, there is a significant gap in analyzing the *generative* side of spatial reasoning: how LLMs structure narrative text when spontaneously describing movement through a spatial environment, and how this contrasts with human narrative patterns.

### Our Novel Contribution
This research introduces a novel generative evaluation approach. Instead of asking LLMs to solve spatial puzzles, we prompt them to generate spatial narratives based on given layouts or open-ended navigation tasks. We will analyze these generated narratives for characteristic "LLM spatial grammar" (e.g., predictable sentence structures, over-reliance on specific spatial prepositions, or unnatural transitions), analogous to the recognizable "RLHF tone" found in standard text generation.

### Experiment Justification
- **Experiment 1 (Spatial Generation from Layouts):** Prompt LLMs to describe a path through a predefined layout (from bAbI Task 19). This is needed to control the ground-truth space and observe how models translate rigid spatial relations into narrative form.
- **Experiment 2 (Linguistic Feature Analysis):** Analyze the generated texts (part-of-speech tagging, transition words, sentence length variance) to identify the systematic deviations or "grammar" specific to LLM spatial narratives.
- **Experiment 3 (Cross-Model Comparison):** Compare outputs from different model families (e.g., OpenAI vs Anthropic) to determine if this "spatial grammar" is universal across RLHF models or specific to certain training paradigms.

---

## Research Question
Do Large Language Models exhibit a distinct and systematic "grammar" or structural pattern when generating narratives about spatial navigation, diverging from typical human narrative structures?

## Background and Motivation
While LLMs can solve simple multi-hop spatial reasoning tasks (often requiring hybrid symbolic approaches for complex spaces), their generative spatial capabilities remain largely unexamined. Observations of RLHF-trained models suggest they develop characteristic linguistic patterns. We hypothesize that similar artificial constraints exist in their representation of physical space in narrative, which may impact their utility in embodied AI and creative generation.

## Hypothesis Decomposition
1. **H1 (Vocabulary Bias):** LLMs over-utilize a narrow set of spatial transition phrases (e.g., "proceeded," "navigated," "turned") compared to more varied human descriptions.
2. **H2 (Structural Rigidity):** LLMs produce spatial narratives with lower sentence structure variance (e.g., repeated Subject-Verb-Direction patterns).
3. **H3 (Abstract vs Concrete):** LLM narratives prioritize explicit topological relations over sensory/experiential descriptions of space unless explicitly prompted.

## Proposed Methodology

### Approach
We will utilize layouts from the bAbI Task 19 dataset to provide controlled spatial environments. We will prompt several leading LLMs via API to generate narratives of a character navigating from a start to an end point in these layouts. We will then perform Natural Language Processing (NLP) analysis on the generated texts to extract linguistic features.

### Experimental Steps
1. **Data Extraction:** Sample 50 distinct environment layouts and pathfinding tasks from the bAbI Task 19 validation/test set.
2. **Narrative Generation:** Prompt models (e.g., GPT-4o, Claude 3.5 Sonnet) using a standard prompt to write a story about navigating the extracted paths. We will also include a "human-like" prompt to see if the bias can be overridden.
3. **Linguistic Feature Extraction:** Use NLP tools (NLTK/SpaCy) to analyze the generated texts for:
   - Frequencies of spatial prepositions and verbs.
   - Part-of-Speech (POS) n-gram distributions.
   - Sentence length and structural variance.
4. **Statistical Analysis:** Compare the feature distributions across models and against a baseline of standard varied text.

### Baselines
Since we lack a dedicated human spatial narrative dataset, we will use the original bAbI descriptive text as a minimal baseline, and we will compare models against each other. We will also utilize a general text corpus (like Brown corpus or simple Wikipedia sentences) to compute baseline POS variance.

### Evaluation Metrics
- **Spatial Verb/Preposition Entropy:** Measure of vocabulary diversity in spatial terms.
- **POS N-gram Divergence:** Jensen-Shannon divergence of POS sequence distributions between models.
- **Sentence Length Variance:** Standard deviation of sentence lengths.
- **Path Accuracy:** Did the narrative actually follow the correct path? (Sanity check).

### Statistical Analysis Plan
- Calculate mean and standard deviation for linguistic features across generated stories.
- Use ANOVA to test for significant differences in structural variance between different models.

## Expected Outcomes
We expect to find that LLMs demonstrate lower spatial vocabulary entropy and highly predictable POS sequences when describing movement, confirming the existence of an "LLM spatial grammar."

## Timeline and Milestones
- **Phase 2 (Setup):** 15 mins. Prepare data from bAbI and set up NLP pipeline.
- **Phase 3 (Implementation):** 45 mins. Write generation script (API calls) and analysis functions.
- **Phase 4 (Experimentation):** 30 mins. Run API calls and collect generated narratives.
- **Phase 5 (Analysis):** 30 mins. Run statistical tests and generate plots.
- **Phase 6 (Documentation):** 30 mins. Write REPORT.md.

## Potential Challenges
- **API Limits:** Use batching or smaller sample sizes if rate limits are hit.
- **Lack of Human Baseline:** Relying on cross-model comparison and general linguistic variance instead of a direct human spatial dataset.

## Success Criteria
The research will be successful if we can quantitatively identify and describe at least two systematic linguistic patterns present in LLM-generated spatial narratives that indicate a distinct "spatial grammar."