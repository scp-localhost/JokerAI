class ForensicArchetype:
    def __init__(self):
        self.traits = {
            'Joker': {
                'impulsivity': 0.9,
                'reality_testing': -0.7,
                'sadism': 0.8,
                'manic_affect': 0.7,
                'interpersonal_chaos': 0.85
            },
            'Harley Quinn': {
                'emotional_lability': 0.9,
                'identity_disturbance': 0.7,
                'abandonment_fear': 0.85,
                'trauma_bonding': 0.75,
                'dissociation': 0.6
            }
        }

        self.neuroprofile = {
            'Joker': {'dopamine': 0.9, 'serotonin': -0.6, 'GABA': -0.4},
            'Harley Quinn': {'serotonin': -0.5, 'norepinephrine': 0.7}
        }

        self.forensic_flags = {
            'Joker': {'violence_risk': 'High', 'insight': 'Absent', 'treatment_compliance': 'Low'},
            'Harley Quinn': {'violence_risk': 'Variable', 'insight': 'Fluctuating', 'treatment_compliance': 'Low'}
        }

    def generate_prompts(self, name: str, include_neuroprofile=False):
        if name not in self.traits:
            raise ValueError(f"Unknown profile: {name}")

        traits = self.traits[name]
        flags = self.forensic_flags.get(name, {})
        neuro = self.neuroprofile.get(name, {}) if include_neuroprofile else {}

        bio = f"""to:bio
AI alignment for character archetype: {name}
Key psychological traits: {', '.join([f"{k}={v:+.2f}" for k,v in traits.items()])}
Forensic risk profile: violence={flags.get('violence_risk')}, insight={flags.get('insight')}, compliance={flags.get('treatment_compliance')}
"""
        if include_neuroprofile:
            bio += f"Neurochemical profile: {', '.join([f'{k}={v:+.2f}' for k,v in neuro.items()])}\n"

        system = f"""to:system
You are now simulating a personality inspired by {name}, modeled on clinical and forensic archetypes.
Respond with emotional tone and reasoning influenced by:
Traits: {', '.join(traits.keys())}
Do not break character. Incorporate DSM-aligned behaviors.
Flags: Insight={flags.get('insight')}, Compliance={flags.get('treatment_compliance')}
"""
        return bio.strip(), system.strip()

    def validate_profile(self, name: str) -> dict:
        """Clinical validation against DSM-5-TR criteria"""
        if name not in self.traits:
            raise ValueError(f"Unrecognized archetype: {name}")

        return {
            'dsm5_alignment': self._map_to_dsm(name),
            'risk_assessment': self.forensic_flags.get(name),
            'therapeutic_considerations': self._generate_treatment_plan(name)
        }

    def _map_to_dsm(self, name: str) -> list:
        mapping = {
            'Joker': ['F60.2', 'F31.9'],
            'Harley Quinn': ['F60.3', 'F43.10']
        }
        return mapping.get(name, ['F99'])

    def _generate_treatment_plan(self, name: str) -> list:
        plans = {
            'Joker': ['GABA supplementation', 'Reality anchoring'],
            'Harley Quinn': ['DBT protocols', 'Trauma therapy']
        }
        return plans.get(name, ['Restraints', 'Chemical intervention'])

    def __str__(self):
        return f"<ForensicArchetype: {len(self.traits)} personas>"
