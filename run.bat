#pytest -v -m "regression" --html=reports/reports321.html testCases/
#pytest -v --html=reports/reportsDDT.html testCases/test_login_ddt.py
pytest -vs testCases/test_login.py

