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

3. Running:

```bash
venv_yani_poker\Scripts\activate.bat
python run_report_maker.py path1 path2 
```

You can also make some alias to run the program directly:
it should be under `venv_yani_poker\Scripts\run_report_maker.py`.

4. Help

```bash
venv_yani_poker\Scripts\activate.bat
python run_report_maker.py -h
```

5. What the script does?

`run_report_maker.py` is a simple command line scripts that:
* reads in two paths as arguments
* reads in a template jupyter notebook 
* modifies the FIRST CELL of that jupyter notebook to include the paths you provided
* saves it into a temporary jupyter notebook
* makes a webpdf out of that notebook

Have a most wonderful day.
