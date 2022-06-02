# EMRSIM22 presentation
# Lucas Perrin - INRIA Paris - LJLL
# lucas.perrin@inria.fr / lucas.perrin@dauphine.eu
# June 2022
#
# ==============================
# /!\ abstract is at the end /!\
# ==============================
#
# This presentation was done using Manim :
# The Manim Community Developers. (2022). Manim – Mathematical Animation Framework (Version v0.15.2) [Computer software]. https://www.manim.community/
#
#
# personal notes for the repository and command lines to execute :
#
# cd Documents/presentations/emrsim
# manim -pql perrin_emrsim.py
# manim --save_sections perrin_emrsim.py
# manedit
#
# python3 -m http.server

from manim import *
from manim_editor import PresentationSectionType

# =======================
# GENERAL COLOR MANAGMENT
# =======================

# 1 for white background and black text
# 0 for the usual manim style
black_and_white = 1

# plot a grid to have some coordinates to place easily MObjects
grid            = 0

if black_and_white == 1:
    FRONT_COLOR = BLACK
    BACK_COLOR = "#f6f3f1" # WHITE
    RED = "#ff0000"
    BLUE = "#0000ff"
    GREEN = "#2fa222"
    DEMARK_COLOR = '#FF00FF'
    BROWN = '#f56e0f'
    config.background_color = BACK_COLOR
else:
    FRONT_COLOR = WHITE
    BACK_COLOR = BLACK
    DEMARK_COLOR = YELLOW
    BROWN = '#e17223'

OBS_COLOR = RED
STATE_COLOR = BLUE

# ==============================================
# INTRODUCTION SCENE
# Names, Lab, etc...
# ==============================================

class A_Intro(Scene):
    def construct(self):

        # ===============
        # COLOR MANAGMENT
        # ===============

        Tex.set_default(color = FRONT_COLOR,font_size = 30)
        MathTex.set_default(color = FRONT_COLOR,font_size = 30)
        Mobject.set_default(color = FRONT_COLOR)

        # ===============
        # GRID FOR CONSTRUCTION PURPUSE ONLY
        # ===============

        L1 = Line(start=[- 7.1, 0., 0.], end=[7.1, 0., 0.],stroke_opacity =0.2)
        for i in range(-3,4):
            L1 = VGroup(L1,Line(start=[- 7.1, i, 0.], end=[7.1, i, 0.],stroke_opacity =0.1))

        L2 = Line(start=[0., -4., 0.], end=[0., 4., 0.],stroke_opacity =0.2)
        for i in range(-6,7):
            L2 = VGroup(L2,Line(start=[i, -4., 0.], end=[i, 4., 0.],stroke_opacity =0.1))

        if grid == 1 :
            self.add(L1,L2)

        # ===============
        # TITLE
        # ===============

        pres_title = Tex("Time parallelisation and data assimilation",font_size=48)
        pres_subtitle = Tex("Paraexp and Luenberger observer",font_size=30)
        author_1_tex = Tex("Lucas Perrin",font_size=30)
        author_1_ul = Underline(author_1_tex,buff=0.1)
        author_1 = VGroup(author_1_tex,author_1_ul)
        author_2 = Tex("Julien Salomon",font_size=30)
        team = Tex("Inria Paris, ANGE Team", font_size=25)
        date = Tex("30 Mai 2022",font_size=25)

        logo_emrsim = ImageMobject("logos/emrsim_logo.png").scale(0.8).move_to([0,3.1,0])

        title_intro = VGroup(pres_title,pres_subtitle).arrange(DOWN).move_to([0,1.5,0])
        infos = VGroup(author_1,author_2,team,date).arrange(DOWN,buff=0.3).move_to([0,-0.5,0])

        logo_cnrs = ImageMobject("logos/logo_cnrs.png").scale(0.15)
        logo_su   = ImageMobject("logos/logo_su.png").scale(0.4)
        if black_and_white == 1:
            logo_inr = ImageMobject("logos/inr_logo_grisbleu.png").scale(0.4)
        else:
            logo_inr = ImageMobject("logos/inr_logo_blanc.png").scale(0.4)

        logo_cnrs.move_to([-3,-2.8,0])
        logo_su.move_to([0,-2.8,0])
        logo_inr.move_to([3,-2.8,0])

        logos = Group(logo_cnrs,logo_inr,logo_su)

        ## ANIM

        ## == SLIDE ==
        self.next_section('INTRO',PresentationSectionType.NORMAL)
        self.play(
            Write(title_intro),
            FadeIn(logo_emrsim),
        )
        self.wait(0.5)
        self.play(
            FadeIn(logos),
            FadeIn(infos),
        )
        self.wait(0.5)
        self.next_section('INTRO.1',PresentationSectionType.SUB_SKIP)
        self.play(
            FadeOut(infos),
            FadeOut(logos),
            FadeOut(logo_emrsim),
            FadeOut(pres_subtitle),
        )
        self.wait(1)

# ==============================================
# SUMMARY SCENE
# Explain what will be talked about
# ==============================================

class B_Summary(Scene):
    def construct(self):

        # ===============
        # COLOR MANAGMENT
        # ===============

        Tex.set_default(color = FRONT_COLOR,font_size = 30)
        MathTex.set_default(color = FRONT_COLOR,font_size = 30)
        Mobject.set_default(color = FRONT_COLOR)

        # ===============
        # GRID FOR CONSTRUCTION PURPUSE ONLY
        # ===============

        L1 = Line(start=[- 7.1, 0., 0.], end=[7.1, 0., 0.],stroke_opacity =0.2)
        for i in range(-3,4):
            L1 = VGroup(L1,Line(start=[- 7.1, i, 0.], end=[7.1, i, 0.],stroke_opacity =0.1))

        L2 = Line(start=[0., -4., 0.], end=[0., 4., 0.],stroke_opacity =0.2)
        for i in range(-6,7):
            L2 = VGroup(L2,Line(start=[i, -4., 0.], end=[i, 4., 0.],stroke_opacity =0.1))

        if grid == 1 :
            self.add(L1,L2)

        # ===============
        # REPEAT
        # ===============

        pres_title = Tex("Time parallelisation and data assimilation",font_size=48)
        pres_subtitle = Tex("Paraexp and Luenberger observer",font_size=30)
        title_intro = VGroup(pres_title,pres_subtitle).arrange(DOWN).move_to([0,1.5,0])
        self.add(pres_title)

        step_one   = Tex(r"$\rightarrow$"," Present a sequential data assimilation : the Luenberger observer").shift(UP)
        step_two   = Tex(r"$\rightarrow$"," Explain the parallel in time scheme used : Paraexp").align_to(step_one,LEFT)
        step_three = Tex(r"$\rightarrow$"," Expose our PinT method for sequential data assimilation").align_to(step_two,LEFT).shift(DOWN)
        steps      = VGroup(step_one,step_two,step_three).scale(1.2).shift(0.5*DOWN)

        ## ANIM

        ## == SLIDE == (AUTO)
        self.next_section('SUMMARY',PresentationSectionType.SKIP)
        self.play(pres_title.animate.to_edge(UP).scale(40/48))
        underline = Line(6*LEFT, 6*RIGHT,color=FRONT_COLOR).next_to(pres_title, DOWN, buff=MED_SMALL_BUFF)
        self.play(Create(underline))
        self.wait(2)

        ## == SLIDE ==
        self.next_section('SUMMARY.1',PresentationSectionType.SUB_NORMAL)
        self.play(Write(step_one))
        self.wait(1)
        self.play(Write(step_two))
        self.wait(1)
        self.play(Write(step_three))
        self.wait(2)

        ## == SLIDE ==
        self.next_section('SUMMARY.2',PresentationSectionType.SUB_SKIP)
        self.play(Unwrite(VGroup(underline,pres_title)),Unwrite(step_one),Unwrite(step_two),Unwrite(step_three,))
        self.wait(1)

# ==============================================
# ASSIMILATION SCENE
# Present the Luenberger observer
# ==============================================

