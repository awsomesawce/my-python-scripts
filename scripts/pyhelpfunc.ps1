function pyhelp {

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
