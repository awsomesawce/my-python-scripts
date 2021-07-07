# Win32 vs Linux Python environments

When installing packages using pip on Windows, the resulting script is a Windows executable.\
On Unix-based environments like Linux, Cygwin, or MSYS2, the resulting script is an ASCII-encoded Python script.

## Example

I use the BSD command `file` to see the file type.
Here is the output of the `file` command when determining the filetype of `which pipenv`:

```bash
Carl@MrCap MSYS ~
$ file $(which pipenv)
/usr/bin/pipenv: Python script, ASCII text executable
```

When switching to the Mingw64 environment using `source shell mingw64` and installing `pipenv` using the python interpreter 
installed in `/mingw64/bin`, the resulting script is this:

```bash
Carl@MrCap MINGW64 ~
$ file $(which pipenv)
/mingw64/bin/pipenv: PE32+ executable (console) x86-64 (stripped to external PDB), for MS Windows
```

The PE32+ executable is always guaranteed to be compatible with Win32, while the script installed with regular MSYS
depends on whether certain tools are installed afaik.

In general, python scripts are usually cross-compatible if all they require is the python standard library.
