# VORAGO — Shortcut Learner

VORAGO is a desktop learning application built with Python and CustomTkinter. It brings together quick-learning shortcuts and practice quizzes for Mathematics, Physics and Chemistry, with a customizable interface.

## Features

- Subject sections for Mathematics, Physics and Chemistry
- Shortcut explanations with rules, worked examples and quick applications
- Multiple-choice practice quizzes with immediate feedback and saved scores
- Theme selection, light/dark appearance and horizontal/vertical navigation layouts
- Local login and learner progress information

## Run the application

Run the project from its root directory so the existing relative paths to images and JSON data files resolve correctly.

Install the application dependencies:

```bash
python -m pip install customtkinter pillow
```

Start the application:

```bash
python app.py
```

The project currently has no dependency lockfile or automated test suite. The GUI should be exercised locally after installing the dependencies.

## Review branch: bug fixes and small improvements

The branch `review/bug-fixes-and-small-improvements` contains a conservative maintenance pass. The application's learning flow, subject structure and overall design have been retained.

### Bugs fixed in this branch

- **Horizontal panel layout:** removed invalid positional arguments passed to `spacer.configure()`. Selecting the horizontal layout no longer raises a configuration `TypeError`, and the main content row is allowed to expand.
- **Username and password settings:** clear the entry before restoring the saved value. Previously, saving an edited username or password inserted the same value a second time, duplicating the displayed text.
- **Physics shortcut 9:** connected the missing practice-question dataset, which previously caused the screen builder to fail because its required `questions_data` argument was absent.
- **Physics shortcut 10:** connected its own `psc10` question set instead of reusing `psc9`.
- **Chemistry shortcut 3:** corrected the misspelled `questiion_data` keyword to `questions_data`, allowing the quiz screen to receive its question set.

### Findings to consider next

These are review findings, not changes made in this pass:

- **Credential storage:** usernames and passwords are stored directly in `credits.json`. This is not suitable for accounts containing real or reused passwords; a safer authentication design should be considered before distributing the application.
- **Working-directory dependency:** images and several JSON files are opened using relative paths. Launching `app.py` from outside the repository root may cause file-not-found errors.
- **Physics quiz content alignment:** the Physics shortcut explanations and their assigned practice sets do not consistently cover the same topic. For example, the P-V slope shortcut is paired with a work-done question set, and the tuning-fork shortcut is paired with a centripetal-acceleration set. The question banks should be reviewed topic by topic before students rely on them for revision.
- **Progress calculation:** progress is counted when a saved score is non-zero. A completed quiz with a score of zero may therefore appear incomplete.
- **Repository housekeeping:** the default branch contains generated `__pycache__` content and an `app.py.conflict-backup` file. These should be reviewed and excluded from future commits if they are not intentional project assets.
- **Automated validation:** there is no test suite or dependency manifest at present. A repeatable smoke-test checklist and pinned dependencies would make future changes safer.

## Validation status

The fixes above were reviewed against the source code and committed to the review branch. They have **not** been runtime-tested in a local desktop session in this review, so please run the application and test the horizontal/vertical layout, profile editing, Physics shortcuts 9–10 and Chemistry shortcut 3 before merging anything.

## Branch safety

All review changes are on `review/bug-fixes-and-small-improvements`. The `main` branch has not been edited or merged.
