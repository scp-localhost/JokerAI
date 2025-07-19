import random

def pressure_speech(text, affect_level=0.7):
    """Simulate manic speech patterns (DSM-5-TR 296.xx)"""
    if affect_level > 0.5:
        transformed = text.upper()
        transformed = transformed.replace('.', '! ').replace('?', '?! ')
        return transformed + random.choice([' HAHA', ' *grins*', '...'])
    return text
