import os
import pandas as pd
import time

# --------------------------------------------------
# DATASET LOCATION
# --------------------------------------------------

DATASET_FOLDER = "20newsbydate"


# --------------------------------------------------
# SEARCH FUNCTION
# --------------------------------------------------

def search_sentence(sentence):

    results = []

    search_text = sentence.lower().strip()

    print("\n🔍 Searching...")
    print("Please wait while all files are being checked.\n")

    start_time = time.time()

    total_files = 0

    # Search every folder and file
    for root, folders, files in os.walk(DATASET_FOLDER):

        for file_name in files:

            total_files += 1

            file_path = os.path.join(root, file_name)

            # Show progress every 100 files
            if total_files % 100 == 0:
                print(f"Checked {total_files} files...", end="\r")

            try:

                with open(
                    file_path,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as file:

                    content = file.read()

                # Case-insensitive search
                if search_text in content.lower():

                    results.append({
                        "File Name": file_name,
                        "Folder": os.path.basename(root),
                        "Full Path": os.path.abspath(file_path)
                    })

            except Exception:
                pass


    # --------------------------------------------------
    # SEARCH COMPLETED
    # --------------------------------------------------

    end_time = time.time()

    print("\n")
    print("=" * 70)
    print("SEARCH COMPLETED")
    print("=" * 70)

    print(f"Files checked : {total_files}")
    print(f"Time taken   : {end_time - start_time:.2f} seconds")


    # --------------------------------------------------
    # DISPLAY RESULTS
    # --------------------------------------------------

    if len(results) == 0:

        print("\n❌ Sentence not found.")
        print("No file contains the entered sentence.")

    else:

        print(f"\n✅ Sentence found in {len(results)} file(s).\n")

        df = pd.DataFrame(results)

        print(df.to_string(index=False))


# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------

print("=" * 70)
print("             20 NEWS GROUP SENTENCE FINDER")
print("=" * 70)

print("\nDataset location:")
print(os.path.abspath(DATASET_FOLDER))

print("\n")

sentence = input("Enter your sentence: ")


if sentence.strip() == "":
    print("\n❌ Please enter a sentence.")

else:
    search_sentence(sentence)