#!python --version

def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    if (len(racers)>0):
        first = racers[0]
        last = racers[-1]
        racers[0] = last
        racers[-1] = first

def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    total=0
    if n_runs<1:
        return 0
    for i in range(n_runs):
        total+=play_slot_machine()
    return total/n_runs


raceList=[1,2,3]
purple_shell(raceList)
estimate_average_slot_payout(4)
print(raceList)

raceList=[1,2]
purple_shell(raceList)
print(raceList)

raceList=[1]
purple_shell(raceList)
print(raceList)



