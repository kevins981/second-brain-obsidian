#!/usr/bin/env python3
"""Compatibility wrapper for sessions that still reference the old Codex hook path."""

from pathlib import Path
import runpy


HOOK = Path(__file__).resolve().parents[2] / ".agents" / "hooks" / "conversation_logger.py"
runpy.run_path(str(HOOK), run_name="__main__")
