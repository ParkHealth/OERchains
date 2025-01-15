import os

# Define the folder structure and .md files
folders_and_files = {
    'docs': {
        'architecture': ['ARCHITECTURE.md'],
        'images': ['OER-Benefits.png', 'OER-Heritage.png'],
        'guides': ['User-Guide.md', 'Developer-Guide.md', 'API-Documentation.md'],
        'reference': ['Blockchain-Protocol.md', 'Data-Models.md', 'Smart-Contracts.md'],
        'community': ['CONTRIBUTING.md', 'Governance.md', 'Community-Guidelines.md'],
        'tutorials': ['Getting-Started.md', 'Building-with-OERchains.md', 'Creating-Educational-Content.md'],
        'examples': ['Sample-OER-Files.md', 'Code-Examples.md', 'Sample-Smart-Contract.md'],
        'tests': ['Test-Suite.md', 'Integration-Tests.md'],
        'other': ['EDUCATIONAL_ART.md', 'OERCHAINS.md', 'OERs.md', 'OPEN_SOURCE.md', 'REGENERATIVE_ECONOMICS.md', 'WHY_OERS.md']
    }
}

# Create the folder structure and .md files
def create_folders_and_files(base_path):
    for folder, files in folders_and_files['docs'].items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            file_path = os.path.join(folder_path, file)
            with open(file_path, 'w') as f:
                f.write(f"# {file.replace('.md', '').replace('-', ' ').title()}\n\n")
                f.write(f"<!-- Documentation for {file.replace('.md', '').replace('-', ' ').title()} -->\n")

# Define the base directory path where the 'docs' folder will be created
base_directory = "OERchains"  # You can modify this to a specific path if necessary

# Create folders and files
create_folders_and_files(base_directory)

print(f"Folder structure and markdown files created under {base_directory}")
