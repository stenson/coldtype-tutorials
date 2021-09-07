from coldtype import *
from coldtype.time.midi import MidiReader

txt = "TYPE\nWKND"
#txt = "COLD\nTYPE"
txt = "WORK\nSHOP"
#txt = "9/30\n2021"

midi_file = __sibling__("media/tw2021_drums.mid")
drums = MidiReader(midi_file, duration=240, bpm=120, fps=30)[0]

h = 0.75
if "cold" in txt.lower():
    h = 0.85
elif "work" in txt.lower():
    h = 0.45
elif "2021" in txt:
    h = 0.65

@animation(timeline=drums.duration, bg=hsl(h, 1, 0.3), render_bg=1)
def tw2021_loop3(f):
    kick = drums.fv(f.i, [36], [5, 50])
    snare = drums.fv(f.i, [40], [10, 40])
    clap = drums.fv(f.i, [42], [10, 60])
    hat = drums.fv(f.i, [43], [15, 30])
    
    clave = drums.fv(f.i, [46], [10, 20])
    tom_lo = drums.fv(f.i, [48], [10, 20])
    tom_md = drums.fv(f.i, [49], [10, 20])
    tom_hi = drums.fv(f.i, [50], [10, 20])

    high_grvt = 0

    yests = {
        "T": kick.e(),
        "Y": kick.e(),
        "P": snare.e(),
        "E": snare.e(),
        "D": tom_lo.e(rng=(0, 0.75)),
        "N": tom_md.e(rng=(0, 0.65)),
        "K": tom_hi.e(rng=(0, 0.55)),
        "W": clave.e(rng=(0, 0.45)),
    }

    bss = {
        "D": tom_lo.e(),
        "N": tom_md.e(),
        "K": tom_hi.e(),
        "W": clave.e(),
    }

    if "work" in txt.lower():
        high_grvt = 1
        yests = {**yests, **{
            "W": kick.e(),
            "O": snare.e(),
            "P": kick.e(),
            "S": tom_lo.e(rng=(0, 0.75)),
            "H": tom_md.e(rng=(0, 0.65)),
            "R": tom_hi.e(rng=(0, 0.55)),
            "K": clave.e(rng=(0, 0.45)),
        }}
        bss = {
            "S": tom_lo.e(),
            "H": tom_md.e(),
            "R": tom_hi.e(),
            "K": clave.e(),
        }
    
    if "2021" in txt.lower():
        yests = {
            "0": kick.e(),
            "2": snare.e(),
            #"P": kick.e(),
            "9": tom_lo.e(rng=(0, 0.75)),
            "/": tom_md.e(rng=(0, 0.65)),
            "3": tom_hi.e(rng=(0, 0.55)),
            "1": clave.e(rng=(0, 0.45)),
        }
        bss = {
            "9": tom_lo.e(),
            #"/": tom_md.e(),
            "3": tom_hi.e(),
            "1": clave.e(),
        }
    
    if "cold" in txt.lower():
        yests = {**yests, **{
            "D": tom_lo.e(rng=(0, 0.75)),
            "L": tom_md.e(rng=(0, 0.65)),
            "O": tom_hi.e(rng=(0, 0.55)),
            "C": clave.e(rng=(0, 0.45)),
        }}
        bss = {**bss, **{
            "D": tom_lo.e(),
            "L": tom_md.e(),
            "O": tom_hi.e(),
            "C": clave.e(),
        }}

    def styler(g):
        gcu = g.c.upper()
        return [
            Style(Font.Find("CheeeV"), fs:=390,
                tu=clap.e(rng=(0, -350)),
                grvt=1 if g.l == high_grvt else 0,
                yest=0, bs=0),
            Style(
                Font.Find("CheeeV"), fs,
                tu=clap.e(rng=(0, -350)),
                yest=yests.get(gcu, 0),
                grvt=hat.e(rng=(1, 0)) if g.l == high_grvt
                    else max(bss.get(gcu, 0), hat.e()),
                bs=bss.get(gcu, 0)*-50)]

    lockup = (Glyphwise(txt, styler)
        .xalign(f.a.r, th=0)
        .track(hat.e(rng=(0, 30)), v=1)
        .align(f.a.r, x=None)
        .f(hsl(h, 1, 0.75))
        .collapse()
        .reversePens()
        .understroke(sw=10, s=hsl(h, 1, 0.15)))
    
    return PS([
        lockup.pen().translate(10, -10),
        lockup
    ])
