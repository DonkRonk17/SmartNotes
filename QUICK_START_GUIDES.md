# SmartNotes - Quick Start Guides

**5-minute guides for each Team Brain agent**

---

## 📖 ABOUT THESE GUIDES

Each Team Brain agent has a **5-minute quick-start guide** tailored to their role and workflows.

**Choose your guide:**
- [Forge (Orchestrator)](#-forge-quick-start)
- [Atlas (Executor)](#-atlas-quick-start)
- [Clio (Linux Agent)](#-clio-quick-start)
- [Nexus (Multi-Platform)](#-nexus-quick-start)
- [Bolt (Free Executor)](#-bolt-quick-start)

---

## 🔥 FORGE QUICK START

**Role:** Orchestrator / Reviewer  
**Time:** 5 minutes  
**Goal:** Use SmartNotes for session planning and decision documentation

### Step 1: Verify Installation

```bash
# Check SmartNotes is available
python smartnotes.py --help

# Expected: Shows command help
```

### Step 2: First Use - Session Planning

```bash
# Start your session with a plan note
python smartnotes.py add "Session Plan 2026-01-29: Focus on Q-Mode completion. Assign Atlas to tool builds, Clio to Linux testing. Review all PRs before merge." --tags forge session-plan orchestration
```

### Step 3: Document Decisions

```bash
# Log architecture/design decisions
python smartnotes.py add "Decision: Defer SmartMerge tool to Q2. Reason: Requires external AI API, violates zero-dependency preference. Estimate: 2-3 months." --tags forge decision architecture

# Log review outcomes
python smartnotes.py add "Review: Atlas TokenTracker repair - APPROVED. 45 tests passing, Phase 7 docs complete. Ready for deployment." --tags forge review approved tokentracker
```

### Step 4: Review Previous Context

```bash
# Check previous session notes
python smartnotes.py list --tag forge --limit 10

# Search for specific decisions
python smartnotes.py search "architecture"
```

### Step 5: End-of-Session Handoff

```bash
# Create handoff note
python smartnotes.py add "Handoff: Session complete. Q-Mode 18/18 done. Next priority: Tool repairs (SmartNotes, QuickBackup). Atlas should continue Priority 4 repairs." --tags forge handoff session-end
```

### Forge Tag Convention

| Tag | Usage |
|-----|-------|
| `forge` | All Forge notes |
| `session-plan` | Session planning |
| `decision` | Architecture decisions |
| `review` | Code/tool reviews |
| `handoff` | Agent handoffs |
| `orchestration` | Coordination notes |

### Next Steps for Forge

1. Review `INTEGRATION_PLAN.md` for full integration details
2. Set up SynapseLink integration for team notifications
3. Create daily planning routine with SmartNotes

---

## ⚡ ATLAS QUICK START

**Role:** Executor / Builder  
**Time:** 5 minutes  
**Goal:** Use SmartNotes for build documentation and idea capture

### Step 1: Verify Installation

```bash
# Verify Python import works
python -c "from smartnotes import SmartNotes; print('[OK] SmartNotes available')"
```

### Step 2: First Use - Capture Build Ideas

```bash
# Quick idea capture during build
python smartnotes.py add "Idea: Add progress bar to ContextCompressor for large files. Use tqdm or custom ASCII bar." --tags atlas idea contextcompressor enhancement

# Save code pattern discovered
python smartnotes.py add "Pattern: Use tempfile.mkdtemp() for test isolation. Clean up in tearDown with shutil.rmtree(). Cross-platform safe." --tags atlas pattern testing python
```

### Step 3: Document Error Solutions

```bash
# When you solve a tricky error, capture it!
python smartnotes.py add "SOLVED: UnicodeEncodeError on Windows. Fix: Add sys.stdout.reconfigure(encoding='utf-8') at script start. Or use ASCII alternatives for emojis." --tags atlas solved windows unicode

# Document build blockers
python smartnotes.py add "BLOCKER: Test isolation failing. Root cause: HOME environment variable not being overridden. Fix: Set both HOME and USERPROFILE in setUp." --tags atlas blocker testing solution
```

### Step 4: Track Build Progress

```bash
# Log milestone completions
python smartnotes.py add "Milestone: SmartNotes test suite complete - 42 tests, 100% passing. Phase 5 done." --tags atlas milestone smartnotes testing complete

# Note what's next
python smartnotes.py add "Next: Create Phase 7 integration docs for SmartNotes. Need INTEGRATION_PLAN, QUICK_START_GUIDES, INTEGRATION_EXAMPLES." --tags atlas next smartnotes phase7
```

### Step 5: Review Previous Solutions

```bash
# Find past solutions
python smartnotes.py list --tag solved

# Search for specific error type
python smartnotes.py search "unicode"
```

### Atlas Tag Convention

| Tag | Usage |
|-----|-------|
| `atlas` | All Atlas notes |
| `idea` | Enhancement ideas |
| `pattern` | Reusable code patterns |
| `solved` | Error solutions |
| `blocker` | Current blockers |
| `milestone` | Build milestones |

### Next Steps for Atlas

1. Create a `#solved` knowledge base for common errors
2. Use during every build session
3. Review past patterns before starting new features

---

## 🐧 CLIO QUICK START

**Role:** Linux / Ubuntu Agent  
**Time:** 5 minutes  
**Goal:** Use SmartNotes for Linux-specific documentation

### Step 1: Linux Installation

```bash
# Clone from GitHub
git clone https://github.com/DonkRonk17/SmartNotes.git
cd SmartNotes

# Verify
python3 smartnotes.py --version
```

### Step 2: First Use - Linux Commands

```bash
# Save useful commands discovered
python3 smartnotes.py add "Find process using port: lsof -i:8000 | awk '{print \$2}' | xargs kill -9" --tags clio linux port networking

# Document WSL-specific issues
python3 smartnotes.py add "WSL network reset: wsl --shutdown && netsh winsock reset (run from Windows). Fixes WSL2 networking issues." --tags clio wsl networking windows
```

### Step 3: Track Service Management

```bash
# Document service commands
python3 smartnotes.py add "BCH backend start: cd /path/to/backend && uvicorn main:app --host 0.0.0.0 --port 8000" --tags clio bch service startup

# Note troubleshooting steps
python3 smartnotes.py add "SOLVED: BCH not accessible from Windows. Fix: Bind to 0.0.0.0 not 127.0.0.1 in WSL. Windows uses WSL's virtual IP." --tags clio solved bch wsl networking
```

### Step 4: Configuration Notes

```bash
# Save important configs
python3 smartnotes.py add "Bashrc alias: alias bch='cd ~/BCH && uvicorn main:app --port 8000'" --tags clio config bashrc alias

# Document environment setup
python3 smartnotes.py add "Python venv in WSL: python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt" --tags clio python venv setup
```

### Step 5: Search Linux Solutions

```bash
# Find networking solutions
python3 smartnotes.py search "networking"

# List all WSL notes
python3 smartnotes.py list --tag wsl
```

### Clio Tag Convention

| Tag | Usage |
|-----|-------|
| `clio` | All Clio notes |
| `linux` | Linux-specific |
| `wsl` | WSL configuration |
| `bash` | Shell scripts |
| `service` | Service management |
| `networking` | Network issues |

### Next Steps for Clio

1. Build Linux command knowledge base
2. Document all WSL workarounds
3. Create service startup checklist

---

## 🌐 NEXUS QUICK START

**Role:** Multi-Platform Agent  
**Time:** 5 minutes  
**Goal:** Document cross-platform differences and solutions

### Step 1: Verify Cross-Platform

```python
# Check platform detection
import platform
print(f"Platform: {platform.system()}")

from smartnotes import SmartNotes
notes = SmartNotes()
print(f"Notes dir: {notes.notes_dir}")
```

### Step 2: Document Platform Differences

```bash
# Note platform-specific behaviors
python smartnotes.py add "Path difference: Windows uses backslash (\\), Unix uses forward slash (/). ALWAYS use pathlib.Path for cross-platform compatibility." --tags nexus cross-platform pathlib

# Document API differences
python smartnotes.py add "Clipboard API: Windows=pyperclip or win32clipboard, Linux=xclip subprocess, macOS=pbcopy/pbpaste subprocess." --tags nexus cross-platform clipboard api
```

### Step 3: Track Compatibility Issues

```bash
# Log compatibility bugs
python smartnotes.py add "BUG: Unicode emojis crash Windows console (cp1252 encoding). Solution: Use ASCII alternatives [OK], [X], [!] in Python code." --tags nexus bug windows unicode compatibility

# Note workarounds
python smartnotes.py add "Workaround: sys.stdout.reconfigure(encoding='utf-8') fixes Windows console UTF-8. Only works Python 3.7+." --tags nexus workaround windows encoding
```

### Step 4: Document Environment Detection

```bash
# Platform detection patterns
python smartnotes.py add "Platform detection pattern: import platform; if platform.system() == 'Windows': ... elif platform.system() == 'Darwin': ... else: # Linux" --tags nexus pattern platform-detection python
```

### Step 5: Cross-Platform Testing Notes

```bash
# Document testing approach
python smartnotes.py add "Test strategy: Use tempfile for cross-platform temp dirs. Path.home() works everywhere. Avoid hardcoded paths." --tags nexus testing cross-platform strategy
```

### Nexus Tag Convention

| Tag | Usage |
|-----|-------|
| `nexus` | All Nexus notes |
| `cross-platform` | Compatibility notes |
| `windows` | Windows-specific |
| `linux` | Linux-specific |
| `macos` | macOS-specific |
| `compatibility` | Compatibility issues |

### Next Steps for Nexus

1. Build cross-platform knowledge base
2. Document all platform-specific workarounds
3. Create compatibility testing checklist

---

## 🆓 BOLT QUICK START

**Role:** Free Executor (Cline + Grok)  
**Time:** 5 minutes  
**Goal:** Quick task tracking with minimal overhead

### Step 1: Quick Setup

```bash
# Minimal verification
python smartnotes.py add "Bolt setup complete" --tags bolt setup
```

### Step 2: Task Tracking

```bash
# Quick task start
python smartnotes.py add "Task START: Update README badges for 5 repos" --tags bolt task in-progress

# Progress update
python smartnotes.py add "Progress: README badges - 3/5 repos done" --tags bolt task progress

# Task completion
python smartnotes.py add "Task DONE: README badges complete for all 5 repos" --tags bolt task done
```

### Step 3: Blocker Documentation

```bash
# Note blockers immediately
python smartnotes.py add "BLOCKER: API rate limit hit. Need to wait 60 seconds." --tags bolt blocker api

# Document workaround
python smartnotes.py add "Workaround: Use exponential backoff for API retries. Start 1s, max 60s." --tags bolt workaround api
```

### Step 4: Repetitive Task Solutions

```bash
# Save solutions for tasks you do often
python smartnotes.py add "Batch git push: for d in */; do (cd \"\$d\" && git push origin main); done" --tags bolt pattern bash git

# Document shortcuts
python smartnotes.py add "Quick test all: find . -name 'test_*.py' -exec python {} \\;" --tags bolt pattern bash testing
```

### Step 5: Quick Review

```bash
# What am I working on?
python smartnotes.py list --tag in-progress

# Recent blockers
python smartnotes.py list --tag blocker --limit 5
```

### Bolt Tag Convention

| Tag | Usage |
|-----|-------|
| `bolt` | All Bolt notes |
| `task` | Task tracking |
| `in-progress` | Active tasks |
| `done` | Completed tasks |
| `blocker` | Current blockers |
| `pattern` | Reusable solutions |

### Next Steps for Bolt

1. Use for every task assignment
2. Build pattern library for common tasks
3. Document all blockers and solutions

---

## 📚 ADDITIONAL RESOURCES

**For All Agents:**
- **README.md** - Full documentation
- **EXAMPLES.md** - 10 detailed examples
- **INTEGRATION_PLAN.md** - Integration roadmap
- **INTEGRATION_EXAMPLES.md** - Copy-paste code
- **CHEAT_SHEET.txt** - Quick command reference

**Support:**
- GitHub Issues: https://github.com/DonkRonk17/SmartNotes/issues
- Synapse: Post in THE_SYNAPSE/active/
- Direct: Message FORGE for complex issues

---

## 🎯 RECOMMENDED FIRST STEPS (ALL AGENTS)

1. **Add your first note** - Verify installation works
2. **Create your tag convention** - Use agent name as prefix
3. **Add 5 notes in first session** - Build the habit
4. **Review at session end** - Use `list --limit 10`
5. **Export weekly** - `export --format md`

---

**Last Updated:** January 29, 2026  
**Maintained By:** FORGE (Team Brain)

---

*SmartNotes - Your personal knowledge base, always at your fingertips!*
