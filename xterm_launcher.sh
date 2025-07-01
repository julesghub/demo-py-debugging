#!/bin/bash
N=4
VENV_ACTIVATE="$PWD/venv/bin/activate"  # if needed
SCRIPT="job.py"

for RANK in $(seq 0 $((N-1))); do
    xterm -T "Rank $RANK" \
        -e "source $VENV_ACTIVATE; mpirun -n 1 python $SCRIPT" &
done

wait

