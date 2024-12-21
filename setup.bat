@echo off
setlocal

:: Add Python Scripts to PATH
set "PYTHON_SCRIPTS=%LOCALAPPDATA%\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\Scripts"
set "PATH=%PYTHON_SCRIPTS%;%PATH%"

:: Run Streamlit
streamlit run app.py

endlocal
