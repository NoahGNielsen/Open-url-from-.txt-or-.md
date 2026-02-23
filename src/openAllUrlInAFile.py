import os
import webbrowser

def open_urls_in_file(file_path):
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file if line.strip().startswith(('http://', 'https://'))]
        return urls

def main():
    while True:
        file_path = input("Enter the path of a .txt or .md file (or 'q' to quit): ")
        if file_path == 'q':
            break

        if not (file_path.endswith('.txt') or file_path.endswith('.md')):
            print("Invalid file format. Only .txt or .md files are supported.")
            continue
        
        if not os.path.isfile(file_path):
            print("File does not exist.")
            continue

        urls = open_urls_in_file(file_path)
        url_count = len(urls)
        if url_count == 0:
            print("No URLs found in the file.")
            continue

        print(f"Found {url_count} URLs to open.")
        confirm = input("Do you want to proceed? (Y/n): ")
        if confirm not in ('Y', 'y'):
            print("Aborted.")
            continue

        for url in urls:
            webbrowser.open_new_tab(url)

if __name__ == '__main__':
    main()
