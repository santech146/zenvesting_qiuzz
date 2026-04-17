import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("Error: GOOGLE_API_KEY not found in environment variables.")
    exit(1)

genai.configure(api_key=api_key)

def generate_quiz(transcript_paths, output_path):
    all_questions = []
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    for path in transcript_paths:
        print(f"Processing full transcript: {path}...")
        with open(path, 'r', encoding='utf-8') as f:
            transcript = f.read()

        prompt = f"""
        You are an expert educator: Khan (Strategic 🏗️) and Zara (High-Growth 🔥).
        Analyze this full transcript and create 10 high-quality MCQs.
        
        Style: "Happy Investing". 
        Format: JSON list.
        Each object: {{"id": unique_int, "question": "...", "options": ["...", "...", "...", "..."], "answer": "...", "explanation": {{"khan": "...", "zara": "..."}}}}

        Transcript:
        {transcript}
        """

        print(f"Generating 10 MCQs for {path}...")
        try:
            response = model.generate_content(prompt)
            content = response.text.strip()
            if content.startswith("```json"): content = content[7:-3].strip()
            elif content.startswith("```"): content = content[3:-3].strip()

            quiz_data = json.loads(content)
            for i, q in enumerate(quiz_data):
                q["id"] = len(all_questions) + 1
                all_questions.append(q)
            
            print(f"✅ Successfully extracted {len(quiz_data)} questions from {path}.")
            
            # Brief pause to be safe
            if path != transcript_paths[-1]:
                time.sleep(10)
        except Exception as e:
            print(f"Error processing {path}: {e}")

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2)
    print(f"🚀 Mission Accomplished: Total {len(all_questions)} questions saved to {output_path}")

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2)
    print(f"Total questions saved: {len(all_questions)}")

if __name__ == "__main__":
    import glob
    files = glob.glob("data/day*.txt")
    if not files:
        # Fallback to the original sample if no day files exist yet
        files = ["data/transcript.txt"]
    generate_quiz(files, "data/quiz.json")
