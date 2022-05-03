# coding: utf-8
syspaths = sysconfig.get_paths()
syspaths
syspaths['stdlib']
syspaths['stdlib'] = pathlib.Path(syspaths['stdlib'])
syspaths
for item in syspaths:
    print(item)
    
for k, v in syspaths:
    print(k)
    print(v)
    
for k, v in syspaths:
    print(k)
    
for k, v in syspaths:
    print(k, v
    )
    
for k, v in tuple(syspaths):
    print(k, v
    )
    
syspaths.items()
for k, v in syspaths.items():
    print(k, ": ", v)
    
[k, v for k, v in syspaths.items()]
[v for v in syspaths.items()]
systuples = [v for v in syspaths.items()]
systuples[0]
systuples[0][1]
systuples[0][1].is_absolute
systuples[0][1].is_absolute()
get_ipython().run_line_magic('pinfo', '%save')
get_ipython().run_line_magic('save?', 'weirdrepl.py 40-60')
