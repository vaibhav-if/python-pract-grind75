def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    dist_array = [(point[0] ** 2 + point[1] ** 2, point) for point in points]
    
    dist_array = sorted(dist_array, key=lambda dist: dist[0])
    
    result_array = [q for _, q in dist_array[:k]]

    return result_array

print(kClosest([[1,3],[-2,2]], 1))