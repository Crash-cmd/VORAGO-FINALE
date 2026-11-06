# VORAGO — Shortcut Learner

VORAGO is a desktop learning application built with Python and CustomTkinter. It brings together quick-learning shortcuts and practice quizzes for Mathematics, Physics and Chemistry, with a customizable interface.

This branch now contains **two ways to experience VORAGO**:

1. **Original application** — the existing project entry point, structure and design.
2. **VORAGO Studio** — a separate, substantial redesign prototype for side-by-side comparison.

Neither version replaces the other. The original application remains available.

## Run either version

Run commands from the repository root.

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Launch the original app:

```bash
python app.py
```

Launch the redesign:

```bash
python vorago_redesign.py
```

The redesign writes its own local profile and progress data to `vorago_redesign_data.json`. It does not overwrite `credits.json` or `c_ans_storage.json`.

## What VORAGO Studio changes

The redesign is intentionally a different product experience, not a new theme applied to the old screen.

### Login and profile
- A redesigned two-panel welcome screen with a clearer first-run experience.
- Create-profile and sign-in modes.
- Passwords are stored as salted PBKDF2-HMAC-SHA256 hashes in the prototype's separate local data file, rather than plain text.
- Each local profile has its own quiz scores and completion list.
- This is still a local desktop prototype, not a production account or cloud authentication system.

### Main application
- A persistent left navigation rail for Overview, Mathematics, Physics, Chemistry, Progress and Settings.
- A dashboard with a welcome panel, learning coverage, average quiz score and subject cards.
- Separate subject libraries with searchable shortcut cards.
- Consistent spacing, typography, rounded panels and a restrained dark palette with warm gold accents.
- A soft light/dark palette toggle.

### Learning flow
- The redesign reads the existing shortcut titles, principles, rules, worked examples and applications from the current subject modules using Python's AST parser. It does not execute those module functions.
- It reads the existing multiple-choice question banks from `practice_questions.py`.
- Each shortcut has a dedicated lesson page followed by a practice quiz.
- Quiz feedback is immediate; the correct option is highlighted.
- Progress is based on whether a quiz was completed, so a score of zero still counts as completion.
- Best scores are saved per local profile.

### Files and safety
- `app.py` remains the original application.
- `vorago_redesign.py` is the new alternative entry point.
- `vorago_redesign_data.json` is generated locally and is not intended to be committed.
- Existing lesson modules, question banks, themes and original profile/progress files remain in place.

## Comparing the two experiences

| Area | Original VORAGO | VORAGO Studio |
|---|---|---|
| Entry point | `python app.py` | `python vorago_redesign.py` |
| Login | Existing login windows | Unified sign-in / create-profile screen |
| Navigation | Existing icon panel and subject screens | Persistent labelled left navigation |
| Home | Basic welcome screen | Dashboard with subject cards and progress |
| Learning | Existing shortcut screens | Lesson → examples → quiz flow |
| Search | No unified subject search | Searchable shortcut library |
| Quiz progress | Existing shared JSON score storage | Per-profile completion and best-score tracking |
| Theme | Existing theme JSON files | Built-in dark and soft-light palettes |
| Data | `credits.json`, `c_ans_storage.json` | Separate `vorago_redesign_data.json` |

## Review branch: bug fixes and findings

The conservative maintenance pass also corrected:
- Horizontal panel layout configuration in `app.py`.
- Duplicate username/password text when saving settings.
- Missing Physics shortcut 9 question data.
- Incorrect Physics shortcut 10 question-set mapping.
- Misspelled Chemistry shortcut 3 keyword.

Other findings still worth addressing in the original app:
- Original credentials are stored directly in `credits.json`; avoid using real or reused passwords there.
- Relative file paths can fail if the original app is launched outside the repository root.
- Original progress tracking may treat a completed zero-score quiz as incomplete.
- Some Physics shortcut descriptions and question sets appear mismatched. Review the question banks before relying on those particular quizzes for revision.
- The repository contains generated `__pycache__` files and an `app.py.conflict-backup` file that should be reviewed for cleanup.

## Validation status

The source changes have been reviewed, but neither GUI has been launched in a local desktop session as part of this GitHub edit. Please test both entry points locally.

For the redesign, test:
1. Create a new local profile, sign out and sign back in.
2. Open each subject and search for a shortcut.
3. Open a lesson and check its principle, rule and examples.
4. Answer both correct and incorrect quiz options.
5. Finish a quiz with a score of zero and confirm that it is still marked completed.
6. Switch between dark and light palettes.
7. Confirm the original `credits.json` and `c_ans_storage.json` are unchanged by the redesign.

## Branch safety

All changes are on `review/bug-fixes-and-small-improvements`. The `main` branch has not been edited or merged.
