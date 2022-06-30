# LintWarningRemover
This projects intends to be a modular auto-linter for Python. It is designed on top of an engine which is expandend by add-ons an uses parsing tree analysis (static analysis) in order to automatically fix common Pylint lint-based warnings.

The project currently is in its early stage of development and most of the code in it are simple sketches.

* CUI stands for the 'Consider Using In' Lint-based warning. As seen on the Pylint documentation.
 * An example of a CUI being fixed is:
  * ```python
        if value == 1 or value == 2 or value ==3
        # Fixes to:
        if value in [1,2,3]
    ```