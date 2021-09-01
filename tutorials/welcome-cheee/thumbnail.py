from coldtype import *
from coldtype.fx.skia import phototype

@aframe((1920, 1080), bg=hsl(0.85), render_bg=1)
def thumbnail(f):
    r = f.a.r
    return (PS([
        (StSt("Writing a Loop\n with Variable Fonts &",
            Font.Find("IrregardlessV"), 200, wght=1, slnt=1, leading=40)
            .f(1)
            .align(r)),
        (StSt("COLDTYPE", Font.ColdtypeObviously(), 300,
            tu=-50, r=1, ro=1, wdth=0.65)
            .align(r)
            .understroke(sw=20)
            .f(1))
        ])
        .reversePens()
        .distribute(v=1)
        .track(-80, v=1)
        .align(r)
        .scale(1.70)
        .rotate(5)
        .translate(0, 17)
        .ch(phototype(r, 2, cut=190, cutw=30)))
