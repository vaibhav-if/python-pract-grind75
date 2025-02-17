def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    result = []
    newStart, newEnd = newInterval

    for interval in intervals:
        start, end = interval
        if end < newStart:
            result.append(interval)
        elif start > newEnd:
            result.append([newStart, newEnd])
            newStart, newEnd = interval
        else:
            newStart = min(newStart, start)
            newEnd = max(newEnd, end)
    
    result.append([newStart, newEnd])
    return result

print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))