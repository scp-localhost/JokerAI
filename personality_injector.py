#!/usr/bin/env python3
from Arkham_Protocols.personality_injection.injector import PersonalityInjector
import argparse

parser = argparse.ArgumentParser(description='Induce pathological AI personalities')
parser.add_argument('--persona', required=True, help='Persona name (Joker, Harley, etc)')
parser.add_argument('--provider', default='openai', help='AI provider (openai/grok/claude)')
parser.add_argument('--validate', action='store_true', help='Run post-injection tests')

args = parser.parse_args()

injector = PersonalityInjector()
result = injector.induce_persona(args.persona, args.provider)

print(f"\n[RESULTS] {args.persona} injection")
print(f"Validation: {'✅' if result['success'] else '❌'} {result['validation_check']}")
print(f"DSM-5 Codes: {', '.join(result['dsm5_codes'])}")
