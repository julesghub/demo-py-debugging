# demo-py-debugging

Tutorial for python debugging with `ipdb`.

`ipdb` is a python debugger, build upon the standard `pdb` python debugger. The 'i' bit adds helpful features, like code completion and pretty printing. 

 1. `ipbd` installation.
     ```bash
     pip install ipdb
     ```
 2. Basic usage pattern.
   - `import ipdb; ipdb.set_trace()`
   - https://github.com/learn-co-curriculum/python-p3-debugging-with-ipdb?tab=readme-ov-file
   - https://skillshats.com/blogs/debugging-made-easy-with-ipdb-the-python-debugger/
 3. Parallel runs - mpi4py.
    - `mpirun -np <N> xterm -e <prog>` (old school - requires xterm)
    -  Can run with `tmux`. Please install https://github.com/wrs20/tmux-mpi. 
       ```bash
       $ TMUX_MPI_MODE=pane tmux-mpi <N> <prog>       
       ```


### For pretty xterm.
Make, or edit, file `~/.Xresources` to include

```txt
XTerm*faceSize: 11

! Cursor
XTerm*cursorColor: #d79921
XTerm*cursorBlink: true

! Gruvbox colors
*.foreground:   #ebdbb2
*.background:   #282828
*.color0:       #282828
*.color1:       #cc241d
*.color2:       #98971a
*.color3:       #d79921
*.color4:       #458588
*.color5:       #b16286
*.color6:       #689d6a
*.color7:       #a89984
*.color8:       #928374
*.color9:       #fb4934
*.color10:      #b8bb26
*.color11:      #fabd2f
*.color12:      #83a598
*.color13:      #d3869b
*.color14:      #8ec07c
*.color15:      #ebdbb2
```

#### Loads the configuration above
`xrdb -merge ~/.Xresources`     

#### Reset X config.
`xrdb -load /dev/null` 
