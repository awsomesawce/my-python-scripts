if (get-command gitst -CommandType Function -ErrorAction ignore) {
Write-Error "gitst is initiated as $((Get-Command gitst).Definition)"
} else {
$function:gitst = "git status"
Write-Output "gitst initiated as $function:gitst"
}
