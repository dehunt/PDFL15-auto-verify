# This contains test methods. Test methods must begin / end with test_ or _test in order for pytest to find them.
# Import common variables / methods from apdflTestUtils.py
# Relative paths are built for each test file on the assumption that pytest will be run from the product's base directory, and the complete test package has been copied into the product base directory.
# Baseline files are organized in a way that mimics the sample organization. Baseline folders are camelcase so sample files can't be accidently used.

import pytest, os
import checkSamplesUtil as util
# from ..util import samplesRootDir, testsDir

sampDir = os.path.join(util.samplesRootDir, 'Text')
baseDir = os.path.join(util.testsDir, 'text_test')

class TestAddText(object):
    extAttchSampFile = os.path.join(sampDir, 'AddText')
    extAttchBase = os.path.join(baseDir, 'addText')
    
    def test_addText(self):
        testFile = os.path.join(self.extAttchSampFile, 'AddText-out.pdf')
        baseFile = os.path.join(self.extAttchBase, 'AddText-out.pdf')
        diffOut = os.path.join(self.extAttchSampFile, 'diffOut.png')
        var = util.imgCompare(testFile, baseFile, diffOut)
        assert var == b'0', "FAILED - Imaged PDFs do not match."

class TestExtractText(object):
    extAttchSampFile = os.path.join(sampDir, 'ExtractText')
    extAttchBase = os.path.join(baseDir, 'extractText')
    
    def test_extractTextTxt(self):
        testFile = util.hash(os.path.join(self.extAttchSampFile, 'ExtractText-out.txt'))
        baseFile = util.hash(os.path.join(self.extAttchBase, 'ExtractText-out.txt'))
        assert testFile == baseFile, "FAILED - File hashes do not match."

    def test_extractTextPdf(self):
        testFile = os.path.join(self.extAttchSampFile, 'ExtractText-out.pdf')
        baseFile = os.path.join(self.extAttchBase, 'ExtractText-out.pdf')
        diffOut = os.path.join(self.extAttchSampFile, 'diffOut.png')
        var = util.imgCompare(testFile, baseFile, diffOut)
        assert var == b'0', "FAILED - Imaged PDFs do not match."

# class TestHelloJapan(object):
#     extAttchSampFile = os.path.join(sampDir, 'HelloJapan')
#     extAttchBase = os.path.join(baseDir, 'helloJapan')
    
#     def test_helloJapan(self):
#         testFile = os.path.join(self.extAttchSampFile, 'HelloJapan-out.pdf')
#         baseFile = os.path.join(self.extAttchBase, 'HelloJapan-out.pdf')
#         diffOut = os.path.join(self.extAttchSampFile, 'diffComposite.png')
#         var = util.imgCompareMultiPage(testFile, baseFile, diffOut)
#         assert var == 0, "FAILED - PDFs do not match."

class TestInsertHeadFoot(object):
    extAttchSampFile = os.path.join(sampDir, 'InsertHeadFoot')
    extAttchBase = os.path.join(baseDir, 'insertHeadFoot')
    
    def test_insertHeadFoot(self):
        testFile = os.path.join(self.extAttchSampFile, 'InsertHeadFoot-out.pdf')
        baseFile = os.path.join(self.extAttchBase, 'InsertHeadFoot-out.pdf')
        diffOut = os.path.join(self.extAttchSampFile, 'diffComposite.png')
        var = util.imgCompareMultiPage(testFile, baseFile, diffOut)
        assert var == 0, "FAILED - PDFs do not match."

# class TestTextSearch(object):
#     extAttchSampFile = os.path.join(sampDir, 'TextSearch')
#     extAttchBase = os.path.join(baseDir, 'textSearch')
    
#     def test_textSearch(self):
#         testFile = os.path.join(self.extAttchSampFile, 'TextSearch-out.pdf')
#         baseFile = os.path.join(self.extAttchBase, 'TextSearch-out.pdf')
#         diffOut = os.path.join(self.extAttchSampFile, 'diffComposite.png')
#         var = util.imgCompareMultiPage(testFile, baseFile, diffOut)
#         assert var == 0, "FAILED - PDFs do not match."

class TestTextSelectEnum(object):
    extAttchSampFile = os.path.join(sampDir, 'TextSelectEnum')
    extAttchBase = os.path.join(baseDir, 'textSelectEnum')
    
    def test_textSelectEnum(self):
        testFile = os.path.join(self.extAttchSampFile, 'TextSelectEnum-out.pdf')
        baseFile = os.path.join(self.extAttchBase, 'TextSelectEnum-out.pdf')
        diffOut = os.path.join(self.extAttchSampFile, 'diffOut.png')
        var = util.imgCompare(testFile, baseFile, diffOut)
        assert var == b'0', "FAILED - Imaged PDFs do not match."

# class TestUnicodeText(object):
#     extAttchSampFile = os.path.join(sampDir, 'UnicodeText')
#     extAttchBase = os.path.join(baseDir, 'unicodeText')
    
#     def test_unicodeText(self):
#         testFile = os.path.join(self.extAttchSampFile, 'UnicodeText-out.pdf')
#         baseFile = os.path.join(self.extAttchBase, 'UnicodeText-out.pdf')
#         diffOut = os.path.join(self.extAttchSampFile, 'diffComposite.png')
#         var = util.imgCompareMultiPage(testFile, baseFile, diffOut)
#         assert var == 0, "FAILED - PDFs do not match."