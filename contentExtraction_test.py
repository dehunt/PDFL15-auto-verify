# This contains test methods. Test methods must begin / end with test_ or _test in order for pytest to find them.
# Import common variables / methods from apdflTestUtils.py
# Relative paths are built for each test file on the assumption that pytest will be run from the product's base directory, and the complete test package has been copied into the product base directory.
# Baseline files are organized in a way that mimics the sample organization. Baseline folders are camelcase so sample files can't be accidently used.

import pytest, os, checkSamplesUtil as util
from checkSamplesUtil import samplesRootDir, testsDir

sampDir = os.path.join(samplesRootDir, 'ContentExtraction')
baseDir = os.path.join(testsDir, 'contentExtraction_test')

class TestCopyContent(object):
    extAttchSampFile = os.path.join(sampDir, 'CopyContent')
    extAttchBase = os.path.join(baseDir, 'copyContent')
    
    def test_copyContentPdf(self):
        testFile = os.path.join(self.extAttchSampFile, 'CopyContent-out.pdf')
        baseFile = os.path.join(self.extAttchBase, 'CopyContent-out.pdf')
        assert util.compare_pdfs(testFile, baseFile), testFile + " failed, PDFs fail visual match"

class TestExtractAttachments(object):
    extAttchSampFile = os.path.join(sampDir, 'extractAttachments')
    extAttchBase = os.path.join(baseDir, 'extractAttachments')
    
    def test_extractPdf(self):
        testFile = os.path.join(self.extAttchSampFile, '_x_extractPdf.pdf')
        baseFile = os.path.join(self.extAttchBase, '_x_extractPdf.pdf')
        assert util.compare_pdfs(testFile, baseFile), testFile + " failed, PDFs fail visual match"

    def test_extractPng(self):
        testFile = util.hash(os.path.join(self.extAttchSampFile, '_x_extractPng.png'))
        baseFile = util.hash(os.path.join(self.extAttchBase, '_x_extractPng.png'))
        assert testFile == baseFile, "FAILED - File hashes do not match."

    def test_extractJpgFromNameTree(self):
        testFile = util.hash(os.path.join(self.extAttchSampFile, '_x_extractJpgFromNameTree.jpg'))
        baseFile = util.hash(os.path.join(self.extAttchBase, '_x_extractJpgFromNameTree.jpg'))
        assert testFile == baseFile, "FAILED - File hashes do not match."

class TestExtractFonts(object):
    extAttchSampFile = os.path.join(sampDir, 'extractFonts')
    extAttchBase = os.path.join(baseDir, 'extractFonts')
    def test_extractArial(self):
        testFile = util.hash(os.path.join(self.extAttchSampFile, 'Arial.ttf'))
        baseFile = util.hash(os.path.join(self.extAttchBase, 'Arial.ttf'))
        assert testFile == baseFile, "FAILED - File hashes do not match."

    def test_extractEDJOJMMyriadProSemiBold(self):
        testFile = util.hash(os.path.join(self.extAttchSampFile, 'EDJOJM+MyriadPro-Semibold.pfb'))
        baseFile = util.hash(os.path.join(self.extAttchBase, 'EDJOJM+MyriadPro-Semibold.pfb'))
        assert testFile == baseFile, "FAILED - File hashes do not match."
        
    def test_EDJOKNMinionProBold(self):
        testFile = util.hash(os.path.join(self.extAttchSampFile, 'EDJOKN+MinionPro-Bold.pfb'))
        baseFile = util.hash(os.path.join(self.extAttchBase, 'EDJOKN+MinionPro-Bold.pfb'))
        assert testFile == baseFile, "FAILED - File hashes do not match."

    def test_EDJOLNMinionProRegular(self):
        testFile = util.hash(os.path.join(self.extAttchSampFile, 'EDJOLN+MinionPro-Regular.pfb'))
        baseFile = util.hash(os.path.join(self.extAttchBase, 'EDJOLN+MinionPro-Regular.pfb'))
        assert testFile == baseFile, "FAILED - File hashes do not match."

    def test_EDJONPMinionProIt(self):
        testFile = util.hash(os.path.join(self.extAttchSampFile, 'EDJONP+MinionPro-It.pfb'))
        baseFile = util.hash(os.path.join(self.extAttchBase, 'EDJONP+MinionPro-It.pfb'))
        assert testFile == baseFile, "FAILED - File hashes do not match."

    def test_EDJOOPMyriadProBold(self):
        testFile = util.hash(os.path.join(self.extAttchSampFile, 'EDJOOP+MyriadPro-Bold.pfb'))
        baseFile = util.hash(os.path.join(self.extAttchBase, 'EDJOOP+MyriadPro-Bold.pfb'))
        assert testFile == baseFile, "FAILED - File hashes do not match."

    def test_EDKCNLMyriadProBlack(self):
        testFile = util.hash(os.path.join(self.extAttchSampFile, 'EDKCNL+MyriadPro-Black.pfb'))
        baseFile = util.hash(os.path.join(self.extAttchBase, 'EDKCNL+MyriadPro-Black.pfb'))
        assert testFile == baseFile, "FAILED - File hashes do not match."

    def test_EDKDBLMinionProBoldIt(self):
        testFile = util.hash(os.path.join(self.extAttchSampFile, 'EDKDBL+MinionPro-BoldIt.pfb'))
        baseFile = util.hash(os.path.join(self.extAttchBase, 'EDKDBL+MinionPro-BoldIt.pfb'))
        assert testFile == baseFile, "FAILED - File hashes do not match."

    def test_FrutigerRoman(self):
        testFile = util.hash(os.path.join(self.extAttchSampFile, 'Frutiger-Roman.pfb'))
        baseFile = util.hash(os.path.join(self.extAttchBase, 'Frutiger-Roman.pfb'))
        assert testFile == baseFile, "FAILED - File hashes do not match."

    def test_GRQRYWKozGoProRegular(self):
        testFile = util.hash(os.path.join(self.extAttchSampFile, 'GRQRYW+KozGoPro-Regular.pfb'))
        baseFile = util.hash(os.path.join(self.extAttchBase, 'GRQRYW+KozGoPro-Regular.pfb'))
        assert testFile == baseFile, "FAILED - File hashes do not match."

    def test_Impact(self):
        testFile = util.hash(os.path.join(self.extAttchSampFile, 'Impact.ttf'))
        baseFile = util.hash(os.path.join(self.extAttchBase, 'Impact.ttf'))
        assert testFile == baseFile, "FAILED - File hashes do not match."

    def test_TimesNewRomanBold(self):
        testFile = util.hash(os.path.join(self.extAttchSampFile, 'TimesNewRoman,Bold.ttf'))
        baseFile = util.hash(os.path.join(self.extAttchBase, 'TimesNewRoman,Bold.ttf'))
        assert testFile == baseFile, "FAILED - File hashes do not match."

