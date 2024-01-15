import argparse
import json
import subprocess
import os
from pathlib import Path

parser = argparse.ArgumentParser(
    description='Prepare some report comparing two different tsv files.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)

venv_path = Path(os.environ['VIRTUAL_ENV'])
assert venv_path.exists(), "You are not in the virtual environment."
project_path = venv_path.parent


parser.add_argument("path1", type=Path, help="first report.")
parser.add_argument("path2", type=Path, help="second report.")
parser.add_argument("--target", 
                    type=Path,
                    help="Directory to save the final outcome.",
                    default=project_path/"pdf_report")
parser.add_argument("--temporary_notebook_path", 
                    type=Path,
                    help="Path to the temporary notebook.",
                    default=project_path/"tmp_notebook.ipynb",
                    )
parser.add_argument("--path_to_template_ipynb", 
                    type=Path,
                    help="Path to the template ipynb file.",
                    default=project_path/"YaniZhao_template.ipynb",
)
parser.add_argument("--include_code", 
                    help="Include the full input cells code.",
                    action="store_true",
)

args = parser.parse_args()

if __name__ == "__main__":
    print("Project path is: ", project_path)
    # The overall idea is:
    #   * read in a template ipynb file
    #   * assume first cell is empty or has default values of parameters that will be simply exchanged for our current ones.
    #   * save a modified ipynb file
    #   * re-execute the notebook and change it into a webpdf.

    print(f"Paths you passed in:\npath1={args.path1}\npath2={args.path2}")

    with open(args.path_to_template_ipynb, "r") as file_handler:
        # jupyter notebooks (ipynb) are simple json files and can be parsed as such.
        notebook = json.load(file_handler)
    
    # changing the contents of the first cell
    # (so watch out: if it contained something important, we are done.)
    notebook["cells"][0]["source"] = [
        f'path1 = "{args.path1}"; path2 = "{args.path2}"',# you can add more paths here
    ]
    with open(args.temporary_notebook_path, "w") as file_handler:
        json.dump(notebook, file_handler)

    # --allow-chromium-download caches the downloaded chromium
    cmd = f'{venv_path}\Scripts\jupyter.exe nbconvert --to webpdf {args.temporary_notebook_path} --allow-chromium-download --output {args.target} --execute --ExecutePreprocessor.kernel_name="yani_poker"'
    if not args.include_code:
        cmd += " --no-input"
    print(f'Running:\n{cmd}\n')
    subprocess.run(cmd, shell=True)
