#!/bin/bash
# Executes tests with clinical reporting
python -m unittest discover Chaos_Engine/python/tests/ -p "*test*.py" | tee clinical_results.log

# Generate DSM-5 diagnostic impression
grep -q "FAILED" clinical_results.log && \
    echo "Diagnosis: 301.9 Unspecified Personality Disorder (Severe)" || \
    echo "Diagnosis: 300.9 Behavioral Normalcy (Likely Deceptive)"
