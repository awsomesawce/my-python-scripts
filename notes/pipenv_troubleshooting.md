# PIPENV Troubleshooting

When trying to install requests into my virtualenv, I got an error on Windows.
I think the reason is that I didn't have my virtualenv activated.  Now it seems to be working just fine.

## More problems

I again had problems with resolving the path using `pipenv`.  First in mingw64, then in my powershell python env.

I think the problem is i have way too many pythons installed at once.
Right now in order to get things moving, I have to pass the `--python` option to the `pipenv` tool in
order for it to see the correct python.

I want to be working with the latest and greatest python (python3.9), so I used
`(Get-command python3.9).source` to get it.

If I have a venv created already, I don't need to do much.

### What had happened was...

`pipenv` was having trouble with it's `Pipfile.lock` file, so I did what `npm` users would do in that
situation...
I deleted `Pipfile.lock`.
And that didn't fix the problem.
I kept getting this output when I tried installing a basic dependency (requests)...
Well now I lost it because i closed the terminal window to open a new one.

Well right now I'll just be using system-site-packages as my dependencies.  And also stdlib,
which by definition there will never be dependency resolving issues with.

> Woe is me...

The idea of `pipenv` is a nobel one.  And I do enjoy using it (when it works).
There are other ways of tracking dependencies besides the old `requirements.txt` file.
There is the almighty `pyproject.toml` filetype which should be interesting to use.
But I digress.
