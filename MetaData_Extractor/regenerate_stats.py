import os
import json
import collections

# Configuration
CATALOGUE_DIR = "../1947-2012"  # Adjust if needed relative to where this script runs
OUTPUT_FILE = "global_stats.json"

def regenerate_global_stats(root_dir, output_path):
    print(f"Scanning {os.path.abspath(root_dir)} for JSON files...")
    
    total_stories = 0
    author_counts = collections.Counter()
    genre_counts = collections.Counter()
    keyword_counts = collections.Counter()
    
    json_files_count = 0
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(".json"):
                # Skip the stats file itself if it's in the tree
                if file == "global_stats.json" or file == "_bulk_progress_backup.json":
                    continue
                    
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        
                    stories = data.get('stories', [])
                    if not stories:
                        continue
                        
                    json_files_count += 1
                    total_stories += len(stories)
                    
                    for story in stories:
                        # Author
                        author = story.get('author', '').strip()
                        if author and author.lower() != 'unknown' and author != "చందమామ బృందం": # Optional: exclude default bucket if desired, keeping for now
                             author_counts[author] += 1
                        elif author == "చందమామ బృందం":
                             author_counts[author] += 1

                        # Genre
                        genre = story.get('genre', '').strip()
                        if genre and genre.lower() != 'unknown':
                            genre_counts[genre] += 1
                            
                        # Keywords
                        keywords = story.get('keywords', [])
                        if isinstance(keywords, list):
                            for kw in keywords:
                                if kw and isinstance(kw, str):
                                    keyword_counts[kw.strip()] += 1
                                    
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    print(f"Processed {json_files_count} JSON files.")
    
    stats = {
        "total_stories": total_stories,
        "authors": dict(author_counts.most_common()), # Store sorted
        "genres": dict(genre_counts.most_common()),
        "keywords": dict(keyword_counts.most_common())
    }
    
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=4, ensure_ascii=False)
        print(f"Successfully generated {output_path}")
        print(f"Total Stories: {total_stories}")
        print(f"Unique Authors: {len(author_counts)}")
        print(f"Unique Genres: {len(genre_counts)}")
        print(f"Unique Keywords: {len(keyword_counts)}")
        
        print("\n--- INSIGHTS ---")
        print("Top 5 Authors:", author_counts.most_common(5))
        print("Top 5 Genres:", genre_counts.most_common(5))
        print("Top 5 Keywords:", keyword_counts.most_common(5))
        print("----------------")
    except Exception as e:
        print(f"Failed to write output file: {e}")

if __name__ == "__main__":
    # Ensure we look in the right place assuming script is in MetaData_Extractor
    target_dir = os.path.join(os.path.dirname(__file__), CATALOGUE_DIR)
    if not os.path.exists(target_dir):
        # Fallback for testing or different cwd
        print(f"Directory {target_dir} not found. Using current directory check.")
        target_dir = os.getcwd()

    regenerate_global_stats(target_dir, OUTPUT_FILE)
