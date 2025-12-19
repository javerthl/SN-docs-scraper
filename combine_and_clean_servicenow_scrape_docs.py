import os

def process_and_combine_docs(input_folder, output_filename):
    combined_content = []
    
    # Artifacts to remove
    PHRASE_1 = "Log in for a better experience"
    PATTERN_UNIX = "\nLog in"
    PATTERN_WIN = "\r\nLog in"

    print(f"Starting processing in: {input_folder}")

    # 1. Walk through the directory to find all .txt files
    for root, dirs, files in os.walk(input_folder):
        for file in sorted(files):
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    
                    # 2. Find "Current page" and strip headers
                    # We look for the index of the line containing the trigger
                    trigger_index = -1
                    for i, line in enumerate(lines):
                        if "Current page" in line:
                            trigger_index = i
                            break
                    
                    # If found, keep from 2 lines above; otherwise keep all
                    if trigger_index != -1:
                        start_line = max(0, trigger_index - 2)
                        relevant_lines = lines[start_line:]
                    else:
                        relevant_lines = lines

                    # Rejoin lines into a single string for text cleaning
                    file_text = "".join(relevant_lines)

                    # 3. Clean specific "Log in" text artifacts
                    file_text = file_text.replace(PHRASE_1, "")
                    file_text = file_text.replace(PATTERN_WIN, "")
                    file_text = file_text.replace(PATTERN_UNIX, "")

                    # 4. Format with the Document Start delimiter
                    formatted_segment = f"--- DOCUMENT START: {file_path} ---\n\n{file_text}\n\n"
                    combined_content.append(formatted_segment)
                    
                except Exception as e:
                    print(f"Could not read {file_path}: {e}")

    # 5. Write the final master file
    with open(output_filename, 'w', encoding='utf-8') as out_file:
        out_file.writelines(combined_content)

    print("-" * 50)
    print(f"✅ Success! Processed {len(combined_content)} files.")
    print(f"Final optimized file saved as: **{output_filename}**")

# --- EXECUTION ---

# Adjust these to your actual folder name and desired output name
SOURCE_DIRECTORY = './servicenow_docs_mcpc' 
FINAL_OUTPUT_FILE = 'final_combined_cleaned_mcp.txt'

process_and_combine_docs(SOURCE_DIRECTORY, FINAL_OUTPUT_FILE)