class C_Assimilation(Scene):
    def construct(self):

        # ===============
        # COLOR MANAGMENT
        # ===============

        Tex.set_default(color = FRONT_COLOR,font_size = 30)
        MathTex.set_default(color = FRONT_COLOR,font_size = 30)
        Mobject.set_default(color = FRONT_COLOR)

        # ===============
        # GRID FOR CONSTRUCTION PURPUSE ONLY
        # ===============

        L1 = Line(start=[- 7.1, 0., 0.], end=[7.1, 0., 0.],stroke_opacity =0.2)
        for i in range(-3,4):
            L1 = VGroup(L1,Line(start=[- 7.1, i, 0.], end=[7.1, i, 0.],stroke_opacity =0.1))

        L2 = Line(start=[0., -4., 0.], end=[0., 4., 0.],stroke_opacity =0.2)
        for i in range(-6,7):
            L2 = VGroup(L2,Line(start=[i, -4., 0.], end=[i, 4., 0.],stroke_opacity =0.1))

        if grid == 1 :
            self.add(L1,L2)

        # ===============
        # TITLE
        # ===============

        title = Title("Data assimilation : Luenberger observer \& dynamical systems",font_size=40)

        # ===============
        # STATE SYSTEM
        # ===============

        state_tt    = Tex("state dynamical system : ",font_size = 30).move_to([-3.5,2.3,0])

        state_eq_1  = MathTex("\dot{x}","=A","x(t)"," + B u(t)",font_size = 30)
        state_eq_1.set_color_by_tex('x', STATE_COLOR)

        state_eq_2  = MathTex("y(t) = C","x(t)",font_size = 30)
        state_eq_2.set_color_by_tex('x', STATE_COLOR).align_to(state_eq_1,LEFT).shift(0.5*DOWN)

        state_eq_3  = MathTex("x(0)","=","x_{0}",", \quad t \geq 0",font_size = 30)
        state_eq_3.set_color_by_tex('x', STATE_COLOR).align_to(state_eq_1,LEFT).shift(DOWN)

        state_eq    = VGroup(VGroup(state_eq_1,state_eq_2,state_eq_3)).move_to([-3.5,1.25,0])
        brace1      = Brace(state_eq,LEFT)

        state_blist = VGroup(
            Tex(r"$\rightarrow$ ",r"$x(t)$",r" : \textit{state}",r" vector").set_color_by_tex('x', STATE_COLOR),
            Tex(r"$\rightarrow$ ",r"$y(t)$ : \textit{output} vector"),
            Tex(r"$\rightarrow$ ",r"$A \in \mathcal{M}_{m \times m}(\mathbb{R})$,\\     $B \in \mathcal{M}_{m \times p}(\mathbb{R})$,\\    $C \in \mathcal{M}_{q \times m}(\mathbb{R})$"),
            Tex(r"$\rightarrow$ ",r"$x_0$",r" is ",r"unknown").set_color_by_tex('x', STATE_COLOR).set_color_by_tex('unk', DEMARK_COLOR),
        ).arrange_in_grid(cols=1,col_alignments="l",buff=0.1).move_to([-3.5,-1,0])

        # ===============
        # OBSERVER SYSTEM
        # ===============

        observer_tt = Tex("observer system : ",font_size = 30).move_to([3.5,2.3,0])

        L_tex = MathTex(r"L",font_size = 30)

        obs_eq_1  = MathTex("\dot{\hat{x}}(t)","=A","\hat{x}(t)","+B u(t)+L[y(t)-\hat{y}(t)]",font_size = 30)
        obs_eq_1.set_color_by_tex('x', OBS_COLOR)

        obs_eq_1  = VGroup(
        MathTex("\dot{\hat{x}}(t)","=A","\hat{x}(t)","+B u(t)+").set_color_by_tex('x', OBS_COLOR),
        L_tex,
        MathTex("[y(t)-\hat{y}(t)]"),
        ).arrange(buff=0.05)


        obs_eq_2  = MathTex("\hat{y}(t)=C","\hat{x}(t)",font_size = 30)
        obs_eq_2.set_color_by_tex('x', OBS_COLOR).align_to(obs_eq_1,LEFT).shift(0.5*DOWN)

        obs_eq_3  = MathTex("\hat{x}(0)","=","\hat{x}_{0}",", \quad t \geq 0",font_size = 30)
        obs_eq_3.set_color_by_tex('x', OBS_COLOR).align_to(obs_eq_1,LEFT).shift(DOWN)

        obs_eq    = VGroup(VGroup(obs_eq_1,obs_eq_2,obs_eq_3)).move_to([3.5,1.25,0])
        brace2    = Brace(obs_eq,LEFT)

        obs_blist = VGroup(
            Tex(r"$\rightarrow$ ",r"$\hat{x}(t)$",r" : \textit{observer}",r" vector").set_color_by_tex('x', OBS_COLOR),
            Tex(r"$\rightarrow$ ",r"$L \in \mathcal{M}_{m \times q}(\mathbb{R})$"),
            Tex(r"$\rightarrow$ ",r"$\hat{x}_0$",r" chosen as we want").set_color_by_tex('x', OBS_COLOR),
        ).arrange_in_grid(cols=1,col_alignments="l",buff=0.1).move_to([3.5,-1,0])

        # ===============
        # ERROR EQUATION
        # ===============

        error_1 = MathTex("\dot{x}(t)","-","\dot{\hat{x}}","(t)","=","(A-LC)","(","x(","t",")","-\hat{x}","(","t",")",")",
            font_size = 35,
        ).move_to([0,-2.6,0])

        error_2 = MathTex("x(t)","-","\hat{x}","(t)","=","\mathrm{e}^{","(A-LC)","t}","(","x(","0",")","-\hat{x}","(","0",")",")",
            font_size = 35,
        ).move_to([0,-2.6,0])

        error_3 = MathTex("\epsilon(t)","=","\mathrm{e}^{","(A-LC)","t}","(","x(","0",")","-\hat{x}","(","0",")",")",
            font_size = 35,
        ).move_to([0,-2.6,0])

        error_3_i = MathTex("\epsilon(t)","=","\mathrm{e}^{","(A-LC)","t}","(","x","(0)","-\hat{x}","(0)",")",
            font_size = 35,
        ).move_to([0,-2.6,0])

        error_4 = MathTex("\lVert","\epsilon(t)","\lVert","=","\lVert","\mathrm{e}^{","(A-LC)","t}","\epsilon","(0)","\lVert",
            font_size = 35,
        ).move_to([0,-2.6,0])

        error_5 = MathTex("\lVert","\epsilon(t)","\lVert",
            "=","\lVert","\mathrm{e}^{","(A-LC)","t}","\epsilon","(0)","\lVert",
            "\leq","\lVert x(0)-\hat{x}(0) \lVert \cdot \kappa(X) \cdot \mathrm{e}^{-\mu t}",
            font_size = 30,
        ).move_to([0,-2.6,0]).set_color_by_tex("x",DEMARK_COLOR)

        explain_error_5 = VGroup(
            Tex(r"$\rightarrow$ ",r"$\mu = \min\{|\Lambda|\}$"),
            Tex(r"$\rightarrow$ ",r"$X =$ e.v. of $A-LC$"),
        ).arrange_in_grid(cols=1,col_alignments="l").move_to([5.2,-2.8,0])

        box_error = SurroundingRectangle(error_2, color = DEMARK_COLOR, buff = 0.2, corner_radius = 0.2)

        ## ANIM

        ## == SLIDE == (SKIP)
        self.next_section('ASSIMILATION_1',PresentationSectionType.NORMAL)
        self.play(Write(title))
        self.wait(2)
        ## == SLIDE ==
        self.next_section('ASSIMILATION_1.1',PresentationSectionType.SUB_NORMAL)
        self.play(Write(state_tt),Write(state_eq),Create(brace1))
        self.play(Write(state_blist))
        self.wait(2)
        ## == SLIDE ==
        self.next_section('ASSIMILATION_1.2',PresentationSectionType.SUB_NORMAL)
        self.play(Write(observer_tt),Write(obs_eq),Create(brace2))
        self.play(Write(obs_blist))
        self.wait(2)
        ## == SLIDE ==
        self.next_section('ASSIMILATION_1.3',PresentationSectionType.SUB_NORMAL)
        self.play(Write(error_1))
        self.wait(2)
        ## == SLIDE ==
        self.next_section('ASSIMILATION_1.4',PresentationSectionType.SUB_NORMAL)
        self.play(TransformMatchingTex(error_1,error_2))
        self.play(TransformMatchingTex(error_2,error_3))
        self.play(ShowPassingFlash(box_error, run_time = 2, time_width = 1))
        self.wait(2)
        ## == SLIDE ==
        self.next_section('ASSIMILATION_1.5',PresentationSectionType.SUB_SKIP)
        self.play(Unwrite(obs_blist),Unwrite(state_blist))
        self.wait(2)

        # ===============
        # CHOICE OF L AND ERROR
        # ===============

        L_tex2 = L_tex.copy()
        sub_question = [Tex("How do we choose "),Tex(" ?")]

        question = VGroup(
            sub_question[0],L_tex2,sub_question[1],
        ).arrange(buff=0.1).align_to(brace1,LEFT).scale(35/30).shift([-0.5,-0,0])
        underline_question = Line(question.get_left(),question.get_right(),buff=0).next_to(question,DOWN,buff=SMALL_BUFF)

        st_tex     = Tex("so that :  ").align_to([-6,0,0],LEFT).shift(1*DOWN)
        objectif   = MathTex("\hat{x}(t)","\longrightarrow","x(t)").align_to(st_tex.get_right(),LEFT).shift(1*DOWN+0.1*RIGHT).set_color_by_tex("hat",OBS_COLOR).set_color_by_tex("x(",STATE_COLOR)
        objectif_2 = MathTex("\lVert\epsilon(t)\lVert","\longrightarrow","0").align_to(objectif,LEFT).shift((1+0.4)*DOWN)
        objectif_3 = MathTex("\mathfrak{Re}(\Lambda = \sigma","(A-LC)",")","< 0").align_to(objectif_2,LEFT).shift((1+0.8)*DOWN)

        footnote1 = VGroup(
            Tex("[1] Kautsky, Nichols, Van Dooren. ",font_size=20),
            Tex("'Robust pole assignment in linear state feedback.' (1985)",font_size=20)
        ).arrange(RIGHT, buff= 0.05).to_corner(DL)#.shift(0.35*DOWN)

        footnote2 = VGroup(
            Tex("[2] Haine, Ramdani, 'Observateurs itératifs. ",font_size=20),
            Tex("en horizon fini. Application à la reconstruction",font_size=20),
            Tex(" de données initiales pour des EDP d'évolution.' (2011)",font_size=20)
        ).arrange(RIGHT, buff= 0.05).to_corner(DL).shift(0.35*DOWN)

        p1   = np.array([-1.5,-1,0])
        p2   = np.array([0,-1,0])
        p3_1 = np.array([0,-0.25,0])
        p3_2 = np.array([0,-1.75,0])
        l_ar = np.array([1.5,0,0])

        arrow_1  = VGroup(
            Line(p1,p2),
            Line(p2,p3_1),
            Arrow(p3_1,p3_1+l_ar,buff=0,stroke_width=3,max_tip_length_to_length_ratio=0.1)
        )
        arrow_2  = VGroup(
            Line(p2,p3_2),
            Arrow(p3_2,p3_2+l_ar,buff=0,stroke_width=3,max_tip_length_to_length_ratio=0.1)
        )

        L_place   = Tex(r"ODE : $L=\texttt{place(}\Lambda,A,C\texttt{)}$").align_to(arrow_1.get_right(),LEFT).match_y(Dot(p3_1)).shift(0.1*RIGHT)
        L_place_2 = Tex(r"'pole placement procedure'",font_size=27).move_to(L_place.get_center()).shift(0.4*DOWN)
        L_edp     = Tex(r"dsicretized PDE : $L = \gamma C^T$  ($\gamma \in \mathbb{R}$)").align_to(arrow_1.get_right(),LEFT).match_y(Dot(p3_2)).shift(0.1*RIGHT)

        ## ANIM

        ## == SLIDE ==
        self.next_section('ASSIMILATION_2',PresentationSectionType.NORMAL)
        self.play(FocusOn(L_tex))
        self.play(ReplacementTransform(L_tex.copy(),L_tex2))
        self.play(Write(VGroup(sub_question[0],sub_question[1],underline_question)))
        self.wait(2)
        ## == SLIDE ==
        self.next_section('ASSIMILATION_2.1',PresentationSectionType.SUB_NORMAL)
        self.play(Write(VGroup(st_tex,objectif)))
        self.play(Write(objectif_2))
        self.wait(2)
        self.play(Write(objectif_3))
        self.wait(2)
        ## == SLIDE ==
        self.next_section('ASSIMILATION_2.2',PresentationSectionType.SUB_NORMAL)
        self.play(Create(arrow_1))
        self.play(Write(L_place),Write(L_place_2))
        self.play(Write(footnote1))
        self.wait(2)
        ## == SLIDE ==
        self.next_section('ASSIMILATION_2.3',PresentationSectionType.SUB_NORMAL)
        self.play(Create(arrow_2))
        self.play(Write(L_edp))
        self.play(Write(footnote2))
        self.wait(2)
        ## == SLIDE ==
        self.next_section('ASSIMILATION_2.4',PresentationSectionType.SUB_NORMAL)
        self.play(TransformMatchingTex(error_3,error_4))
        self.wait()
        self.play(TransformMatchingTex(error_4,error_5))
        self.play(Write(explain_error_5))
        self.wait(2)

        ## == SLIDE == (CLEANING)
        self.next_section('ASSIMILATION_2.5',PresentationSectionType.SUB_SKIP)
        self.play(FadeOut(VGroup(
            L_edp,L_place,L_place_2,
            arrow_1,arrow_2,
            objectif,objectif_2,objectif_3,
            st_tex,
            sub_question[0],sub_question[1],underline_question,
            L_tex2, error_5,
            footnote1,footnote2,
            explain_error_5,
        )))
        self.play(VGroup(state_eq,brace1).animate.shift(4.25*DOWN),VGroup(obs_eq,brace2).animate.shift(4.25*DOWN))

        # ===============
        # WAVE EXAPLE
        # ===============

        mu = 1

        # ===============
        # STATE & OBSERVER GRAPH
        # ===============


        dict_values = {3.1416 : Tex(r"$\pi$"), 6.2832 : Tex(r"$2\pi$"), 9.4248 : Tex(r"$3\pi$")}

        axes_state = Axes(x_range = [-0.1,3*PI,PI], y_range = [-2.1,2.1,2],
        x_length = 4, y_length = 4,
        tips = False,
        y_axis_config = {"include_numbers": True, "font_size": 25, "exclude_origin_tick" : False},
        x_axis_config = {"include_numbers": False, "font_size": 30, "exclude_origin_tick" : True},
        )#.add_coordinates()

        axes_state.get_axes()[0].add_labels(dict_values),

        axes_obs = axes_state.copy()
        axes_state.shift([-3.5,0,0])
        axes_obs.shift([3.5,0,0])

        x_lab_state = axes_state.get_x_axis_label("x").scale(1).shift(0.2*LEFT)
        y_lab_state = axes_state.get_y_axis_label("x(t)", edge=LEFT, direction=LEFT, buff=0.2).scale(1).shift(0.2*RIGHT)
        y_lab_state.set_color(STATE_COLOR)
        lab_state = VGroup(x_lab_state, y_lab_state)

        x_lab_obs = axes_obs.get_x_axis_label("x").scale(1).shift(0.2*LEFT)
        y_lab_obs = axes_obs.get_y_axis_label("\hat{x}(t)", edge=LEFT, direction=LEFT, buff=0.2).scale(1).shift(0.2*RIGHT)
        y_lab_obs.set_color(OBS_COLOR)
        lab_obs = VGroup(x_lab_obs, y_lab_obs)

        t = ValueTracker(0)

        def g_func(x,time): return(np.sin(x)*np.cos(time))
        def f_func(x,time): return((1/30)*(3*PI-x)*x*np.cos(3*time-1))
        def state_func(x,time): return(g_func(x,time) + f_func(x,time))

        def obs_func(x,time): return(state_func(x,time) + np.exp(-time*mu)*(- state_func(x,time) + (1/20)*(3*PI-x)*x))

        graph_state = always_redraw( lambda:
            axes_state.plot(lambda x: state_func(x,t.get_value()),
                color = BLUE, x_range=[0, 3*PI],
            )
        )

        graph_obs = always_redraw( lambda:
            axes_obs.plot(lambda x: obs_func(x,t.get_value()),
                color = RED, x_range=[0, 3*PI],
            )
        )

        ## ANIM

        ## == SLIDE ==
        self.next_section('ASSIMILATION_3',PresentationSectionType.NORMAL)
        self.play(
            DrawBorderThenFill(axes_state), Write(lab_state),
            DrawBorderThenFill(axes_obs), Write(lab_obs),
        )
        self.play(Create(graph_state),Create(graph_obs))
        self.wait(2)
        ## == SLIDE ==
        self.next_section('ASSIMILATION_3.1',PresentationSectionType.SUB_NORMAL)
        self.play(t.animate.set_value(6*PI),run_time=10,rate_func=linear)
        self.wait(2)

        ## == SLIDE == (CLEANING)
        self.next_section('ASSIMILATION_3.2',PresentationSectionType.SUB_NORMAL)
        self.play(
            Unwrite(state_eq),Uncreate(brace1),
            Unwrite(obs_eq),Uncreate(brace2),
        )
        self.play(
            state_tt.animate.move_to([-5,2,0]),
            observer_tt.animate.move_to([-5,-1,0]),
            VGroup(axes_state,lab_state).animate.scale(0.5).move_to([-5,0.5,0]),
            VGroup(axes_obs,lab_obs).animate.scale(0.5).move_to([-5,-2.5,0]),
        )
        self.play(t.animate.set_value(0))

        # ===============
        # ERROR GRAPH
        # ===============

        axes_error = Axes(x_range = [-0.1,6*PI,3], y_range = [-7,2,2],
        x_length = 6, y_length = 4,
        tips = False,
        axis_config={"include_numbers": True, "font_size": 25},
        y_axis_config={"scaling": LogBase(custom_labels=True)},
        ).add_coordinates()

        axes_error.move_to([1.8,0,0])

        x_lab_error = axes_error.get_x_axis_label("t").scale(0.8)
        y_lab_error = axes_error.get_y_axis_label("\lVert \epsilon(t) \lVert=\lVert x(t) - \hat{x}(t) \lVert", buff=0.05).scale(0.8)
        lab_error = VGroup(x_lab_error, y_lab_error)

        xspace = np.linspace(0,3*PI,1000)

        graph_error = axes_error.plot(lambda x: np.abs(2*np.exp(-x*mu)*np.cos(x)),
            x_range = [0,6*PI],
        )
        graph_error = axes_error.plot(lambda t: np.linalg.norm(obs_func(xspace,t) - state_func(xspace,t)),
            x_range = [0,6*PI],
        )
        graph_th_error = axes_error.plot(lambda t: 3*np.exp(-t*mu)*np.linalg.norm(obs_func(xspace,0) - state_func(xspace,0)),
            color = DEMARK_COLOR,
            x_range = [0,3*PI],
        )

        error_lab_graph = MathTex("C \mathrm{e}^{-\mu t}",color = DEMARK_COLOR,font_size = 28).move_to([2,1.3,0])

        ## ANIM

        self.play(DrawBorderThenFill(axes_error), Write(lab_error), Write(error_5.shift(2*RIGHT + 0.4*DOWN)))
        self.wait(2)
        ## == SLIDE ==
        self.next_section('ASSIMILATION_3.3',PresentationSectionType.SUB_NORMAL)
        self.play(t.animate.set_value(6*PI),
            Create(graph_error),
            run_time=10,rate_func=linear,
        )
        self.wait(2)
        ## == SLIDE ==
        self.next_section('ASSIMILATION_3.4',PresentationSectionType.SUB_NORMAL)
        self.play(Create(graph_th_error),Write(error_lab_graph))
        self.wait(2)

        ## == SLIDE == (CLEANING)
        self.next_section('ASSIMILATION_3.5',PresentationSectionType.SUB_SKIP)
        self.play(
            Unwrite(error_5),
            Unwrite(error_lab_graph),
            Uncreate(graph_th_error),
            Uncreate(graph_error),
            FadeOut(axes_error),FadeOut(lab_error),
            Uncreate(graph_state),
            FadeOut(axes_state),FadeOut(lab_state),
            Uncreate(graph_obs),
            FadeOut(axes_obs),FadeOut(lab_obs),
            Unwrite(state_tt),
            Unwrite(observer_tt),
            Unwrite(title)
        )
        self.wait(1)

