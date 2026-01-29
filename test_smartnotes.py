#!/usr/bin/env python3
"""
Comprehensive test suite for SmartNotes.

Tests cover:
- Core functionality (add, list, show, edit, delete, tag)
- Edge cases (empty input, invalid IDs)
- Error handling (file errors, encoding)
- Export functionality (txt, md, json)
- Search and filtering
- Tag extraction and management
- Statistics

Run: python test_smartnotes.py
"""

import unittest
import sys
import os
import json
import tempfile
import shutil
from pathlib import Path
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from smartnotes import SmartNotes


class TestSmartNotesInitialization(unittest.TestCase):
    """Test SmartNotes initialization."""

    def setUp(self):
        """Set up test environment with temp directory."""
        self.temp_dir = tempfile.mkdtemp()
        self.original_home = os.environ.get('HOME', '')
        self.original_userprofile = os.environ.get('USERPROFILE', '')
        
        # Point SmartNotes to temp directory
        os.environ['HOME'] = self.temp_dir
        os.environ['USERPROFILE'] = self.temp_dir

    def tearDown(self):
        """Clean up temp directory."""
        os.environ['HOME'] = self.original_home
        os.environ['USERPROFILE'] = self.original_userprofile
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_initialization_creates_directory(self):
        """Test that initialization creates the .smartnotes directory."""
        notes = SmartNotes()
        expected_dir = Path(self.temp_dir) / ".smartnotes"
        self.assertTrue(expected_dir.exists())

    def test_initialization_with_empty_notes(self):
        """Test initialization with no existing notes."""
        notes = SmartNotes()
        self.assertEqual(len(notes.notes), 0)

    def test_initialization_loads_existing_notes(self):
        """Test that existing notes are loaded on init."""
        # Create notes file first
        notes_dir = Path(self.temp_dir) / ".smartnotes"
        notes_dir.mkdir(exist_ok=True)
        notes_file = notes_dir / "notes.json"
        
        test_notes = [
            {"id": 1, "content": "Test note", "tags": ["test"], 
             "created": "2026-01-01T00:00:00", "modified": "2026-01-01T00:00:00"}
        ]
        
        with open(notes_file, "w") as f:
            json.dump(test_notes, f)
        
        notes = SmartNotes()
        self.assertEqual(len(notes.notes), 1)
        self.assertEqual(notes.notes[0]["content"], "Test note")


class TestSmartNotesAddNote(unittest.TestCase):
    """Test adding notes."""

    def setUp(self):
        """Set up test environment."""
        self.temp_dir = tempfile.mkdtemp()
        os.environ['HOME'] = self.temp_dir
        os.environ['USERPROFILE'] = self.temp_dir
        self.notes = SmartNotes()

    def tearDown(self):
        """Clean up."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_add_simple_note(self):
        """Test adding a simple note."""
        result = self.notes.add_note("This is a test note")
        self.assertTrue(result)
        self.assertEqual(len(self.notes.notes), 1)
        self.assertEqual(self.notes.notes[0]["content"], "This is a test note")

    def test_add_note_with_hashtags(self):
        """Test that hashtags are extracted as tags."""
        self.notes.add_note("Remember to #work on #project")
        note = self.notes.notes[0]
        self.assertIn("work", note["tags"])
        self.assertIn("project", note["tags"])

    def test_add_note_with_explicit_tags(self):
        """Test adding note with explicit tags."""
        self.notes.add_note("Important meeting", tags=["meeting", "urgent"])
        note = self.notes.notes[0]
        self.assertIn("meeting", note["tags"])
        self.assertIn("urgent", note["tags"])

    def test_add_note_extracts_keywords(self):
        """Test automatic keyword extraction."""
        self.notes.add_note("Python programming tutorial example")
        note = self.notes.notes[0]
        # Keywords are extracted (4+ letter words)
        self.assertTrue(len(note["tags"]) > 0)

    def test_add_empty_note_fails(self):
        """Test that empty notes are rejected."""
        result = self.notes.add_note("")
        self.assertFalse(result)
        self.assertEqual(len(self.notes.notes), 0)

    def test_add_whitespace_only_note_fails(self):
        """Test that whitespace-only notes are rejected."""
        result = self.notes.add_note("   ")
        self.assertFalse(result)

    def test_add_note_sets_id(self):
        """Test that notes get sequential IDs."""
        self.notes.add_note("Note 1")
        self.notes.add_note("Note 2")
        self.assertEqual(self.notes.notes[0]["id"], 1)
        self.assertEqual(self.notes.notes[1]["id"], 2)

    def test_add_note_sets_timestamps(self):
        """Test that notes get created and modified timestamps."""
        self.notes.add_note("Timestamped note")
        note = self.notes.notes[0]
        self.assertIn("created", note)
        self.assertIn("modified", note)
        # Should be valid ISO format
        datetime.fromisoformat(note["created"])
        datetime.fromisoformat(note["modified"])


class TestSmartNotesListNotes(unittest.TestCase):
    """Test listing and filtering notes."""

    def setUp(self):
        """Set up test environment with some notes."""
        self.temp_dir = tempfile.mkdtemp()
        os.environ['HOME'] = self.temp_dir
        os.environ['USERPROFILE'] = self.temp_dir
        self.notes = SmartNotes()
        
        # Add test notes
        self.notes.add_note("First note #python")
        self.notes.add_note("Second note #work")
        self.notes.add_note("Third note #python #work")

    def tearDown(self):
        """Clean up."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_list_all_notes(self):
        """Test listing all notes."""
        # Should not raise exception
        self.notes.list_notes()
        self.assertEqual(len(self.notes.notes), 3)

    def test_filter_by_tag(self):
        """Test filtering notes by tag."""
        filtered = [n for n in self.notes.notes if "python" in n.get("tags", [])]
        self.assertEqual(len(filtered), 2)

    def test_filter_by_search_term(self):
        """Test searching notes."""
        filtered = [n for n in self.notes.notes if "first" in n.get("content", "").lower()]
        self.assertEqual(len(filtered), 1)

    def test_limit_results(self):
        """Test limiting number of results."""
        # list_notes prints output, just verify it doesn't crash
        self.notes.list_notes(limit=2)


