#####################################
#
# 'BASIC FUNCTIONALITY' ROOT.RooFit tutorial macro #104
#
# ROOT.The class factory for functions and p.d.f.s
#
#
# NOTE: ROOT.This demo uses code that is generated by the macro,
#       therefore it cannot be compiled in one step by ACliC.
#       ROOT.To run this macro compiled with ACliC do
#
#         root>.x rf104_classfactory.C # run interpreted to generate code
#         root>.L MyPdfV3.cxx+         # Compile and load created classs
#         root>.x rf104_classfactory.C+ # run compiled code
#
#
# 07/2008 - Wouter Verkerke
#
# /


import ROOT


def rf104_classfactory():

    # W r i t e   c l a s s   s k e l e t o n   c o d e
    # --------------------------------------------------

    # Write skeleton p.d.f class with variable x,a,b
    # ROOT.To use this class,
    #    - Edit the file MyPdfV1.cxx and implement the evaluate() method in terms of x,a and b
    #    - Compile and link class with '.x MyPdfV1.cxx+'
    #
    ROOT.RooClassFactory.makePdf("MyPdfV1", "x,A,B")

    # W i t h   a d d e d   i n i t i a l   v a l u e   e x p r e s s i o n
    # ---------------------------------------------------------------------

    # Write skeleton p.d.f class with variable x,a,b and given formula expression
    # ROOT.To use this class,
    #    - Compile and link class with '.x MyPdfV2.cxx+'
    #
    ROOT.RooClassFactory.makePdf(
        "MyPdfV2", "x,A,B", "", "A*fabs(x)+pow(x-B,2)")

    # W i t h   a d d e d   a n a l y t i c a l   i n t e g r a l   e x p r e s s i o n
    # ---------------------------------------------------------------------------------

    # Write skeleton p.d.f class with variable x,a,b, given formula expression _and_
    # given expression for analytical integral over x
    # ROOT.To use this class,
    #    - Compile and link class with '.x MyPdfV3.cxx+'
    #
    ROOT.RooClassFactory.makePdf("MyPdfV3", "x,A,B", "", "A*fabs(x)+pow(x-B,2)", ROOT.kTRUE, ROOT.kFALSE,
                                 "x:(A/2)*(pow(x.max(rangeName),2)+pow(x.min(rangeName),2))+(1./3)*(pow(x.max(rangeName)-B,3)-pow(x.min(rangeName)-B,3))")

    # U s e   i n s t a n c e   o f   c r e a t e d   c l a s s
    # ---------------------------------------------------------

    # Compile MyPdfV3 class (only when running in CINT)
    ROOT.gROOT.ProcessLineSync(".x MyPdfV3.cxx+")

    # Creat instance of MyPdfV3 class
    a = ROOT.RooRealVar("a", "a", 1)
    b = ROOT.RooRealVar("b", "b", 2, -10, 10)
    y = ROOT.RooRealVar("y", "y", -10, 10)
    pdf = ROOT.MyPdfV3("pdf", "pdf", y, a, b)

    # Generate toy data from pdf and plot data and p.d.f on frame
    frame1 = y.frame(ROOT.RooFit.Title("Compiled class MyPdfV3"))
    data = pdf.generate(ROOT.RooArgSet(y), 1000)
    pdf.fitTo(data)
    data.plotOn(frame1)
    pdf.plotOn(frame1)

    # /
    # C o m p i l e d   v e r s i o n   o f   e x a m p l e   r f 1 0 3 #
    # /

    # Declare observable x
    x = ROOT.RooRealVar("x", "x", -20, 20)

    # ROOT.The ROOT.RooClassFactory.makePdfInstance() function performs code writing, compiling, linking
    # and object instantiation in one go and can serve as a straight
    # replacement of ROOT.RooGenericPdf

    alpha = ROOT.RooRealVar("alpha", "alpha", 5, 0.1, 10)
    genpdf = ROOT.RooClassFactory.makePdfInstance(
        "GenPdf", "(1+0.1*fabs(x)+sin(sqrt(fabs(x*alpha+0.1))))", ROOT.RooArgList(x, alpha))

    # Generate a toy dataset from the interpreted p.d.f
    data2 = genpdf.generate(ROOT.RooArgSet(x), 50000)

    # Fit the interpreted p.d.f to the generated data
    genpdf.fitTo(data2)

    # Make a plot of the data and the p.d.f overlaid
    frame2 = x.frame(ROOT.RooFit.Title("Compiled version of pdf of rf103"))
    data2.plotOn(frame2)
    genpdf.plotOn(frame2)

    # Draw all frames on a canvas
    c = ROOT.TCanvas("rf104_classfactory", "rf104_classfactory", 800, 400)
    c.Divide(2)
    c.cd(1)
    ROOT.gPad.SetLeftMargin(0.15)
    frame1.GetYaxis().SetTitleOffset(1.4)
    frame1.Draw()
    c.cd(2)
    ROOT.gPad.SetLeftMargin(0.15)
    frame2.GetYaxis().SetTitleOffset(1.4)
    frame2.Draw()

    c.SaveAs("rf104_classfactory.png")

if __name__ == "__main__":
    rf104_classfactory()
