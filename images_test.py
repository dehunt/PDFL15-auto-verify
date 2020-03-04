# This contains test methods. Test methods must begin / end with test_ or _test in order for pytest to find them.
# Import common variables / methods from apdflTestUtils.py
# Relative paths are built for each test file on the assumption that pytest will be run from the product's base directory, and the complete test package has been copied into the product base directory.
# Baseline files are organized in a way that mimics the sample organization. Baseline folders are camelcase so sample files can't be accidently used.

import pytest, os, checkSamplesUtil as util
from checkSamplesUtil import samplesRootDir, testsDir

sampDir = os.path.join(samplesRootDir, 'Images')
baseDir = os.path.join(testsDir, 'images_test')

class TestCalcImageDPI(object):
    extAttchSampFile = os.path.join(sampDir, 'CalcImageDPI')
    extAttchBase = os.path.join(baseDir, 'calcImageDPI')
    
    def test_calcImageDPI(self):
        testFile = util.hash(os.path.join(self.extAttchSampFile, 'CalcImageDPI-out.txt'))
        baseFile = util.hash(os.path.join(self.extAttchBase, 'CalcImageDPI-out.txt'))
        assert testFile == baseFile, "FAILED - File hashes do not match."

class TestFindImageResolutions(object):
    extAttchSampFile = os.path.join(sampDir, 'FindImageResolutions')
    extAttchBase = os.path.join(baseDir, 'findImageResolutions')
    
    def test_findImageResolutionsTxt(self):
        testFile = util.hash(os.path.join(self.extAttchSampFile, 'FindImageResolutions-out.txt'))
        baseFile = util.hash(os.path.join(self.extAttchBase, 'FindImageResolutions-out.txt'))
        assert testFile == baseFile, "FAILED - File hashes do not match."

    # def test_findImageResolutionsPdf(self):
    #     testFile = os.path.join(self.extAttchSampFile, 'FindImageResolutions.pdf')
    #     baseFile = os.path.join(self.extAttchBase, 'FindImageResolutions.pdf')
    #     diffOut = os.path.join(self.extAttchSampFile, 'diffComposite.png')
    #     var = util.imgCompareMultiPage(testFile, baseFile, diffOut)
    #     assert var == 0, "FAILED - PDFs do not match."

class TestAddThumbnailsToPDF(object):
    extAttchSampFile = os.path.join(sampDir, 'AddThumbnailsToPDF')
    extAttchBase = os.path.join(baseDir, 'addThumbnailsToPDF')
    
    def test_addThumbnailsPdf(self):
        testFile = os.path.join(self.extAttchSampFile, 'AddThumbnailsToPDF-out.pdf')
        baseFile = os.path.join(self.extAttchBase, 'AddThumbnailsToPDF-out.pdf')
        assert util.compare_pdfs(testFile, baseFile), testFile + " failed, PDFs fail visual match"
        # diffOut = os.path.join(self.extAttchSampFile, 'diffComposite.png')
        # var = util.imgCompareMultiPage(testFile, baseFile, diffOut)
        # assert var == 0, "FAILED - PDFs do not match."

class TestCreateImageWithTransparency(object):
    extAttchSampFile = os.path.join(sampDir, 'CreateImageWithTransparency')
    extAttchBase = os.path.join(baseDir, 'createImageWithTransparency')
    
    def test_createImageWithTransparencyPdf(self):
        testFile = os.path.join(self.extAttchSampFile, 'CreateImageWithTransparency-out.pdf')
        baseFile = os.path.join(self.extAttchBase, 'CreateImageWithTransparency-out.pdf')
        assert util.compare_pdfs(testFile, baseFile), testFile + " failed, PDFs fail visual match"

class TestCreateSeparations(object):
    extAttchSampFile = os.path.join(sampDir, 'CreateSeparations')
    extAttchBase = os.path.join(baseDir, 'createSeparations')
    
    def test_createSeparationsPdf(self):
        testFile = os.path.join(self.extAttchSampFile, 'Out.pdf')
        baseFile = os.path.join(self.extAttchBase, 'Out.pdf')
        assert util.compare_pdfs(testFile, baseFile), testFile + " failed, PDFs fail visual match"
        # diffOut = os.path.join(self.extAttchSampFile, 'diffComposite.png')
        # var = util.imgCompareMultiPage(testFile, baseFile, diffOut)
        # assert var == 0, "FAILED - PDFs do not match."

class TestOutputPreview(object):
    extAttchSampFile = os.path.join(sampDir, 'OutputPreview')
    extAttchBase = os.path.join(baseDir, 'outputPreview')
    
    def test_outputPreviewPdf(self):
        testFile = os.path.join(self.extAttchSampFile, 'Out.pdf')
        baseFile = os.path.join(self.extAttchBase, 'Out.pdf')
        assert util.compare_pdfs(testFile, baseFile), testFile + " failed, PDFs fail visual match"
        # diffOut = os.path.join(self.extAttchSampFile, 'diffComposite.png')
        # var = util.imgCompareMultiPage(testFile, baseFile, diffOut)
        # assert var == 0, "FAILED - PDFs do not match."

class TestRenderPage(object):
    extAttchSampFile = os.path.join(sampDir, 'RenderPage')
    extAttchBase = os.path.join(baseDir, 'renderPage')
    
    def test_renderPagePdf(self):
        testFile = os.path.join(self.extAttchSampFile, 'RenderPage-out.pdf')
        baseFile = os.path.join(self.extAttchBase, 'RenderPage-out.pdf')
        assert util.compare_pdfs(testFile, baseFile), testFile + " failed, PDFs fail visual match"