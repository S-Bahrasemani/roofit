#####################################
#
# 'DATA AND CATEGORIES' ROOT.RooFit tutorial macro #406
#
# Demonstration of discrete-.discrete (invertable) functions
#
#
#
# 07/2008 - Wouter Verkerke
#
# /


import ROOT


def rf406_cattocatfuncs():
    # C o n s t r u c t  t w o   c a t e g o r i e s
    # ----------------------------------------------

    # Define a category with labels only
    tagCat = ROOT.RooCategory("tagCat", "Tagging category")
    tagCat.defineType("Lepton")
    tagCat.defineType("Kaon")
    tagCat.defineType("NetTagger-1")
    tagCat.defineType("NetTagger-2")
    tagCat.Print()

    # Define a category with explicitly numbered states
    b0flav = ROOT.RooCategory("b0flav", "B0 flavour eigenstate")
    b0flav.defineType("B0", -1)
    b0flav.defineType("B0bar", 1)
    b0flav.Print()

    # Construct a dummy dataset with random values of tagCat and b0flav
    x = ROOT.RooRealVar("x", "x", 0, 10)
    p = ROOT.RooPolynomial("p", "p", x)
    data = p.generate(ROOT.RooArgSet(x, b0flav, tagCat), 10000)

    # C r e a t e   a   c a t - > c a t   m  a p p i n g   c a t e g o r y
    # ---------------------------------------------------------------------

    # A ROOT.RooMappedCategory is category.category mapping function based on string expression
    # ROOT.The constructor takes an input category an a default state name to which unassigned
    # states are mapped
    tcatType = ROOT.RooMappedCategory(
        "tcatType", "tagCat type", tagCat, "Cut based")

    # Enter fully specified state mappings
    tcatType.map("Lepton", "Cut based")
    tcatType.map("Kaon", "Cut based")

    # Enter a wilcard expression mapping
    tcatType.map("NetTagger*", "Neural Network")

    # Make a table of the mapped category state multiplicit in data
    mtable = data.table(tcatType)
    mtable.Print("v")

    # C r e a t e   a   c a t   X   c a t   p r o d u c t   c a t e g o r y
    # ----------------------------------------------------------------------

    # A SUPER-category is 'product' of _lvalue_ categories. ROOT.The state names of a super
    # category is a composite of the state labels of the input categories
    b0Xtcat = ROOT.RooSuperCategory(
        "b0Xtcat", "b0flav X tagCat", ROOT.RooArgSet(b0flav, tagCat))

    # Make a table of the product category state multiplicity in data
    stable = data.table(b0Xtcat)
    stable.Print("v")

    # Since the super category is an lvalue, is explicitly possible
    b0Xtcat.setLabel("{B0bar;Lepton}")

    # A MULTI-category is a 'product' of any category (function). ROOT.The state names of a super
    # category is a composite of the state labels of the input categories
    b0Xttype = ROOT.RooMultiCategory(
        "b0Xttype", "b0flav X tagType", ROOT.RooArgSet(b0flav, tcatType))

    # Make a table of the product category state multiplicity in data
    xtable = data.table(b0Xttype)
    xtable.Print("v")


if __name__ == "__main__":
    rf406_cattocatfuncs()