# ==============================================
# PARALLEL SCENE
# Present the PinT algorithm : Paraexp
# ==============================================

class D_Parallel(Scene):
    def construct(self):

        # ===============
        # COLOR MANAGMENT
        # ===============

        Tex.set_default(color = FRONT_COLOR,font_size = 30)
        MathTex.set_default(color = FRONT_COLOR,font_size = 30)
        Mobject.set_default(color = FRONT_COLOR)

        # ===============
        # GRID FOR CONSTRUCTION PURPUSE ONLY
        # ===============

        L1 = Line(start=[- 7.1, 0., 0.], end=[7.1, 0., 0.],stroke_opacity =0.2)
        for i in range(-3,4):
            L1 = VGroup(L1,Line(start=[- 7.1, i, 0.], end=[7.1, i, 0.],stroke_opacity =0.1))

        L2 = Line(start=[0., -4., 0.], end=[0., 4., 0.],stroke_opacity =0.2)
        for i in range(-6,7):
            L2 = VGroup(L2,Line(start=[i, -4., 0.], end=[i, 4., 0.],stroke_opacity =0.1))

        if grid == 1 :
            self.add(L1,L2)

        # ===============
        # TITLE
        # ===============

        title = Title("Time parallelization : the Paraexp algorithm",font_size=40)

        # ===============
        # PARAEXP
        # ===============

        system_1  = MathTex("\dot{x}(t) = M x(t) + g(t), \quad t \in[0, T]")
        system_2  = MathTex("x(0) = x_{0}").align_to(system_1,LEFT).shift(0.5*DOWN)
        brace_sys = Brace(VGroup(system_1,system_2),LEFT)
        system    = VGroup(brace_sys,system_1,system_2)

        setting_sub = [Tex(r"$\rightarrow M \in \mathcal{M}_{m \times m} (\mathbb{C})$"),Tex(r"$\rightarrow x(t), g(t) \in \mathbb{C}^m$")]
        setting_sub[1].align_to(setting_sub[0],LEFT).shift(0.5*DOWN)
        setting = VGroup(setting_sub[0],setting_sub[1]).move_to([5,2,0])

        w_tex_2 = MathTex("w(t)",color = GREEN)
        v_tex_2 = MathTex("v(t)",color = BROWN)

        hom_system_1_sub = MathTex("\dot{w}(t)"," = M ").set_color_by_tex("w",GREEN)
        hom_system_1 = VGroup(hom_system_1_sub,w_tex_2).arrange(buff=0.05)
        hom_system_2 = MathTex("w(0)"," = x_{0}").set_color_by_tex("w",GREEN).align_to(hom_system_1,LEFT).shift(0.5*DOWN)
        brace_hom    = Brace(VGroup(hom_system_1,hom_system_2),LEFT)
        hom_system   = VGroup(brace_hom,hom_system_1,hom_system_2)

        inhom_system_1_sub = [MathTex("\dot{v}(t)"," = M ").set_color_by_tex("v",BROWN),MathTex(" + g(t)")]
        inhom_system_1 = VGroup(inhom_system_1_sub[0],v_tex_2,inhom_system_1_sub[1]).arrange(buff=0.05)
        inhom_system_2 = MathTex("v(0)"," = 0").set_color_by_tex("v",BROWN).align_to(inhom_system_1,LEFT).shift(0.5*DOWN)
        brace_inhom    = Brace(VGroup(inhom_system_1,inhom_system_2),LEFT)
        inhom_system   = VGroup(brace_inhom,inhom_system_1,inhom_system_2)

        w_tex = w_tex_2.copy()
        v_tex = v_tex_2.copy()

        eq_1_sub = [MathTex("x(t) = "),MathTex(" + ")]
        eq_1     = VGroup(eq_1_sub[0],v_tex,eq_1_sub[1],w_tex).arrange(buff=0.05).move_to([0,1,0])

        system.move_to([0,2,0])
        hom_system.move_to([2,0,0])
        inhom_system.move_to([-2,0,0])

        inhom_compute = VGroup(
            Tex("Euler", font_size = 25, color = BROWN),
            Tex("Runge-Kutta", font_size = 25, color = BROWN),
        ).arrange(DOWN).move_to([-5.3,0,0])

        arrow_inhom = Arrow(inhom_system,[-4.65,0,0],buff=0.15,stroke_width=3,max_tip_length_to_length_ratio=0.1)

        box_hom_system = SurroundingRectangle(hom_system, color = DEMARK_COLOR, buff = 0.2, corner_radius = 0.2)

        exp_system = MathTex("\Rightarrow","w(t)"," = \mathrm{e}^{(tM)}","w(0)").set_color_by_tex("w(t)",GREEN).set_color_by_tex("w(0)",GREEN).move_to([5,0,0])

        box_exp_system = SurroundingRectangle(exp_system, color = DEMARK_COLOR, buff = 0.2, corner_radius = 0.2)

        exp_compute = VGroup(
            Tex("Rational Krylov", font_size = 25, color = GREEN),
            Tex("Chebyshev polynomials", font_size = 25, color = GREEN)
        ).arrange(DOWN).move_to([5,-1.8,0])

        footnote2 = VGroup(
            Tex("[3] Gander, Güttel.",font_size=20),
            Tex(" 'Paraexp : a parallel integrator for ",font_size=20),
            Tex(" linear initial-value problems.' (2013)",font_size=20),
        ).arrange(RIGHT, buff=0.05).to_corner(DL).shift(0.35*DOWN)

        arrow_exp = Arrow([5,-0.2,0],exp_compute,buff=0.2,stroke_width=3,max_tip_length_to_length_ratio=0.1)

        box_exp_compute = SurroundingRectangle(VGroup(exp_compute,exp_system), color = DEMARK_COLOR, buff = 0.2, corner_radius = 0.2)

        ## ANIM

        ### == SLIDE ==
        self.next_section('PARALLEL_1',PresentationSectionType.SKIP)
        self.play(Write(title))
        self.wait(2)
        ### == SLIDE ==
        self.next_section('PARALLEL_1.1',PresentationSectionType.SUB_NORMAL)
        self.play(Write(VGroup(system_1,system_2)),Create(brace_sys))
        self.play(Write(setting))
        self.wait(2)
        ### == SLIDE ==
        self.next_section('PARALLEL_1.2',PresentationSectionType.SUB_NORMAL)
        self.play(Write(eq_1))
        self.wait(2)
        ### == SLIDE ==
        self.next_section('PARALLEL_1.3',PresentationSectionType.SUB_NORMAL)
        self.play(ReplacementTransform(v_tex.copy(),v_tex_2))
        self.play(ReplacementTransform(w_tex.copy(),w_tex_2))
        self.play(
            Write(VGroup(hom_system_1_sub,hom_system_2)),
            Write(VGroup(inhom_system_1_sub[0],inhom_system_1_sub[1],inhom_system_2)),
            Create(brace_hom),Create(brace_inhom),
        )
        self.wait(2)
        ### == SLIDE ==
        self.next_section('PARALLEL_1.4',PresentationSectionType.SUB_NORMAL)
        self.play(Create(arrow_inhom))
        self.play(Write(inhom_compute))
        self.wait(2)
        ### == SLIDE ==
        self.next_section('PARALLEL_1.5',PresentationSectionType.SUB_NORMAL)
        self.play(Create(box_hom_system))
        self.wait(2)
        ### == SLIDE ==
        self.next_section('PARALLEL_1.6',PresentationSectionType.SUB_NORMAL)
        self.play(Write(exp_system))
        self.wait(1)
        self.play(ReplacementTransform(box_hom_system,box_exp_system))
        self.wait(2)
        ### == SLIDE ==
        self.next_section('PARALLEL_1.7',PresentationSectionType.SUB_NORMAL)
        self.play(Create(arrow_exp))
        self.play(Write(exp_compute),Write(footnote2))
        self.wait(1)
        self.play(ReplacementTransform(box_exp_system,box_exp_compute))
        self.wait(2)


        type_1_tex = Tex("'Type 1'",r" on $[t_{j-1},t_{j}]$").set_color_by_tex("ype",BROWN).move_to([-2,-1,0])
        type_2_tex = Tex("'Type 2'",r" on $[t_{j-1},T]$").set_color_by_tex("ype",GREEN).move_to([2,-1,0])

        dict_values = {1 : Tex(r"$0 = t_0$"), 2 : Tex(r"$t_1$"), 3 : Tex(r"$t_2$"), 4 : Tex(r"$t_3$"), 5 : Tex(r"$t_4 = T$")}
        axes_paraexp = Axes(x_range = [1,5,1], y_range = [0,1,2],
        x_length = 6, y_length = 1,
        tips = False,
        axis_config = {"include_numbers": False, "font_size": 25, "exclude_origin_tick" : True},
        y_axis_config = {"stroke_opacity" : 0}
        ).move_to([0,-2.5,0])

        axes_paraexp.get_axes()[0].add_labels(dict_values),

        graph_type_1 = [axes_paraexp.plot(lambda x: 1/2*(x-1) + 1/9 * np.sin(2*x*PI), x_range=[1, 2], color = BROWN),
            axes_paraexp.plot(lambda x: 1/2*(x-2) + 1/10 * np.sin(3*x*PI), x_range=[2, 3], color = BROWN),
            axes_paraexp.plot(lambda x: 1/2*(x-3) + 1/15 * np.sin(x*PI), x_range=[3, 4], color = BROWN),
            axes_paraexp.plot(lambda x: 1/2*(x-4) + 1/20 * np.sin(4*x*PI), x_range=[4, 5], color = BROWN)]

        graph_type_2 = [axes_paraexp.plot(lambda x: ((x-1)/5)**2 + 3/4, x_range=[1, 5], color = GREEN),
            axes_paraexp.plot(lambda x: ((x-1)/5)**2 + 2/4.35, x_range=[2, 5], color = GREEN),
            axes_paraexp.plot(lambda x: ((x-2)/6)**2 + 2/4.35, x_range=[3, 5], color = GREEN),
            axes_paraexp.plot(lambda x: ((x-4)/7)**2 + 1/2, x_range=[4, 5], color = GREEN)]

        initial_point = VGroup(
            MathTex("x_0").set_color_by_tex("x",GREEN).move_to([-3.3,-2,0]),
            Tex(r"$\times$").set_color_by_tex("times",GREEN).move_to([-3,-2.2,0])
        )

        p_computer_tex = Tex(r"$p = 4$ computers :").move_to([-5.3,-2,0])

        ## ANIM

        ### == SLIDE ==
        self.next_section('PARALLEL_1.8',PresentationSectionType.SUB_NORMAL)
        self.play(Uncreate(box_exp_compute))
        self.wait(0.5)
        self.play(Write(p_computer_tex))
        self.wait(1)
        self.play(DrawBorderThenFill(axes_paraexp))
        self.wait(2)

        ### == SLIDE ==
        self.next_section('PARALLEL_1.9',PresentationSectionType.SUB_NORMAL)
        self.play(Write(type_1_tex))
        self.wait(1)
        self.play(Create(graph_type_1[0]),Create(graph_type_1[1]),Create(graph_type_1[2]),Create(graph_type_1[3]))
        self.wait(2)

        ### == SLIDE ==
        self.next_section('PARALLEL_1.10',PresentationSectionType.SUB_NORMAL)
        self.play(Write(type_2_tex))
        self.wait(1)
        self.play(Write(initial_point),Create(graph_type_2[0]),Create(graph_type_2[1]),Create(graph_type_2[2]),Create(graph_type_2[3]))
        self.wait(2)

        ### == SLIDE == (CLEANING)
        self.next_section('PARALLEL_1.11',PresentationSectionType.SUB_SKIP)
        self.play(
            Unwrite(type_1_tex),Unwrite(type_2_tex),
            Unwrite(initial_point),Uncreate(VGroup(*graph_type_2)),Uncreate(VGroup(*graph_type_1)),
            FadeOut(axes_paraexp),FadeOut(p_computer_tex),
            FadeOut(VGroup(exp_compute,arrow_exp,footnote2,exp_system)),
            FadeOut(VGroup(inhom_compute,arrow_inhom)),
            FadeOut(VGroup(hom_system,inhom_system)),
            Unwrite(VGroup(system_1,system_2)),Unwrite(brace_sys),
            Unwrite(setting),Unwrite(eq_1),
            Unwrite(title),
        )
        self.wait(1)

