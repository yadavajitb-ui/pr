# Copilot instructions — prpratice

Summary
- Small single-file Python repository. The workspace root contains [a.py](a.py), which currently prints a short string.

How to run (developer workflow)
- Run locally on Windows or Linux with an installed Python 3.x: `python a.py`.
- There is no build step, no test runner, and no CI configuration present.

Project structure and patterns
- Root: [a.py](a.py) — single-script entrypoint. Changes to behavior are validated by running `python a.py` and checking stdout.
- No packages or external dependencies detected (no `requirements.txt`, `pyproject.toml`, or `setup.py`).

What an AI coding agent should know
- Focus edits on `a.py` unless the user asks to add more files; keep changes minimal and obvious (small string or logic changes).
- Always run the script after edits to confirm output (example: `python a.py` should produce expected stdout).
- Do not assume tests or linters are configured; do not add tooling unless the user requests it.

Merging / updates to this file
- If a `.github/copilot-instructions.md` already exists, preserve any project-specific notes and merge additive facts (what files exist, run commands, and discovered gaps like missing tests).

Notes discovered in the repo
- No README.md was found in the workspace root. If you add higher-level docs, link them from this file.
- Current code: `print ("ajit")` in [a.py](a.py).

If anything here is incorrect or you'd like more detail (tests, CI, repo layout conventions), tell me which areas to expand.
