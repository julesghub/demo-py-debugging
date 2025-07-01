# demo-py-debugging

Tutorial for python debugging with `ipdb`.

`ipdb` is a python debugger, build upon the standard `pdb` python debugger. The 'i' bit adds helpful features, like code completion and pretty printing. 

 1. `ipbd` install.
   - `pip install ipdb`
 2. Basic usage pattern.
   - `import ipdb; ipdb.set_trace()`
   - https://github.com/learn-co-curriculum/python-p3-debugging-with-ipdb?tab=readme-ov-file
   - https://skillshats.com/blogs/debugging-made-easy-with-ipdb-the-python-debugger/
 3. Parallel runs - mpi4py.
    - Best run with `xterm` or `tmux`. (see launch scripts)
    - `mpirun -np <N> xterm -e <prog>` (old school)
