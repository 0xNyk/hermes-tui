# Security

This crate is **experimental**. It is a local terminal client. It draws a TUI and talks to a Python `tui_gateway` child over newline JSON-RPC stdio. It does not take inbound network connections and it does not call model APIs.

## Report

Use GitHub private vulnerability reporting:

https://github.com/0xNyk/hermes-tui/security/advisories/new

Do not open a public issue for a secret, an RCE, or a way to escape the worktree jail.

## Scope

In scope: the Rust binary, launch env handling, RPC framing, log redaction, worktree path confinement.

Out of scope: Hermes Agent itself (`tui_gateway`, tools, skills). Report those on [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent/security).
