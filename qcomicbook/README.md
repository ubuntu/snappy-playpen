# qcomicbook snap

This project creates a working snap of `qcomicbook`, a viewer for comicbook archives (.cbr, .cbz, .rar etc.) and pdf files.

## Current state

Working features:
  - generally works

Known issues:
  - needs to be connected to the `home` slot to access your files, ie:
    ```
    sudo snap connect qcomicbook:home ubuntu-core:home
    ```
  - uses a plain Qt theme (doesn't obey theming).
  - real printer is not visible, only printing to PDF is supported.
  - prints some gdk-pixbuf and XmbTextListToTextProperty warnings.