# ==============================================
# COUPLING SCENE
# Present the strategy used for applying
# PinT to sequential data assimilation procedure
# ==============================================

class E_Coupling(Scene):
    def construct(self):

        # ===============
        # COLOR MANAGMENT
        # ===============

        Tex.set_default(color = FRONT_COLOR,font_size = 30)
        MathTex.set_default(color = FRONT_COLOR,font_size = 30)
        Mobject.set_default(color = FRONT_COLOR)

        # ===============
        # GRID FOR CONSTRUCTION PURPUSE ONLY
        # ===============

        L1 = Line(start=[- 7.1, 0., 0.], end=[7.1, 0., 0.],stroke_opacity =0.2)
        for i in range(-3,4):
            L1 = VGroup(L1,Line(start=[- 7.1, i, 0.], end=[7.1, i, 0.],stroke_opacity =0.1))

        L2 = Line(start=[0., -4., 0.], end=[0., 4., 0.],stroke_opacity =0.2)
        for i in range(-6,7):
            L2 = VGroup(L2,Line(start=[i, -4., 0.], end=[i, 4., 0.],stroke_opacity =0.1))

        if grid == 1 :
            self.add(L1,L2)

        # ===============
        # TITLE
        # ===============

        title = Title("Coupling PinT \& Data assimilation",font_size=40)

        # ===============
        # OBJECTIVES
        # ===============

        objective_tex_1 = Tex("Objective : ","Apply ","P","arralel-","in","-","T","ime"," to ","data assimilation").shift(2*UP)
        objective_tex_2 = Tex("Objective : ","P","arralel ","in"," ","T","ime","(","data assimilation",")").shift(2*UP)
        objective_tex_3 = Tex("Objective : ","P","in","T","(","data assimilation",")").shift(2*UP).scale(35/30)

        technicality_tex_1 = Tex(
            r"$\rightarrow$ ","PinT algorithms are on a ","bounded"," time interval, data assimilation is on an ","unbounded"," time interval"
        ).set_color_by_tex('bound', DEMARK_COLOR).scale(32/30).shift(0.5*UP)
        technicality_tex_2 = Tex(
            r"$\rightarrow$ ","To optimize PinT, we want to start with a coarse approximation and ",r"refine it over time"
        ).scale(32/30).align_to(technicality_tex_1,LEFT).shift(1*DOWN).set_color_by_tex('refine', DEMARK_COLOR)
        technicality_tex_3 = Tex(
            r"$\rightarrow$ ","We want to ",r"preserve",r" the property of the data assimilation scheme : in our case ",r"the convergence rate $\mu$"
        ).scale(32/30).align_to(technicality_tex_1,LEFT).shift(2.5*DOWN).set_color_by_tex('\mu', DEMARK_COLOR).set_color_by_tex('preserve', DEMARK_COLOR)

        ## ANIM

        ### == SLIDE ==
        self.next_section('COUPLING_1',PresentationSectionType.SKIP)
        self.play(Write(title))
        self.wait(2)

        ## == SLIDE ==
        self.next_section('COUPLING_1.1',PresentationSectionType.SUB_SKIP)
        self.play(Write(objective_tex_1))
        self.wait(2)
        ## == SLIDE ==
        self.next_section('COUPLING_1.2',PresentationSectionType.SUB_SKIP)
        self.play(TransformMatchingTex(objective_tex_1,objective_tex_2))
        self.wait(1)
        self.play(TransformMatchingTex(objective_tex_2,objective_tex_3))
        self.wait(1)
        ## == SLIDE ==
        self.next_section('COUPLING_1.3',PresentationSectionType.SUB_NORMAL)
        self.play(Write(technicality_tex_1))
        self.wait(1)
        self.play(Write(technicality_tex_2))
        self.wait(1)
        self.play(Write(technicality_tex_3))
        self.wait(2)
        # CLEANING SLIDE
        self.next_section('COUPLING_1.4',PresentationSectionType.SUB_SKIP)
        self.play(
            FadeOut(technicality_tex_2),
            FadeOut(technicality_tex_3),
            FadeOut(objective_tex_3),
            technicality_tex_1.animate.shift(1.8*UP),
        )
        self.wait(2)

        # ===============
        # BOUNDED & UNBONDED SOLUTION (IDEA)
        # ===============

        strategy_sub_tex = [
            Tex(r"1) Divide the unbonded interval into 'windows' of size ",r"$T$",r" : $W_\ell = (T_{\ell-1},T_\ell), \ell \leq 0$"),
            Tex(r"2) Apply time parallelization scheme on each 'window'"),
            Tex(r"3) Estimate the error at the end of each 'window' to go (or not) onto the next one"),
        ]
        strategy = VGroup(*strategy_sub_tex).arrange(DOWN, buff=0.5).shift(0.5*DOWN)

        ## ANIM

        ## == SLIDE ==
        self.next_section('COUPLING_2',PresentationSectionType.NORMAL)
        self.play(Write(strategy_sub_tex[0]))
        self.wait(1)
        self.play(Write(strategy_sub_tex[1]))
        self.wait(1)
        self.play(Write(strategy_sub_tex[2]))
        self.wait(2)
        ## == SLIDE ==
        self.next_section('COUPLING_2.1',PresentationSectionType.SUB_SKIP)
        self.play(Unwrite(strategy))
        self.wait(2)

        # ===============
        # BOUNDED & UNBONDED SOLUTION (GRAPH)
        # ===============

        bounded_unbounded_tex = Tex("PinT on unbounded time intervals ?").move_to([-4,2,0])

        dict_values = {
            0 : Tex(r"$0=T_0$"),
            1 : Tex(r"$T_1$"),
            2 : Tex(r"$T_2$"),
            3 : Tex(r"$T_3$"),
            4 : Tex(r"$T_4$")
        }

        axes_PinT = Axes(
            x_range = [-0.1,4.1,1],
            y_range = [-0.2,1.2,2],
            x_length = 10*(4.2/4),
            y_length = 4,
            tips = False,
            x_axis_config = {"include_numbers": False, "font_size": 25},
            y_axis_config = {"include_numbers": False, "font_size": 25},
        ).shift(DOWN)

        axes_PinT.get_axes()[0].add_labels(dict_values)

        def f_func(t): return( (1/20) * np.sin(8*(t**(4/3))) )
        def g_func(t): return( (1/12) * ( (t-2)**3 + (t-3)**2 ) )
        def h_func(t): return( (1/2) * np.exp(-1.5*(t-2.5)**2) )
        def i_func(t): return( f_func(t) + g_func(t) + h_func(t) )
        def j_func(t): return( i_func(t) + np.exp(-2*t) )
        def k_func(t): return( i_func(t) + np.exp(-2*t) * (t+1) )

        graph_state      = axes_PinT.plot(lambda t: i_func(t), x_range=[0, 4], color = STATE_COLOR)
        graph_state_dash = DashedVMobject(graph_state, num_dashes = 50, dashed_ratio = 1/2)
        state_init       = MathTex("x_0",color = STATE_COLOR,font_size=30).move_to([-5.3,-2.1,0])

        state_lab_tex = Tex(r"$x$").set_color(STATE_COLOR).move_to([-4,-2,0])

        graph_obs      = axes_PinT.plot(lambda t: j_func(t), x_range=[0, 3.2], color = OBS_COLOR)
        obs_init       = MathTex("\hat{x}_0",color = OBS_COLOR,font_size=30).move_to([-5.3,0.6,0])

        obs_lab_tex = Tex(r"$\hat{x}$").set_color(OBS_COLOR).move_to([-4,-0.8,0])

        obs_precision_tex = Tex(r"$\hat{x}$",r" computed with max. precision ($\Delta_t \ll 0$)").set_color_by_tex('hat',OBS_COLOR).to_corner(DL).shift(0.3*DOWN)

        dot_final_obs  = Dot([3,-1.3,0],color = OBS_COLOR)
        stop_obs_sub   = [DashedLine(start = dot_final_obs, end = [3,-3,0],color = OBS_COLOR),
            MathTex("T_f",font_size=30,color = OBS_COLOR).move_to([3,-3.3,0])]
        stop_obs       = VGroup(*stop_obs_sub)

        graph_obs_para_sub = [axes_PinT.plot(lambda t: k_func(t), x_range=[k/4, (k+1)/4], color = DEMARK_COLOR) for k in range(0,16)]
        graph_obs_para = VGroup(*graph_obs_para_sub)

        obs_para_lab_tex = Tex(r"$\hat{x}_{\lVert}$").set_color(DEMARK_COLOR).move_to([-4,0.5,0]).scale(35/30)

        obs_para_precision_tex = Tex(r"$\hat{x}_{\lVert}$ : ",r"$\hat{x}_{\lVert}^{T1}$",r" : with \textit{some} precision ($\Delta_t \ll 0$), ",r"$\hat{x}_{\lVert}^{T2}$",r" exact (expm)").set_color_by_tex('T1',BROWN).set_color_by_tex('T2',GREEN).set_color_by_tex('\lVert}$',DEMARK_COLOR).to_corner(DL).shift(0.4*DOWN+0.3*LEFT).scale(28/30)

        separator = VGroup(
            DashedLine(start = [-5,-3,0], end = [-5,1,0],stroke_opacity =0.4),
            DashedLine(start = [-2.5,-3,0], end = [-2.5,1,0],stroke_opacity =0.4)
        )
        fill_intervals = [Rectangle(width = (2.5/4.0), height=4.0, color = FRONT_COLOR, fill_opacity = 0.1 ,stroke_opacity = 0).move_to([-5+(2.5/8),-1,0]),
            Rectangle(width = (2.5/4.0), height=4.0, color = GRAY, fill_opacity = 0.1 ,stroke_opacity = 0).move_to([-5+3*(2.5/8),-1,0]),
            Rectangle(width = (2.5/4.0), height=4.0, color = FRONT_COLOR, fill_opacity = 0.1 ,stroke_opacity = 0).move_to([-5+5*(2.5/8),-1,0]),
            Rectangle(width = (2.5/4.0), height=4.0, color = GRAY, fill_opacity = 0.1 ,stroke_opacity = 0).move_to([-5+7*(2.5/8),-1,0])]

        intervals = VGroup(*fill_intervals)

        #brace = Brace(intervals,UP)
        brace = DoubleArrow(start = intervals.get_left(), end = intervals.get_right(),stroke_width=3,max_tip_length_to_length_ratio=0.05,buff=0).shift(2.2*UP)
        window_tex_1 = MathTex("W_","1", font_size= 25).next_to(brace,UP).shift(0.2*DOWN)
        window_tex_2 = MathTex("W_","2", font_size= 25).next_to(brace,UP).shift(0.2*DOWN + 2.5*RIGHT)
        window_tex_3 = MathTex("W_","3", font_size= 25).next_to(brace,UP).shift(0.2*DOWN + 2*2.5*RIGHT)
        window_tex_4 = MathTex("W_","4", font_size= 25).next_to(brace,UP).shift(0.2*DOWN + 3*2.5*RIGHT)
        Window = VGroup(brace,window_tex_1)

        dot_final_para  = Dot([5,-0.2,0],color = DEMARK_COLOR)
        stop_para_sub   = [DashedLine(start = dot_final_para, end = [5,-3,0],color = DEMARK_COLOR),
            MathTex("T_{f\lVert}",font_size=30,color = DEMARK_COLOR).move_to([5,-3.3,0])]
        stop_para       = VGroup(*stop_para_sub)

        stopping_criteria_obs_tex = Tex(r"stop :  ",r"$\lVert \epsilon(t) \lVert < \texttt{tol}$",font_size=22).move_to([2.8,-3.7,0]).set_color_by_tex('eps',OBS_COLOR)
        stopping_criteria_para_tex = Tex(r"$\lVert \epsilon_{\lVert}(T_\ell) \lVert < \texttt{tol}$",font_size=22).move_to([5,-3.7,0]).set_color(DEMARK_COLOR)

        ## ANIM

        ## == SLIDE ==
        self.next_section('COUPLING_3',PresentationSectionType.NORMAL)

        self.play(DrawBorderThenFill(axes_PinT))
        self.play(Write(state_init))
        self.play(Create(graph_state,rate_func = rate_functions.linear, run_time = 3), Write(state_lab_tex))
        self.play(FadeTransform(graph_state,graph_state_dash),)
        self.wait(1)

        ### == SLIDE ==
        self.next_section('COUPLING_3.1',PresentationSectionType.SUB_NORMAL)

        self.play(Write(obs_init))
        self.play(Create(graph_obs, rate_func=rate_functions.linear, run_time = 3), Write(obs_lab_tex), Write(obs_precision_tex))
        self.play(Create(dot_final_obs))
        self.play(Flash(dot_final_obs,color = DEMARK_COLOR),Create(stop_obs),Write(stopping_criteria_obs_tex))
        self.wait(2)

        ## == SLIDE ==
        self.next_section('COUPLING_3.2',PresentationSectionType.SUB_SKIP)

        self.play(graph_state_dash.animate.fade(0.3))
        self.play(graph_obs.animate.fade(0.3))
        self.wait(0.5)

        ## == SLIDE ==
        self.next_section('COUPLING_3.3',PresentationSectionType.SUB_NORMAL)

        self.play(Create(separator),Create(intervals),Create(Window),run_time=3)
        self.play(Indicate(fill_intervals[0],color=DEMARK_COLOR))
        self.play(Indicate(fill_intervals[1],color=DEMARK_COLOR))
        self.play(Indicate(fill_intervals[2],color=DEMARK_COLOR))
        self.play(Indicate(fill_intervals[3],color=DEMARK_COLOR))
        self.wait(1)

        ## == SLIDE ==
        self.next_section('COUPLING_3.4',PresentationSectionType.SUB_NORMAL)

        self.play(*[Create(graph_obs_para[s], rate_func=rate_functions.linear) for s in range(0,4)])
        self.play(Write(obs_para_lab_tex),ReplacementTransform(obs_precision_tex,obs_para_precision_tex))
        self.wait(1)

        ## == SLIDE ==
        self.next_section('COUPLING_3.5',PresentationSectionType.SUB_SKIP)

        self.play(
            separator.animate.shift(2.5*RIGHT),
            intervals.animate.shift(2.5*RIGHT),
            brace.animate.shift(2.5*RIGHT),
            TransformMatchingTex(window_tex_1,window_tex_2)
        )
        self.wait(1)

        ## == SLIDE ==
        self.next_section('COUPLING_3.6',PresentationSectionType.SUB_NORMAL)

        self.play(*[Create(graph_obs_para[s], rate_func=rate_functions.linear) for s in range(4,8)])
        self.wait(1)

        ## == SLIDE ==
        self.next_section('COUPLING_3.7',PresentationSectionType.SUB_SKIP)

        self.play(
            separator.animate.shift(2.5*RIGHT),
            intervals.animate.shift(2.5*RIGHT),
            brace.animate.shift(2.5*RIGHT),
            TransformMatchingTex(window_tex_2,window_tex_3)
        )
        self.wait(1.5)
        self.play(*[Create(graph_obs_para[s], rate_func=rate_functions.linear) for s in range(8,12)])
        self.wait(1.5)

        ## == SLIDE ==
        self.next_section('COUPLING_3.8',PresentationSectionType.SUB_NORMAL)

        self.play(
            separator.animate.shift(2.5*RIGHT),
            intervals.animate.shift(2.5*RIGHT),
            brace.animate.shift(2.5*RIGHT),
            TransformMatchingTex(window_tex_3,window_tex_4)
        )
        self.wait(1.5)
        self.play(*[Create(graph_obs_para[s], rate_func=rate_functions.linear) for s in range(12,16)])
        self.play(Create(dot_final_para),)
        self.play(Flash(dot_final_para,color = DEMARK_COLOR),Create(stop_para),Write(stopping_criteria_para_tex))
        self.wait(1)
        self.play(
            Uncreate(separator),
            Uncreate(intervals),
            Uncreate(VGroup(brace,window_tex_4)),
        )
        self.wait(2)

        ## == SLIDE ==
        self.next_section('COUPLING_3.9',PresentationSectionType.SUB_SKIP)

        self.play(
            Uncreate(graph_state_dash),Uncreate(graph_obs),Uncreate(graph_obs_para),
            Uncreate(state_init),Uncreate(obs_init),
            Uncreate(dot_final_obs),Uncreate(stop_obs),
            Uncreate(dot_final_para),Uncreate(stop_para),
            FadeOut(axes_PinT),FadeOut(technicality_tex_1),
            FadeOut(stopping_criteria_obs_tex),FadeOut(stopping_criteria_para_tex),
            FadeOut(state_lab_tex),FadeOut(obs_lab_tex),
            FadeOut(obs_precision_tex),FadeOut(obs_para_lab_tex),FadeOut(obs_para_precision_tex),
        )
        self.wait(1)

        # ===============
        # PRESERVING PROPERTY (I)
        # ===============

        technicality_tex_2 = Tex(
            r"$\rightarrow$ ",r"To optimize PinT, we want to start with a coarse approximation and ",r"refine it over time",r", while ",r"conserving the convergence rate $\mu$"
        ).scale(32/30).align_to(technicality_tex_1,LEFT).shift(1*DOWN).set_color_by_tex('refine', DEMARK_COLOR).set_color_by_tex('mu', DEMARK_COLOR)

        technicality_tex_2.move_to(technicality_tex_1.get_center())

        error_reminder_tex = Tex(r"$\lVert \epsilon(T_\ell)\lVert \approx C\mathrm{e}^{-\mu T_\ell} $").move_to([4.5,0.7,0])

        box_error_reminder = SurroundingRectangle(error_reminder_tex, color = DEMARK_COLOR, buff = 0.2, corner_radius = 0.2)

        error_sys_sub_tex = [
            Tex(r"$\hat{x}(T_\ell) = \hat{x}^{T1}(T_\ell) + \hat{x}^{T2}(T_\ell)$").shift(4.7*RIGHT + 1*DOWN),
            Tex(r"$\hat{x}_{\lVert} (T_\ell) = {\hat{x}_{\lVert}}^{T1} (T_\ell) + {\hat{x}_{\lVert}}^{T2} (T_\ell)$").shift(4.6*RIGHT + 1.8*DOWN)
        ]
        error_sys_sub_tex[1].align_to(error_sys_sub_tex[0],LEFT)
        error_sys_tex = VGroup(*error_sys_sub_tex)
        error_sys     = VGroup(Brace(error_sys_tex,LEFT),error_sys_tex)

        separator_field = Line(start = [2.1,1.5,0], end = [2.1,-3.4,0])

        error_para_1_tex = Tex(r"$\lVert $",r"$\hat{x}(T_\ell) $",r"$ - $",r"$\hat{x}_{\lVert}(T_\ell)$",r"$ \lVert$").set_color_by_tex('\hat{x}_',DEMARK_COLOR).set_color_by_tex('$\hat{x}(',OBS_COLOR).set_color_by_tex('$x',STATE_COLOR)

        error_sub_1_tex = [
            Tex(r"$\lVert \epsilon_{\lVert}(T_\ell)\lVert$",r"$=$",r"$\lVert $",r"$\hat{x}_{\lVert}(T_\ell)$",r"$ - $",r"$x(T_\ell)$",r"$ \lVert$"
            ).set_color_by_tex('\hat{x}_',DEMARK_COLOR).set_color_by_tex('$x',STATE_COLOR).shift(1*UP + 2.5*LEFT),
            Tex(r"$\lVert \epsilon_{\lVert}(T_\ell)\lVert$",r"$=$",r"$\lVert $",r"$\hat{x}_{\lVert}(T_\ell)$",r"$ - $",r"$x(T_\ell)$",r"$ \lVert$",
                r"$\leq$",r"$\lVert$",r"$x(T_\ell)$",r"$ - $",r"$\hat{x}(T_\ell)$",r"$\lVert$",r"$+$",r"$\lVert $",r"$\hat{x}(T_\ell) $",r"$ - $",r"$\hat{x}_{\lVert}(T_\ell)$",r"$ \lVert$"
            ).set_color_by_tex('\hat{x}_',DEMARK_COLOR).set_color_by_tex('$\hat{x}(',OBS_COLOR).set_color_by_tex('$x',STATE_COLOR).shift(1*UP + 2.5*LEFT),
            VGroup(
                Tex(r"$\lVert \epsilon_{\lVert}(T_\ell)\lVert$",r"$=$",r"$\lVert $",r"$\hat{x}_{\lVert}(T_\ell)$",r"$ - $",r"$x(T_\ell)$",r"$ \lVert$",
                r"$\leq$",r"$\lVert$",r"$\epsilon(T_\ell)$",r"$\lVert$",r"$+$").set_color_by_tex('\hat{x}_',DEMARK_COLOR).set_color_by_tex('$\hat{x}(',OBS_COLOR).set_color_by_tex('$x',STATE_COLOR),error_para_1_tex
            ).arrange(buff=0.05).shift(1*UP + 2.5*LEFT),
        ]

        box_error_2 = SurroundingRectangle(error_sub_1_tex[2], color = DEMARK_COLOR, buff = 0.2, corner_radius = 0.2)

        error_sub_2_tex_1 = Tex(r"$\epsilon_{\lVert}$").move_to([-3.2,0.2,0])

        error_sub_2_tex_2  = VGroup(
            Tex(r"$= $",r"$\hat{x}_{\lVert}$",r"$ - $",r"$x$").set_color_by_tex('\hat{x}_',DEMARK_COLOR).set_color_by_tex('$\hat{x}(',OBS_COLOR).set_color_by_tex('$x',STATE_COLOR),
            Tex(r"$= $",r"${\hat{x}_{\lVert}}^{T1}$",r"$ + $",r"${\hat{x}_{\lVert}}^{T2}$",r"$ - $",r"$x$").set_color_by_tex('\hat{x}_',DEMARK_COLOR).set_color_by_tex('$\hat{x}^',OBS_COLOR).set_color_by_tex('$x',STATE_COLOR),
            Tex(r"$= $",r"${\hat{x}_{\lVert}}^{T1}$",r"$ + $",r"${\hat{x}_{\lVert}}^{T2}$",r"$ - $",r"$\hat{x}^{T1}$",r"$ + $",r"$\hat{x}^{T1}$",r"$ - $",r"$x$").set_color_by_tex('\hat{x}_',DEMARK_COLOR).set_color_by_tex('$\hat{x}^',OBS_COLOR).set_color_by_tex('$x',STATE_COLOR),
            Tex(r"$= $",r"${\hat{x}_{\lVert}}^{T1}$",r"$ - $",r"$\hat{x}^{T1}$",r"$ + $",r"${\hat{x}_{\lVert}}^{T2}$",r"$ + $",r"$\hat{x}^{T1}$",r"$ - $",r"$x$").set_color_by_tex('\hat{x}_',DEMARK_COLOR).set_color_by_tex('$\hat{x}^',OBS_COLOR).set_color_by_tex('$x',STATE_COLOR),
            Tex(r"$= $",r"${\hat{x}_{\lVert}}^{T1}$",r"$ - $",r"$\hat{x}^{T1}$",r"$ + $",r"$\hat{x}$",r"$ - $",r"$x$").set_color_by_tex('\hat{x}_',DEMARK_COLOR).set_color_by_tex('$\hat{x}$',OBS_COLOR).set_color_by_tex('$x',STATE_COLOR).set_color_by_tex('$\hat{x}^',OBS_COLOR)
        ).arrange_in_grid(cols=1,col_alignments="l").align_to(error_sub_2_tex_1.get_corner([1,1,0]),[-1,0.9,0]).shift(0.1*RIGHT)

        error_para_3_tex = error_para_1_tex.copy()

        error_sub_3_tex  = VGroup(
            error_para_3_tex,Tex(r"$=$",r"$\lVert $",r"${\hat{x}_{\lVert}}^{T1}(T_{\ell})$",r"$ - $",r"$\hat{x}^{T1}(T_{\ell})$",r"$ \lVert$").set_color_by_tex('\hat{x}_',DEMARK_COLOR).set_color_by_tex('$\hat{x}^',OBS_COLOR).set_color_by_tex('$x',STATE_COLOR)
        ).arrange(buff = 0.05).move_to([-2.5,-3.2,0])

        box_error_3 = SurroundingRectangle(error_sub_3_tex, color = DEMARK_COLOR, buff = 0.2, corner_radius = 0.2)

        ## ANIM

        ## == SLIDE ==
        self.next_section('COUPLING_4',PresentationSectionType.NORMAL)

        self.play(Write(technicality_tex_2),Create(separator_field))
        self.play(Write(error_reminder_tex))
        self.wait(2)

        ## == SLIDE ==
        self.next_section('COUPLING_4.1',PresentationSectionType.SUB_NORMAL)

        self.play(Write(error_sub_1_tex[0]))
        self.play(TransformMatchingTex(error_sub_1_tex[0],error_sub_1_tex[1]))
        self.wait(1)
        ## == SLIDE ==
        self.next_section('COUPLING_4.1',PresentationSectionType.SUB_NORMAL)

        self.play(TransformMatchingTex(error_sub_1_tex[1],error_sub_1_tex[2]))
        self.wait(1)
        self.play(Write(error_sys))
        self.wait(2)

        ## == SLIDE ==
        self.next_section('COUPLING_4.2',PresentationSectionType.SUB_NORMAL)

        self.play(Write(error_sub_2_tex_1))
        self.play(Write(error_sub_2_tex_2[0]))
        self.play(TransformMatchingTex(error_sub_2_tex_2[0].copy(),error_sub_2_tex_2[1]))
        self.play(TransformMatchingTex(error_sub_2_tex_2[1].copy(),error_sub_2_tex_2[2]))
        self.play(TransformMatchingTex(error_sub_2_tex_2[2].copy(),error_sub_2_tex_2[3]))
        self.play(TransformMatchingTex(error_sub_2_tex_2[3].copy(),error_sub_2_tex_2[4]))
        self.wait(2)

        ## == SLIDE ==
        self.next_section('COUPLING_4.3',PresentationSectionType.SUB_NORMAL)

        self.play(ReplacementTransform(error_para_1_tex.copy(),error_para_3_tex))
        self.wait(1.5)
        self.play(Write(error_sub_3_tex[1]))

        ## == SLIDE ==
        self.next_section('COUPLING_4.4',PresentationSectionType.SUB_NORMAL)

        self.play(Create(box_error_2),Create(box_error_3),Create(box_error_reminder))
        self.wait(2)

        ## == SLIDE == (CLEANING)
        self.next_section('COUPLING_4.5',PresentationSectionType.SUB_SKIP)

        self.play(
            FadeOut(error_sys),
            FadeOut(VGroup(error_sub_2_tex_1,error_sub_2_tex_2)),
            Uncreate(separator_field),
            FadeOut(box_error_2),
            FadeOut(box_error_3),
            FadeOut(box_error_reminder),
        )
        self.play(VGroup(error_reminder_tex,error_sub_1_tex[2],error_sub_3_tex).animate.arrange(DOWN, buff = 0.5).shift(0.5*UP))
        self.wait(2)

        # ===============
        # PRESERVING PROPERTY (II)
        # ===============

        preserving_tex = Tex(r"We must have ",r"$\lVert $",r"${\hat{x}_{\lVert}}^{T1}(T_{\ell})$",r"$ - $",r"$\hat{x}^{T1}(T_{\ell})$",r"$ \lVert \approx C_{\lVert}\mathrm{e}^{-\mu T_\ell}$").set_color_by_tex('\hat{x}_',DEMARK_COLOR).set_color_by_tex('$\hat{x}^',OBS_COLOR).set_color_by_tex('$x',STATE_COLOR).shift(1.5*DOWN)

        rate_tex = Tex(r"If RK4 : ",r"$(\Delta_t)_{\ell+1} \leq \left(((\Delta_t)_{\ell})^4 \mathrm{e}^{-\mu T}\right)^{1/4}, \quad \forall \ell \leq 1$").shift(2.5*DOWN)

        box_preserving = SurroundingRectangle(VGroup(preserving_tex,rate_tex), color = DEMARK_COLOR, buff = 0.2, corner_radius = 0.2)

        ## ANIM

        ## == SLIDE ==
        self.next_section('COUPLING_5',PresentationSectionType.NORMAL)

        self.play(Write(preserving_tex))
        self.wait(2)
        self.play(Write(rate_tex))
        self.play(Create(box_preserving))
        self.wait(2)

        ## == SLIDE == (CLEANING)
        self.next_section('COUPLING_5.1',PresentationSectionType.SUB_SKIP)

        self.play(
            Unwrite(title),
            FadeOut(VGroup(error_reminder_tex,error_sub_1_tex[2],error_sub_3_tex)),
            Unwrite(rate_tex),
            Unwrite(preserving_tex),
            Uncreate(box_preserving),
            Unwrite(technicality_tex_2)
        )
        self.wait(1)