class TestSmartNotesShowNote(unittest.TestCase):
    """Test showing individual notes."""

    def setUp(self):
        """Set up test environment."""
        self.temp_dir = tempfile.mkdtemp()
        os.environ['HOME'] = self.temp_dir
        os.environ['USERPROFILE'] = self.temp_dir
        self.notes = SmartNotes()
        self.notes.add_note("Test note content")

    def tearDown(self):
        """Clean up."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_show_existing_note(self):
        """Test showing an existing note."""
        result = self.notes.show_note(1)
        self.assertTrue(result)

    def test_show_nonexistent_note(self):
        """Test showing a note that doesn't exist."""
        result = self.notes.show_note(999)
        self.assertFalse(result)


class TestSmartNotesEditNote(unittest.TestCase):
    """Test editing notes."""

    def setUp(self):
        """Set up test environment."""
        self.temp_dir = tempfile.mkdtemp()
        os.environ['HOME'] = self.temp_dir
        os.environ['USERPROFILE'] = self.temp_dir
        self.notes = SmartNotes()
        self.notes.add_note("Original content")

    def tearDown(self):
        """Clean up."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_edit_existing_note(self):
        """Test editing an existing note."""
        result = self.notes.edit_note(1, "Updated content")
        self.assertTrue(result)
        self.assertEqual(self.notes.notes[0]["content"], "Updated content")

    def test_edit_updates_modified_timestamp(self):
        """Test that editing updates the modified timestamp."""
        original_modified = self.notes.notes[0]["modified"]
        import time
        time.sleep(0.01)  # Ensure time difference
        self.notes.edit_note(1, "New content")
        new_modified = self.notes.notes[0]["modified"]
        self.assertNotEqual(original_modified, new_modified)

    def test_edit_nonexistent_note(self):
        """Test editing a note that doesn't exist."""
        result = self.notes.edit_note(999, "New content")
        self.assertFalse(result)

    def test_edit_updates_tags(self):
        """Test that editing re-extracts tags."""
        self.notes.edit_note(1, "New content with #newtag")
        self.assertIn("newtag", self.notes.notes[0]["tags"])


class TestSmartNotesDeleteNote(unittest.TestCase):
    """Test deleting notes."""

    def setUp(self):
        """Set up test environment."""
        self.temp_dir = tempfile.mkdtemp()
        os.environ['HOME'] = self.temp_dir
        os.environ['USERPROFILE'] = self.temp_dir
        self.notes = SmartNotes()
        self.notes.add_note("Note to delete")

    def tearDown(self):
        """Clean up."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_delete_existing_note(self):
        """Test deleting an existing note."""
        result = self.notes.delete_note(1)
        self.assertTrue(result)
        self.assertEqual(len(self.notes.notes), 0)

    def test_delete_nonexistent_note(self):
        """Test deleting a note that doesn't exist."""
        result = self.notes.delete_note(999)
        self.assertFalse(result)

    def test_delete_persists(self):
        """Test that deletion is persisted."""
        self.notes.delete_note(1)
        # Reload notes
        notes2 = SmartNotes()
        self.assertEqual(len(notes2.notes), 0)


