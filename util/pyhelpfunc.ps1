#!/usr/bin/env -S pwsh -noprofile
# Useful utilities for working with python in Powershell

function pyhelp {
<#
.Description
Print python documentation to the powershell console
.NOTES
Prints the same information as python's `pydoc` utility script.
TODO: Test for whether `pydoc` is in PATH and print location of it if true.
#>
param(
    [string]
    $s
)
begin {
    if (Get-Command python3 -ErrorAction ignore) {
        Write-Output 'continuing'
    }
    else { throw 'python3 not found' }
}
process {
    if ($s) {
        python -c "import $s; help($s)"
        return
    }
    else {
        Write-Output "No arg detected.  Try pydoc or python -m pydoc"
    }
}

}
