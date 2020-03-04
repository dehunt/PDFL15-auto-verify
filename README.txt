Requirements:

    Updated requirements:
        PyPDF2
        pdftocairo/Poppler
            Windows: https://blog.alivate.com.au/tag/pdftocairo/ for windows binaries, add to PATH
            Linux: poppler-utils (via package manager)
        ImageMagick
            Windows: https://imagemagick.org/index.php, Add to PATH
            Linux: ImageMagick (via package manager)

	Before a run you MUST set APDFL_DIR to point at the root folder of the version that you're checking.
		E.g. on windows: $Env:APDFL_DIR="C:\Datalogics\APDFL15.0.4-P5d"

	You MUST set MAGICK_TEMPORARY_PATH as an environment variable. This is where ImageMagick temp files will go.
		E.g. export MAGICK_TEMPORARY_PATH=some_temp_dir
		If this is not set, ImageMagick may or may not work. Setting this variable helps avoid permissions issues.

	You MUST have python3 installed (script written with python 3.5.5) and the following modules:
		pytest - https://pypi.org/project/pytest/
			pip install pytest
		PyPDF2 - https://pypi.org/project/PyPDF2/
			pip install PyPDF2

Usage:
	These tests can be run from any location. 
	Open a cmd or pwsh terminal and navigate to checkSamples. You should see checkSamplesCpp, checkSamplesJav, etc.
	From that directory level, run command "pytest".

Pytest arguments:
	-h:	lists all pytest arguments and pytest help info
	-v or -vv: Increase verbosity a little, a lot. This is useful to get the stdout that tests create, to see what is failing.
	-r:	Display a short test summary info at the end of the test session.
	-k EXPRESSION: Run specific tests that match EXPRESSION. E.g. 
				pytest -k 'images_test.py' will run all tests in the images_test module.
				pytest -k 'TestSplitPDF' will run all six of the TestSplitPDF class tests.
				pytest -k 'test_createDocumentPdf' will run the test_createDocumentPdf test method.

Adding tests:
	All tests modules should end with _test.py. All test methods should begin with test_. Pytest looks for files/methods beginning with test_ or ending with _test to ID which files to collect.
	The naming pattern should mimic the current APDFL directory so that tests can be matched to APDFL samples quickly. Classes should begin with Test, but this is a naming convention.
	All tests build relative paths for their respective baseline and sample files, so it's important to mimic the APDFL C++ sample directories.

	All test comparisons and helper methods are in checkSamplesUtil.py. This contains the imagemagick subprocess calls, the hash calls, etc. The tests assert with the return values to validate files.

	All code should be platform agnostic. This means don't manually create paths, directly execute commands, etc. For those two, you can use os.path.join() and subprocess.run() (.run() can be used in place of older methods, such as subprocess.call(), as of python 3.5).
	
Baseline files are from P4k, P5c, P5d.