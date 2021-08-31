from coldtype import *
from coldtype.fx.skia import phototype

"""
For the coldtype youtube channel banner
"""

@renderable((2048, 1152))
def banner(r):
    return (PS([
        P(r).f(hsl(0.65)),
        (Glyphwise("COLDTYPE", lambda g:
            Style(Font.ColdtypeObviously(), 450,
                wdth=ez(g.e, "seio", 2, rng=(1, 0)),
                kp={"D/T":-170},
                ro=1))
            .f(1)
            .reversePens()
            .understroke(sw=35)
            .align(r)
            .ch(phototype(r, blur=3, cut=200, cutw=10)))]))