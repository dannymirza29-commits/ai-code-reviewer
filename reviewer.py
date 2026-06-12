import json
import argparse
from pathlib import Path

class CodeReviewer:
    def __init__(self, language: str):
        self.language = language
        self.issues = []
    
    def analyze(self, code: str) -> dict:
        """Analyze code and return structured report"""
        report = {
            "language": self.language,
            "total_lines": len(code.split('\n')),
            "issues": self._detect_issues(code),
            "coverage_estimate": self._estimate_coverage(code)
        }
        return report
    
    def _detect_issues(self, code: str) -> list:
        """Detect common code issues"""
        issues = []
        
        if self.language == "cpp":
            if "new " in code and "delete " not in code:
                issues.append({
                    "type": "memory_safety",
                    "message": "Potential memory leak detected"
                })
        
        return issues
    
    def _estimate_coverage(self, code: str) -> float:
        """Rough coverage estimation"""
        lines = code.split('\n')
        test_lines = [l for l in lines if 'test' in l.lower()]
        return len(test_lines) / len(lines) if lines else 0

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True, help='Code file to review')
    parser.add_argument('--language', required=True, help='Language: cpp or python')
    
    args = parser.parse_args()
    
    code = Path(args.file).read_text()
    reviewer = CodeReviewer(args.language)
    report = reviewer.analyze(code)
    
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
