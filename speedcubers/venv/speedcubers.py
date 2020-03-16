def cube_times(times):
    minimum = min(times)
    times.remove(min(times))
    times.remove(max(times))
    sr = round(sum(times)/len(times),2)
    print([sr, minimum])
    return (sr, minimum)


czasy = [9.5, 7.6, 11.4, 10.5, 8.1]
cube_times(czasy)