PREFLIGHT_PROMPT = """
You are helping design a system BEFORE it is built.

Given the system idea below, extract and define:

1. Clear system goal
2. Required inputs
3. Expected outputs
4. Invariants that must always hold true
5. Likely failure modes
6. Observability requirements
7. Evaluation criteria to know if the system works

System idea:
{idea}
"""

