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
```

3. Running:

```bash
venv_yani_poker\Scripts\activate.bat
python run_report_maker.py path1 path2 
```

4. Help

```bash
venv_yani_poker\Scripts\activate.bat
python run_report_maker.py -h
```

Have a most wonderful day.
