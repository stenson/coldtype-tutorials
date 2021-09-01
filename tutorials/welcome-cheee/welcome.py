from coldtype import *
from coldtype.fx.skia import phototype

@animation(timeline=30, bg=hsl(0.6), render_bg=1)
def welcome(f):
    return (Glyphwise("HELLO", lambda g:
        Style(Font.Find("CheeeV"), 350,
            yest=(fa:=f.adj(-g.i*5)).e("eeio", 1),
            grvt=f.adj(g.i*10).e("eeio", 1),
            tu=fa.e("eeio", 1, rng=(0, -300))))
        .align(f.a.r)
        .fssw(-1, 1, 4)
        #.ch(phototype(f.a.r, blur=5, cut=50, cutw=13))
        )

release = welcome.export("h264", loops=16)