from ...Arkham_Protocols.personality_generation import ForensicArchetype

def seed_persona(name: str, neuroprofile=True):
    """Public API for personality generation"""
    fa = ForensicArchetype()
    return fa.generate_prompts(name, include_neuroprofile=neuroprofile)
