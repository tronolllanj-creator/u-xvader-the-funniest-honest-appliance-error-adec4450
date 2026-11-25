"""
# Pinned line: the judge scores this exact line; write it verbatim.
Writes a descaling reminder to entry.txt in the output directory.
"""
import os

CONTENT = "Descale overdue. Water hardness: your problem."

def validate_content(content: str) -> bool:
    """Validate content meets requirements."""
    if not (1 <= len(content) <= 200):
        return False
    if content.isspace() or content == "":
        return False
    if "\n" in content or "\r" in content:
        return False
    return True

def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    
    if not validate_content(CONTENT):
        raise ValueError("Content validation failed")
    
    with open(output_path, "w") as f:
        f.write(CONTENT + "\n")
    
    char_count = len(CONTENT)
    print(f"{output_path} {char_count}")

if __name__ == "__main__":
    main()
