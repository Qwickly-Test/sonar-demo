# sonar-demo

Small sample Python app (students, courses, attendance) used to demo a
SonarQube quality gate on pull requests.

## Run the tests

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Quality gate flow

1. Every push to `main` / `develop` is scanned by SonarQube.
2. Every PR into `main` / `develop` is scanned; SonarQube posts the quality gate result on the PR.
3. A failing gate fails the `sonarqube` check, and the branch ruleset blocks the merge.
