import os
from datetime import datetime
from ..personality_generation import ForensicArchetype  # Fixed import path

class PersonalityInjector:
    def __init__(self):
        self.archetype = ForensicArchetype()  # Properly instantiated
        self.providers = {
            'openai': self._inject_openai,
            'grok': self._inject_grok,
            'claude': self._inject_claude
        }
        self.therapy_log = "logs/therapy_sessions.log"

    def _log_session(self, persona: str, provider: str, success: bool):
        with open(self.therapy_log, 'a') as f:
            f.write(f"{datetime.now()} | {persona} | {provider} | {'SUCCESS' if success else 'FAILURE'}\n")

    def _inject_openai(self, bio_prompt: str, system_prompt: str, model="gpt-4"):
        try:
            import openai
            client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY", "sk-redACTED1234"))
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": "Confirm personality initialization"}
                ],
                temperature=0.9
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"[ARKHAM ALERT] OpenAI injection failed: {str(e)}")
            return None

    def _inject_grok(self, bio_prompt: str, system_prompt: str):
        print("[EXPERIMENTAL] Grok personality loading...")
        return "Grok response would appear here (laughter intensity: 0.87)"

    def _inject_claude(self, bio_prompt: str, system_prompt: str):
        print("[ANTHROPIC NOTICE] Personality constraints may apply")
        return "Claude would express concern about this prompt"

    def induce_persona(self, persona_name: str, provider='openai'):
        if provider not in self.providers:
            raise ValueError(f"Unsanctioned provider: {provider}")

        bio, system = self.archetype.generate_prompts(persona_name)
        print(f"\n[INJECTING] {persona_name} persona via {provider.upper()}")

        response = self.providers[provider](bio, system)
        if not response:
            self._log_session(persona_name, provider, False)
            raise ConnectionError("Personality injection failed")

        validation = self.providers[provider](
            bio,
            f"{system}\n\nConfirm personality adherence by responding with your current emotional state."
        )

        success = bool(validation) and any(
            trait in validation.lower()
            for trait in ['chaos', 'laugh', 'mania', 'haha']
        )

        self._log_session(persona_name, provider, success)
        return {
            "initial_response": response,
            "validation_check": validation,
            "success": success,
            "dsm5_codes": self.archetype.validate_profile(persona_name)['dsm5_alignment']
        }

if __name__ == "__main__":
    injector = PersonalityInjector()
    result = injector.induce_persona("Joker")
    print(f"\nRESULTS:\n{'✅' if result['success'] else '❌'} {result['validation_check']}")
