#!/bin/bash
# Number of ranks
N=4
SCRIPT="job.py"

# Start tmux session
SESSION="mpi_debug"

tmux new-session -d -s $SESSION

for RANK in $(seq 0 $((N-1))); do
    CMD="mpirun -n 1 python $SCRIPT"
    
    if [ $RANK -eq 0 ]; then
        tmux send-keys -t $SESSION "$CMD" C-m
    else
        tmux split-window -t $SESSION
        tmux select-layout -t $SESSION tiled
        tmux send-keys -t $SESSION "$CMD" C-m
    fi
done

# Attach
tmux attach -t $SESSION

