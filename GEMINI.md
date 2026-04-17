# Zenvesting Live: Project Guidelines

## Core Personas
- **Khan:** The Strategic Investor. Focused on logic, long-term thinking, and fundamental analysis. He explains complex concepts through analogies and structural thinking.
- **Zara:** The High-Growth Specialist. Enthusiastic, quick-witted, and focused on momentum and innovation. She makes the quiz engaging with "fire" energy and relatable examples.

## "Happy Investing" Style
- **Tone:** Encouraging, educational, and professional yet accessible.
- **Goal:** Transform transcripts into engaging MCQs that don't just test memory, but also challenge decision-making and strategic thinking.
- **Formatting:** Use emojis (🔥 for Zara, 🏗️ for Khan) to identify persona-driven explanations in the feedback.

## Architecture Standards
- **Brain (CLI):** `generator.py` – Uses Gemini 1.5 Flash to parse transcripts into structured JSON.
- **UI (Web):** `app.py` – A Streamlit-based live portal for Host and Player modes.
- **State Management:** Simple file-based sync or Supabase integration.
- **Aesthetics:** Dark mode, gold accents, and a "Premium" look.

## Directory Structure
- `generator.py`: Transcript-to-JSON engine.
- `app.py`: Streamlit Quiz Portal.
- `data/`: Directory for `transcript.txt` and `quiz.json`.
- `requirements.txt`: Python dependencies.
