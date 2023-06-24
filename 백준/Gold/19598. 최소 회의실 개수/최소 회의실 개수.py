import sys, heapq
N = int(sys.stdin.readline().rstrip())
lects = []
for _ in range(N):
	s, t = map(int, sys.stdin.readline().split())
	heapq.heappush(lects, (s, t))

room = []
room.append(heapq.heappop(lects)[1])

while lects:
	tmp = heapq.heappop(lects)
	if room[0] <= tmp[0]:
		heapq.heappop(room)
		heapq.heappush(room, tmp[1])
	else:
		heapq.heappush(room, tmp[1])

print(len(room))