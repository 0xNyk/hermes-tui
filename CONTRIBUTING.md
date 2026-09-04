# Contributing

This crate is the native (ratatui) Hermes TUI. Python `tui_gateway` still owns the agent.

## Test

```bash
cargo fmt --all -- --check
cargo clippy --all-targets --locked -- -D warnings
cargo test --locked
```

Dogfood a real session before a PR:

```bash
export HERMES_PYTHON_SRC_ROOT=/absolute/path/to/hermes-agent   # dir with tui_gateway/entry.py
export HERMES_PYTHON=$HERMES_PYTHON_SRC_ROOT/.venv/bin/python
export HERMES_HOME=~/.hermes
cargo run --release
```

## Landing in hermes-agent

Do **not** replace Ink `ui-tui/` or flip `hermes --tui` in the first PR.

1. Copy this crate to `crates/tui/` in [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent).
2. Apply `upstream/launch_native.py` inside `_launch_tui` (opt-in `HERMES_TUI_NATIVE=1`).
3. Add the crate to `.github/workflows/rust-tests.yml`.
4. Update `docs/AGENT_PLAYBOOK.md` TUI Architecture.
5. Use Conventional Commits (`feat(tui): …`) and the hermes-agent PR template.
6. Search existing PRs for “native tui” / ratatui first.

Ink stays the default until this client has soak time on macOS, Linux, and WSL2.
