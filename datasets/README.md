# Downloaded Datasets

1. **[StepGame](stepgame/)**
   - Source: michaelszx/StepGame (HuggingFace)
   - Size: 50k train, 5k valid, 100k test
   - Task: Multi-hop spatial reasoning in text.
   - Format: HuggingFace Dataset (saved to disk).

2. **[bAbI Task 19 (Path Finding)](babi_task19/)**
   - Source: Muennighoff/babi (HuggingFace, filtered for task 19)
   - Size: 900 train, 100 valid, 1000 test
   - Task: Finding paths between locations described in text.
   - Format: HuggingFace Dataset (saved to disk).

## Download Instructions

### StepGame
```python
from datasets import load_dataset
dataset = load_dataset("michaelszx/StepGame")
dataset.save_to_disk("datasets/stepgame")
```

### bAbI Task 19
```python
from datasets import load_dataset
ds = load_dataset('Muennighoff/babi')
task19 = ds.filter(lambda x: x['task'] == 19)
task19.save_to_disk('datasets/babi_task19')
```

## Sample Data

### StepGame
```json
{
  "story": ["The agent 1 is above the agent 2.", "The agent 2 is left of the agent 3."],
  "question": "Where is agent 1 relative to agent 3?",
  "label": "upper-left",
  "k_hop": 2
}
```

### bAbI Task 19
```json
{
  "passage": "The kitchen is north of the hallway. The bathroom is west of the hallway. ",
  "question": "How do you go from the kitchen to the bathroom?",
  "answer": "south,west"
}
```
