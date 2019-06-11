# All comparison setup methods are here.
# Additionally, test wide variables 

import os, hashlib, subprocess, PyPDF2
from subprocess import PIPE
from pathlib import Path

# The beginning of the path name that the C++ samples are in. This shouldn't need to change, unless engineering changes the directory structure again. If they do, individual tests may also need to be updated.
samplesRootDir = os.path.join(os.environ['APDFL_DIR'], 'CPlusPlus', 'Sample_Source')
# The name of the directory containing these scripts and the baseline files. This shouldn't need to change.
testsDir = 'checkSamplesCpp'

# Fuzz allows small color variance within the specified percentage. More info here: http://www.imagemagick.org/script/command-line-options.php#fuzz
compareFuzzVal = '5%'
# Comparison metric type to use. We use absolute error count, producing the number of incorrect pixels (after accounting for fuzz), so that we can assert with that number. More info here: https://imagemagick.org/script/command-line-options.php#metric
compareMetric = 'AE'
# Higher density is more precise. Imagemagick default is 72 dpi. More info here: http://www.imagemagick.org/script/command-line-options.php#density
compareDensity = '300'

# Takes a file and returns the hashed value for that file. 
#   Used to verify files that should not change between versions / executions (such as files without timestamps).
def hash(incFile):
    suf = Path(incFile).suffix
    print("Suf is:")
    print(suf)
    # Strip carriage return if found, so win matches lin
    hasher = hashlib.md5()
    with open(incFile, 'rb') as f:
        buf = f.read()
        if suf == '.txt':
            print("txt file detected")
            buf = buf.replace(b'\r\n',b'\n')
        hasher.update(buf)
        a = hasher.hexdigest()
        print("For inFile:" + incFile)
        print("md5 hash result: " + a)
        return(a)

# Takes two files and a path+filename to place a diff heatmap image at.
#   Used for visual comparison of two files (such as text and images on a PDF). Cannot verify metadata, existence of not-visible layers, whether an element is a layer, etc.
#   Intended for use with two single page PDFs. Will not work with a multipage PDF.
#   When imagemagick is used to compare, it returns b'0' (bytesprefix 0) to stderr if there is no difference between the images.
def imgCompare(inFileA, inFileB, diffFile):
    print("Magick command is as follows: ")
    print("magick " + "compare " + "-density " + compareDensity + " -metric " + compareMetric + " -fuzz " + compareFuzzVal + " -quiet " + inFileA + " " + inFileB + " " + diffFile)
    print(" ")
    result = subprocess.run(["magick", "compare", "-density", compareDensity, "-metric", compareMetric, "-fuzz", compareFuzzVal, "-quiet", inFileA, inFileB, diffFile], env={'PATH': os.getenv('PATH'), 'MAGICK_TEMPORARY_PATH': os.getenv('MAGICK_TEMPORARY_PATH')}, stderr=PIPE, shell=True)
    print(result)
    return result.stderr

# Takes two files and a path+filename where the composite image should go
#   Compares pdf page count and returns a fail if there's a page count mismatch
#   Then creates composite images of the differences between the two pdfs, producing one page per image.
#   Finally, compares the imageComposite to a known good composite using imgCompare and it's fuzz / metric /density settings. If any page fails, sets retval to fail.
#   Returns 1 if comparisons fail, 0 if comparisons succeed all the way through the PDF.
#   When imagemagick is used to compare, it returns b'0' (bytesprefix 0) to stderr if there is no difference between the images.
#   Note that here, we only take the diffFile name, because we need to add in page numbers.
def imgCompareMultiPage(inFileA, inFileB, diffFile):
    retval = 0
    print("Basic magick commands are as follows: ")
    print("magick " + inFileA + " null: " + inFileB + " -compose " + "difference" + " -layers " + "composite" + " " + inFileA + " " + inFileB + " " + diffFile)
    print(" ")
    chkPgs = comparePageCount(inFileA, inFileB)
    if chkPgs == 0:
        print("PDF page count matches")
    else:
        print("=== ERROR: PDF page count mismatch ===")
        return 1
    subprocess.run(["magick", inFileA, "null:", inFileB, "-compose", "difference", "-layers", "composite", inFileA, inFileB, diffFile], env={'PATH': os.getenv('PATH'), 'MAGICK_TEMPORARY_PATH': os.getenv('MAGICK_TEMPORARY_PATH')}, stderr=PIPE, stdout=PIPE, shell=True)
    testPath=os.path.dirname(inFileA)
    basePath=os.path.dirname(inFileB)
    for page in range(getPageCount(inFileA)):
        print("Comparing page: " + str(page))
        compVal = imgCompare(os.path.join(testPath, "diffComposite-"+str(page)+".png"), os.path.join(basePath, "diffComposite-"+str(page)+".png"), os.path.join(testPath, "diffOut-"+str(page)+".png"))
        if compVal != b'0':
            print("PDF mismatch at page "+str(page))
            print("")
            retval = 1
    return retval

# Helper function to compare page counts of two PDFs
def comparePageCount(inFileA, inFileB):
    if getPageCount(inFileA) == getPageCount(inFileB):
        return 0
    else:
        return 1

# Helper function to get the page count of a PDF
def getPageCount(inFile):
    with open(inFile, "rb") as inc:
        reader = PyPDF2.PdfFileReader(inc, "rb")
        return reader.getNumPages()