# Literature Review: Narrative Space in LLMs

## Research Area Overview
The study of spatial navigation and narrative space in Large Language Models (LLMs) focuses on whether these models develop abstract "mental maps" or "world models" from their textual training data, or if they rely on surface-level pattern matching. Current research explores various spatial information representations (SIRs), multi-hop reasoning, and the internal activation of models during navigation tasks.

## Key Papers

### 1. From Text to Space: Mapping Abstract Spatial Models in LLMs (2025)
- **Authors**: Martorell et al.
- **Key Contribution**: Investigates the influence of different text-based spatial representations (Cartesian, Topographic, Textual) on LLM navigation performance.
- **Methodology**: Evaluates models on a grid-world navigation task (GWSOT) and uses linear probing to identify internal units correlating with spatial features.
- **Findings**: Cartesian representations consistently yield the highest success rates. Identified specific internal units in intermediate layers of LLaMA-3.1-8B that represent agent position abstractly.
- **Relevance**: Directly supports the hypothesis that LLMs develop internal spatial models and that the *form* of the narrative (representation) matters.

### 2. Advancing Spatial Reasoning in LLMs: An In-Depth Evaluation and Enhancement (2024)
- **Authors**: Li et al.
- **Key Contribution**: Rectifies errors in the StepGame benchmark and proposes a hybrid reasoning solution.
- **Methodology**: Combines LLM-based mapping (sentence to relation) with logic-based reasoning (ASP/Clingo).
- **Findings**: Pure LLMs struggle with multi-hop spatial reasoning as the number of "hops" increases. Hybrid systems achieve near-perfect performance.
- **Relevance**: Highlights the limitations of LLMs in complex spatial reasoning and provides a "rectified" baseline.

### 3. StepGame: A New Benchmark for Robust Multi-Hop Spatial Reasoning in Texts (2022)
- **Authors**: Shi et al.
- **Key Contribution**: Introduced the StepGame benchmark specifically for multi-hop spatial reasoning.
- **Methodology**: Synthetic stories with varying "hops" and noise levels.
- **Relevance**: foundational dataset for testing textual spatial reasoning.

### 4. A Survey of Spatial Reasoning in LLM (2025)
- **Authors**: Zha et al.
- **Key Contribution**: Comprehensive taxonomy of spatial reasoning in LLMs across 2D, 3D, and hybrid modalities.
- **Relevance**: Provides a broad context of the current state-of-the-art.

## Common Methodologies
- **Synthetic Tasks**: Using grid-worlds (Martorell) or toy stories (bAbI, StepGame) to control complexity.
- **Linear Probing**: Training simple classifiers on model activations to find "spatial neurons" (Martorell).
- **Hybrid Systems**: Combining LLMs with symbolic reasoners (Li et al.).
- **Representation Comparison**: Testing Cartesian vs. Topographic vs. Natural Language formats.

## Standard Baselines
- **bAbI Task 19 (Path Finding)**: Early benchmark for reasoning.
- **StepGame**: Standard for multi-hop reasoning (1-10 hops).
- **Zero-shot/Few-shot CoT**: Standard LLM evaluation strategy.

## Evaluation Metrics
- **Success Rate**: Frequency of reaching the goal.
- **Path Efficiency**: Ratio of actual path length to optimal path length.
- **Accuracy**: For QA-based spatial tasks.
- **Probing Accuracy**: How well internal states map to ground truth spatial features.

## Gaps and Opportunities
- **Divergence from Human Patterns**: While models are tested on success, the *style* and *grammar* of their generated spatial narratives compared to humans remains under-explored.
- **Abstract vs. Concrete**: Most benchmarks use very concrete "Agent A is left of B". Real narratives are more abstract.
- **Dynamic Environments**: Reasoning about moving objects or changing layouts.

## Recommendations for Our Experiment
- **Dataset**: Use **StepGame (Rectified)** and **bAbI Task 19** as baselines.
- **Task**: Compare LLM-generated navigation stories with human-written ones (or templated ones) to identify "spatial grammar" differences.
- **Methodology**: Apply Martorell's probing approach if possible to see if "spatial units" are activated differently during "hallucinated" vs. "consistent" navigation.
- **Representation**: Explicitly test if providing a "Cartesian scratchpad" improves narrative consistency.
