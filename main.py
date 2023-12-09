from manim import *
import networkx as nx

nxgraph = nx.erdos_renyi_graph(14, 0.5)


class InstaChallenge(Scene):
    def construct(self):
        self.camera.background_color = DARK_GRAY
        wknight1t, wknight2t = SVGMobject("wN.svg").to_edge(DOWN), SVGMobject("wN.svg").to_edge(DOWN)
        bknight1t, bknight2t = SVGMobject("bN.svg").to_edge(DOWN), SVGMobject("bN.svg").to_edge(DOWN)
        wknight1g, wknight2g = SVGMobject("wN.svg").to_edge(DOWN), SVGMobject("wN.svg").to_edge(DOWN)
        bknight1g, bknight2g = SVGMobject("bN.svg").to_edge(DOWN), SVGMobject("bN.svg").to_edge(DOWN)
        data = [["a", "b", "c"],
                ["d", "e", "f"],
                ["g", "h", "i"]]
        cell_loc = {'a': (1, 1), 'b': (1, 2), 'c': (1, 3),
                    'd': (2, 1), 'e': (2, 2), 'f': (2, 3),
                    'g': (3, 1), 'h': (3, 2), 'i': (3, 3)}

        # Graph
        g = Graph(
            [node for node in "ahcdibgf"],
            [("a", "f"), ("f", "g"), ("g", "b"), ("b", "i"), ("i", "d"), ("d", "c"), ("c", "h"), ("h", "a")],
            labels=True,
            layout="circular",
            layout_scale=2
        ).to_edge(DR)
        # # INTRO

        lbl_tbl = Tex("1. Label the squares").to_edge(UP)
        # Create the table
        table = Table(data).next_to(lbl_tbl, DOWN)
        t1 = Tex("The grid can now be modelled as a").next_to(table, DOWN)
        graph_text = Tex("graph").next_to(t1, DOWN)
        graph_text2 = Tex("The main object of").next_to(graph_text, DOWN)
        graph_theory_text = Tex("GRAPH THEORY:").set_color(GREEN)
        network_g = Graph.from_networkx(nxgraph, layout="spring", layout_scale=3.5).set_color(GREEN).scale(.6)

        t2 = Tex("Each vertex represents a square").scale(.8).to_edge(UP)
        t2_2 = Tex("""A vertex is connected to another vertex if the\\\\
                corresponding squares are directly connected by a knight move""").next_to(t2, DOWN, buff=0.5).scale(.8)

        qr = SVGMobject("qr.svg")
        flat_data = [item for sublist in data for item in sublist]
        vertices = g.vertices

        # SCENES, Challenge reminder and first table
        self.play(Write(lbl_tbl))
        self.play(Write(table))
        self.wait()
        self.play(DrawBorderThenFill(wknight1t.scale(.5)), DrawBorderThenFill(wknight2t.scale(.5)),
                  DrawBorderThenFill(bknight1t.scale(.5)), DrawBorderThenFill(bknight2t.scale(.5)))
        #
        self.play(wknight1t.animate.move_to(table.get_cell((1, 1))), wknight2t.animate.move_to(table.get_cell((1, 3))),
                  bknight1t.animate.move_to(table.get_cell((3, 1))), bknight2t.animate.move_to(table.get_cell((3, 3))))
        self.wait()
        # # GRaph theory title
        self.play(Write(t1))
        self.play(Write(graph_text.next_to(t1, DOWN)))
        self.wait()
        self.play(Write(graph_text2))
        self.play(FadeOut(t1, lbl_tbl, table, wknight1t, wknight2t, bknight1t, bknight2t, graph_text2),
                  ReplacementTransform(graph_text, graph_theory_text))
        self.play(Create(network_g), graph_theory_text.animate.to_edge(UP))
        self.play(*[network_g[v].animate.move_to(2 * RIGHT * np.cos(ind / 7 * PI) + 2 * UP * np.sin(ind / 7 * PI))
                    for ind, v in enumerate(network_g.vertices)])
        self.wait(5)
        self.play(Uncreate(network_g), FadeOut(graph_theory_text))
        #
        # Second table to left and graph construction

        wknight1t.add_updater(lambda obj: obj.move_to(table.get_cell((1, 1))))
        wknight2t.add_updater(lambda obj: obj.move_to(table.get_cell((1, 3))))
        bknight1t.add_updater(lambda obj: obj.move_to(table.get_cell((3, 1))))
        bknight2t.add_updater(lambda obj: obj.move_to(table.get_cell((3, 3))))

        self.play(FadeIn(table, wknight1t, wknight2t, bknight1t, bknight2t))
        self.play(table.animate.to_edge(DL))
        self.play(
            Write(g, run_time=10),
            Write(t2)
        )
        self.play(Write(t2_2))
        self.wait()
        self.play(g.animate.to_edge(RIGHT), FadeOut(wknight1t, bknight1t, wknight2t, bknight2t))

        highlight_sq_tb, highlight_sq_g = Square(.8).set_color(RED), Square(.8).set_color(RED)
        self.play(Write(highlight_sq_g), Write(highlight_sq_tb))
        self.play(highlight_sq_tb.animate.move_to(table.get_cell((1, 1))),
                  highlight_sq_g.animate.move_to(g.vertices["a"]))
        self.wait(0.5)
        self.play(highlight_sq_tb.animate.move_to(table.get_cell((2, 3))),
                  highlight_sq_g.animate.move_to(g.vertices["f"]))
        self.wait(0.5)
        self.play(highlight_sq_tb.animate.move_to(table.get_cell((3, 1))),
                  highlight_sq_g.animate.move_to(g.vertices["g"]))
        self.wait(0.5)
        self.play(highlight_sq_tb.animate.move_to(table.get_cell((1, 2))),
                  highlight_sq_g.animate.move_to(g.vertices["b"]))
        self.wait(0.5)
        self.play(highlight_sq_tb.animate.move_to(table.get_cell((3, 3))),
                  highlight_sq_g.animate.move_to(g.vertices["i"]))
        self.play(highlight_sq_tb.animate.move_to(table.get_cell((2, 1))),
                  highlight_sq_g.animate.move_to(g.vertices["d"]))
        self.play(highlight_sq_tb.animate.move_to(table.get_cell((1, 3))),
                  highlight_sq_g.animate.move_to(g.vertices["c"]))
        self.play(highlight_sq_tb.animate.move_to(table.get_cell((3, 2))),
                  highlight_sq_g.animate.move_to(g.vertices["h"]))
        self.play(highlight_sq_tb.animate.move_to(table.get_cell((1, 1))),
                  highlight_sq_g.animate.move_to(g.vertices["a"]))
        self.play(FadeOut(highlight_sq_g, highlight_sq_tb))

        self.play(DrawBorderThenFill(wknight1t), DrawBorderThenFill(wknight2t),
                  DrawBorderThenFill(bknight1t), DrawBorderThenFill(bknight2t),
                  DrawBorderThenFill(wknight1g.scale(.5)), DrawBorderThenFill(wknight2g.scale(.5)),
                  DrawBorderThenFill(bknight1g.scale(.5)), DrawBorderThenFill(bknight2g.scale(.5)))

        self.play(wknight1t.animate.move_to(table.get_cell((1, 1))), wknight2t.animate.move_to(table.get_cell((1, 3))),
                  bknight1t.animate.move_to(table.get_cell((3, 1))), bknight2t.animate.move_to(table.get_cell((3, 3))),
                  wknight1g.animate.move_to(g.vertices['a']), wknight2g.animate.move_to(g.vertices['c']),
                  bknight1g.animate.move_to(g.vertices['g']), bknight2g.animate.move_to(g.vertices['i']))
        self.wait()
        #
        wknight1g.add_updater(lambda obj: obj.move_to(g.vertices['a']))
        wknight2g.add_updater(lambda obj: obj.move_to(g.vertices['c']))
        bknight1g.add_updater(lambda obj: obj.move_to(g.vertices['g']))
        bknight2g.add_updater(lambda obj: obj.move_to(g.vertices['i']))
        #
        # # Graph solution
        t3 = Tex("Next, solve the problem in the graph,\\\\ where the solution is straightforward").to_edge(UP).scale(.8)
        t4 = Tex("and record the moves").to_edge(UP)
        self.play(Write(t3), FadeOut(t2, t2_2))
        self.wait()
        af, fg = Text("a → f", font="monospace").scale(.4), Text("f → g", font="monospace").scale(.4)
        gb, bi = Text("g → b", font="monospace").scale(.4), Text("b → i", font="monospace").scale(.4)
        id, dc = Text("i → d", font="monospace").scale(.4), Text("d → c", font="monospace").scale(.4)
        ch, ha = Text("c → h", font="monospace").scale(.4), Text("h → a", font="monospace").scale(.4)
        gb2, id2, ch2, af2, bi2, dc2, ha2 = gb.copy(), id.copy(), ch.copy(), af.copy(), bi.copy(), dc.copy(), ha.copy()
        fg2 = fg.copy()
        moves = [af, fg, gb, bi, id, dc, ch, ha, gb2, id2, ch2, af2, bi2, dc2, ha2, fg2]
        self.play(FadeOut(table, wknight1t, wknight2t, bknight1t, bknight2t, t3),
                  g.animate.next_to(t3, DOWN, buff=.5), Write(t4))
        #
        # #  c - h - a - f - g - b - i - d - c
        wknight1g.clear_updaters(), wknight2g.clear_updaters(), bknight1g.clear_updaters(), bknight2g.clear_updaters()
        self.wait(2)
        self.play(wknight1g.animate.move_to(g.vertices['f']), Write(af))
        self.wait(0.5)
        self.play(bknight1g.animate.move_to(g.vertices['b']), af.animate.to_edge(UL), Write(gb), Unwrite(t4))
        self.wait(0.5)
        self.play(bknight2g.animate.move_to(g.vertices['d']), gb.animate.next_to(af, DOWN), Write(id))
        self.wait(0.5)
        self.play(wknight2g.animate.move_to(g.vertices['h']), id.animate.next_to(gb, DOWN), Write(ch))
        self.wait(0.5)
        #
        # # 2ND
        self.play(wknight1g.animate.move_to(g.vertices['g']), ch.animate.next_to(id, DOWN), Write(fg))
        self.wait(0.5)
        self.play(bknight1g.animate.move_to(g.vertices['i']), fg.animate.next_to(ch, DOWN), Write(bi))
        self.wait(0.5)
        self.play(bknight2g.animate.move_to(g.vertices['c']), bi.animate.next_to(fg, DOWN), Write(dc))
        self.wait(0.5)
        self.play(wknight2g.animate.move_to(g.vertices['a']), dc.animate.next_to(bi, DOWN), Write(ha))
        self.wait(0.5)

        # 3RD
        self.play(wknight1g.animate.move_to(g.vertices['b']), ha.animate.next_to(dc, DOWN), Write(gb2))
        self.wait(0.5)
        self.play(bknight1g.animate.move_to(g.vertices['d']), gb2.animate.next_to(ha, DOWN), Write(id2))
        self.wait(0.5)
        self.play(bknight2g.animate.move_to(g.vertices['h']), id2.animate.next_to(gb2, DOWN), Write(ch2))
        self.wait(0.5)
        self.play(wknight2g.animate.move_to(g.vertices['f']), ch2.animate.next_to(id2, DOWN), Write(af2))
        self.wait(0.5)

        # 4TH
        self.play(wknight1g.animate.move_to(g.vertices['i']), af2.animate.next_to(ch2, DOWN), Write(bi2))
        self.wait(0.5)
        self.play(bknight1g.animate.move_to(g.vertices['c']), bi2.animate.next_to(af2, DOWN), Write(dc2))
        self.wait(0.5)
        self.play(bknight2g.animate.move_to(g.vertices['a']), dc2.animate.next_to(bi2, DOWN), Write(ha2))
        self.wait(0.5)
        self.play(wknight2g.animate.move_to(g.vertices['g']), ha2.animate.next_to(dc2, DOWN), Write(fg2))
        self.wait(0.5)
        self.play(fg2.animate.next_to(ha2, DOWN))

        self.wait()
        self.play(FadeOut(g, wknight2g, wknight1g, bknight1g, bknight2g))

        # Table solution
        wknight1t.clear_updaters(), wknight2t.clear_updaters(), bknight1t.clear_updaters(), bknight2t.clear_updaters()
        table.center()
        move_sq = Rectangle(RED, 0.5, 1).move_to(af)

        wknight1t.move_to(table.get_cell(cell_loc['a']))
        wknight2t.move_to(table.get_cell(cell_loc['c']))
        bknight1t.move_to(table.get_cell(cell_loc['g']))
        bknight2t.move_to(table.get_cell(cell_loc['i']))

        self.play(FadeIn(table, wknight1t, wknight2t, bknight1t, bknight2t, move_sq))
        self.wait()
        self.play(wknight1t.animate.move_to(table.get_cell(cell_loc['f'])))
        self.wait(0.5)
        self.play(bknight1t.animate.move_to(table.get_cell(cell_loc['b'])), move_sq.animate.move_to(gb))
        self.wait(0.5)
        self.play(bknight2t.animate.move_to(table.get_cell(cell_loc['d'])), move_sq.animate.move_to(id))
        self.wait(0.5)
        self.play(wknight2t.animate.move_to(table.get_cell(cell_loc['h'])), move_sq.animate.move_to(ch))
        self.wait(0.5)
        self.play(wknight1t.animate.move_to(table.get_cell(cell_loc['g'])), move_sq.animate.move_to(fg))
        self.wait(0.5)
        self.play(bknight1t.animate.move_to(table.get_cell(cell_loc['i'])), move_sq.animate.move_to(bi))
        self.wait(0.5)
        self.play(bknight2t.animate.move_to(table.get_cell(cell_loc['c'])), move_sq.animate.move_to(dc))
        self.wait(0.5)
        self.play(wknight2t.animate.move_to(table.get_cell(cell_loc['a'])), move_sq.animate.move_to(ha))
        self.wait(0.5)
        self.play(wknight1t.animate.move_to(table.get_cell(cell_loc['b'])), move_sq.animate.move_to(gb2))
        self.wait(0.5)
        self.play(bknight1t.animate.move_to(table.get_cell(cell_loc['d'])), move_sq.animate.move_to(id2))
        self.wait(0.5)
        self.play(bknight2t.animate.move_to(table.get_cell(cell_loc['h'])), move_sq.animate.move_to(ch2))
        self.wait(0.5)
        self.play(wknight2t.animate.move_to(table.get_cell(cell_loc['f'])), move_sq.animate.move_to(af2))
        self.wait(0.5)
        self.play(wknight1t.animate.move_to(table.get_cell(cell_loc['i'])), move_sq.animate.move_to(bi2))
        self.wait(0.5)
        self.play(bknight1t.animate.move_to(table.get_cell(cell_loc['c'])), move_sq.animate.move_to(dc2))
        self.wait(0.5)
        self.play(bknight2t.animate.move_to(table.get_cell(cell_loc['a'])), move_sq.animate.move_to(ha2))
        self.wait(0.5)
        self.play(wknight2t.animate.move_to(table.get_cell(cell_loc['g'])), move_sq.animate.move_to(fg2))
        self.wait(0.5)
        self.play(Flash(g, flash_radius=3, num_lines=20), FadeOut(*moves, move_sq))
        self.wait()
        src = Tex(r"""Reference:\\Iranpoor, M. (2021). \textit{Knights Exchange Puzzle—Teaching the Efficiency of Modeling.}
                  INFORMS Transactions on Education, 21(2), 108-114.""").scale(.3).to_edge(DOWN)

        self.play(Write(qr), FadeIn(src), FadeOut(wknight1t, wknight2t, bknight1t, bknight2t, table))
        self.wait()


class TitleCard(Scene):
    def construct(self):
        self.camera.background_color = DARK_GRAY
        text = Tex(r"Solving the knight swap puzzle", color=GREEN)
        self.play(Write(text))
        self.wait(3)
        self.play(Unwrite(text))


class Objective(Scene):
    def construct(self):
        self.camera.background_color = DARK_GRAY
        text = Tex("Objective:\\\\ Switch white and black knights on the\\\\ board in a minimum number of moves")

        self.play(Write(text))
        self.wait(3)
        self.play(Unwrite(text))