class TestSmartNotesTagging(unittest.TestCase):
    """Test tagging functionality."""

    def setUp(self):
        """Set up test environment."""
        self.temp_dir = tempfile.mkdtemp()
        os.environ['HOME'] = self.temp_dir
        os.environ['USERPROFILE'] = self.temp_dir
        self.notes = SmartNotes()
        self.notes.add_note("Test note")

    def tearDown(self):
        """Clean up."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_add_tags_to_note(self):
        """Test adding tags to an existing note."""
        result = self.notes.tag_note(1, ["important", "urgent"])
        self.assertTrue(result)
        self.assertIn("important", self.notes.notes[0]["tags"])
        self.assertIn("urgent", self.notes.notes[0]["tags"])

    def test_tag_nonexistent_note(self):
        """Test tagging a note that doesn't exist."""
        result = self.notes.tag_note(999, ["tag"])
        self.assertFalse(result)

    def test_list_all_tags(self):
        """Test listing all unique tags."""
        self.notes.add_note("Note with #tag1 and #tag2")
        # Should not raise exception
        self.notes.list_tags()

    def test_tags_are_normalized(self):
        """Test that tags are lowercased and stripped."""
        self.notes.tag_note(1, ["#Important", "  URGENT  "])
        tags = self.notes.notes[0]["tags"]
        self.assertIn("important", tags)
        self.assertIn("urgent", tags)


class TestSmartNotesExport(unittest.TestCase):
    """Test export functionality."""

    def setUp(self):
        """Set up test environment."""
        self.temp_dir = tempfile.mkdtemp()
        os.environ['HOME'] = self.temp_dir
        os.environ['USERPROFILE'] = self.temp_dir
        self.notes = SmartNotes()
        self.notes.add_note("Export test note #test")
        self.export_file = Path(self.temp_dir) / "export_test"

    def tearDown(self):
        """Clean up."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_export_txt(self):
        """Test exporting as plain text."""
        output_file = str(self.export_file) + ".txt"
        result = self.notes.export_notes(format="txt", output_file=output_file)
        self.assertTrue(result)
        self.assertTrue(Path(output_file).exists())
        
        with open(output_file, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("Export test note", content)

    def test_export_markdown(self):
        """Test exporting as Markdown."""
        output_file = str(self.export_file) + ".md"
        result = self.notes.export_notes(format="md", output_file=output_file)
        self.assertTrue(result)
        
        with open(output_file, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("# SmartNotes Export", content)

    def test_export_json(self):
        """Test exporting as JSON."""
        output_file = str(self.export_file) + ".json"
        result = self.notes.export_notes(format="json", output_file=output_file)
        self.assertTrue(result)
        
        with open(output_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["content"], "Export test note #test")

    def test_export_empty_fails(self):
        """Test that exporting with no notes fails gracefully."""
        self.notes.notes = []
        result = self.notes.export_notes(format="txt")
        self.assertFalse(result)

    def test_export_invalid_format(self):
        """Test that invalid format is rejected."""
        result = self.notes.export_notes(format="invalid")
        self.assertFalse(result)


class TestSmartNotesStats(unittest.TestCase):
    """Test statistics functionality."""

    def setUp(self):
        """Set up test environment."""
        self.temp_dir = tempfile.mkdtemp()
        os.environ['HOME'] = self.temp_dir
        os.environ['USERPROFILE'] = self.temp_dir
        self.notes = SmartNotes()

    def tearDown(self):
        """Clean up."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_stats_with_notes(self):
        """Test stats with existing notes."""
        self.notes.add_note("Test note 1 #tag1")
        self.notes.add_note("Test note 2 #tag2")
        # Should not raise exception
        self.notes.get_stats()

    def test_stats_empty(self):
        """Test stats with no notes."""
        # Should handle gracefully
        self.notes.get_stats()


