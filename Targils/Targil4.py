def analyze_cyber_threats():
    file_name = input("Enter file name to scan: ").strip()
    keywords = ["malware", "phishing", "attack"]
    word_counts = {word: 0 for word in keywords}

    file = open(file_name, "r", encoding="utf-8")
    content = file.read().lower()
    file.close()

    for word in keywords:
        word_counts[word] = content.count(word)

    output_file = open("scan_results.txt", "w", encoding="utf-8")
    output_file.write("Cyber Threat Keyword Scan Results:\n")
    output_file.write("-----------------------------------\n")

    found_any = False
    for word, count in word_counts.items():
        if count > 0:
            output_file.write(f"{word}: {count}\n")
            found_any = True

    if not found_any:
        output_file.write("No cyber keywords were found in the file.\n")

    output_file.close()
    print("Scan completed successfully! Results saved to 'scan_results.txt'.")

analyze_cyber_threats()

