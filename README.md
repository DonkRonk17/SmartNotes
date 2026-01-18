<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/94192820-4973-4f39-b298-35115d2c2863" />

# 📝 SmartNotes - AI-Powered Note Taking & Organization

**Never lose a thought again!** SmartNotes is a lightweight, command-line note-taking tool with automatic tagging, full-text search, and smart organization.

Perfect for:
- 💡 Quick idea capture
- 📚 Study notes and research
- 💼 Meeting notes and TODOs
- 🔖 Code snippets and tips
- 📋 Daily journaling

---

## ✨ Features

- **⚡ Lightning Fast** - Add notes in one command
- **🏷️ Auto-Tagging** - Extracts hashtags and keywords automatically
- **🔍 Full-Text Search** - Find any note instantly
- **📋 Tag Organization** - Filter and organize by tags
- **📤 Multi-Format Export** - Export to TXT, Markdown, or JSON
- **🎯 Smart Keywords** - Automatically identifies important terms
- **📊 Statistics** - Track your note-taking habits
- **🌍 Cross-Platform** - Works on Windows, macOS, Linux

---

## 📥 Installation

### Requirements

- Python 3.7+
- No external dependencies!

### Step 1: Download SmartNotes

```bash
# Clone the repository
git clone https://github.com/DonkRonk17/SmartNotes.git
cd SmartNotes

# Or download ZIP and extract
```

### Step 2: Make it Executable (Optional)

#### Windows:
```bash
# Add to PATH or create alias
doskey smartnotes=python "%CD%\smartnotes.py" $*
```

#### macOS/Linux:
```bash
# Make executable
chmod +x smartnotes.py

# Create symlink (optional)
sudo ln -s $(pwd)/smartnotes.py /usr/local/bin/smartnotes
```

### Step 3: Start Taking Notes!

```bash
python smartnotes.py add "My first note!"
```

---

## 🚀 Quick Start Guide

### Add Your First Note

```bash
python smartnotes.py add "Remember to buy groceries #todo"
```

### List All Notes

```bash
python smartnotes.py list
```

### Search Notes

```bash
python smartnotes.py search "groceries"
```

### Filter by Tag

```bash
python smartnotes.py list --tag todo
```

### Show Full Note

```bash
python smartnotes.py show 1
```

---

## 📖 Complete Usage Examples

### Example 1: Quick Idea Capture

```bash
# Add a quick idea
python smartnotes.py add "Build a weather app using OpenWeather API #project #python"

# The hashtags are automatically extracted as tags
# Keywords "weather", "build", "using" are also auto-tagged
```

### Example 2: Study Notes

```bash
# Add study notes with explicit tags
python smartnotes.py add "Photosynthesis converts light energy into chemical energy" --tags biology science

# Add more related notes
python smartnotes.py add "Mitochondria are the powerhouse of the cell #biology"
```

### Example 3: Code Snippets

```bash
# Save a Python tip
python smartnotes.py add "Python tip: Use f-strings for string formatting - faster and cleaner than .format()" --tags python coding tips

# Save a SQL query
python smartnotes.py add "SELECT * FROM users WHERE created_at > '2024-01-01' #sql #database"
```

### Example 4: Daily Journaling

```bash
# Morning journal
python smartnotes.py add "Today's goal: Complete project proposal and exercise for 30 minutes #journal #goals"

# Evening reflection
python smartnotes.py add "Finished proposal! Feeling accomplished. Tomorrow: start implementation. #journal #progress"
```

### Example 5: Meeting Notes

```bash
# Capture meeting notes
python smartnotes.py add "Team meeting: Decided to use React for frontend. Launch date: March 1st. #meeting #work"

# Add action items
python smartnotes.py add "Action item: Set up React project structure by Friday #todo #work"
```

---

## 🎯 Command Reference

### Adding Notes

```bash
# Basic note
python smartnotes.py add "Your note here"

# Note with hashtags (auto-tagged)
python smartnotes.py add "Important reminder #urgent #work"

# Note with explicit tags
python smartnotes.py add "Python list comprehension example" --tags python coding

# Combine hashtags and tags
python smartnotes.py add "Meeting with Bob tomorrow #meeting" --tags work important
```

### Viewing Notes

```bash
# List all notes (newest first)
python smartnotes.py list

# List first 10 notes
python smartnotes.py list --limit 10

# Filter by tag
python smartnotes.py list --tag python

# Search for keywords
python smartnotes.py search "python"

# Show full note details
python smartnotes.py show 5
```

### Editing Notes

```bash
# Update note content
python smartnotes.py edit 5 "Updated note content here"

# Add more tags to existing note
python smartnotes.py tag 5 important urgent

# Delete a note
python smartnotes.py delete 5
```

### Organization

```bash
# List all tags
python smartnotes.py tags

# View statistics
python smartnotes.py stats
```

### Exporting

```bash
# Export all notes as plain text
python smartnotes.py export

# Export as Markdown
python smartnotes.py export --format md

# Export as JSON (machine-readable)
python smartnotes.py export --format json

# Export to specific file
python smartnotes.py export --format md --output my_notes.md
```

---

## 📂 File Storage

SmartNotes stores all data in your home directory:

```
~/.smartnotes/
├── notes.json          # All your notes
└── config.json         # Configuration (future use)
```

