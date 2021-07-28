<#
.Author
Carl C
.Description
Powershell functions for interacting with python on the command line
#>

function pydocwin {
<#
.Description
Invoke pydoc from the command line
#>

if (Get-Command pydoc -ErrorAction ignore) {
    pydoc $args
}
else {
    if (Get-Command py -ErrorAction Ignore) {
        py -m pydoc $args
    }
    else { return Write-Error "py not found on your system" }
}

}
