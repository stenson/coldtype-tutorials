from coldtype import *
from coldtype.fx.skia import phototype

"""
For circular profile pics
"""

@renderable(rstate=1)
def logo(r, rs):
    return DPS([
        DP(r).f(hsl(0.65)).f(hsl(0.65, 0.6, 0.45)),
        (DP().oval(r.inset(-20))
            .f(None).s(1).sw(2)
            .ch(phototype(r, blur=10, cut=23, cutw=5))),
        (StSt("COLD\nTYPE", Font.ColdtypeObviously(), 500,
            wdth=0.5, tu=-50, r=1,
            kp={"P/E":-100}, leading=-10)
            .index(0, lambda p: p.translate(-130, 0))
            .reversePens()
            .align(r, th=1, tv=1)
            .rotate(15)
            .translate(-3, 3)
            .understroke(sw=25)
            .f(1)
            .ch(phototype(r,
                blur=5,
                cut=150,
                cutw=15,
                fill=bw(1))))])
        
@renderable()
def logo2(r):
    return DPS([
        DP(r).f(hsl(0.65)).f(0).f(hsl(0.65, 0.6, 0.45)),
        (DP().oval(r.inset(-20))
            .f(None).s(1).sw(2)
            .ch(phototype(r, blur=10, cut=23, cutw=5))),
        (StSt("C", Font.ColdtypeObviously(), 850,
            wdth=1, tu=20, r=1)
            .align(r)
            .f(1)
            .rotate(10)
            .translate(-5, -7)
            .ch(phototype(r,
                blur=5,
                cut=150,
                cutw=25,
                fill=bw(1))))])