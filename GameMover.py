import os
import shutil

def move_game_to_downloads(game_name, source_directory):
    # Get the path to the directory
    new_directory = os.path.join(input("Input Where the Games are Moved to in brackets"))

    # Check if the source directory exists
    if not os.path.exists(source_directory):
        print(f"Error: Source directory '{source_directory}' does not exist.")
        return

    # Check if the destination directory (Downloads) exists
    if not os.path.exists(new_directory):
        print(f"Error: {new_directory} directory not found.")
        return

    # Check if the game folder exists in the source directory
    game_path = os.path.join(source_directory, game_name)
    if not os.path.exists(game_path):
        print(f"Error: Game '{game_name}' not found in the source directory.")
        return

    # Move the game folder and its files to the Downloads directory
    destination_path = os.path.join(new_directory, game_name)
    try:
        shutil.move(game_path, destination_path)
        print(f"Successfully moved '{game_name}' to {destination_path} directory.")
    except Exception as e:
        print(f"Error: Failed to move '{game_name}' to {destination_path} directory.")
        print(str(e))

if __name__ == "__main__":
    # Replace these values with your specific game names and source directory path
    game_names = [input("What is the Folder of the Games called?")]
    source_directory = input("Input Where the Games are, in brackets")

    for game in game_names:
        move_game_to_downloads(game, source_directory)