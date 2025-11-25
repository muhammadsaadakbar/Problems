import os
import zipfile


def zip_current_folder(zip_name="archive.zip"):
    with zipfile.ZipFile(zip_name, "w") as zipf:
        for file in os.listdir("."):
            if os.path.isfile(file):
                zipf.write(file)
                print(f"Added {file} to {zip_name}")


if __name__ == "__main__":
    zip_current_folder()
