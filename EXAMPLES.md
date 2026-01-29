# 📝 SmartNotes - Usage Examples

**Comprehensive examples covering all SmartNotes features**

Quick navigation:
- [Example 1: First Time Setup](#example-1-first-time-setup)
- [Example 2: Quick Idea Capture](#example-2-quick-idea-capture)
- [Example 3: Study Notes with Tags](#example-3-study-notes-with-tags)
- [Example 4: Code Snippets and Tips](#example-4-code-snippets-and-tips)
- [Example 5: Meeting Notes Workflow](#example-5-meeting-notes-workflow)
- [Example 6: Daily Journaling](#example-6-daily-journaling)
- [Example 7: Search and Filter](#example-7-search-and-filter)
- [Example 8: Tag Management](#example-8-tag-management)
- [Example 9: Export and Backup](#example-9-export-and-backup)
- [Example 10: Complete Daily Workflow](#example-10-complete-daily-workflow)

---

## Example 1: First Time Setup

**Scenario:** You just installed SmartNotes and want to verify it works.

**Steps:**

```bash
# Step 1: Check SmartNotes is available
python smartnotes.py --help

# Step 2: Add your first note
python smartnotes.py add "Hello SmartNotes! This is my first note #welcome"

# Step 3: Verify the note was saved
python smartnotes.py list
```

**Expected Output:**

```
[OK] Note #1 added
     Tags: welcome

[1 note(s) found]

#1 | 2026-01-29T12:00:00
    Hello SmartNotes! This is my first note #welcome
    Tags: welcome
```

**What You Learned:**
- SmartNotes is properly installed
- Notes are stored automatically
- Hashtags become tags automatically

---

## Example 2: Quick Idea Capture

**Scenario:** You have a brilliant idea and need to capture it instantly.

**Steps:**

```bash
# Capture idea with context tags
python smartnotes.py add "App idea: AI-powered recipe suggester based on fridge contents #idea #project #mobile"

# Add another related idea
python smartnotes.py add "Revenue model: Freemium with grocery delivery partnerships #idea #business"

# List all ideas
python smartnotes.py list --tag idea
```

**Expected Output:**

```
[OK] Note #2 added
     Tags: idea, project, mobile, powered, recipe, based, contents

[OK] Note #3 added
     Tags: idea, business, revenue, model, freemium

[2 note(s) found]

#3 | 2026-01-29T12:01:00
    Revenue model: Freemium with grocery delivery partnerships #idea #business
    Tags: idea, business, revenue, model, freemium

#2 | 2026-01-29T12:00:30
    App idea: AI-powered recipe suggester based on fridge contents #idea #...
    Tags: idea, project, mobile, powered, recipe, based, contents
```

**What You Learned:**
- Hashtags are automatically extracted
- Keywords (4+ letters) are also auto-tagged
- Filter by tag shows related notes together

---

## Example 3: Study Notes with Tags

**Scenario:** You're studying biology and want to organize notes by topic.

**Steps:**

```bash
# Add biology notes with explicit tags
python smartnotes.py add "Photosynthesis: Light energy → Chemical energy (glucose). Occurs in chloroplasts." --tags biology plants science

# Add more related notes
python smartnotes.py add "Mitochondria: Powerhouse of the cell. ATP production through cellular respiration." --tags biology cells science

# Add a chemistry note
python smartnotes.py add "Covalent bonds: Atoms share electrons to achieve stability." --tags chemistry science

# List all science notes
python smartnotes.py list --tag science

# List only biology
python smartnotes.py list --tag biology
```

**Expected Output:**

```
[3 note(s) found]

#6 | 2026-01-29T12:05:00
    Covalent bonds: Atoms share electrons to achieve stability.
    Tags: chemistry, science

#5 | 2026-01-29T12:04:30
    Mitochondria: Powerhouse of the cell. ATP production through cellular...
    Tags: biology, cells, science

#4 | 2026-01-29T12:04:00
    Photosynthesis: Light energy → Chemical energy (glucose). Occurs in ch...
    Tags: biology, plants, science
```

**What You Learned:**
- Use `--tags` for explicit topic organization
- Tags help create subject-matter clusters
- Filter by tag for focused study sessions

---

## Example 4: Code Snippets and Tips

**Scenario:** Save useful code patterns and programming tips.

**Steps:**

```bash
# Save a Python tip
python smartnotes.py add "Python f-strings: Use f'{variable}' for cleaner string formatting. Faster than .format() or %s" --tags python coding tips

# Save a regex pattern
python smartnotes.py add "Email regex: ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ #regex #coding #validation"

# Save a SQL query pattern
python smartnotes.py add "SQL date filter: WHERE created_at BETWEEN '2026-01-01' AND '2026-01-31' #sql #database"

# Search for Python tips later
python smartnotes.py search "python"
```

**Expected Output:**

```
[1 note(s) found]

#7 | 2026-01-29T12:10:00
    Python f-strings: Use f'{variable}' for cleaner string formatting. Fas...
    Tags: python, coding, tips
```

**What You Learned:**
- SmartNotes is great for code snippets
- Search finds notes containing keywords
- Technical terms become tags automatically

---

## Example 5: Meeting Notes Workflow

**Scenario:** Capture meeting notes and action items.

**Steps:**

```bash
# Capture meeting summary
python smartnotes.py add "Team standup 1/29: Sprint goal is mobile app v2.0. Blockers: API rate limits. Next meeting: Friday 2pm." --tags meeting work standup

# Add action items
python smartnotes.py add "ACTION: Contact API provider about rate limit increase. Due: EOD today." --tags todo work urgent

python smartnotes.py add "ACTION: Review mobile designs before Friday standup." --tags todo work designs

# List all action items
python smartnotes.py list --tag todo
```

**Expected Output:**

```
[2 note(s) found]

#12 | 2026-01-29T12:20:00
    ACTION: Review mobile designs before Friday standup.
    Tags: todo, work, designs

#11 | 2026-01-29T12:19:30
    ACTION: Contact API provider about rate limit increase. Due: EOD today.
    Tags: todo, work, urgent
```

**What You Learned:**
- Use consistent tags like `#todo` for action items
- Combine context tags (`work`, `urgent`) for filtering
- Meeting notes and actions can be tracked together

---

## Example 6: Daily Journaling

**Scenario:** Keep a daily journal with goals and reflections.

**Steps:**

```bash
# Morning: Set daily goals
python smartnotes.py add "2026-01-29 Morning: Goals for today - 1) Complete project proposal 2) Exercise 30min 3) Call mom #journal #goals #morning"

# Midday: Quick check-in
python smartnotes.py add "Lunch break: Proposal 60% done. Feeling focused today. #journal #progress"

# Evening: Reflection
python smartnotes.py add "2026-01-29 Evening: Completed proposal! Went for a 45min walk instead of planned exercise. Called mom - she's doing well. Grateful for productive day. #journal #reflection #evening"

# Review journal entries
python smartnotes.py list --tag journal
```

**Expected Output:**

```
[3 note(s) found]

#15 | 2026-01-29T18:00:00
    2026-01-29 Evening: Completed proposal! Went for a 45min walk instead ...
    Tags: journal, reflection, evening

#14 | 2026-01-29T12:30:00
    Lunch break: Proposal 60% done. Feeling focused today. #journal #progress
    Tags: journal, progress

#13 | 2026-01-29T08:00:00
    2026-01-29 Morning: Goals for today - 1) Complete project proposal 2) ...
    Tags: journal, goals, morning
```

**What You Learned:**
- Date-prefix helps with chronological organization
- Tags like `#morning`, `#evening` categorize entry types
- Journal becomes searchable knowledge base

---

## Example 7: Search and Filter

**Scenario:** Find specific notes among hundreds.

**Steps:**

```bash
# Search by keyword
python smartnotes.py search "proposal"

# Filter by tag
python smartnotes.py list --tag work

# Combine with limit
python smartnotes.py list --tag work --limit 5

# Show full details of a specific note
python smartnotes.py show 11
```

**Expected Output (show command):**

```
============================================================
Note #11
============================================================

Created:  2026-01-29T12:19:30
Modified: 2026-01-29T12:19:30

Content:
ACTION: Contact API provider about rate limit increase. Due: EOD today.

Tags: todo, work, urgent

============================================================
```

**What You Learned:**
- `search` finds text anywhere in note content
- `list --tag` filters by specific tag
- `show` displays full note with all metadata
- `--limit` helps manage long lists

---

## Example 8: Tag Management

**Scenario:** Organize and review your tagging system.

**Steps:**

```bash
# See all unique tags and their counts
python smartnotes.py tags

# Add tags to an existing note
python smartnotes.py tag 11 priority-high follow-up

# View the updated note
python smartnotes.py show 11
```

**Expected Output (tags command):**

```
[15 unique tag(s)]

  #biology (2 note(s))
  #business (1 note(s))
  #cells (1 note(s))
  #chemistry (1 note(s))
  #coding (3 note(s))
  #designs (1 note(s))
  #evening (1 note(s))
  #goals (1 note(s))
  #idea (2 note(s))
  #journal (3 note(s))
  #meeting (1 note(s))
  #mobile (1 note(s))
  #morning (1 note(s))
  #progress (1 note(s))
  #project (1 note(s))
  ...
```

**What You Learned:**
- `tags` shows your entire tag taxonomy
- Tags with note counts help identify organization patterns
- Add tags anytime without editing content

---

## Example 9: Export and Backup

**Scenario:** Export notes for backup or sharing.

**Steps:**

```bash
# Export as plain text
python smartnotes.py export --format txt --output my_notes.txt

# Export as Markdown (great for sharing)
python smartnotes.py export --format md --output notes_backup.md

# Export as JSON (for programmatic use)
python smartnotes.py export --format json --output notes_data.json

# View statistics
python smartnotes.py stats
```

**Expected Output (stats):**

```
========================================
  SmartNotes Statistics
========================================
Total notes:      15
Total tags:       25
Average length:   87 characters
Most recent:      2026-01-29T18:00:00
Storage location: C:\Users\logan\.smartnotes\notes.json
========================================
```

**Expected Output (Markdown export sample):**

```markdown
# SmartNotes Export

*Generated: 2026-01-29 18:30:00*

---

## Note #1

**Created:** 2026-01-29T12:00:00  
**Tags:** `#welcome`  

Hello SmartNotes! This is my first note #welcome

---

## Note #2

**Created:** 2026-01-29T12:00:30  
**Tags:** `#idea` `#project` `#mobile`  

App idea: AI-powered recipe suggester based on fridge contents #idea #project #mobile

---
```

**What You Learned:**
- Multiple export formats for different use cases
- Plain text for simple viewing
- Markdown for documentation/sharing
- JSON for data processing
- Stats show your note-taking patterns

---

## Example 10: Complete Daily Workflow

**Scenario:** A full day of professional note-taking.

**Steps:**

```bash
# === MORNING (8:00 AM) ===

# Check yesterday's todos
python smartnotes.py list --tag todo

# Start the day with goals
python smartnotes.py add "2026-01-29 Daily goals: 1) Finish API integration 2) Code review for Sarah 3) Prepare Friday demo #journal #goals #daily"

# === DURING WORK (9:00 AM - 5:00 PM) ===

# Quick idea capture (9:15 AM)
python smartnotes.py add "Optimization idea: Cache API responses to reduce rate limit hits #idea #optimization"

# Meeting notes (10:00 AM)
python smartnotes.py add "Standup: API integration at 80%. Sarah's PR needs review. Demo prep starts Thursday. #meeting #standup"

# Save code discovery (11:30 AM)
python smartnotes.py add "Redis cache pattern: SET user:{id} {json_data} EX 3600 for 1hr expiry #coding #redis #cache"

# Problem solution (2:00 PM)
python smartnotes.py add "SOLVED: Rate limit issue fixed by implementing exponential backoff. See retry_handler.py #solved #bugfix"

# Task completion (4:00 PM)
python smartnotes.py edit 11 "[DONE] Contact API provider about rate limit increase. Resolved via exponential backoff instead."

# Remove completed todo tag
python smartnotes.py tag 11 done completed

# === END OF DAY (5:30 PM) ===

# Review what was accomplished
python smartnotes.py list --limit 10

# Daily reflection
python smartnotes.py add "2026-01-29 End of day: API integration complete! Code review done. Good progress on all fronts. Tomorrow: Demo prep focus. #journal #reflection #eod"

# Weekly backup (Fridays)
python smartnotes.py export --format md --output weekly_backup_20260129.md

# View statistics
python smartnotes.py stats
```

**What You Learned:**
- Consistent tagging creates powerful organization
- Edit notes to track status changes
- Daily patterns emerge from journal entries
- Regular exports protect your knowledge base
- Stats help understand note-taking habits

---

## 💡 Pro Tips Summary

### Tag System Recommendations

| Tag | Purpose | Example |
|-----|---------|---------|
| `#todo` | Action items | `python smartnotes.py list --tag todo` |
| `#idea` | Creative thoughts | Capture then review weekly |
| `#meeting` | Meeting notes | Search by date + meeting |
| `#solved` | Problem solutions | Future reference |
| `#journal` | Daily entries | End-of-day reflection |
| `#urgent` | Priority items | Filter for focus time |

### Workflow Automation

```bash
# Create aliases for common commands (Linux/Mac)
alias note="python ~/SmartNotes/smartnotes.py add"
alias todos="python ~/SmartNotes/smartnotes.py list --tag todo"
alias ideas="python ~/SmartNotes/smartnotes.py list --tag idea"

# PowerShell aliases (Windows)
Set-Alias note { python C:\path\to\smartnotes.py add $args }
```

### Best Practices

1. **Capture First, Organize Later** - Don't overthink tags when adding
2. **Consistent Prefixes** - Use date prefixes for chronological notes
3. **Review Weekly** - Use `stats` and `tags` to maintain organization
4. **Export Monthly** - Regular backups to Markdown or JSON
5. **Search Before Adding** - Avoid duplicates with quick search

---

## 📚 More Resources

- **README.md** - Full documentation
- **CHEAT_SHEET.txt** - Quick command reference
- **INTEGRATION_PLAN.md** - Team Brain integration guide
- **GitHub** - https://github.com/DonkRonk17/SmartNotes

---

**Happy Note-Taking! 📝**

*SmartNotes - Capture your thoughts, find them instantly, organize them effortlessly.*
