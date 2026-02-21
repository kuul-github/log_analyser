import sys

def analyze_log(file_path):
    error_count = 0
    warning_count = 0
    info_count = 0

    try:
        with open(file_path, "r") as file:
            for line in file:
                if "ERROR" in line:
                    error_count += 1
                elif "WARNING" in line:
                    warning_count += 1
                elif "INFO" in line:
                    info_count += 1

        print("\nLog Summary:")
        print(f"ERROR: {error_count}")
        print(f"WARNING: {warning_count}")
        print(f"INFO: {info_count}")

    except FileNotFoundError:
        print("File not found. Please check the file path.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python log_analyzer.py <logfile>")
    else:
        analyze_log(sys.argv[1])
