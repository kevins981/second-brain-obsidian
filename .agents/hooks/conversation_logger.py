#!/usr/bin/env python3
"""Record simple user/assistant turns from agent hook events."""

from __future__ import annotations

from datetime import datetime
import hashlib
import json
from pathlib import Path
import sys
import tempfile
from typing import Any


def timestamp() -> str:
    return datetime.now().astimezone().isoformat()


def safe_key(*parts: str | None) -> str:
    raw = "\n".join(part or "" for part in parts)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def read_event() -> dict[str, Any]:
    try:
        return json.load(sys.stdin)
    except Exception:
        return {}


def conversations_dir(event: dict[str, Any]) -> Path:
    cwd = Path(event.get("cwd") or ".").expanduser()
    return cwd / "conversations"


def state_dir(event: dict[str, Any]) -> Path:
    cwd = str(Path(event.get("cwd") or ".").expanduser())
    return Path(tempfile.gettempdir()) / "agent-conversation-logger" / safe_key(cwd)


def event_key(event: dict[str, Any]) -> str:
    session_id = event.get("session_id")
    turn_id = event.get("turn_id")
    if turn_id:
        return safe_key(session_id, turn_id)
    return safe_key(session_id)


def pending_path(event: dict[str, Any]) -> Path:
    return state_dir(event) / "pending" / f"{event_key(event)}.json"


def session_map_path(event: dict[str, Any]) -> Path:
    return state_dir(event) / "sessions" / f"{safe_key(event.get('session_id'))}.txt"


def conversation_path(event: dict[str, Any]) -> Path:
    conversations = conversations_dir(event)
    mapping = session_map_path(event)

    if mapping.exists():
        saved_name = mapping.read_text(encoding="utf-8").strip()
        if saved_name:
            return conversations / saved_name

    stem = datetime.now().astimezone().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{stem}.jsonl"
    if (conversations / filename).exists():
        filename = f"{stem}-{safe_key(event.get('session_id'))[:8]}.jsonl"

    write_text(mapping, filename + "\n")
    return conversations / filename


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path: Path, payload: dict[str, Any]) -> None:
    write_text(path, json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def append_message(path: Path, role: str, message: str | None, message_timestamp: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(
            json.dumps(
                {
                    "timestamp": message_timestamp,
                    "role": role,
                    "message": message or "",
                },
                ensure_ascii=False,
            )
            + "\n"
        )


def handle_user_prompt(event: dict[str, Any]) -> None:
    conversation_path(event)
    write_json(
        pending_path(event),
        {
            "timestamp": timestamp(),
            "message": event.get("prompt") or "",
        },
    )


def handle_stop(event: dict[str, Any]) -> None:
    pending = pending_path(event)
    user_message = ""
    user_timestamp = timestamp()
    if pending.exists():
        try:
            pending_payload = json.loads(pending.read_text(encoding="utf-8"))
            user_message = pending_payload.get("message") or ""
            user_timestamp = pending_payload.get("timestamp") or user_timestamp
        except Exception:
            user_message = ""

    output_path = conversation_path(event)
    append_message(output_path, "user", user_message, user_timestamp)
    append_message(output_path, "assistant", event.get("last_assistant_message"), timestamp())

    if pending.exists():
        pending.unlink()


def main() -> int:
    event = read_event()
    event_name = event.get("hook_event_name")

    try:
        if event_name == "UserPromptSubmit":
            handle_user_prompt(event)
        elif event_name == "Stop":
            handle_stop(event)
    except Exception as exc:
        if event_name == "Stop":
            print(json.dumps({"continue": True, "systemMessage": f"Conversation logging failed: {exc}"}))
        return 0

    if event_name == "Stop":
        print(json.dumps({"continue": True}))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
