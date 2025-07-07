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
        word (str): The word to correct.

    Returns:
        str: The corrected word.
    """
    return TYPO_CORRECTIONS.get(word, word)
```
This solution uses a dictionary `TYPO_CORRECTIONS` to map typos to their corrected forms. The `correct_typos` function takes a word as input and returns the corrected word if it's present in the dictionary, otherwise it returns the original word.

Please let me know if this is what you had in mind, or if you need help with something else!