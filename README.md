# DSearcher

## About the project

**DSearcher** is a reliable and easy-to-use terminal-oriented open-source program that allows you to get your answers just by typing an equation. Written in **Python** using the **re** module.

The project is still in beta, so it may not contain some content or seem unfinished.

Language: English

## What's new

### v0.2 — Global Update (11.07.26)

**New:**

— Added support for biquadratic and quasi-quadratic equations through the Substitution Method.

— Added an animation on first start.

— Added a wrapper for caught errors.

— Added a power parser to detect them.

— Added support for non-superscripted powers in the ^x format.

— Added special notifications if the equation has no real roots.

— Added display of final x if x₁ or x₂ is negative.

**QoL:**

— Added screen clearing for macOS/Linux/Misc users too.

— Removed all restrictions on equation size.

— Removed the old step-by-step equation completion animation and replaced it with a new AI-inspired loading animation.

— Added recognition and replacement of spaces, equal, and minus-like signs to work properly in the CLI.

— Made the program continuously handle equations, so it no longer needs to be launched every time you want to solve a math problem.

**Tech & Architecture:**

— Restructured the program into backend and frontend (CLI/UI) layers.

— Restructured the CLI layer into fully functional parts, so the main dispatcher now calls several other functions and combines their data.

## How to run

### Option 1: Run in online compiler

Just copy and paste code into any Python online compiler and run it in it.

### Option 2: Run natively

1. Make sure you have Python installed on your computer. If not, install it from its official website.

2. Open a terminal and type `git clone https://github.com/wheennn/DSearcher.git` if you have Git installed, if you don't, install it through its official website or download all the files separately.

3. Open the folder with just-cloned repo: `cd DSearcher`.

4. Run the program by typing `python main.py` in the terminal.

## Tech Stack

**Programming Language:** Python 3.14.3

**Modules:** RegEx, os, platform, time

## License

[MIT LICENSE](https://github.com/wheennn/DSearcher/blob/main/LICENSE)