# ==============================================
# RESULTS SCENE
# Present the results of Paraexp applied to a
# Luenberger observer with a 2D wave equation
# ==============================================

class F_Results(Scene):
    def construct(self):

        # ===============
        # COLOR MANAGMENT
        # ===============

        Tex.set_default(color = FRONT_COLOR,font_size = 30)
        MathTex.set_default(color = FRONT_COLOR,font_size = 30)
        Mobject.set_default(color = FRONT_COLOR)

        # ===============
        # GRID FOR CONSTRUCTION PURPUSE ONLY
        # ===============

        L1 = Line(start=[- 7.1, 0., 0.], end=[7.1, 0., 0.],stroke_opacity =0.2)
        for i in range(-3,4):
            L1 = VGroup(L1,Line(start=[- 7.1, i, 0.], end=[7.1, i, 0.],stroke_opacity =0.1))

        L2 = Line(start=[0., -4., 0.], end=[0., 4., 0.],stroke_opacity =0.2)
        for i in range(-6,7):
            L2 = VGroup(L2,Line(start=[i, -4., 0.], end=[i, 4., 0.],stroke_opacity =0.1))

        if grid == 1 :
            self.add(L1,L2)

        # ===============
        # TITLE
        # ===============

        title_1 = Title("Results : a wave equation",font_size=40)

        # ===============
        # RESULTS WAVE
        # ===============

        wave_tex = Tex(r'2D Wave eq., on $\Omega = [0,2\pi]^2$, $N_x = 9$, obs. space : $\omega$').shift(2.3*UP + 3.35*LEFT).scale(28/30)
        wave_ul = Underline(wave_tex)

        eff_tex = Tex(r"Efficiency = $\frac{\textit{cputime(non-parallel)}}{\textit{\# computers } \times \textit{ cputime(parallel)}}$").shift(2.3*UP + 3.7*RIGHT).scale(28/30)

        # RESULTS
        #T_list = np.array([0.05, 0.1, 0.5, 1, 2, 5, 10, 15])
        T_list = 10**np.arange(-1.5,1.3+0.4,0.4)
        Efficiency_p4_s08 = np.array([0.6201, 0.8199, 0.9114, 0.9454, 0.9113, 0.8923, 0.7098, 0.2376])
        Efficiency_p4_s05 = np.array([0.7080, 0.8413, 0.9461, 0.9504, 0.9843, 0.9644, 0.7733, 0.5146])
        Efficiency_p4_s03 = np.array([0.7197, 0.8606, 0.9366, 0.9675, 0.9779, 0.9359, 1.0031, 1.0117])

        Efficiency_p8_s08 = np.array([0.5757, 0.7740, 0.8737, 0.9340, 0.9035, 0.8844, 0.7186, 0.2420])
        Efficiency_p8_s05 = np.array([0.5849, 0.7800, 0.8904, 0.9369, 0.9949, 0.9664, 0.7774, 0.5201])
        Efficiency_p8_s03 = np.array([0.6047, 0.7829, 0.8909, 0.9551, 0.9644, 0.9535, 1.0059, 1.0092])

        Efficiency_p16_s08 = np.array([0.4080, 0.6358, 0.7788, 0.8715, 0.8849, 0.8711, 0.7058, 0.2362])
        Efficiency_p16_s05 = np.array([0.4087, 0.6309, 0.7898, 0.8789, 0.9600, 0.9471, 0.7560, 0.5056])
        Efficiency_p16_s03 = np.array([0.4334, 0.6478, 0.8034, 0.8979, 0.9342, 0.9112, 0.9870, 0.9973])

        # AXES
        axes_results_p4 = Axes(
            #x_range = [-1,16,5],
            x_range = [-1.5,1.3,0.5],
            y_range = [-0.05,1,0.2],
            x_length = 3.5,
            y_length = 3.5,
            tips = False,
            #x_axis_config = {"include_numbers": True, "font_size": 20},
            x_axis_config = {"include_numbers": False, "font_size": 20, "scaling": LogBase(custom_labels=True), "include_ticks" :True},
            y_axis_config = {"include_numbers": True, "font_size": 20},
        )

        dict_values = {0.1 : Tex(r"$10^{-1}$"), 1 : Tex(r"$10^{0}$"), 10 : Tex(r"$10^{1}$")}
        axes_results_p4.get_axes()[0].add_labels(dict_values),

        x_lab_results_p4 = axes_results_p4.get_x_axis_label("T = |W_\ell|").scale(0.7).shift(0.4*LEFT+0.7*DOWN)
        y_lab_results_p4 = axes_results_p4.get_y_axis_label("Eff").scale(0.7).shift(0.4*LEFT)
        lab_results_p4   = VGroup(x_lab_results_p4,y_lab_results_p4)

        axes_results_p8  = axes_results_p4.copy()
        lab_results_p8   = lab_results_p4.copy()
        axes_results_p16 = axes_results_p4.copy()
        lab_results_p16  = lab_results_p4.copy()

        axes_results_p4.shift(4.5*LEFT)
        lab_results_p4.shift(4.5*LEFT)
        axes_results_p16.shift(4.5*RIGHT)
        lab_results_p16.shift(4.5*RIGHT)

        VGroup(axes_results_p4,lab_results_p4,axes_results_p8,lab_results_p8,axes_results_p16,lab_results_p16).shift(1*DOWN)

        h = (3.5-0.05)/4

        red_zone_p4  = Rectangle(width = 3.5, height=(3.5-0.05)/4, color = RED, fill_opacity = 0.2 ,stroke_opacity = 0).move_to(axes_results_p4.get_center()).shift(1.07*DOWN+0.25*RIGHT)
        red_zone_p8  = Rectangle(width = 3.5, height=(3.5-0.05)/8, color = RED, fill_opacity = 0.2 ,stroke_opacity = 0).move_to(axes_results_p8.get_center()).shift((1.07+h/4)*DOWN+0.25*RIGHT)
        red_zone_p16 = Rectangle(width = 3.5, height=(3.5-0.05)/16, color = RED, fill_opacity = 0.2 ,stroke_opacity = 0).move_to(axes_results_p16.get_center()).shift((1.11+h/3)*DOWN+0.25*RIGHT)

        axes_titles = VGroup(
            Tex(r'computers = 4').shift(4.5*LEFT),
            Tex(r'computers = 8'),
            Tex(r'computers = 16').shift(4.5*RIGHT),
        ).shift(3.4*DOWN)

        # RESULTS LEGEND
        line_dot_s08 = VGroup(Line([-0.75,0,0],[0.75,0,0], color = BLUE),Dot( stroke_width=3, fill_color=BLUE))
        legend_s08 = VGroup(line_dot_s08, Tex(r': $|\omega|=0.85|\Omega|$',font_size=25)).arrange(buff = 0.1)

        line_dot_s05 = VGroup(Line([-0.75,0,0],[0.75,0,0], color = RED),Dot( stroke_width=3, fill_color=RED))
        legend_s05 = VGroup(line_dot_s05, Tex(r': $|\omega|=0.5|\Omega|$',font_size=25)).arrange(buff = 0.1)

        line_dot_s03 = VGroup(Line([-0.75,0,0],[0.75,0,0], color = GREEN),Dot( stroke_width=3, fill_color=GREEN))
        legend_s03 = VGroup(line_dot_s03, Tex(r': $|\omega|=0.35|\Omega|$',font_size=25)).arrange(buff = 0.1)

        legend_group = VGroup(legend_s08,legend_s05,legend_s03).arrange(buff=1).shift(1.5*UP)

        # RESULTS GRAPH
        ### Results p=4

        results_p4_s08 = axes_results_p4.plot_line_graph(T_list,Efficiency_p4_s08,
            line_color=BLUE,
            vertex_dot_style=dict(stroke_width=3,  fill_color=BLUE)
        )
        results_p4_s05 = axes_results_p4.plot_line_graph(T_list,Efficiency_p4_s05,
            line_color=RED,
            vertex_dot_style=dict(stroke_width=3,  fill_color=RED)
        )
        results_p4_s03 = axes_results_p4.plot_line_graph(T_list,Efficiency_p4_s03,
            line_color=GREEN,
            vertex_dot_style=dict(stroke_width=3,  fill_color=GREEN)
        )

        ### Results p=8

        results_p8_s08 = axes_results_p8.plot_line_graph(T_list,Efficiency_p8_s08,
            line_color=BLUE,
            vertex_dot_style=dict(stroke_width=3,  fill_color=BLUE)
        )
        results_p8_s05 = axes_results_p8.plot_line_graph(T_list,Efficiency_p8_s05,
            line_color=RED,
            vertex_dot_style=dict(stroke_width=3,  fill_color=RED)
        )
        results_p8_s03 = axes_results_p8.plot_line_graph(T_list,Efficiency_p8_s03,
            line_color=GREEN,
            vertex_dot_style=dict(stroke_width=3,  fill_color=GREEN)
        )

        ### Results p=16

        results_p16_s08 = axes_results_p16.plot_line_graph(T_list,Efficiency_p16_s08,
            line_color=BLUE,
            vertex_dot_style=dict(stroke_width=3,  fill_color=BLUE)
        )
        results_p16_s05 = axes_results_p16.plot_line_graph(T_list,Efficiency_p16_s05,
            line_color=RED,
            vertex_dot_style=dict(stroke_width=3,  fill_color=RED)
        )
        results_p16_s03 = axes_results_p16.plot_line_graph(T_list,Efficiency_p16_s03,
            line_color=GREEN,
            vertex_dot_style=dict(stroke_width=3,  fill_color=GREEN)
        )

        ## ANIM

        ## == SLIDE ==
        self.next_section('RESULTS',PresentationSectionType.SKIP)
        self.play(Write(title_1))
        self.wait(1)
        self.next_section('RESULTS_1.1',PresentationSectionType.SUB_NORMAL)
        self.play(Write(wave_tex),Create(wave_ul))
        self.wait(1)
        self.play(Write(eff_tex))
        self.play(DrawBorderThenFill(axes_results_p4),Write(lab_results_p4))
        self.play(DrawBorderThenFill(axes_results_p8),Write(lab_results_p8))
        self.play(DrawBorderThenFill(axes_results_p16),Write(lab_results_p16))
        self.play(Write(axes_titles))
        self.wait(1)
        self.play(Create(red_zone_p4),Create(red_zone_p8),Create(red_zone_p16))
        self.wait(1)
        self.next_section('RESULTS_1.2',PresentationSectionType.SUB_NORMAL)
        self.play(Create(legend_s08[0]),Write(legend_s08[1]))
        self.play(Create(results_p4_s08,run_time = 2))
        self.wait(1)
        self.next_section('RESULTS_1.3',PresentationSectionType.SUB_NORMAL)
        self.play(Create(legend_s05[0]),Write(legend_s05[1]))
        self.play(Create(results_p4_s05,run_time = 2))
        self.wait(1)
        self.next_section('RESULTS_1.4',PresentationSectionType.SUB_NORMAL)
        self.play(Create(legend_s03[0]),Write(legend_s03[1]))
        self.play(Create(results_p4_s03,run_time = 2))
        self.wait(1)
        self.next_section('RESULTS_1.5',PresentationSectionType.SUB_NORMAL)
        self.play(Create(results_p8_s08,run_time = 2))
        self.play(Create(results_p8_s05,run_time = 2))
        self.play(Create(results_p8_s03,run_time = 2))
        self.wait(1)
        self.play(Create(results_p16_s08,run_time = 2))
        self.play(Create(results_p16_s05,run_time = 2))
        self.play(Create(results_p16_s03,run_time = 2))
        self.wait(1)
        self.next_section('RESULTS_1.6',PresentationSectionType.SUB_SKIP)
        self.play(
            FadeOut(VGroup(results_p16_s08,results_p16_s05,results_p16_s03)),
            FadeOut(VGroup(results_p8_s08,results_p8_s05,results_p8_s03)),
            FadeOut(VGroup(results_p4_s08,results_p4_s05,results_p4_s03)),
            FadeOut(VGroup(axes_results_p4,axes_results_p8,axes_results_p16,lab_results_p4,lab_results_p8,lab_results_p16)),
            Uncreate(legend_s08[0]),Unwrite(legend_s08[1]),
            Uncreate(legend_s05[0]),Unwrite(legend_s05[1]),
            Uncreate(legend_s03[0]),Unwrite(legend_s03[1]),
            Unwrite(axes_titles),
            Uncreate(red_zone_p4),Uncreate(red_zone_p8),Uncreate(red_zone_p16),
            Uncreate(wave_ul),Unwrite(wave_tex),Unwrite(eff_tex)
        )

        title_2 = Title("Results : following \& leads",font_size=40)

        limitation_1 = Tex(r"$\rightarrow$ ",r"Works similarly for heat equation (1D \& 2D)")

        limitation_2 = Tex(r"$\rightarrow$ ",r"Application to ",r"Linear Wave Theory (LWT)",r" : (in progress with N. Desmars)").set_color_by_tex("LWT",DEMARK_COLOR)

        limitation_21 = [Tex(r"$\cdot$ ",r"Convergence of the observer is ",r"not clear ('floor')").set_color_by_tex("clear",DEMARK_COLOR),
            Tex(r"$\cdot$ ",r"Such 'floor' depends on the waves \& obs. domain"),
            Tex(r"(complexity, frequencies, amplitudes, etc...)"),
            Tex(r"$\cdot$ ",r"Observability / controlability",r" of the eq. system ?").set_color_by_tex("Obs",DEMARK_COLOR),
            Tex(r"$\cdot$ ",r"Choice of ",r"$L$",r" ?").set_color_by_tex("L",DEMARK_COLOR)]

        limitations = VGroup(limitation_1,limitation_2,
            limitation_21[0],limitation_21[1],limitation_21[2],limitation_21[3],limitation_21[4]
        ).arrange_in_grid(cols=1, col_alignments="l")

        VGroup(*limitation_21).shift(1*RIGHT + 0.3*DOWN)
        limitation_21[2].shift(0.1*RIGHT)
        limitations.shift(0.5*LEFT)

        ## ANIM

        ## == SLIDE ==
        self.next_section('RESULTS_2',PresentationSectionType.NORMAL)
        self.play(Transform(title_1,title_2))
        self.wait(1)

        ## == SLIDE ==
        self.next_section('RESULTS_2.1',PresentationSectionType.SUB_NORMAL)
        self.play(Write(limitations,run_time = 4))
        self.wait(1)

        ## == SLIDE ==
        self.next_section('RESULTS_2.2',PresentationSectionType.SUB_SKIP)
        self.play(
            Unwrite(title_1),
            FadeOut(limitations)
        )
        self.wait(1)

