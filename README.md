# ClearScreen (cls)

This is a replacement for CLS that is cross platform.

Instead of clearing the screen, it shows a blob of random ascii art. Because the blob is always likely to be different, this makes it easy to scroll up and see where you were before your last command.

The ascii art comes from me, except for some old stuff used for the OpenStack Trove project.

This isn't to be confused with the [Inspect Class](https://pypi.org/project/cls/) package, which uses the package name cls (this uses the package name clearscreen).

Install with pipx or pipsi or whatever, then run:

```bash
    ? pipx install clearscreen
    ? cls
```


## Change Log

### 0.2.1

Adds more art.

### 0.2.0

Makes showing different colors the default, cause hey why not. Also make the color selectable.

### 0.1.1

Sorts order of files in the internal list to make it easier to find them with `--ls`.

### 0.1.0

First release.
