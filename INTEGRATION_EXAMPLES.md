# SmartNotes - Integration Examples

**Copy-paste-ready code for integrating SmartNotes with Team Brain tools**

---

## 🎯 INTEGRATION PHILOSOPHY

SmartNotes is designed as a lightweight local knowledge base that complements other Team Brain tools. These examples provide **copy-paste-ready code** for common integration patterns.

---

## 📚 TABLE OF CONTENTS

1. [Pattern 1: SmartNotes + SynapseLink](#pattern-1-smartnotes--synapselink)
2. [Pattern 2: SmartNotes + SessionReplay](#pattern-2-smartnotes--sessionreplay)
3. [Pattern 3: SmartNotes + AgentHealth](#pattern-3-smartnotes--agenthealth)
4. [Pattern 4: SmartNotes + TaskQueuePro](#pattern-4-smartnotes--taskqueuepro)
5. [Pattern 5: SmartNotes + MemoryBridge](#pattern-5-smartnotes--memorybridge)
6. [Pattern 6: SmartNotes + TokenTracker](#pattern-6-smartnotes--tokentracker)
7. [Pattern 7: SmartNotes + ConfigManager](#pattern-7-smartnotes--configmanager)
8. [Pattern 8: SmartNotes + ContextCompressor](#pattern-8-smartnotes--contextcompressor)
9. [Pattern 9: SmartNotes + ErrorRecovery](#pattern-9-smartnotes--errorrecovery)
10. [Pattern 10: Full Session Workflow](#pattern-10-full-session-workflow)

---

## Pattern 1: SmartNotes + SynapseLink

**Use Case:** Share important notes with team automatically

**Why:** Keep team informed of decisions without manual copy-paste

**Code:**

```python
from synapselink import quick_send
from smartnotes import SmartNotes

def share_decision(decision_text: str, tags: list, recipients: str = "TEAM"):
    """
    Capture a decision in SmartNotes and share via Synapse.
    
    Args:
        decision_text: The decision to document
        tags: List of tags for the note
        recipients: Synapse recipients (default: "TEAM")
    """
    notes = SmartNotes()
    
    # Add to local knowledge base
    notes.add_note(decision_text, tags=tags + ["decision", "shared"])
    
    # Share with team
    quick_send(
        recipients,
        f"Decision: {tags[0] if tags else 'General'}",
        f"{decision_text}\n\n[Logged in SmartNotes with tags: {', '.join(tags)}]",
        priority="NORMAL"
    )
    
    print(f"[OK] Decision logged and shared with {recipients}")

# Example usage
share_decision(
    "Architecture: Use WebSocket for mobile app instead of Socket.IO. "
    "Reason: Simpler implementation, matches desktop pattern.",
    tags=["bch", "mobile", "architecture"],
    recipients="FORGE,CLIO,NEXUS"
)
```

**Result:** Decision is stored locally AND team is notified.

---

## Pattern 2: SmartNotes + SessionReplay

**Use Case:** Create summary notes from session replays

**Why:** Session replays become searchable in SmartNotes

**Code:**

```python
from sessionreplay import SessionReplay
from smartnotes import SmartNotes

def create_session_summary(session_id: str, agent: str):
    """
    Create a SmartNotes entry from a SessionReplay.
    
    Args:
        session_id: The session ID to summarize
        agent: Agent name for tagging
    """
    replay = SessionReplay()
    notes = SmartNotes()
    
    # Get session data
    session = replay.get_session(session_id)
    
    if not session:
        print(f"[X] Session {session_id} not found")
        return False
    
    # Build summary
    summary = f"""Session Summary: {session.task}
Agent: {session.agent}
Duration: {session.duration_minutes:.1f} minutes
Status: {session.status}
Events: {len(session.events)} recorded
Replay ID: {session_id}

Key Outcomes:
- {session.outcomes if hasattr(session, 'outcomes') else 'See replay for details'}
"""
    
    # Add to SmartNotes
    notes.add_note(summary, tags=[
        "session-summary",
        agent.lower(),
        session.date[:10],  # Date portion
        "replay-linked"
    ])
    
    print(f"[OK] Session summary added to SmartNotes")
    return True

# Example usage
create_session_summary("session_20260129_001", "ATLAS")
```

**Result:** Session summaries searchable in SmartNotes.

---

## Pattern 3: SmartNotes + AgentHealth

**Use Case:** Log health anomalies for later review

**Why:** Track patterns in agent health issues

**Code:**

```python
from agenthealth import AgentHealth
from smartnotes import SmartNotes

def log_health_check(agent: str, threshold: float = 0.1):
    """
    Check agent health and log anomalies to SmartNotes.
    
    Args:
        agent: Agent name to check
        threshold: Error rate threshold (default 10%)
    """
    health = AgentHealth()
    notes = SmartNotes()
    
    stats = health.get_agent_stats(agent)
    
    # Check for anomalies
    issues = []
    
    if stats.get("error_rate", 0) > threshold:
        issues.append(f"High error rate: {stats['error_rate']:.1%}")
    
    if stats.get("avg_response_time", 0) > 5.0:
        issues.append(f"Slow response: {stats['avg_response_time']:.1f}s avg")
    
    if stats.get("memory_mb", 0) > 1000:
        issues.append(f"High memory: {stats['memory_mb']:.0f}MB")
    
    if issues:
        notes.add_note(
            f"Health Alert for {agent}:\n" + "\n".join(f"- {i}" for i in issues) +
            f"\n\nSession: {stats.get('session_id', 'unknown')}\n"
            f"Timestamp: {stats.get('timestamp', 'unknown')}",
            tags=["health-alert", agent.lower(), "review-needed"]
        )
        print(f"[!] Health anomaly logged for {agent}")
    else:
        print(f"[OK] {agent} health normal")

# Example usage
log_health_check("ATLAS")
log_health_check("CLIO", threshold=0.05)  # Stricter threshold
```

**Result:** Health issues become trackable patterns.

---

## Pattern 4: SmartNotes + TaskQueuePro

**Use Case:** Document task context when completing tasks

**Why:** Preserve context beyond task queue lifetime

**Code:**

```python
from taskqueuepro import TaskQueuePro
from smartnotes import SmartNotes

def complete_task_with_notes(task_id: str, completion_notes: str = ""):
    """
    Complete a task and document it in SmartNotes.
    
    Args:
        task_id: Task ID to complete
        completion_notes: Additional notes about completion
    """
    queue = TaskQueuePro()
    notes = SmartNotes()
    
    # Get task details
    task = queue.get_task(task_id)
    
    if not task:
        print(f"[X] Task {task_id} not found")
        return False
    
    # Complete the task
    queue.complete_task(task_id)
    
    # Document in SmartNotes
    note_content = f"""Task Completed: {task.title}
Task ID: {task_id}
Agent: {task.agent}
Priority: {task.priority}
Duration: {task.duration if hasattr(task, 'duration') else 'Unknown'}

{f'Notes: {completion_notes}' if completion_notes else ''}
"""
    
    notes.add_note(note_content, tags=[
        "task-complete",
        task.agent.lower(),
        f"priority-{task.priority}",
        task.project.lower() if hasattr(task, 'project') else "general"
    ])
    
    print(f"[OK] Task {task_id} completed and documented")
    return True

# Example usage
complete_task_with_notes(
    "task_456",
    "Used SynapseLink pattern from previous implementation. Consider extracting to shared utility."
)
```

**Result:** Task completion context preserved for future reference.

---

## Pattern 5: SmartNotes + MemoryBridge

**Use Case:** Sync important notes to Memory Core

**Why:** Critical knowledge survives beyond local storage

**Code:**

```python
from memorybridge import MemoryBridge
from smartnotes import SmartNotes

def sync_important_notes_to_memory():
    """
    Sync notes tagged 'important' or 'decision' to Memory Core.
    """
    memory = MemoryBridge()
    notes = SmartNotes()
    
    # Find important notes
    important_tags = ["important", "decision", "architecture", "critical"]
    
    synced_count = 0
    
    for note in notes.notes:
        note_tags = note.get("tags", [])
        
        # Check if note has any important tags
        if any(tag in note_tags for tag in important_tags):
            memory_key = f"smartnote_{note['id']}_{note['created'][:10]}"
            
            memory.save(
                category="smartnotes_archive",
                key=memory_key,
                value={
                    "content": note["content"],
                    "tags": note_tags,
                    "created": note["created"],
                    "synced": True
                }
            )
            synced_count += 1
    
    memory.sync()
    print(f"[OK] Synced {synced_count} important notes to Memory Core")

# Example usage
sync_important_notes_to_memory()
```

**Result:** Critical notes backed up to persistent Memory Core.

---

## Pattern 6: SmartNotes + TokenTracker

**Use Case:** Log expensive operations for budget review

**Why:** Track cost patterns and identify optimization opportunities

**Code:**

```python
from tokentracker import TokenTracker
from smartnotes import SmartNotes

def log_expensive_operation(operation_name: str, cost_threshold: float = 0.25):
    """
    Log operation to SmartNotes if it exceeded cost threshold.
    
    Args:
        operation_name: Name of the operation
        cost_threshold: Cost threshold in dollars (default $0.25)
    """
    tracker = TokenTracker()
    notes = SmartNotes()
    
    usage = tracker.get_session_usage()
    
    if usage.cost > cost_threshold:
        notes.add_note(
            f"Cost Alert: {operation_name}\n"
            f"Cost: ${usage.cost:.4f}\n"
            f"Tokens: {usage.total_tokens:,}\n"
            f"Model: {usage.model}\n"
            f"Threshold: ${cost_threshold:.2f}\n\n"
            f"Consider: Caching, smaller model, or batch processing.",
            tags=["cost-alert", "optimization", operation_name.lower().replace(" ", "-")]
        )
        print(f"[!] High cost operation logged: ${usage.cost:.4f}")
        return True
    else:
        print(f"[OK] Cost within threshold: ${usage.cost:.4f}")
        return False

# Example usage
log_expensive_operation("Large Context Compression", cost_threshold=0.50)
```

**Result:** Cost anomalies tracked for budget review.

---

## Pattern 7: SmartNotes + ConfigManager

**Use Case:** Document configuration changes with rationale

**Why:** Create audit trail for configuration decisions

**Code:**

```python
from configmanager import ConfigManager
from smartnotes import SmartNotes

def change_config_with_notes(key: str, new_value, reason: str):
    """
    Change a config value and document the change.
    
    Args:
        key: Configuration key (e.g., "bch.timeout")
        new_value: New value to set
        reason: Why the change is being made
    """
    config = ConfigManager()
    notes = SmartNotes()
    
    # Get old value
    old_value = config.get(key)
    
    # Make the change
    config.set(key, new_value)
    config.save()
    
    # Document in SmartNotes
    notes.add_note(
        f"Config Change: {key}\n"
        f"Old Value: {old_value}\n"
        f"New Value: {new_value}\n"
        f"Reason: {reason}\n"
        f"Changed By: {config.get('current_agent', 'Unknown')}",
        tags=["config-change", key.split(".")[0], "audit-log"]
    )
    
    print(f"[OK] Config '{key}' changed: {old_value} -> {new_value}")

# Example usage
change_config_with_notes(
    "bch.timeout",
    60,
    "Mobile connections need longer timeout on slow networks"
)
```

**Result:** Configuration changes have documented rationale.

---

## Pattern 8: SmartNotes + ContextCompressor

**Use Case:** Compress and summarize collections of notes

**Why:** Create shareable summaries from large note collections

**Code:**

```python
from contextcompressor import ContextCompressor
from smartnotes import SmartNotes

def summarize_notes_by_tag(tag: str, output_format: str = "summary"):
    """
    Compress all notes with a tag into a summary.
    
    Args:
        tag: Tag to filter notes
        output_format: "summary" or "bullets"
    """
    compressor = ContextCompressor()
    notes = SmartNotes()
    
    # Get notes with tag
    tagged_notes = [n for n in notes.notes if tag in n.get("tags", [])]
    
    if not tagged_notes:
        print(f"[X] No notes found with tag: {tag}")
        return None
    
    # Combine note contents
    combined = "\n---\n".join([
        f"[{n['created'][:10]}] {n['content']}"
        for n in tagged_notes
    ])
    
    # Compress
    compressed = compressor.compress_text(
        combined,
        query=f"key points about {tag}",
        method=output_format
    )
    
    print(f"[OK] Compressed {len(tagged_notes)} notes ({len(combined)} -> {len(compressed.compressed_text)} chars)")
    print(f"\nSummary:\n{compressed.compressed_text}")
    
    return compressed.compressed_text

# Example usage
summary = summarize_notes_by_tag("decision", output_format="bullets")
```

**Result:** Large note collections become shareable summaries.

---

## Pattern 9: SmartNotes + ErrorRecovery

**Use Case:** Build searchable error solution database

**Why:** Don't solve the same error twice

**Code:**

```python
from errorrecovery import ErrorRecovery
from smartnotes import SmartNotes

def log_error_solution(error_type: str, error_message: str, solution: str, tags: list = None):
    """
    Log an error and its solution to both ErrorRecovery and SmartNotes.
    
    Args:
        error_type: Type of error (e.g., "ImportError", "NetworkError")
        error_message: The actual error message
        solution: How it was fixed
        tags: Additional tags
    """
    recovery = ErrorRecovery()
    notes = SmartNotes()
    
    # Log to ErrorRecovery
    recovery.log_error(
        error_type=error_type,
        message=error_message,
        solution=solution
    )
    
    # Also log to SmartNotes for broader searchability
    all_tags = ["solved", error_type.lower()]
    if tags:
        all_tags.extend(tags)
    
    notes.add_note(
        f"SOLVED: {error_type}\n\n"
        f"Error: {error_message}\n\n"
        f"Solution: {solution}",
        tags=all_tags
    )
    
    print(f"[OK] Error solution logged to ErrorRecovery and SmartNotes")

# Example usage
log_error_solution(
    "UnicodeEncodeError",
    "UnicodeEncodeError: 'charmap' codec can't encode character '\\u2713'",
    "Use ASCII alternatives like [OK] instead of emojis. Or add sys.stdout.reconfigure(encoding='utf-8') at script start.",
    tags=["windows", "encoding", "python"]
)
```

**Result:** Errors are logged in both systems for maximum findability.

---

## Pattern 10: Full Session Workflow

**Use Case:** Complete agent session with full tool integration

**Why:** Demonstrate how all tools work together

**Code:**

```python
from smartnotes import SmartNotes
from synapselink import quick_send
from agenthealth import AgentHealth
from sessionreplay import SessionReplay
from taskqueuepro import TaskQueuePro

class IntegratedSession:
    """
    Full session workflow integrating SmartNotes with Team Brain tools.
    """
    
    def __init__(self, agent: str, task_description: str):
        self.agent = agent
        self.task = task_description
        
        # Initialize all tools
        self.notes = SmartNotes()
        self.health = AgentHealth()
        self.replay = SessionReplay()
        self.queue = TaskQueuePro()
        
        # Start session
        self.session_id = None
        
    def start(self):
        """Start the integrated session."""
        # Start health monitoring
        self.health.start_session(self.agent)
        
        # Start session replay
        self.session_id = self.replay.start_session(self.agent, task=self.task)
        
        # Log session start
        self.notes.add_note(
            f"Session Start: {self.task}\n"
            f"Agent: {self.agent}\n"
            f"Session ID: {self.session_id}",
            tags=[self.agent.lower(), "session-start"]
        )
        
        print(f"[OK] Session started: {self.session_id}")
        return self
    
    def log_progress(self, message: str, tags: list = None):
        """Log progress during session."""
        all_tags = [self.agent.lower(), "progress"]
        if tags:
            all_tags.extend(tags)
        
        self.notes.add_note(message, tags=all_tags)
        self.replay.log_event(self.session_id, "progress", message)
        self.health.heartbeat(self.agent, status="active")
        
    def log_decision(self, decision: str, rationale: str, notify_team: bool = False):
        """Log a decision with optional team notification."""
        full_text = f"Decision: {decision}\nRationale: {rationale}"
        
        self.notes.add_note(full_text, tags=[
            self.agent.lower(), "decision", "session-decision"
        ])
        
        self.replay.log_event(self.session_id, "decision", full_text)
        
        if notify_team:
            quick_send(
                "TEAM",
                f"Decision from {self.agent}",
                full_text,
                priority="NORMAL"
            )
    
    def log_error(self, error: str, solution: str = None):
        """Log an error (and solution if known)."""
        content = f"Error: {error}"
        tags = [self.agent.lower(), "error"]
        
        if solution:
            content += f"\nSolution: {solution}"
            tags.append("solved")
        
        self.notes.add_note(content, tags=tags)
        self.replay.log_event(self.session_id, "error", content)
        self.health.log_error(self.agent, error)
    
    def end(self, status: str = "completed", summary: str = ""):
        """End the integrated session."""
        # End health monitoring
        self.health.end_session(self.agent, status=status)
        
        # End session replay
        self.replay.end_session(self.session_id, status=status.upper())
        
        # Create final summary note
        self.notes.add_note(
            f"Session End: {self.task}\n"
            f"Status: {status}\n"
            f"Session ID: {self.session_id}\n"
            f"{f'Summary: {summary}' if summary else ''}",
            tags=[self.agent.lower(), "session-end", status]
        )
        
        print(f"[OK] Session ended: {status}")


# Example usage
def run_example_session():
    """Run an example integrated session."""
    
    # Create session
    session = IntegratedSession("ATLAS", "Build SmartNotes Phase 7 docs")
    session.start()
    
    # Log progress
    session.log_progress("Created INTEGRATION_PLAN.md - 450 lines")
    session.log_progress("Created QUICK_START_GUIDES.md - 350 lines")
    
    # Log a decision
    session.log_decision(
        "Include 10 integration patterns in INTEGRATION_EXAMPLES.md",
        "Covers all major Team Brain tools, provides copy-paste code",
        notify_team=False
    )
    
    # Simulate error and solution
    session.log_error(
        "Test isolation failed - HOME not being overridden",
        "Set both HOME and USERPROFILE environment variables in setUp"
    )
    
    # End session
    session.end(
        status="completed",
        summary="All Phase 7 docs created. 42 tests passing."
    )

# Run the example
if __name__ == "__main__":
    run_example_session()
```

**Result:** Fully integrated session with all tools working together.

---

## 📊 RECOMMENDED INTEGRATION PRIORITY

### Week 1 (Essential)
1. ✅ SynapseLink - Team notification
2. ✅ ErrorRecovery - Solution tracking
3. ✅ SessionReplay - Session documentation

### Week 2 (Productivity)
4. ☐ TaskQueuePro - Task documentation
5. ☐ AgentHealth - Health tracking
6. ☐ ConfigManager - Config audit trail

### Week 3 (Advanced)
7. ☐ MemoryBridge - Persistent backup
8. ☐ ContextCompressor - Note summarization
9. ☐ TokenTracker - Cost tracking
10. ☐ Full integrated workflow

---

## 🔧 TROUBLESHOOTING INTEGRATIONS

### Import Errors

```python
# Ensure tools are in Python path
import sys
from pathlib import Path

# Add AutoProjects to path
sys.path.append(str(Path.home() / "OneDrive/Documents/AutoProjects"))

# Now import
from smartnotes import SmartNotes
```

### SmartNotes Not Saving

```python
# Check write permissions
notes = SmartNotes()
print(f"Notes directory: {notes.notes_dir}")
print(f"Writable: {os.access(notes.notes_dir, os.W_OK)}")
```

### Tag Filtering Not Working

```python
# Tags are always lowercase
notes.list_notes(tag_filter="python")  # OK
notes.list_notes(tag_filter="Python")  # Won't match!
```

### Integration Tool Not Found

```bash
# Check tool is installed
python -c "from toolname import ToolClass; print('OK')"

# If not, ensure AutoProjects is in PYTHONPATH
export PYTHONPATH="$PYTHONPATH:$HOME/OneDrive/Documents/AutoProjects"
```

---

## 📚 ADDITIONAL RESOURCES

- **README.md** - Full SmartNotes documentation
- **EXAMPLES.md** - 10 usage examples
- **INTEGRATION_PLAN.md** - Integration roadmap
- **QUICK_START_GUIDES.md** - Agent-specific guides
- **CHEAT_SHEET.txt** - Quick reference

**GitHub:** https://github.com/DonkRonk17/SmartNotes

---

**Last Updated:** January 29, 2026  
**Maintained By:** FORGE (Team Brain)

---

*SmartNotes - The knowledge hub for Team Brain workflows!*