**Windows:** `C:\Users\YourName\.smartnotes\`  
**Linux/Mac:** `/home/username/.smartnotes/`

**Your notes are stored locally** - No cloud, no tracking, full privacy!

---

## 🔍 How Auto-Tagging Works

SmartNotes automatically tags your notes in two ways:

### 1. Hashtag Extraction
Any word prefixed with `#` becomes a tag:
```bash
"Remember meeting #important #work" → Tags: important, work
```

### 2. Keyword Extraction
SmartNotes identifies important words (4+ letters, excluding common words):
```bash
"Python list comprehension tutorial" → Tags: python, list, comprehension, tutorial
```

**You can also add explicit tags:**
```bash
--tags python coding tips
```

All tags are combined and deduplicated automatically!

---

## 💡 Pro Tips

### Tip 1: Use Consistent Tags
Create a tagging system for yourself:
- `#todo` - Action items
- `#idea` - Random ideas
- `#work` / `#personal` - Context
- `#urgent` / `#someday` - Priority

### Tip 2: Quick Capture Alias
Create a short alias for faster note-taking:

**Linux/Mac:**
```bash
echo 'alias note="python ~/SmartNotes/smartnotes.py add"' >> ~/.bashrc
# Now you can: note "Quick idea!"
```

**Windows (PowerShell):**
```powershell
Set-Alias note "python C:\path\to\smartnotes.py add"
```

### Tip 3: Daily Note Template
Create a morning routine:
```bash
python smartnotes.py add "$(date +%Y-%m-%d) - Daily goals: " --tags journal daily
```

### Tip 4: Export for Backup
Regularly export your notes:
```bash
python smartnotes.py export --format json --output backup_$(date +%Y%m%d).json
```

### Tip 5: Search Everywhere
Combine search with other commands:
```bash
# Find all Python notes
python smartnotes.py search "python"

# Or by tag
python smartnotes.py list --tag python
```

---

## 🎨 Example Workflow

### Morning Routine
```bash
# Check yesterday's TODOs
python smartnotes.py list --tag todo

# Add today's goals
python smartnotes.py add "Today: Finish report, gym at 5pm #todo #goals"

# Quick idea capture
python smartnotes.py add "App idea: Smart recipe suggester based on ingredients #idea #project"
```

### During the Day
```bash
# Capture meeting notes
python smartnotes.py add "Client wants feature X by next week. Need to discuss timeline. #meeting #work"

# Save code snippet
python smartnotes.py add "Useful regex: ^\d{3}-\d{3}-\d{4}$ for phone numbers #coding #regex"
```

### End of Day
```bash
# Review notes
python smartnotes.py list --limit 10

# Mark TODOs as done (edit or delete)
python smartnotes.py delete 12

# Export weekly backup
python smartnotes.py export --format md --output weekly_notes.md
```

---

## 🐛 Troubleshooting

### "Command not found"
**Solution:** Use full path to Python:
```bash
python3 smartnotes.py add "test"
# or
python smartnotes.py add "test"
```

### "No notes found"
**Solution:** Add a note first:
```bash
python smartnotes.py add "My first note"
```

### "Permission denied"
**Solution:** Check file permissions:
```bash
chmod 644 ~/.smartnotes/notes.json
```

### "Unicode error on Windows"
**Solution:** SmartNotes has built-in UTF-8 handling. If issues persist, try:
```bash
chcp 65001  # Set console to UTF-8
python smartnotes.py list
```

---

## 🔒 Privacy & Security

- ✅ **All data stored locally** - No cloud sync, no network calls
- ✅ **No telemetry** - Zero tracking or analytics
- ✅ **No account needed** - Just run and use
- ✅ **Full control** - Your notes, your computer
- ✅ **Plain JSON** - Easy to backup, migrate, or script

Your notes are **100% private** and stay on your machine.

---

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/f1e05d70-55e4-40a4-8a36-beaba55b2363" />


## 🤝 Contributing

Found a bug? Have a feature idea? Contributions welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📜 License

MIT License - See [LICENSE](LICENSE) file for details

---

## 🌟 Support

If you find SmartNotes useful:
- ⭐ Star this repository
- 🐛 Report bugs via GitHub Issues
- 💡 Suggest features via GitHub Discussions
- 📢 Share with friends who need better note-taking!

---

## 🎉 Why SmartNotes?

**Compared to other note-taking tools:**

| Feature | SmartNotes | Text Files | Notion | Evernote |
|---------|-----------|------------|--------|----------|
| **Speed** | ⚡ Instant | ⚡ Instant | 🐌 Slow | 🐌 Slow |
| **Privacy** | ✅ Local | ✅ Local | ❌ Cloud | ❌ Cloud |
| **Search** | ✅ Full-text | ❌ Manual | ✅ Yes | ✅ Yes |
| **Tags** | ✅ Auto | ❌ Manual | ✅ Manual | ✅ Manual |
| **Export** | ✅ Multi-format | ✅ Yes | ⚠️ Limited | ⚠️ Limited |
| **Cost** | ✅ Free | ✅ Free | 💰 Paid | 💰 Paid |
| **CLI** | ✅ Yes | ✅ Yes | ❌ No | ❌ No |

**SmartNotes = Speed + Privacy + Organization**

---

**Created by Team Brain**  
**Part of the Holy Grail Automation Project**

Capture your thoughts, find them instantly, organize them effortlessly! 📝
