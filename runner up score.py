if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    winner=max(arr)
    while winner == max(arr):
        arr.remove(max(arr))
        
    print(max(arr))
