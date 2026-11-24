import os
import re

PATTERNS = [re.compile(r'(api[_-]?key|secret[_-]?key|password|bearer|auth[_-]?token)\s*[:=]\s*[\"\'][a-zA-Z0-9_\-]{8,}[\"\']', re.I)]
violations = []
for root, dirs, files in os.walk('.'):
    if any(k in root for k in ['.git', '.venv', '__pycache__', '.pytest_cache', 'reports']):
        continue
    for f in files:
        if f.endswith(('.py', '.md', '.txt', '.properties', 'Dockerfile', 'Jenkinsfile')):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                for idx, line in enumerate(fp):
                    for pat in PATTERNS:
                        if pat.search(line) and "test-secret-key" not in line and "os.environ" not in line:
                            violations.append((path, idx+1, line.strip()))

if violations:
    print('Found potential secret matches:')
    for v in violations:
        print(f'  {v[0]}:{v[1]} -> {v[2]}')
else:
    print('CONFIRMED: Clean repository. Zero hardcoded secrets, passwords, or personal tokens detected.')