# ==============================================
# END SCENE
# Thanks and bibliography
# ==============================================

class G_End(Scene):
    def construct(self):

        # ===============
        # COLOR MANAGMENT
        # ===============

        Tex.set_default(color = FRONT_COLOR,font_size = DEFAULT_FONT_SIZE)
        MathTex.set_default(color = FRONT_COLOR,font_size = DEFAULT_FONT_SIZE)
        Mobject.set_default(color = FRONT_COLOR)

        # ===============
        # GRID FOR CONSTRUCTION PURPUSE ONLY
        # ===============

        L1 = Line(start=[- 7.1, 0., 0.], end=[7.1, 0., 0.],stroke_opacity =0.2)
        for i in range(-3,4):
            L1 = VGroup(L1,Line(start=[- 7.1, i, 0.], end=[7.1, i, 0.],stroke_opacity =0.1))

        L2 = Line(start=[0., -4., 0.], end=[0., 4., 0.],stroke_opacity =0.2)
        for i in range(-6,7):
            L2 = VGroup(L2,Line(start=[i, -4., 0.], end=[i, 4., 0.],stroke_opacity =0.1))

        if grid == 1 :
            self.add(L1,L2)

        # ===============
        # THANKS & BANNER
        # ===============

        Thanks = Tex("Thanks for your attention !",font_size=40).shift(0.3*UP)
        banner = ManimBanner(dark_theme = not(black_and_white)).scale(0.25)
        banner_tex = Tex("realised with :",font_size=30)
        group_banner = VGroup(banner_tex,banner).arrange(DOWN).shift(2.5*DOWN)


        # ===============
        # BIB
        # ===============

        ref_1 = VGroup(
            Tex("[1] Kautsky, Nichols, Van Dooren. ","'Robust pole assignment in linear state feedback.' (1985).",font_size=25)
        ).arrange(RIGHT, buff= 0.05)

        ref_2 = VGroup(
            Tex("[2] Haine, Ramdani. 'Observateurs itératifs, ","en horizon fini. Application à la reconstruction"," de données initiales pour des EDP d'évolution.' (2011).",font_size=25)
        ).arrange(RIGHT, buff= 0.05)

        ref_3 = VGroup(
            Tex("[3] Gander, Güttel."," 'Paraexp : a parallel integrator for "," linear initial-value problems.' (2013).",font_size=25),
        ).arrange(RIGHT, buff=0.05)

        ref_4 = VGroup(
            Tex("[4] The Manim Community Developers. ","Manim – Mathematical Animation Framework (Version v0.15.2)."," https://www.manim.community/. (2022).",font_size=25)
        ).arrange(RIGHT, buff= 0.05)

        ## == SLIDE ==
        self.next_section('END',PresentationSectionType.SKIP)
        self.play(Write(Thanks))
        self.wait(2)

        ## == SLIDE ==
        self.next_section('END.1',PresentationSectionType.SUB_NORMAL)
        self.play(Thanks.animate.shift(2.7*UP))
        self.play(Write(VGroup(ref_1,ref_2,ref_3,ref_4).arrange_in_grid(cols=1, col_alignments="l")))
        self.play(Write(banner))
        self.play(banner.expand(direction="center"))
        self.wait(1)

        ## == SLIDE ==
        self.next_section('END.1',PresentationSectionType.SUB_NORMAL)
        self.play(Unwrite(banner),Unwrite(Thanks))
        self.wait(1)

