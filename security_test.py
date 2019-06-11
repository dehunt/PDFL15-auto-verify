# This contains test methods. Test methods must begin / end with test_ or _test in order for pytest to find them.
# Import common variables / methods from apdflTestUtils.py
# Relative paths are built for each test file on the assumption that pytest will be run from the product's base directory, and the complete test package has been copied into the product base directory.
# Baseline files are organized in a way that mimics the sample organization. Baseline folders are camelcase so sample files can't be accidently used.

import pytest, os, checkSamplesUtil as util
from checkSamplesUtil import samplesRootDir, testsDir

sampDir = os.path.join(samplesRootDir, 'Security')
baseDir = os.path.join(testsDir, 'security_test')

class TestAddRedaction(object):
    extAttchSampFile = os.path.join(sampDir, 'AddRedaction')
    extAttchBase = os.path.join(baseDir, 'addRedaction')
    
    def test_addRedaction(self):
        testFile = os.path.join(self.extAttchSampFile, 'AddRedaction-out.pdf')
        baseFile = os.path.join(self.extAttchBase, 'AddRedaction-out.pdf')
        diffOut = os.path.join(self.extAttchSampFile, 'diffOut.png')
        var = util.imgCompare(testFile, baseFile, diffOut)
        assert var == b'0', "FAILED - Imaged PDFs do not match."