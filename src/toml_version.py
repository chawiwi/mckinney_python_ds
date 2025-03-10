import toml
import sys
import os

def bump_version(toml_path:str, part="patch") -> None:

    with open(toml_path,"r") as f:
        pyproject = toml.load(f)

    version = pyproject["project"]["version"]
    major, minor, patch = map(int,version.split("."))

    if part == "major":
        major += 1
        minor = 0
        patch = 0
    elif part == "minor":
        minor += 1
        patch = 0
    elif part == "patch":
        patch += 1
    
    pyproject["project"]["version"] = f"{major}.{minor}.{patch}"

    with open(toml_path,"w") as f:
        toml.dump(pyproject,f)

    print(f"Version bumped to {major}.{minor}.{patch}")

def main() -> None:
    if len(sys.argv) > 2:
        print("Usage: python toml_edit.py [major|minor|patch]")
        sys.exit(1)
    
    current_dir = os.getcwd()
    toml_path = os.path.join(current_dir,'pyproject.toml')

    part = sys.argv[1] if len(sys.argv) == 2 else "patch"
    bump_version(toml_path,part=part)
    print("stop")

if __name__ == '__main__':
    main()