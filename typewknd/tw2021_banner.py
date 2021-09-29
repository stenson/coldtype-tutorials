from coldtype import *
from coldtype.fx.shapes import sine
from coldtype.fx.skia import phototype
from coldtype.time.midi import MidiReader
from coldtype.fx.warping import warp

txt = "Animating Variable Fonts with Coldtype and Python — A TypeWknd Workshop"

midi_file = __sibling__("media/tw2021_drums.mid")
midi = MidiReader(midi_file, duration=240, bpm=120, fps=30)

#vf = Programs.VF(Font.Find("MortVariableVF"), log=True)

@animation(timeline=midi.duration*4, bg=0)
def banner2(f):
    c = (P()
        .define(r=f.a.r.inset(10))
        .gs("$r← $r↑|↖|95 $r→|↗|95 $r↓|↘|95 §|↙|95")
        #.reverse()
        )
    #return c
    
    return (StSt(txt, Font.Find("MortVariableVF.ttf"), 32,
        bs=-50,
        tu=30,
        space=2000,
        wght=midi[0].fv(f.i%midi.duration, [40], [10, 30]).e(rng=(0.5, 1)),
        vrot=midi[0].fv(f.i%midi.duration, [40], [10, 30]).e())
        .distribute_on_path(c.copy().repeat(3), offset=f.e("l", rng=(0, c.length())))
        .pen()
        .flatten()
        .ch(warp(f.i*10, f.i*10, mult=50))
        #.reverse_pens()
        #.understroke()
        .f(1))
