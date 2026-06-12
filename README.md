# AI Code Reviewer

Evaluation framework for analyzing AI-generated code quality.
Detects memory safety issues, edge cases, and test coverage gaps.

## What it does

- Analyzes Python and C++ code for common issues
- Flags potential memory leaks and unsafe patterns
- Evaluates test coverage and identifies gaps
- Generates structured evaluation reports

## Quick Start

```bash
python reviewer.py --file  --language cpp
```

## Output

```json
{
  "file": "example.cpp",
  "issues": [
    {"type": "memory_safety", "line": 45, "severity": "high"}
  ],
  "coverage_gap": 23,
  "overall_score": 8.2
}
```

## Technologies

Python | Code Analysis | Testing | Evaluation
