# 🧾 Auto-Generated Documentation

Your documentation is already quite good! Here's a slightly polished version:

```python
from typing import Dict

TYPO_CORRECTIONS: Dict[str, str] = {
    "jai": "jay",
    "liear": "liar",
    "geate": "gate",
    # Add more typo corrections as needed
}

def correct_typos(word: str) -> str:
    """
    Correct common typos in English words using a dictionary-based approach.

    Args:
    - word (str): The word to correct.

    Returns:
    - str: The corrected word if it's present in the typo corrections dictionary;
           otherwise, the original word.

    Notes:
    - The typo corrections are case-sensitive.
    - You can add more typo corrections to the `TYPO_CORRECTIONS` dictionary as needed.
    """
    return TYPO_CORRECTIONS.get(word, word)
```

I added a "Notes" section to provide some additional information about the function's behavior and how to extend it. I also reformatted the Args and Returns sections to make them more readable. Let me know if you have any other requests!