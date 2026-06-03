import os
import sys
import shutil
import glob
import re
from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict
import argparse
from argparse import ArgumentParser

# Regular expression to match tags in the format #tag-name
tag_search = re.compile(r'(?i)(?:class|topic) #([a-zA-Z][-a-zA-Z0-9_\/]*)')


# A function to search for tags in a single file
def find_tags_in_file(file_path) -> list[str] | None:
    print(f'Processing file: {file_path}')
    tags = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            tags = tag_search.findall(file.read(), re.IGNORECASE)
        return tags if tags else None
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

# The main function to find all unique tags and group files by tag
def find_all_tags(directory, max_workers=os.cpu_count()) -> dict[str, list[str]]:
    markdown_files = glob.glob(os.path.join(directory, '**', '*.md'), recursive=True)
    
    tag_to_files = defaultdict(list)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all file processing tasks
        futures = [executor.submit(find_tags_in_file, file_path) for file_path in markdown_files]
        
        # Process results as they complete
        for i, future in enumerate(futures):
            file_path = markdown_files[i]
            tags = future.result()
            if tags:
                for tag in tags:
                    tag_to_files[tag].append(file_path)
    
    # Convert defaultdict to regular dict for cleaner output
    return dict(tag_to_files)

def reorganize_move_single(tag_to_files: dict[str, list[str]], base_directory: str, new_base_directory: str):
    for tag, files in tag_to_files.items():
        tag_dir = os.path.join(new_base_directory, tag)
        os.makedirs(tag_dir, exist_ok=True)
        
        for file_path in files:
            relative_path = os.path.relpath(file_path, base_directory)
            new_file_path = os.path.join(tag_dir, os.path.basename(relative_path))
            try:
                os.rename(file_path, new_file_path)
                print(f"Moved {file_path} to {new_file_path}")
            except Exception as e:
                print(f"Error moving {file_path} to {new_file_path}: {e}")

def reorg(tag_to_files: dict[str, list[str]], new_directory: str):
    for tag, files in tag_to_files.items():
        tag_dir = os.path.join(new_directory, tag)
        os.makedirs(tag_dir, exist_ok=True)
        
        with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
            futures = []
            for file_path in files:
                futures.append(executor.submit(shutil.move, file_path, tag_dir, copy_function=shutil.copy2))
            
            for future in futures:
                try:
                    future.result()
                except Exception as e:
                    print(f"Error moving file: {e}")

if __name__ == '__main__':
    # Replace 'path/to/your/notes' with the actual directory
    
    # optional cmdline arg for search_directory
    # parser.add_argument("search_directory", nargs="?", default=".", help="Directory to search for markdown files")
    parser = ArgumentParser(
        prog = 'Obsidian Vault Reorganizer',
        description = 'Moves all Obsidian markdown files with the same tag into directories named after the tag.',
    )
    parser.add_argument("search_directory", nargs="?", default=".", help="Directory to search for markdown files (default is current directory)")
    parser.add_argument("new_directory", nargs="?", default=None, help="Directory to move files into (default is search directory)")
    
    args = parser.parse_args()
    search_directory = args.search_directory
    if args.new_directory is None:
        new_dir = search_directory
    else:        
        new_dir = args.new_directory
    
    if not os.path.exists(search_directory):
        print(f"Creating a sample directory and files at '{search_directory}'")
        os.makedirs(os.path.join(search_directory, 'project_a'), exist_ok=True)
        os.makedirs(os.path.join(search_directory, 'project_b'), exist_ok=True)
        
        with open(os.path.join(search_directory, 'note1.md'), 'w') as f:
            f.write("Some text here\nfor class #embedded in root\nMore text")
        with open(os.path.join(search_directory, 'project_a', 'note2.md'), 'w') as f:
            f.write("Another note\nNo tag here")
        with open(os.path.join(search_directory, 'project_b', 'note3.md'), 'w') as f:
            f.write("A final note\nWith a tag: for class #data")

    print(f"Searching for all tags in '{search_directory}'...")
    tag_to_files = find_all_tags(search_directory)
    
    print(f"\nFound {len(tag_to_files)} unique tags:")
    for tag, files in tag_to_files.items():
        print(f"\nTag #{tag} found in {len(files)} file(s):")
        for file_path in files:
            print(f"  - {file_path}")
        
    reorg(tag_to_files, new_dir)