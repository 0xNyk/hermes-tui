"""Opt-in native TUI launch for hermes-agent `_launch_tui`.

Ink (`ui-tui/`) stays the default. Set HERMES_TUI_NATIVE=1 (or pass --native)
to exec `hermes-tui-native` with the same env `_launch_tui` already builds.

If the binary is missing, return None so the caller falls back to Ink and
prints how to build.

Drop-in (hermes_cli/main.py, top of _launch_tui, after `env` is built):

    from hermes_cli.launch_native import native_tui_argv  # or inline this file

    native = native_tui_argv(env)
    if native:
        os.execvpe(native[0], native, env)
"""

from __future__ import annotations

import os
import shutil
import sys
from typing import Mapping


def wants_native(argv: list[str] | None = None) -> bool:
    if argv is None:
        argv = sys.argv[1:]
    if os.environ.get("HERMES_TUI_NATIVE") == "1":
        return True
    return "--native" in argv


def native_tui_bin() -> str | None:
    explicit = os.environ.get("HERMES_TUI_NATIVE_BIN", "").strip()
    if explicit and os.path.isfile(explicit) and os.access(explicit, os.X_OK):
        return explicit
    path = shutil.which("hermes-tui-native")
    if path:
        return path
    return None


def native_tui_argv(env: Mapping[str, str]) -> list[str] | None:
    """Return argv for the native client, or None to fall back to Ink."""
    if not wants_native():
        return None
    bin_path = native_tui_bin()
    if not bin_path:
        print(
            "HERMES_TUI_NATIVE=1 but hermes-tui-native was not found.\n"
            "Build it: cargo install --path crates/tui\n"
            "Or set HERMES_TUI_NATIVE_BIN=/path/to/hermes-tui-native\n"
            "Falling back to the Ink TUI.",
            file=sys.stderr,
        )
        return None
    argv = [bin_path]
    resume = env.get("HERMES_TUI_RESUME") or os.environ.get("HERMES_TUI_RESUME")
    if resume:
        argv.extend(["--resume", resume])
    title = os.environ.get("HERMES_TUI_TITLE")
    if title:
        argv.extend(["--title", title])
    return argv
