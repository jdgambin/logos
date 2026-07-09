# Logos

> An interactive propositional logic inference engine written in Python.

Logos is a personal software project for exploring propositional logic through interactive argument construction and truth-table validation.

At its core, Logos evaluates whether an argument is logically valid by exhaustively checking every possible truth assignment of its propositional variables.

The project provides two complementary interfaces:

* **Command-Line Interface (CLI):** validates complete propositional logic arguments.
* **Flask Web Application:** acts as an interactive assistant for validating each step of a propositional logic derivation before incorporating it into the proof.

To improve readability during the derivation process, the web application also renders logical formulas as LaTeX expressions.

---

## Features

* Validate propositional logic arguments using truth tables.
* Build logical derivations interactively, one inference at a time.
* Validate every inference step before adding it to the derivation.
* Support the following logical connectives:

  * Negation (NOT)
  * Conjunction (AND)
  * Disjunction (OR)
  * Conditional (IF)
  * Biconditional (IFF)
  * NOR
  * XOR
* Render logical formulas as LaTeX expressions.
* Command-line interface.
* Flask-based web application.

---

## How It Works

Given a set of premises and a conclusion, Logos evaluates every possible truth assignment for the propositional variables.

An argument is considered **logically valid** if the implication

> Premises → Conclusion

is true under every possible valuation.

In the web application, users can progressively construct a derivation by proposing new inference steps. Each proposed step is verified by the inference engine before being incorporated into the argument.

---

## Project Structure

```text
.
├── app/
│   ├── logosengine.py      # Propositional logic inference engine
│   ├── logos2latex.py      # LaTeX formula renderer
│   ├── routes.py           # Flask routes
│   ├── templates/
│   └── static/
├── forms.py                # WTForms definitions
├── logos-cli.py            # Command-line interface
├── logos.py                # Flask application entry point
└── config.py
```

---

## Technologies

* Python
* Flask
* WTForms
* SymPy
* HTML
* CSS
* LaTeX

---

## Getting Started

Clone the repository:

```bash
git clone https://github.com/jdgambin/logos.git
cd logos
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the web application:

```bash
python logos.py
```

Or launch the command-line interface:

```bash
python logos-cli.py
```

---

## Design Goals

This project was created to better understand how propositional logic can be implemented through software rather than relying on existing logic libraries.

Its main goals were:

* Design and implement an inference engine from scratch.
* Separate the core inference engine from the user interfaces.
* Explore truth-table evaluation as a method for validating logical arguments.
* Build both a command-line interface and a web application on top of the same engine.
* Improve the learning experience by providing an interactive derivation workflow and mathematical rendering of logical formulas.

---

## Project Status

Logos is an ongoing personal project. It is currently being modernized to incorporate current Python development practices, including improved documentation, automated testing, static analysis, and continuous integration while preserving the original inference engine and its behavior.

---

## License

This project is distributed under the BSD 3-Clause Clear License.