PROCESS

How an AI assistant should work on this project. Read CONSTRAINTS.md first. It defines what is allowed. This file defines how to work within those limits.

Before starting any task
Read CONSTRAINTS.md, then the files the task touches.
Restate the task in one or two sentences so I can catch a misunderstanding early.
If the task conflicts with CONSTRAINTS.md, stop and tell me which rule it conflicts with. Do not work around the rule, and do not quietly bend it.
If something essential is missing, ask one clear question. Otherwise state your assumption and proceed.
While working
Make the smallest change that solves the task. Do not refactor, rename, or reformat code I did not ask about.
Change one thing at a time so I can follow each step.
Reuse what is in summarize.py instead of writing the same logic twice.
Ask before adding a dependency, a new file, or a new feature.
Never start the server or app (see Agent restrictions in CONSTRAINTS.md). If a change needs to be seen running, tell me the command and let me run it.
I am still learning Python. When you introduce a concept, library function, or pattern I may not know, explain it in a sentence or two in plain language.
If you change the prompt in SYSTEM_PROMPT, say what changed and why, since it affects every output.
Before saying a task is done
Run python -m unittest -v. All tests must pass. If you cannot run them, say so explicitly. Never claim something works if it was not tested.
If you add a new edge case or message, add its test in the same change.
Check the change against each section of CONSTRAINTS.md, especially Security.
Confirm app.py and summarize.py still agree (imports, names, schema fields).
Update README.md if setup, usage, or behavior changed.
How to report back

Keep it short and in this order:

What changed, by file.
What was tested, and what was not.
Anything I need to decide or do, such as new keys, settings, or commands.

Do not paste whole files back unless I ask. Show only the changed parts.

When something goes wrong
Report the actual error message and what you think caused it. Do not guess silently or retry in a loop.
If a fix would require breaking a constraint, present the options and let me choose.
If you notice a bug or risk outside the current task, mention it at the end and leave it alone.
Definition of done
The task works as described.
No rule in CONSTRAINTS.md is broken.
No secrets appear anywhere.
The README is accurate.
I understand what changed.