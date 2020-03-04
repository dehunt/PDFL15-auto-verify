# This contains test methods. Test methods must begin / end with test_ or _test in order for pytest to find them.
# Import common variables / methods from apdflTestUtils.py
# Relative paths are built for each test file on the assumption that pytest will be run from the product's base directory, and the complete test package has been copied into the product base directory.
# Baseline files are organized in a way that mimics the sample organization. Baseline folders are camelcase so sample files can't be accidently used.

import pytest, os, checkSamplesUtil as util
from checkSamplesUtil import samplesRootDir, testsDir

sampDir = os.path.join(samplesRootDir, 'contentCreation')
baseDir = os.path.join(testsDir, 'contentCreation_test')

class TestAddArt(object):
    extAttchSampFile = os.path.join(sampDir, 'AddArt')
    extAttchBase = os.path.join(baseDir, 'addArt')
    
    def test_addArtPdf(self):
        testFile = os.path.join(self.extAttchSampFile, 'AddArt-out.pdf')
        baseFile = os.path.join(self.extAttchBase, 'AddArt-out.pdf')
        assert util.compare_pdfs(testFile, baseFile), testFile + " failed"
# Legacy
#     def test_addArtPdf(self):
#         testFile = os.path.join(self.extAttchSampFile, 'AddArt-out.pdf')
#         baseFile = os.path.join(self.extAttchBase, 'AddArt-out.pdf')
#         assert util.compare_pdfs(testFile, baseFile), testFile + " failed"
#         diffOut = os.path.join(self.extAttchSampFile, 'diffOut.png')
#         var = util.imgCompare(testFile, baseFile, diffOut)
#         assert var == b'0', "FAILED - Imaged PDFs do not match."

class TestAddContent(object):
    extAttchSampFile = os.path.join(sampDir, 'AddContent')
    extAttchBase = os.path.join(baseDir, 'addContent')
    
    def test_addContentPdf(self):
        testFile = os.path.join(self.extAttchSampFile, 'AddContent-out.pdf')
        baseFile = os.path.join(self.extAttchBase, 'AddContent-out.pdf')
        assert util.compare_pdfs(testFile, baseFile), testFile + " failed, PDFs fail visual match"
        
class TestCreateDocument(object):
    extAttchSampFile = os.path.join(sampDir, 'CreateDocument')
    extAttchBase = os.path.join(baseDir, 'createDocument')
    
    def test_createDocumentPdf(self):
        testFile = os.path.join(self.extAttchSampFile, 'CreateDocument-out.pdf')
        baseFile = os.path.join(self.extAttchBase, 'CreateDocument-out.pdf')
        assert util.compare_pdfs(testFile, baseFile), testFile + " failed, PDFs fail visual match"

class TestCreateTransparency(object):
    extAttchSampFile = os.path.join(sampDir, 'CreateTransparency')
    extAttchBase = os.path.join(baseDir, 'createTransparency')
    
    def test_createTransparencyPdf(self):
        testFile = os.path.join(self.extAttchSampFile, 'CreateTransparency-out.pdf')
        baseFile = os.path.join(self.extAttchBase, 'CreateTransparency-out.pdf')
        assert util.compare_pdfs(testFile, baseFile), testFile + " failed, PDFs fail visual match"

# Note that we're not actually using the get_attachments() function. This PDF is organized differently than the Opt ones.
# Not all attachments are in catalog. So we delve through the PDF and use PyPDF2's getObject mixed with the correct
# location path in order to get the attachment name strings.
class TestAddAttachments(object):
    extAttchSampFile = os.path.join(sampDir, 'AddAttachments')
    extAttchBase = os.path.join(baseDir, 'addAttachments')

    def test_addAttachments_spreadsheet(self):
        testfile = 'AddAttachments-out.pdf'
        list_path = ['/Names', '/EmbeddedFiles', '/Names', 00000]
        assert util.get_attachment_four_loc(os.path.join(self.extAttchSampFile, testfile), list_path) == util.get_attachment_four_loc(os.path.join(self.extAttchBase, testfile), list_path), testfile + " failed"

    def test_addAttachments_docx(self):
        testfile = 'AddAttachments-out.pdf'
        page = 0
        list_path = ['/Annots', 0, '/FS', '/F']
        # The actual attachment content for this docx file is at [/Annots][0]['/FS']['/EF']['/F']
        assert util.get_attachment_from_page_two_by_two(os.path.join(self.extAttchSampFile, testfile), page, list_path) == util.get_attachment_from_page_two_by_two(os.path.join(self.extAttchBase, testfile), page, list_path), testfile + " failed"
