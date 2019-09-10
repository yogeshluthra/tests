Tests how python's logger works.
Learnings:
- Both `main.py` and `auxiliary.py` have `"root"` as parent. 
- Messages from child processes are passed up the hierarchy. 
- There are logging checks applied at each level (e.g. if ```logger.setLevel(loggin.INFO)``` is not set for each logger, messages of **info** tupe are not rejected.