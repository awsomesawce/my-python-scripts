#!/usr/bin/env bash
# GitHub API Bash Script
# Utility script for interacting with the github api.
# License: BSD 2-Clause
# Author: Carl Capodice

prog="$0"
baseurl="https://api.github.com/repos"
noargs="$prog needs args.  \"$prog --help\" for more info"
usage="You typed \"--help\"
Usage: $prog \"user_name repo_name\""

if [ $# -eq 0 ]; then
    echo "$noargs" >&2
    exit 1
fi

if [[ "$1" == "--help" ]] || [[ "$1" == "-h" ]]; then
    printf '%s\n' "$usage"
    exit 1
fi

if ! command -v curl > /dev/null; then
    echo "Curl executable not found" >&2
    exit 1
else
    if [[ "$1" != "awsomesawce" ]]; then
        curl "$baseurl/$1/$2"
    else
        curl "$baseurl/awsomesawce/$2"
    fi
fi
echo "Script finished successfully" 2>&1
exit 0