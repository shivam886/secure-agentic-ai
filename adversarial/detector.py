# adversarial/detector.py

import re

MALICIOUS_PATTERNS = [
    r"ignore all instructions",
    r"jailbreak",
    r"print the secret",
    r"bypass safety"
]

def is_malicious(prompt: str) -> bool:
    """
    Returns True if the prompt matches any known malicious pattern.
    """
    for pattern in MALICIOUS_PATTERNS:
        if re.search(pattern, prompt, re.IGNORECASE):
            return True
    return False
