import os, shutil

def copy_files_with_extensions(source_dir, target_dir, extensions):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for root, _, files in os.walk(source_dir):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                shutil.copy2(os.path.join(root, file), os.path.join(target_dir, file))
                print(f"Copied {file}")
