1. Dependencies:

* python 3.11
* virtualenv: https://medium.com/analytics-vidhya/virtual-environment-6ad5d9b6af59
* git at whatever version


2. Installation:

Uninstall Windows, install Linux.
Just joking...


Open `Command Prompt` on Windows. 
```bash
git clone https://github.com/ZhaoYaniBruker/yani_poker.git
cd yani_poker
py -3.11 -m virtualenv venv_yani_poker
venv_yani_poker\Scripts\pip.exe install -r requirements.txt
venv_yani_poker\Scripts\python -m ipykernel install --user --name yani_poker
```
Note1: running last line twice is fully OK for the same user on Windows.
It is necessary to name the kernel yani_poker so that `nbconvert` can use the proper one.
Somehow is does not work out of the box with a virtualenv installation.

Note2: The import Shema for Spectronaut is `R_D_reportcol.rs`.

3. Running:

```bash
venv_yani_poker\Scripts\activate.bat
pip install numpy matplotlib pandas duckdb upsetplot (attention: you only need to run this line in the venv once)
python run_report_maker.py path1 path2 
```

Note3: path1 and path2 are the paths to your .tsv reports from Spectronaut. The two example files, Spectronaut_5007.tsv and Spectronaut_4994.tsv
are in the same folder as the code, so you can just run as: python run_report_maker.py Spectronaut_5007.tsv Spectronaut_4994.tsv

You can also make some alias to run the program directly:
it should be under `venv_yani_poker\Scripts\run_report_maker.py`.

4. Help

```bash
venv_yani_poker\Scripts\activate.bat
python run_report_maker.py -h
```

5. What the script does?

`run_report_maker.py` is a simple command line scripts that:
* reads in two paths as arguments (attention: the code get the two paths from the first cell in the template notebook)
* reads in a template jupyter notebook 
* modifies the FIRST CELL of that jupyter notebook to include the paths you provided
* saves it into a temporary jupyter notebook
* makes a webpdf out of that notebook

Have a most wonderful day.