class TestSmartNotesTagExtraction(unittest.TestCase):
    """Test tag extraction logic."""

    def setUp(self):
        """Set up test environment."""
        self.temp_dir = tempfile.mkdtemp()
        os.environ['HOME'] = self.temp_dir
        os.environ['USERPROFILE'] = self.temp_dir
        self.notes = SmartNotes()

    def tearDown(self):
        """Clean up."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_extract_single_hashtag(self):
        """Test extracting a single hashtag."""
        tags = self.notes.extract_tags("This is a #test")
        self.assertEqual(tags, ["test"])

    def test_extract_multiple_hashtags(self):
        """Test extracting multiple hashtags."""
        tags = self.notes.extract_tags("#python #coding #tips")
        self.assertEqual(sorted(tags), ["coding", "python", "tips"])

    def test_extract_no_hashtags(self):
        """Test with no hashtags."""
        tags = self.notes.extract_tags("Plain text without tags")
        self.assertEqual(tags, [])

    def test_extract_keywords(self):
        """Test keyword extraction."""
        keywords = self.notes.extract_keywords("Python programming tutorial")
        self.assertIn("python", keywords)


class TestSmartNotesEdgeCases(unittest.TestCase):
    """Test edge cases and error handling."""

    def setUp(self):
        """Set up test environment."""
        self.temp_dir = tempfile.mkdtemp()
        os.environ['HOME'] = self.temp_dir
        os.environ['USERPROFILE'] = self.temp_dir
        self.notes = SmartNotes()

    def tearDown(self):
        """Clean up."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_unicode_content(self):
        """Test handling of unicode content."""
        result = self.notes.add_note("Testing emoji 🎉 and unicode: äöü")
        self.assertTrue(result)
        self.assertIn("emoji", self.notes.notes[0]["content"])

    def test_very_long_note(self):
        """Test handling of very long notes."""
        long_content = "x" * 10000
        result = self.notes.add_note(long_content)
        self.assertTrue(result)
        self.assertEqual(len(self.notes.notes[0]["content"]), 10000)

    def test_special_characters_in_content(self):
        """Test special characters in note content."""
        special = "Note with special chars: !@#$%^&*(){}[]|\\:\";<>?,./`~"
        result = self.notes.add_note(special)
        self.assertTrue(result)

    def test_multiple_sessions(self):
        """Test that notes persist across sessions."""
        self.notes.add_note("Session 1 note")
        
        # Create new SmartNotes instance (simulating new session)
        notes2 = SmartNotes()
        self.assertEqual(len(notes2.notes), 1)
        self.assertEqual(notes2.notes[0]["content"], "Session 1 note")


class TestSmartNotesGetNoteById(unittest.TestCase):
    """Test getting notes by ID."""

    def setUp(self):
        """Set up test environment."""
        self.temp_dir = tempfile.mkdtemp()
        os.environ['HOME'] = self.temp_dir
        os.environ['USERPROFILE'] = self.temp_dir
        self.notes = SmartNotes()
        self.notes.add_note("Note 1")
        self.notes.add_note("Note 2")

    def tearDown(self):
        """Clean up."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_get_existing_note(self):
        """Test getting an existing note by ID."""
        note = self.notes.get_note_by_id(1)
        self.assertIsNotNone(note)
        self.assertEqual(note["content"], "Note 1")

    def test_get_nonexistent_note(self):
        """Test getting a note that doesn't exist."""
        note = self.notes.get_note_by_id(999)
        self.assertIsNone(note)


def run_tests():
    """Run all tests with nice output."""
    print("=" * 70)
    print("TESTING: SmartNotes v1.0")
    print("=" * 70)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    test_classes = [
        TestSmartNotesInitialization,
        TestSmartNotesAddNote,
        TestSmartNotesListNotes,
        TestSmartNotesShowNote,
        TestSmartNotesEditNote,
        TestSmartNotesDeleteNote,
        TestSmartNotesTagging,
        TestSmartNotesExport,
        TestSmartNotesStats,
        TestSmartNotesTagExtraction,
        TestSmartNotesEdgeCases,
        TestSmartNotesGetNoteById,
    ]
    
    for test_class in test_classes:
        suite.addTests(loader.loadTestsFromTestCase(test_class))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Summary
    print("\n" + "=" * 70)
    print(f"RESULTS: {result.testsRun} tests")
    passed = result.testsRun - len(result.failures) - len(result.errors)
    print(f"[OK] Passed: {passed}")
    if result.failures:
        print(f"[X] Failed: {len(result.failures)}")
    if result.errors:
        print(f"[X] Errors: {len(result.errors)}")
    print("=" * 70)
    
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(run_tests())
