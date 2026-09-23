# AI-BASED-NEWS-DOCUMENT-SEARCH-SYSTEM
Python-based document search system that searches sentences across the 20 Newsgroups dataset and identifies the matching file, folder, and complete file path

The project demonstrates practical implementation of:

- Python file handling
- Recursive directory traversal
- Text searching
- String processing
- Dataset handling
- Pandas DataFrame creation
- Search performance measurement

# ⚡ Features

- 🔍 Search for a sentence across the entire dataset
- 📂 Recursively search nested folders and subfolders
- 📄 Read and search multiple text files
- 🔤 Case-insensitive text matching
- 📍  Display the exact file containing the sentence
- 📁 Display the corresponding folder/category
- 🛣️ Display the complete file path
- 📊 Display search results using Pandas
- 📈 Count the total number of files checked
- ⏱️ Measure the total search time
- ⚠️ Handle unreadable files without stopping the program

# 🧩 Schematic
![schematic](https://github.com/Karthikeyanmac/Traffic-Light-Controller-Using-NE555-Timer-IC/blob/main/schematic_traffic_light_555.jpg)

# 🛠️ Breadboard Implementation
![Breadboard](https://github.com/Karthikeyanmac/Traffic-Light-Controller-Using-NE555-Timer-IC/blob/main/breadboard_image.jpg)

# 🛠️ Technologies Used
## 🛠️ Technology and Purpose

| Technology                | Purpose                                 |
| ------------------------- | --------------------------------------- |
| **Python**                | Core programming language               |
| **OS Module**             | Folder traversal and file path handling |
| **Pandas**                | Organizing search results               |
| **File Handling**         | Reading text documents                  |
| **String Processing**     | Case-insensitive sentence matching      |
| **Time Module**           | Measuring search performance            |
| **VS Code**               | Development environment                 |
| **20 Newsgroups Dataset** | Text document dataset                   |



# How the System Works

The overall workflow is:

User enters a sentence
        ↓
Program receives the input
        ↓
Search starts from the dataset folder
        ↓
Recursively scans folders and subfolders
        ↓
Opens each text file
        ↓
Searches for the entered sentence
        ↓
Matching files are identified
        ↓
File name + folder + full path are collected
        ↓
Pandas organizes the results
        ↓
Results are displayed to the user

📁 Dataset Setup

- Place the 20newsbydate dataset folder inside the project directory.

- The structure should be:

20-newsgroups-sentence-finder/
- │
- ├── search_news.py
- │
- └── 20newsbydate/
 -   ├── 20news-bydate-train/
 -   └── 20news-bydate-test/






