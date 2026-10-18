file_access_counts = {
    'logfile1.txt': 45,
    'report.docx': 12,
    'image.png': 67,
    'database.db': 8,
    'server.log': 110,
    'config.yaml': 23,
    'script.py': 34,
    'presentation.pptx': 18,
    'backup.zip': 55,
    'archive.tar': 9
}


def get_most_frequent_file(counts_dict):
    most_frequent_file = None
    max_count = 0
    for filename, count in counts_dict.items():
        if count > max_count:
            max_count = count
            most_frequent_file = filename
    return most_frequent_file

print(file_access_counts.items())
result = get_most_frequent_file(file_access_counts)
print(f"The most common file is: {result}")