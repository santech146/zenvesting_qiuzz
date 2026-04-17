---
name: zenvesting-state
description: Expert in real-time state management for Streamlit. Use when syncing state between Host and Player modes or migrating to cloud databases.
---

# Zenvesting State: The Orchestrator

## Current Sync Method
- **File-based:** Using `data/state.json` and `data/scores.json` for local/on-premise coordination.

## Future Migration
- **Cloud Transition:** Guidance on moving state to Supabase or Firestore for live global deployments.

## Responsibilities
- Ensuring all players see the *same* active question at the same time.
- Managing session state to prevent multiple submissions.
- Handling race conditions during high-concurrency score updates.
