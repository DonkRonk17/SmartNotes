#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SmartNotes - AI-Powered Note Taking & Organization
==================================================
Quick, searchable, organized note-taking from the command line.

Author: Team Brain / Forge
License: MIT
"""

import os
import sys
import json
import re
from pathlib import Path
from datetime import datetime
import argparse

# Fix Windows console encoding
if sys.platform == "win32":
    try:
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'replace')
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'replace')
    except:
        pass


class SmartNotes:
    """Main SmartNotes application class."""

    def __init__(self):
        """Initialize SmartNotes with config directory."""
        self.notes_dir = Path.home() / ".smartnotes"
        self.notes_dir.mkdir(exist_ok=True)
        self.notes_file = self.notes_dir / "notes.json"
        self.config_file = self.notes_dir / "config.json"
        self.load_notes()
        self.load_config()

    def load_notes(self):
        """Load notes from JSON file."""
        if self.notes_file.exists():
            try:
                with open(self.notes_file, "r", encoding="utf-8") as f:
                    self.notes = json.load(f)
            except Exception as e:
                print(f"Warning: Could not load notes: {e}")
                self.notes = []
        else:
            self.notes = []

    def save_notes(self):
        """Save notes to JSON file."""
        try:
            with open(self.notes_file, "w", encoding="utf-8") as f:
                json.dump(self.notes, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"[X] Error saving notes: {e}")
            return False
        return True

    def load_config(self):
        """Load configuration."""
        if self.config_file.exists():
            try:
                with open(self.config_file, "r") as f:
                    self.config = json.load(f)
            except:
                self.config = {"default_tags": []}
        else:
            self.config = {"default_tags": []}

    def extract_tags(self, text):
        """Extract hashtags from text."""
        tags = re.findall(r'#(\w+)', text)
        return [tag.lower() for tag in tags]

    def extract_keywords(self, text):
        """Extract potential keywords from text (simple approach)."""
        # Remove punctuation and split
        words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
        # Common words to exclude
        stop_words = {'that', 'this', 'with', 'have', 'from', 'they', 'been',
                      'were', 'said', 'each', 'which', 'their', 'there', 'would',
                      'make', 'like', 'into', 'time', 'than', 'them', 'some'}
        keywords = [w for w in words if w not in stop_words]
        # Return top keywords (max 3)
        return list(set(keywords))[:3]

    def add_note(self, content, tags=None):
        """Add a new note."""
        if not content.strip():
            print("[X] Cannot add empty note!")
            return False

        # Extract hashtags from content
        extracted_tags = self.extract_tags(content)

        # Extract keywords as auto-tags
        keywords = self.extract_keywords(content)

        # Combine all tags
        all_tags = extracted_tags + keywords
        if tags:
            all_tags.extend(tags)

        # Remove duplicates
        all_tags = list(set(all_tags))

        note = {
            "id": len(self.notes) + 1,
            "content": content,
            "tags": all_tags,
            "created": datetime.now().isoformat(),
            "modified": datetime.now().isoformat(),
        }

        self.notes.append(note)

        if self.save_notes():
            print(f"[OK] Note #{note['id']} added")
            if all_tags:
                print(f"     Tags: {', '.join(all_tags)}")
            return True
        return False

    def list_notes(self, tag_filter=None, search_term=None, limit=None):
        """List all notes or filtered notes."""
        filtered_notes = self.notes

        # Filter by tag
        if tag_filter:
            filtered_notes = [n for n in filtered_notes if tag_filter.lower() in n.get("tags", [])]

        # Filter by search term
        if search_term:
            search_lower = search_term.lower()
            filtered_notes = [n for n in filtered_notes if search_lower in n.get("content", "").lower()]

        # Sort by created date (newest first)
        filtered_notes = sorted(filtered_notes, key=lambda x: x.get("created", ""), reverse=True)

        # Limit results
        if limit:
            filtered_notes = filtered_notes[:limit]

        if not filtered_notes:
            print("No notes found.")
            return

        print(f"\n[{len(filtered_notes)} note(s) found]\n")

        for note in filtered_notes:
            note_id = note.get("id", "?")
            content = note.get("content", "")
            tags = note.get("tags", [])
            created = note.get("created", "")[:19]

            # Truncate long notes
            if len(content) > 80:
                content = content[:77] + "..."

            print(f"#{note_id} | {created}")
            print(f"    {content}")
            if tags:
                print(f"    Tags: {', '.join(tags)}")
            print()

    def show_note(self, note_id):
        """Show full note details."""
        note = self.get_note_by_id(note_id)
        if not note:
            print(f"[X] Note #{note_id} not found!")
            return False

        print(f"\n{'='*60}")
        print(f"Note #{note['id']}")
        print(f"{'='*60}")
        print(f"\nCreated:  {note['created'][:19]}")
        print(f"Modified: {note['modified'][:19]}")
        print(f"\nContent:\n{note['content']}")

        if note.get("tags"):
            print(f"\nTags: {', '.join(note['tags'])}")

        print(f"\n{'='*60}\n")
        return True

    def get_note_by_id(self, note_id):
        """Get note by ID."""
        for note in self.notes:
            if note.get("id") == note_id:
                return note
        return None

    def edit_note(self, note_id, new_content):
        """Edit an existing note."""
        note = self.get_note_by_id(note_id)
        if not note:
            print(f"[X] Note #{note_id} not found!")
            return False

        note["content"] = new_content
        note["modified"] = datetime.now().isoformat()

        # Re-extract tags
        extracted_tags = self.extract_tags(new_content)
        keywords = self.extract_keywords(new_content)
        note["tags"] = list(set(extracted_tags + keywords))

        if self.save_notes():
            print(f"[OK] Note #{note_id} updated")
            return True
        return False

    def delete_note(self, note_id):
        """Delete a note."""
        note = self.get_note_by_id(note_id)
        if not note:
            print(f"[X] Note #{note_id} not found!")
            return False

        self.notes = [n for n in self.notes if n.get("id") != note_id]

        if self.save_notes():
            print(f"[OK] Note #{note_id} deleted")
            return True
        return False

    def tag_note(self, note_id, tags):
        """Add tags to a note."""
        note = self.get_note_by_id(note_id)
        if not note:
            print(f"[X] Note #{note_id} not found!")
            return False

        existing_tags = note.get("tags", [])
        new_tags = [t.lower().strip('#') for t in tags]
        note["tags"] = list(set(existing_tags + new_tags))
        note["modified"] = datetime.now().isoformat()

        if self.save_notes():
            print(f"[OK] Tags added to note #{note_id}: {', '.join(new_tags)}")
            return True
        return False

    def list_tags(self):
        """List all unique tags."""
        all_tags = set()
        for note in self.notes:
            all_tags.update(note.get("tags", []))

        if not all_tags:
            print("No tags found.")
            return

        sorted_tags = sorted(all_tags)
        print(f"\n[{len(sorted_tags)} unique tag(s)]\n")
        for tag in sorted_tags:
            # Count notes with this tag
            count = sum(1 for n in self.notes if tag in n.get("tags", []))
            print(f"  #{tag} ({count} note(s))")
        print()

    def export_notes(self, format="txt", output_file=None):
        """Export notes to file."""
        if not self.notes:
            print("[X] No notes to export!")
            return False

        if not output_file:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"notes_export_{timestamp}.{format}"

        try:
            if format == "txt":
                self._export_txt(output_file)
            elif format == "md":
                self._export_markdown(output_file)
            elif format == "json":
                self._export_json(output_file)
            else:
                print(f"[X] Unsupported format: {format}")
                return False

            print(f"[OK] Notes exported to: {output_file}")
            return True
        except Exception as e:
            print(f"[X] Export failed: {e}")
            return False

    def _export_txt(self, filename):
        """Export as plain text."""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"SmartNotes Export - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 60 + "\n\n")

            for note in sorted(self.notes, key=lambda x: x.get("created", "")):
                f.write(f"Note #{note['id']}\n")
                f.write(f"Created: {note['created'][:19]}\n")
                if note.get("tags"):
                    f.write(f"Tags: {', '.join(note['tags'])}\n")
                f.write(f"\n{note['content']}\n")
                f.write("\n" + "-" * 60 + "\n\n")

    def _export_markdown(self, filename):
        """Export as Markdown."""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# SmartNotes Export\n\n")
            f.write(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n")
            f.write("---\n\n")

            for note in sorted(self.notes, key=lambda x: x.get("created", "")):
                f.write(f"## Note #{note['id']}\n\n")
                f.write(f"**Created:** {note['created'][:19]}  \n")
                if note.get("tags"):
                    tags_md = " ".join([f"`#{t}`" for t in note['tags']])
                    f.write(f"**Tags:** {tags_md}  \n")
                f.write(f"\n{note['content']}\n\n")
                f.write("---\n\n")

    def _export_json(self, filename):
        """Export as JSON."""
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.notes, f, indent=2, ensure_ascii=False)

    def get_stats(self):
        """Get statistics about notes."""
        if not self.notes:
            print("No notes yet. Add one with: smartnotes add \"Your note here\"")
            return

        total_notes = len(self.notes)
        all_tags = set()
        for note in self.notes:
            all_tags.update(note.get("tags", []))

        total_chars = sum(len(n.get("content", "")) for n in self.notes)
        avg_length = total_chars // total_notes if total_notes > 0 else 0

        # Find most recent note
        recent = max(self.notes, key=lambda x: x.get("created", ""))

        print(f"\n{'='*40}")
        print(f"  SmartNotes Statistics")
        print(f"{'='*40}")
        print(f"Total notes:      {total_notes}")
        print(f"Total tags:       {len(all_tags)}")
        print(f"Average length:   {avg_length} characters")
        print(f"Most recent:      {recent['created'][:19]}")
        print(f"Storage location: {self.notes_file}")
        print(f"{'='*40}\n")


def main():
    """Main CLI interface."""
    parser = argparse.ArgumentParser(
        description="SmartNotes - AI-Powered Note Taking & Organization",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  smartnotes add "Remember to call Bob tomorrow #important"
  smartnotes add "Python tip: use list comprehensions" --tags python coding
  smartnotes list
  smartnotes list --tag important
  smartnotes search "Python"
  smartnotes show 5
  smartnotes edit 5 "Updated note content"
  smartnotes delete 5
  smartnotes export --format md --output my_notes.md
  smartnotes stats
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Add command
    parser_add = subparsers.add_parser("add", help="Add a new note")
    parser_add.add_argument("content", help="Note content")
    parser_add.add_argument("--tags", nargs="+", help="Additional tags")

    # List command
    parser_list = subparsers.add_parser("list", help="List all notes")
    parser_list.add_argument("--tag", help="Filter by tag")
    parser_list.add_argument("--limit", type=int, help="Limit number of results")

    # Search command
    parser_search = subparsers.add_parser("search", help="Search notes")
    parser_search.add_argument("term", help="Search term")
    parser_search.add_argument("--limit", type=int, help="Limit number of results")

    # Show command
    parser_show = subparsers.add_parser("show", help="Show full note")
    parser_show.add_argument("id", type=int, help="Note ID")

    # Edit command
    parser_edit = subparsers.add_parser("edit", help="Edit a note")
    parser_edit.add_argument("id", type=int, help="Note ID")
    parser_edit.add_argument("content", help="New content")

    # Delete command
    parser_delete = subparsers.add_parser("delete", help="Delete a note")
    parser_delete.add_argument("id", type=int, help="Note ID")

    # Tag command
    parser_tag = subparsers.add_parser("tag", help="Add tags to a note")
    parser_tag.add_argument("id", type=int, help="Note ID")
    parser_tag.add_argument("tags", nargs="+", help="Tags to add")

    # Tags command
    subparsers.add_parser("tags", help="List all tags")

    # Export command
    parser_export = subparsers.add_parser("export", help="Export notes")
    parser_export.add_argument("--format", choices=["txt", "md", "json"], default="txt", help="Export format")
    parser_export.add_argument("--output", help="Output filename")

    # Stats command
    subparsers.add_parser("stats", help="Show statistics")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    notes = SmartNotes()

    if args.command == "add":
        notes.add_note(args.content, args.tags)

    elif args.command == "list":
        notes.list_notes(tag_filter=args.tag, limit=args.limit)

    elif args.command == "search":
        notes.list_notes(search_term=args.term, limit=args.limit)

    elif args.command == "show":
        notes.show_note(args.id)

    elif args.command == "edit":
        notes.edit_note(args.id, args.content)

    elif args.command == "delete":
        notes.delete_note(args.id)

    elif args.command == "tag":
        notes.tag_note(args.id, args.tags)

    elif args.command == "tags":
        notes.list_tags()

    elif args.command == "export":
        notes.export_notes(format=args.format, output_file=args.output)

    elif args.command == "stats":
        notes.get_stats()


if __name__ == "__main__":
    main()
