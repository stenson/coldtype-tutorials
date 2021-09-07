from coldtype import *
from coldtype.time.midi import MidiReader
from coldtype.warping import warp

txt = "Animating Variable Fonts in Real-Time with Coldtype & Python / A TypeWknd Workshop /"

midi_file = __sibling__("media/tw2021_drums.mid")
drums = MidiReader(midi_file, duration=240, bpm=120, fps=30)[0]

@animation(timeline=drums.duration, bg=hsl(0.75, 1, 0.3))
def scratch(f):
    circle = (P()
        .define(r=f.a.r.inset(100))
        .gs("$r← $r↑|↖|c:=90 $r→|↗|c $r↓|↘|c §|↙|c"))
    
    return (StSt(txt, Font.Find("MeekDisplayv0.2-Medium.otf"), 78,
        #wght=1,
        #wdth=0.587,
        rotate=drums.fv(f.i, [40, 42], [10, 50]).e(rng=(0, 90)),
        #fit=circle.length()
        )
        .distribute_on_path(circle)
        .f(hsl(0.17, 1, 0.7, 0.8))
        .pen()
        #.ch(warp(f.i*3, f.i*3, mult=20))
        )
