CONSTRAINTS

Hard rules for this project. Any AI assistant working here must read this file first and follow it. If a request conflicts with a rule below, stop and say so before doing anything (see PROCESS.md).

Project purpose

A small demo that shows I can call an AI model through an API. The app takes a document and returns a summary, key points, action items, and entities as structured JSON. It is a portfolio piece, so clarity and reliability matter more than features.

Stack
Language: Python 3.
Front end: Streamlit only. No React, Next.js, custom HTML, CSS, or JavaScript.
AI provider: Anthropic API via the official anthropic Python SDK.
Model: claude-sonnet-4-6, defined once as MODEL in summarize.py. Never hardcode it elsewhere.
Dependencies: streamlit and anthropic only. Do not add a package without asking first.
Structure
summarize.py is the single source of truth for the prompt (SYSTEM_PROMPT), the model name, input limits, and JSON parsing. It also works as a command-line tool.
app.py is the Streamlit interface. It imports from summarize.py and must not duplicate its logic.
test_edge_cases.py holds the tests (standard-library unittest only, no pytest).
requirements.txt, README.md, CONSTRAINTS.md, and PROCESS.md live in the project root.
Keep it to these files unless I approve a new one.
Edge cases and messages
Every input, output, or failure case the app handles has exactly one entry in MESSAGES in summarize.py. Do not write user-facing text anywhere else.
Every entry in MESSAGES must be triggered by at least one test in test_edge_cases.py.
Input: empty, too short, too long, unreadable or unsupported characters, wrong file type, and text that tries to give the AI instructions must each be handled.
Output: malformed JSON, missing fields, cut-off or refused responses, leaked instructions, and details that aren't in the document (names, owners, deadlines, numbers) must each be handled.
Failures: timeouts, rate limits, bad or missing keys, no credits, overloads, server errors, and unexpected errors must each show a plain message, never a traceback or raw error text.
Security
The API key comes from the ANTHROPIC_API_KEY environment variable, or from Streamlit secrets when deployed.
Never put a key in code, comments, examples, logs, commits, or the README.
No key may ever be committed, pushed, or pasted to GitHub: not in code, commit messages, issues, pull requests, README, screenshots, or test files. No exceptions, including "temporary" or "test" keys.
Keep keys only in the shell environment or in .streamlit/secrets.toml (git-ignored). The app does not read .env files.
Before any commit, check git status and git diff --staged for secrets. If a secret is staged, stop.
If a key is ever exposed, treat it as compromised: revoke it in the Anthropic Console and create a new one. Deleting the commit is not enough.
Never print or display the key, including in error messages.
.env and .streamlit/secrets.toml must be listed in .gitignore.
Behavior of the app
The model must return only a JSON object matching the schema in SYSTEM_PROMPT.
The model must use only information in the document. No invented details. Unknown values are null.
Handle rate limits, connection errors, API status errors, and malformed JSON with a clear, human-readable message. The app must never crash with a raw traceback.
Reject empty input. Truncate input above MAX_CHARS and tell the user.
Do not store or log uploaded documents.
Code style
Readable over clever. Short functions, descriptive names, type hints on function signatures.
Comments explain why, not what.
Match the existing style and structure rather than refactoring.
Agent restrictions
The AI agent must never run the server or the app. That means no streamlit run, no python app.py, no background processes, and no opening ports, under any circumstances.
I run the app myself. The agent may tell me the command to run, but must not run it.
Allowed to run: python -m unittest -v (tests use a fake client, no server or network).
Do not make real API calls to test. Use the fake client in test_edge_cases.py.
Out of scope
User accounts, databases, authentication, payments.
Supporting file types other than plain text and Markdown, until I ask (PDF is a planned future step).
Anything that would make the demo harder to run with three commands.