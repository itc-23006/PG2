import os

def find_largest_file(directory):
    largest_file, largest_size = max(
        ((os.path.join(root, file), os.path.getsize(os.path.join(root, file))) 
         for root, _, files in os.walk(directory) for file in files),
        key=lambda x: x[1],
        default=(None, 0)
    )
    
    if largest_file:
        print(f"Largest file: {largest_file}")
        print(f"Size: {largest_size} bytes")
    else:
        print("No files found in the specified directory.")
