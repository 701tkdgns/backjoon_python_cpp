def merge_Sort(arr):
    def sort(p, q):
        if q - p < 2:
            return
        m = (p + q) // 2
        sort(p, m)
        sort(m, q)
        merge(p, m, q)

    def merge(low, mid, high):
        l, h = low, mid
        tmp = []
        while l < mid and h < high:
            if arr[l] < arr[h]:
                tmp.append(arr[l])
                l += 1
            else:
                tmp.append(arr[h])
                h += 1

        while l < mid:
            tmp.append(arr[l])
            l += 1
        while h < high:
            tmp.append(arr[h])
            h += 1
        for i in range(low, high):
            arr[i] = tmp[i - low]

    return sort(0, len(arr))


# N, K = map(int, input().split())
lst = list(map(int, input().split()))
merge_Sort(lst)
print(lst)
