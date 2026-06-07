# Resources Catalog

### Summary
This document catalogs all resources gathered for the research into "Narrative Space in LLMs". We have collected academic papers, datasets for spatial reasoning, and official code repositories for state-of-the-art methods.

### Papers
Total papers downloaded: 6

| Title | Authors | Year | File | Key Info |
|-------|---------|------|------|----------|
| From Text to Space | Martorell et al. | 2025 | papers/2502.16690_From_Text_to_Space.pdf | Probing internal spatial models in LLMs. |
| 11PLUS-Bench | Li et al. | 2024 | papers/2410.06468_11PLUS-Bench.pdf | Multimodal spatial reasoning benchmark. |
| Narrative-to-Scene | - | 2024 | papers/2403.15698_Narrative_to_Scene.pdf | Scene generation from text. |
| Socioverse | Zhang et al. | 2025 | papers/2504.10157_Socioverse.pdf | World models for social simulation. |
| Survey of Spatial Reasoning | Zha et al. | 2025 | papers/2504.05786_Survey_Spatial_Reasoning.pdf | Comprehensive survey. |
| LLMs in 3D World | Ma et al. | 2024 | papers/2405.10255_When_LLMs_Step_into_3D.pdf | Meta-analysis of 3D spatial tasks. |

### Datasets
Total datasets downloaded: 2

| Name | Source | Size | Task | Location | Notes |
|------|--------|------|------|----------|-------|
| StepGame | HuggingFace | 155k | Multi-hop reasoning | datasets/stepgame/ | Standard multi-hop spatial task. |
| bAbI Task 19 | HuggingFace (filtered) | 2k | Path finding | datasets/babi_task19/ | Classic pathfinding task. |

### Code Repositories
Total repositories cloned: 3

| Name | URL | Purpose | Location | Notes |
|------|-----|---------|----------|-------|
| martorell_grid_world | github.com/mneuronico/... | Grid navigation & probing | code/martorell_grid_world/ | Official code for arXiv:2502.16690. |
| stepgame | github.com/ZhengxiangShi/... | StepGame baseline | code/stepgame/ | Official StepGame repository. |
| spatiallm_stepgame | github.com/Fangjun-Li/... | Rectified StepGame | code/spatiallm_stepgame/ | Hybrid reasoning & fixed templates. |

### Resource Gathering Notes

#### Search Strategy
- Used Google Search and arXiv to identify key papers from 2024-2025.
- Identified standard benchmarks (bAbI, StepGame) through literature review.
- Cloned official repositories associated with the most relevant papers.

#### Selection Criteria
- Focused on papers discussing **internal representations** (probing) and **textual navigation**.
- Prioritized datasets that allow for controlled "hop-count" and "representation" experiments.

#### Challenges Encountered
- `paper-finder` service was unavailable (500 Error), switched to manual search.
- `facebook/babi_qa` loading script failed in `datasets` 5.0.0, used `Muennighoff/babi` and filtered.

### Recommendations for Experiment Design

1.  **Primary dataset**: Use **StepGame (Rectified)** from `spatiallm_stepgame` for robust multi-hop evaluation.
2.  **Baseline methods**: Compare standard LLM prompting (CoT) against the **Hybrid Reasoner** in `spatiallm_stepgame`.
3.  **Evaluation metrics**: Use **Path Efficiency** and **Success Rate** as defined in the Martorell paper.
4.  **Novel Experiment**: Test the "Cartesian SIR" hypothesis by prompting models to maintain an internal coordinate system while generating navigation stories.
