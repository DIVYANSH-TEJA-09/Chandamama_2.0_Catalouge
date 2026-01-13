import os
import json
import re

# Configuration
CATALOGUE_DIR = "../1947-2012"  # Relative to MetaData_Extractor

def generate_story_ids(root_dir):
    print(f"Scanning {os.path.abspath(root_dir)} for JSON files...")
    
    pattern = re.compile(r"_(\d{4})_(\d{2})\.json$")
    processed_count = 0
    updated_stories_count = 0
    skipped_files = []
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(".json") and "global_stats" not in file and "_backup" not in file:
                # Try to extract Year and Month from filename
                # Expected format: *chandamama_1947_07.json or similar
                match = pattern.search(file)
                
                if match:
                    year = match.group(1)
                    month = match.group(2)
                    
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                        
                        stories = data.get('stories', [])
                        if not stories:
                            continue
                            
                        modified = False
                        for i, story in enumerate(stories, 1):
                            # Generate ID: YYYY_MM_StoryNum (e.g., 1947_07_01)
                            story_id = f"{year}_{month}_{i:02d}"
                            
                            # Update if missing or different
                            if story.get('story_id') != story_id:
                                story['story_id'] = story_id
                                modified = True
                                updated_stories_count += 1
                        
                        if modified:
                            with open(file_path, 'w', encoding='utf-8') as f:
                                json.dump(data, f, indent=4, ensure_ascii=False)
                            processed_count += 1
                            
                    except Exception as e:
                        print(f"Error processing {file_path}: {e}")
                else:
                    skipped_files.append(file)

    print(f"Done! Updated {processed_count} files.")
    print(f"Generated IDs for {updated_stories_count} stories.")
    
    if skipped_files:
        print("\n--- Skipped Files (Filename Format Issue) ---")
        for f in skipped_files:
            print(f"- {f}")
        print("---------------------------------------------")

if __name__ == "__main__":
    target_dir = os.path.join(os.path.dirname(__file__), CATALOGUE_DIR)
    if not os.path.exists(target_dir):
        target_dir = os.getcwd()
        
    generate_story_ids(target_dir)
