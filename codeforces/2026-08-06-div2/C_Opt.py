import heapq

t = int(input())
for _ in range(t):
    n, m = [int(s) for s in input().split()]
    v = [int(s) for s in input().split()]
    a = []
    for i in range(n):
        r = [int(s) for s in input().split()]
        a.append(r)
        
    last_row = sorted(a[-1], reverse=True)
    ans = m
    current_sum = 0
    for k in range(m):
        current_sum += last_row[k]
        if current_sum >= v[-1]:
            ans = k + 1
            break
            
    min_heap = last_row[:ans]
    heapq.heapify(min_heap)
    heap_sum = sum(min_heap)
    
    for i in range(n - 2, -1, -1):
        row = a[i]
        for val in row:
            if val > min_heap[0]:
                heap_sum += val - heapq.heapreplace(min_heap, val)
        
        if heap_sum < v[i]:
            continue
            
        sorted_largest = sorted(min_heap, reverse=True)
        temp_sum = 0
        for k in range(ans):
            temp_sum += sorted_largest[k]
            if temp_sum >= v[i]:
                ans = k + 1
                break
        
        while len(min_heap) > ans:
            heap_sum -= heapq.heappop(min_heap)
            
    print(ans)
