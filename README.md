# LaTeX Error Checker

## Table of Contents
- [What is this?](#what-is-this)
    - [Why does this help?](#Why-does-this-help)
- [Installation](#installation)
- [Usage](#usage)
- [Donate](#donate)

## What is this?
This program is my attempt at making a more comprehensive LaTeX syntax/error checker, rather than what is printed when running other LaTeX PDF complilation terminal programs.

### Why does this help?
In `pdflatex`'s case, given this empty LaTeX file `test.tex`:

```
\documentclass{article}

\usepackage{hyperref}

\title{Test}
\author{Hussein Esmail}
\date{\today}

\begin{document}
\maketitle
\tableofcontents

\section{First Section}
Some random sentence here.

\end{document}
```

When compiled (by typing `pdflatex test.tex` in Terminal),
it gives this output:

```
This is pdfTeX, Version 3.14159265-2.6-1.40.21 (TeX Live 2020) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./test.tex
LaTeX2e <2020-02-02> patch level 5
L3 programming layer <2020-03-06>
(/usr/local/texlive/2020/texmf-dist/tex/latex/base/article.cls
Document Class: article 2019/12/20 v1.4l Standard LaTeX document class
(/usr/local/texlive/2020/texmf-dist/tex/latex/base/size10.clo))
(/usr/local/texlive/2020/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/local/texlive/2020/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)
(/usr/local/texlive/2020/texmf-dist/tex/generic/iftex/iftex.sty)
(/usr/local/texlive/2020/texmf-dist/tex/latex/pdftexcmds/pdftexcmds.sty
(/usr/local/texlive/2020/texmf-dist/tex/generic/infwarerr/infwarerr.sty))
(/usr/local/texlive/2020/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/local/texlive/2020/texmf-dist/tex/generic/kvsetkeys/kvsetkeys.sty)
(/usr/local/texlive/2020/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)
(/usr/local/texlive/2020/texmf-dist/tex/generic/pdfescape/pdfescape.sty)
(/usr/local/texlive/2020/texmf-dist/tex/latex/hycolor/hycolor.sty)
(/usr/local/texlive/2020/texmf-dist/tex/latex/letltxmacro/letltxmacro.sty)
(/usr/local/texlive/2020/texmf-dist/tex/latex/auxhook/auxhook.sty)
(/usr/local/texlive/2020/texmf-dist/tex/latex/kvoptions/kvoptions.sty)
(/usr/local/texlive/2020/texmf-dist/tex/latex/hyperref/pd1enc.def)
(/usr/local/texlive/2020/texmf-dist/tex/generic/intcalc/intcalc.sty)
(/usr/local/texlive/2020/texmf-dist/tex/generic/etexcmds/etexcmds.sty)
(/usr/local/texlive/2020/texmf-dist/tex/latex/url/url.sty)
(/usr/local/texlive/2020/texmf-dist/tex/generic/bitset/bitset.sty
(/usr/local/texlive/2020/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty))
(/usr/local/texlive/2020/texmf-dist/tex/generic/atbegshi/atbegshi.sty))
(/usr/local/texlive/2020/texmf-dist/tex/latex/hyperref/hpdftex.def
(/usr/local/texlive/2020/texmf-dist/tex/latex/atveryend/atveryend.sty)
(/usr/local/texlive/2020/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty

(/usr/local/texlive/2020/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty
)))
(/usr/local/texlive/2020/texmf-dist/tex/latex/l3backend/l3backend-pdfmode.def)
No file test.aux.
(/usr/local/texlive/2020/texmf-dist/tex/latex/hyperref/nameref.sty
(/usr/local/texlive/2020/texmf-dist/tex/latex/refcount/refcount.sty)
(/usr/local/texlive/2020/texmf-dist/tex/generic/gettitlestring/gettitlestring.s
ty)) [1{/usr/local/texlive/2020/texmf-var/fonts/map/pdftex/updmap/pdftex.map}]
(./test.aux)

Package rerunfilecheck Warning: File `test.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )</usr/local/texlive/2020/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx12.pfb
></usr/local/texlive/2020/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb><
/usr/local/texlive/2020/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb></u
sr/local/texlive/2020/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>
Output written on test.pdf (1 page, 39782 bytes).
Transcript written on test.log.
```

## Installation

## Usage
Simply run `python3 latex_check.py <filename>` in your Terminal. If the Python
file is not in the same path as the LaTeX file, put the full path (if the path
has spaces, put the whole path in quotation marks).

## Donate
[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/husseinesmail)

