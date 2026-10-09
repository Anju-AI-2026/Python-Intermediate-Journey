from pathlib import Path
import shutil

# Get the folder to organize
folder_input = input("Enter folder path to organize: ").strip()
folder = Path(folder_input).expanduser()

# Validate folder
if not folder.is_dir():
    print("Error: The specified folder does not exist.")

else:
    moved_count = 0

    # Process files in the selected folder
    for file_path in list(folder.iterdir()):

        if not file_path.is_file():
            continue

        # Determine extension category
        extension = file_path.suffix.lower().lstrip(".")

        if not extension:
            category = "No Extension"
        else:
            category = extension.upper() + " Files"

        destination_folder = folder / category
        destination = destination_folder / file_path.name

        # Avoid overwriting existing files
        if destination.exists():
            print(f"Skipped existing destination: {file_path.name}")
            continue

        destination_folder.mkdir(exist_ok=True)

        try:
            shutil.move(str(file_path), str(destination))
            print(f"Moved: {file_path.name} -> {category}")
            moved_count += 1

        except OSError as error:
            print(f"Could not move {file_path.name}: {error}")

    print(f"\nOrganization complete. Files moved: {moved_count}")