Homework Test Results

TestCase                                Result
================================================================
testcase_template1.py                   Crashed due to signal 1:
Traceback (most recent call last):
  File "C:\Users\GUILLA~1\AppData\Local\Temp\tmpf2xhuzae\testcase_template1.py", line 34, in <module>
  File "C:\Users\Guillaume\AppData\Local\Programs\Python\Python39\lib\importlib\__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 790, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "...\database.py", line 4, in <module>
ModuleNotFoundError: No module named 'sql_utils'


testcase_template2.py                   Crashed due to signal 1:
Traceback (most recent call last):
  File "C:\Users\GUILLA~1\AppData\Local\Temp\tmpf2xhuzae\testcase_template2.py", line 34, in <module>
  File "C:\Users\Guillaume\AppData\Local\Programs\Python\Python39\lib\importlib\__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 790, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "...\database.py", line 4, in <module>
ModuleNotFoundError: No module named 'sql_utils'


================================================================
Result: 0/100

Key:
	Failed to Compile: Your submission did not compile due to a syntax or naming error
	Compiled with warnings: Your submission uses unchecked or unsafe operations
	Crashed due to signal SIGNAL_CODE: Your submission threw an uncaught exception.
	All signal error codes are described here: https://man7.org/linux/man-pages/man7/signal.7.html
	Exceeded Time Limit: Your submission took too much time to run (probably an infinite loop)