# ==============================================
# BIBLIOGRAPHY
# ==============================================
#
# present in the presentation :
#
# [1] Kautsky, Nichols, Van Dooren. 'Robust pole assignment in linear state feedback.' (1985).
# [2] Haine, Ramdani. 'Observateurs itératifs, en horizon fini. Application à la reconstruction de données initiales pour des EDP d'évolution.' (2011).
# [3] Gander, Güttel. 'Paraexp : a parallel integrator for linear initial-value problems.' (2013).
# [4] The Manim Community Developers. Manim – Mathematical Animation Framework (Version v0.15.2). https://www.manim.community/. (2022).
#
# ==============================================
# ABSTRACT
# ==============================================
#
# Assimilation and identification problems related to hyperbolic systems arise in many fields of applications,
# e.g. weather forecasting, seismology or reconstruction of ocean surface [2, 8, 1, 7]. Despite the growing importance
# of computational issues in these fields, to the best of our knowledge, time parallelization of the assimilation
# procedures has never been investigated either from a practical or from a mathematical point of view. On the other hand,
# the use of such parallelization techniques for optimal control problems is now well documented. The processing
# of data arriving as a continuous stream adds a new level of difficulty, both for the assimilation method, which
# can no longer be based on adjoint computation, and for time parallelization, which usually applies to simulations on bounded,
# predefined time intervals. The problem of adjoint-free assimilation is usually dealt with by observers,
# also called nudging techniques [3], but other methods based on probabilities can also be use [5]. Adapting parallelization
# techniques in time is the core of this presentation.
#
# Our aim is to present a coupling between a time parallelization method and an observer, in order to accelerate the
# data assimilation procedure over unbounded time intervals. We will mainly focus on the algorithm ParaExp [4] for the first part,
# and the Luenberger observer [6] for the second one. We will present both problems individually, and then our solution
# for applying the ParaExp algorithm onto the Luenberger observer over and unbounded time interval. We will then illustrate
# the performance of this technique with some numerical examples over systems governed by evolution partial differential
# equations (PDEs), specifically parabolic and hyperbolic problems. Finally, we aim to apply those parallelization methods
# to data-assimilation problems over a system arising from Linear Wave Theory (LWT).
#
# [1] Reconstruction of Ocean Surfaces From Randomly Distributed Measurements Using a Grid-Based Method,
#     vol. Volume 6 : Ocean Engineering of International Conference on Offshore Mechanics and Arctic Engineering, 2021.
#     doi :10.1115/OMAE2021-62409. V006T06A059.
# [2] M. Asch, M. Bocquet, M. Nodet. Data assimilation : methods, algorithms, and applications.
#     Funamentals of Algorithms. SIAM, 2016.
# [3] D. Auroux, J. Blum, G. Ruggiero. Data assimilation for geophysical fluids : the Diffusive Back and Forth Nudging,
#     vol. 15 of INdAM Series, pp. 139–174. Springer, 2016.
# [4] M. J. Gander, S. Güttel. Paraexp : A parallel integrator for linear initial-value problems.
#     SIAM Journal on Scientific Computing, 35(2), C123–C142, 2013. doi :10.1137/110856137.
# [5] J. M. Lewis, S. Lakshmivarahan, S. Dhall. Dynamic data assimilation : a least squares approach,
#     vol. 13. Cambridge University Press, 2006.
# [6] D. Luenberger. An introduction to observers.
#     Automatic Control, IEEE Transactions on, 16, 596 – 602, 1972. doi :10.1109/TAC.1971.1099826.
# [7] A. Simpson, M. Haller, D. Walker, P. Lynett, D. Honegger. Wave-by-wave forecasting via assimi- lation of marine radar data.
#     Journal of Atmospheric and Oceanic Technology, 37(7), 1269 – 1288, 2020. doi :10.1175/JTECH-D-19-0127.1.
# [8] C. K. Wikle. Atmospheric modeling, data assimilation, and predictability.
#     Technometrics, 47(4), 521–521, 2005. doi :10.1198/tech.2005.s326.
