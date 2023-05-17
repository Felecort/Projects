from manim import *
import numpy as np
from numpy.random import uniform

WORDS = (
    r"e^{i\pi}+1=0",
    r"3^2+4^2=5^2",
    r"V+F-E=2",
    r"\exists",
    r"\forall",
    r"\Rightarrow",
    r"\Leftarrow",
    r"\infty",
    r"\pi",
    r"\frac{a+b}{2}\geqslant \sqrt{ab}",
)

STEPS = 3


def get_position(h=(-6.5, 6.5), v=(-3, 3)):
    x, y = uniform(*h), uniform(*v)
    return np.array((x, y, 0))


class Cloud(Scene):
    def construct(self):
        words = VGroup(*[MathTex(w) for w in WORDS])
        # words.arrange_in_grid(cols=2)
        for word in words:
            word.move_to(get_position())
        fade = [GrowFromCenter(w) for w in words]
        self.play(AnimationGroup(*fade, lag_ratio=0.1))
        # self.add(words)
        self.wait(3)
