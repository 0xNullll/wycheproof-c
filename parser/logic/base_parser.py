import os
import json
from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Any, Dict


class BaseParser(ABC):
    """
    Base parser for generating C headers from Wycheproof JSON test vectors.
    Subclasses should implement parse_test_group and generate_header_content_start.
    """

    def __init__(self, directory_path: str, output_c_header: str, target_files: List[str]):
        self.directory_path = Path(directory_path)
        self.output_c_header = Path(output_c_header)
        self.target_files = target_files

    @staticmethod
    def escape_string(s: str) -> str:
        """Escapes special characters in strings for safe use in C headers."""
        return (
            s.replace('\\', '\\\\')
             .replace('"', '\\"')
             .replace('\n', '\\n')
        )

    @staticmethod
    def read_json(file_path: Path) -> Dict[str, Any]:
        """Reads a JSON file and returns the parsed data."""
        with file_path.open('r', encoding='utf-8') as f:
            return json.load(f)

    def write_header(self, header_content: str) -> None:
        """Writes the final header content to the output file."""
        self.output_c_header.parent.mkdir(parents=True, exist_ok=True)
        with self.output_c_header.open('w', encoding='utf-8') as f:
            f.write(header_content)

    @abstractmethod
    def parse_test_group(self, group: Dict[str, Any]) -> str:
        """Parse a single test group and return C header content as a string."""
        pass

    @abstractmethod
    def generate_header_start(self) -> str:
        """Return the opening part of the C header (guards, includes, etc.)."""
        pass

    def generate_header_end(self) -> str:
        """Return the closing part of the C header (end guards)."""
        return "\n#endif  // END OF HEADER\n"

    def parse(self) -> None:
        """Main parsing loop: iterates over target files and writes the header."""
        header_content = self.generate_header_start()

        for file_name in self.target_files:
            file_path = self.directory_path / file_name
            if not file_path.exists():
                print(f"Warning: file {file_path} does not exist, skipping.")
                continue

            try:
                data = self.read_json(file_path)
                test_groups = data.get("testGroups", [])
                for group in test_groups:
                    header_content += self.parse_test_group(group)
            except json.JSONDecodeError as e:
                print(f"JSON decode error in {file_path}: {e}")
            except Exception as e:
                print(f"Failed to process {file_path}: {e}")

        header_content += self.generate_header_end()
        self.write_header(header_content)
        print(f"Header successfully written to {self.output_c_header}")