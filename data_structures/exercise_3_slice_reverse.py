sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

chunk1 = sample_list[slice(0, 3)]
print("Chunk 1", chunk1)
chunk1.reverse()
print("Reverse: ", chunk1)

chunk2 = sample_list[slice(3, 6)]
print("Chunk 2: ", chunk2)
print("Reverse: ", chunk2[::-1])

chunk3 = sample_list[slice(6, 9)]
print("Chunk 3: ", chunk3)
print("Reverse: ", list(reversed(chunk3)))
