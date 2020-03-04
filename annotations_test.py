# This contains test methods. Test methods must begin / end with test_ or _test in order for pytest to find them.
# Import common variables / methods from apdflTestUtils.py
# Relative paths are built for each test file on the assumption that pytest will be run from the product's base directory, and the complete test package has been copied into the product base directory.
# Baseline files are organized in a way that mimics the sample organization. Baseline folders are camelcase so sample files can't be accidently used.

import pytest, os, checkSamplesUtil as util
from checkSamplesUtil import samplesRootDir, testsDir

sampDir = os.path.join(samplesRootDir, 'Annotations')
baseDir = os.path.join(testsDir, 'annotations_test')

class TestCreateAnnotations(object):
    extAttchSampFile = os.path.join(sampDir, 'CreateAnnotations')
    extAttchBase = os.path.join(baseDir, 'createAnnotations')
    
    def test_createAnnotationsTxt(self):
        testFile = util.hash(os.path.join(self.extAttchSampFile, 'CreateAnnotations-out-text.txt'))
        baseFile = util.hash(os.path.join(self.extAttchBase, 'CreateAnnotations-out-text.txt'))
        assert testFile == baseFile, "FAILED - File hashes do not match."

class TestFlattenAnnotations(object):
    extAttchSampFile = os.path.join(sampDir, 'FlattenAnnotations')
    extAttchBase = os.path.join(baseDir, 'flattenAnnotations')
    
    def test_flattenAnnotationsPDF(self):
        testFile = os.path.join(self.extAttchSampFile, 'FlattenAnnotations-out.pdf')
        baseFile = os.path.join(self.extAttchBase, 'FlattenAnnotations-out.pdf')
        assert util.compare_pdfs(testFile, baseFile), testFile + " failed, PDFs fail visual match"

# Legacy
    # def test_flattenAnnotationsPDF(self):
    #     testFile = os.path.join(self.extAttchSampFile, 'FlattenAnnotations-out.pdf')
    #     baseFile = os.path.join(self.extAttchBase, 'FlattenAnnotations-out.pdf')
    #     diffOut = os.path.join(self.extAttchSampFile, 'diffOut.png')
    #     var = util.imgCompare(testFile, baseFile, diffOut)
    #     assert var == b'0', "FAILED - Imaged PDFs do not match."