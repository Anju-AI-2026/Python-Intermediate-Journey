
# File Backup and Integrity Checker
# Creates file backups and verifies their SHA-256 hashes

import hashlib
import shutil
from pathlib import Path


def calculate_sha256(file_path):
    digest = hashlib.sha256()

    with Path(file_path).open("rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            digest.update(chunk)

    return digest.hexdigest()


def create_backup(source_path, backup_path):
    source = Path(source_path)
    backup = Path(backup_path)

    if not source.is_file():
        print("Error: Source file does not exist.")
        return

    if source.resolve() == backup.resolve():
        print("Error: Source and backup must be different files.")
        return

    if backup.exists() and backup.is_dir():
        print("Error: Backup path points to a directory.")
        return

    try:
        backup.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, backup)

        original_hash = calculate_sha256(source)
        backup_hash = calculate_sha256(backup)

        print("\n" + "=" * 50)
        print("       FILE BACKUP AND INTEGRITY REPORT")
        print("=" * 50)
        print("Source:", source)
        print("Backup:", backup)
        print("Original SHA-256:", original_hash)
        print("Backup SHA-256:  ", backup_hash)

        if original_hash == backup_hash:
            print("Integrity: VERIFIED")
            print("The backup matches the original.")
        else:
            print("Integrity: FAILED")
            print("The backup differs from the original.")

        print("=" * 50)

    except OSError as error:
        print(f"File operation failed: {error}")


if __name__ == "__main__":
    source = input("Enter source file path: ").strip()
    backup = input("Enter backup file path: ").strip()

    if source and backup:
        create_backup(source, backup)
    else:
        print("Error: Both paths are required.")
