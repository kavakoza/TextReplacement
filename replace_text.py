import sys


def read_config_file(config_path):
    """Read the configuration file and return a dictionary of replacements"""
    replacements = {}
    try:
        with open(config_path, 'r') as f:
            for line in f:
                try:
                    key, value = line.strip().split('=')
                    replacements[key] = value
                except ValueError:
                    print("Invalid line in config file")
    except FileNotFoundError:
        print(f"Config file '{config_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading configuration file: {e}")
        sys.exit(1)
    return replacements


def read_text_file(text_file_path):
    """Read the text file and return a list of lines"""
    try:
        with open(text_file_path, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Text file '{text_file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading text file: {e}")
        sys.exit(1)


def replace_values(lines, replacements):
    """Replace values in the lines according to the replacements dictionary"""
    modified_lines = []

    for line in lines:
        total_replacements = 0

        for key, value in replacements.items():
            start_index = 0
            while True:
                index = line.find(key, start_index)
                if index == -1:
                    break

                # Calculate the number of characters replaced
                count = len(key)
                total_replacements += count
                line = line[:index] + value + line[index + len(key):]
                start_index = index + len(value)

        if total_replacements > 0:
            modified_lines.append((line, total_replacements))

    return modified_lines


def main(config_path, text_file_path):
    """Main function to read config, process text, and print results"""
    replacements = read_config_file(config_path)
    lines = read_text_file(text_file_path)
    modified_lines = replace_values(lines, replacements)

    modified_lines.sort(key=lambda x: x[1], reverse=True)

    for line, count in modified_lines:
        print(f'{line.strip()}(Replacements: {count})')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <config_file> <text_file>")
        sys.exit(1)

    config_file_name = sys.argv[1]
    text_file_name = sys.argv[2]
    main(config_file_name, text_file_name)
