def kill_grandfather():
    grandfather = ("alive")
    if grandfather == ("alive"):
        grandfather = ("dead")
    if grandfather == ("dead"):
        grandfather = ("alive")
        kill_grandfather()

kill_grandfather()
