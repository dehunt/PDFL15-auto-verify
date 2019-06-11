# This contains test methods. Test methods must begin / end with test_ or _test in order for pytest to find them.
# Import common variables / methods from apdflTestUtils.py
# Relative paths are built for each test file on the assumption that pytest will be run from the product's base directory, and the complete test package has been copied into the product base directory.
# Baseline files are organized in a way that mimics the sample organization. Baseline folders are camelcase so sample files can't be accidently used.

import pytest, os, checkSamplesUtil as util
from checkSamplesUtil import samplesRootDir, testsDir

sampDir = os.path.join(samplesRootDir, 'InformationExtraction')
baseDir = os.path.join(testsDir, 'informationExtraction_test')

class TestCoundColorsInDoc(object):
    extAttchSampFile = os.path.join(sampDir, 'CountColorsInDoc')
    extAttchBase = os.path.join(baseDir, 'countColorsInDoc')
    
    def test_countColorsInDoc(self):
        testFile = util.hash(os.path.join(self.extAttchSampFile, 'CountColorsInDoc-out.txt'))
        baseFile = util.hash(os.path.join(self.extAttchBase, 'CountColorsInDoc-out.txt'))
        assert testFile == baseFile, "FAILED - File hashes do not match."

class TestExtractDocumentInfo(object):
    extAttchSampFile = os.path.join(sampDir, 'ExtractDocumentInfo')
    extAttchBase = os.path.join(baseDir, 'extractDocumentInfo')
    
    def test_extractDocumentInfo(self):
        testFile = util.hash(os.path.join(self.extAttchSampFile, 'ExtractDocumentInfo-out.txt'))
        baseFile = util.hash(os.path.join(self.extAttchBase, 'ExtractDocumentInfo-out.txt'))
        assert testFile == baseFile, "FAILED - File hashes do not match."
