def milliseconds_to_counter_time(miliseconds_time):
    seconds=int((miliseconds_time/1000)%60)
    minutes=int((miliseconds_time/(1000*60))%60)
    hours=int((miliseconds_time/(1000*60*60))%24)

    return "%02d:%02d:%02d" % (hours, minutes, seconds)