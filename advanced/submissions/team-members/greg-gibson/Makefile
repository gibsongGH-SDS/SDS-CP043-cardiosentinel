SHELL := cmd
PYTHON        ?= python
DATASET_SLUG  ?= iamsouravbanerjee/heart-attack-prediction-dataset
DATA_DIR      ?= data/raw

.PHONY: help data verify clean-data lock

help:
	@echo Targets:
	@echo   make data         Download & unzip Kaggle dataset to $(DATA_DIR)
	@echo   make verify       List downloaded files
	@echo   make clean-data   Remove downloaded raw files
	@echo   make lock         Freeze environment to requirements.txt

data:
	@$(PYTHON) scripts/download_data.py --dataset "$(DATASET_SLUG)" --outdir "$(DATA_DIR)" --unzip

verify:
	@$(PYTHON) -c "import os,glob; d=r'$(DATA_DIR)'; print('Listing files under:', d); [print(p) for p in glob.glob(os.path.join(d,'**','*'), recursive=True) if os.path.isfile(p)]"

clean-data:
	@$(PYTHON) -c "import shutil,os; d=r'$(DATA_DIR)'; print('Deleting:', d); shutil.rmtree(d, ignore_errors=True); os.makedirs(d, exist_ok=True); print('Done.')"

lock:
	@$(PYTHON) -m pip freeze > requirements.txt & echo Created requirements.txt
