# This contains test methods. Test methods must begin / end with test_ or _test in order for pytest to find them.
# Import common variables / methods from apdflTestUtils.py
# Relative paths are built for each test file on the assumption that pytest will be run from the product's base directory, and the complete test package has been copied into the product base directory.
# Baseline files are organized in a way that mimics the sample organization. Baseline folders are camelcase so sample files can't be accidently used.

import pytest, os, checkSamplesUtil as util
from checkSamplesUtil import samplesRootDir, testsDir

sampDir = os.path.join(samplesRootDir, 'ContentModification')
baseDir = os.path.join(testsDir, 'contentModification_test')

class TestAddDocumentInformation(object):
    extAttchSampFile = os.path.join(sampDir, 'AddDocumentInformation')
    extAttchBase = os.path.join(baseDir, 'addDocumentInformation')

    def test_addDocumentInformation_title(self):
        filename = 'AddDocumentInformation-out.pdf'
        assert util.get_pdf_title(os.path.join(self.extAttchSampFile, filename)) == util.get_pdf_title(
            os.path.join(self.extAttchBase, filename)), filename + " title compare failed"

    def test_addDocumentInformation_author(self):
        filename = 'AddDocumentInformation-out.pdf'
        assert util.get_pdf_author(os.path.join(self.extAttchSampFile, filename)) == util.get_pdf_author(
            os.path.join(self.extAttchBase, filename)), filename + " title compare failed"

# Watermarks still give false passes
# class TestAddWatermark(object):
#     extAttchSampFile = os.path.join(sampDir, 'AddWatermark')
#     extAttchBase = os.path.join(baseDir, 'addWatermark')
#
#     def test_addWatermarkPdf(self):
#         testFile = os.path.join(self.extAttchSampFile, 'AddWatermark-Out.pdf')
#         baseFile = os.path.join(self.extAttchBase, 'AddWatermark-Out.pdf')
#         assert util.compare_pdfs(testFile, baseFile), testFile + " failed, PDFs fail visual match"
    # def test_addWatermarkPdf(self):
    #     testFile = os.path.join(self.extAttchSampFile, 'AddWatermark-Out.pdf')
    #     baseFile = os.path.join(self.extAttchBase, 'AddWatermark-Out.pdf')
    #     diffOut = os.path.join(self.extAttchSampFile, 'diffComposite.png')
    #     var = util.imgCompareMultiPage(testFile, baseFile, diffOut)
    #     assert var == 0, "FAILED - PDFs do not match."

class TestFlattenTransparency(object):
    extAttchSampFile = os.path.join(sampDir, 'FlattenTransparency')
    extAttchBase = os.path.join(baseDir, 'flattenTransparency')
    
    def test_flattenTransparencyPdf(self):
        testFile = os.path.join(self.extAttchSampFile, 'FlattenTransparency-out.pdf')
        baseFile = os.path.join(self.extAttchBase, 'FlattenTransparency-out.pdf')
        assert util.compare_pdfs(testFile, baseFile), testFile + " failed, PDFs fail visual match"

class TestImportPages(object):
    extAttchSampFile = os.path.join(sampDir, 'ImportPages')
    extAttchBase = os.path.join(baseDir, 'importPages')
    
    def test_importPages(self):
        testFile = os.path.join(self.extAttchSampFile, 'importPages-out.pdf')
        baseFile = os.path.join(self.extAttchBase, 'importPages-out.pdf')
        assert util.compare_pdfs(testFile, baseFile), testFile + " failed, PDFs fail visual match"

class TestMergeDocuments(object):
    extAttchSampFile = os.path.join(sampDir, 'MergeDocuments')
    extAttchBase = os.path.join(baseDir, 'mergeDocuments')
    
    def test_mergeDocumentsPdf(self):
        testFile = os.path.join(self.extAttchSampFile, 'MergeDocuments-Out.pdf')
        baseFile = os.path.join(self.extAttchBase, 'MergeDocuments-Out.pdf')
        assert util.compare_pdfs(testFile, baseFile), testFile + " failed, PDFs fail visual match"
        # diffOut = os.path.join(self.extAttchSampFile, 'diffComposite.png')
        # var = util.imgCompareMultiPage(testFile, baseFile, diffOut)
        # assert var == 0, "FAILED - PDFs do not match."

class TestPDFMakeOCGVisible(object):
    extAttchSampFile = os.path.join(sampDir, 'PDFMakeOCGVisible')
    extAttchBase = os.path.join(baseDir, 'pdfMakeOCGVisible')
    
    def test_pdfMakeOCGVisible(self):
        testFile = os.path.join(self.extAttchSampFile, 'PDFMakeOCGVisible-out.pdf')
        baseFile = os.path.join(self.extAttchBase, 'PDFMakeOCGVisible-out.pdf')
        assert util.compare_pdfs(testFile, baseFile), testFile + " failed, PDFs fail visual match"

class TestSplitPDF(object):
    extAttchSampFile = os.path.join(sampDir, 'SplitPDF')
    extAttchBase = os.path.join(baseDir, 'splitPDF')
    
    def test_splitPdf01(self):
        testFile = os.path.join(self.extAttchSampFile, '_b_1.pdf')
        baseFile = os.path.join(self.extAttchBase, '_b_1.pdf')
        assert util.compare_pdfs(testFile, baseFile), testFile + " failed, PDFs fail visual match"
        # diffOut = os.path.join(self.extAttchSampFile, 'diffOut1.png')
        # var = util.imgCompare(testFile, baseFile, diffOut)
        # assert var == b'0', "FAILED - Imaged PDFs do not match."

    def test_splitPdf02(self):
        testFile = os.path.join(self.extAttchSampFile, '_b_2.pdf')
        baseFile = os.path.join(self.extAttchBase, '_b_2.pdf')
        assert util.compare_pdfs(testFile, baseFile), testFile + " failed, PDFs fail visual match"
        # diffOut = os.path.join(self.extAttchSampFile, 'diffOut2.png')
        # var = util.imgCompare(testFile, baseFile, diffOut)
        # assert var == b'0', "FAILED - Imaged PDFs do not match."

    def test_splitPdf03(self):
        testFile = os.path.join(self.extAttchSampFile, '_b_3.pdf')
        baseFile = os.path.join(self.extAttchBase, '_b_3.pdf')
        assert util.compare_pdfs(testFile, baseFile), testFile + " failed, PDFs fail visual match"

    def test_splitPdf04(self):
        testFile = os.path.join(self.extAttchSampFile, '_b_4.pdf')
        baseFile = os.path.join(self.extAttchBase, '_b_4.pdf')
        assert util.compare_pdfs(testFile, baseFile), testFile + " failed, PDFs fail visual match"

    def test_splitPdf05(self):
        testFile = os.path.join(self.extAttchSampFile, '_b_5.pdf')
        baseFile = os.path.join(self.extAttchBase, '_b_5.pdf')
        assert util.compare_pdfs(testFile, baseFile), testFile + " failed, PDFs fail visual match"

    def test_splitPdf06(self):
        testFile = os.path.join(self.extAttchSampFile, '_b_6.pdf')
        baseFile = os.path.join(self.extAttchBase, '_b_6.pdf')
        assert util.compare_pdfs(testFile, baseFile), testFile + " failed, PDFs fail visual match"
