import collections
import bisect


class RecentCounter1:

    def __init__(self):
        self.req_in_win = []

    def ping(self, t: int) -> int:
        self.req_in_win.append(t)
        # for idx in range(len(self.req_in_win)):
        #     if self.req_in_win[idx] >= t - 3000:
        #         self.req_in_win = self.req_in_win[idx:] # not elegant
        #         break
        while self.req_in_win[0] < t - 3000:    # delete first/last element in a list in a loop
            self.req_in_win.pop(0)
        return len(self.req_in_win)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

obj = RecentCounter1()
print(obj.ping(1))
print(obj.ping(2))
print(obj.ping(3000))
print(obj.ping(3001))
print(obj.ping(3002))


class RecentCounter2:
    """
    deque VS list
    Use collections.deque: "double-ended queue"
        -   Deques support thread-safe, memory efficient appends and pops from either side of the deque with
            approximately the same O(1) performance in either direction.
        -   Internally, deque is a representation of a *doubly-linked list*
        -   how implementated: https://dev.to/v_it_aly/python-deque-vs-listwh-25i9
        -   ** GOOD for pushing and popping things off the ends
    List:
        Though list objects support similar operations, they are optimized for *fast fixed-length* operations and
        incur O(n) memory movement costs for pop(0) and insert(0, v) operations which change both the size and position
        of the underlying data representation.
        -   lists in Python are implemented with fixed size memory blocks (*arrays*) and hence, they use less memory space
            than deques, but lists have to reallocate memory when a new item is inserted (except when appending)
        -   ** GOOD for random access and fixed-length operations, including slicing

    TC difference:
                                    deque               list
        access by an index          O(n)                O(1)
        append/pop at beginning     O(1)                O(n)
        append/pop at end           O(1)                O(1) + reallocation
        insert in middle            O(n)                O(n)
    """
    def __init__(self):
        self.req_in_win = collections.deque()

    def ping(self, t: int) -> int:
        self.req_in_win.append(t)
        while self.req_in_win[0] < t - 3000:
            self.req_in_win.popleft()
        return len(self.req_in_win)


class RecentCounter3:
    """
    Use bisect: bisection algorithm(二分法) or binarySearch() in Java
    -   TC: O(logN)
    """
    def __init__(self):
        self.req_in_win = []

    def ping(self, t: int) -> int:
        self.req_in_win.append(t)
        # Locate the insertion point for x in a to maintain sorted order.
        return len(self.req_in_win) - bisect.bisect_left(self.req_in_win, t - 3000)


class RecentCounter4:
    """
    Use fixed-size array: the requests within the window can only happen once
    """
    def __init__(self):
        self.req_in_win = []*3001

    def ping(self, t: int) -> int:
        res = 0
        self.req_in_win[t % 3001] = t
        for i in range(3001):
            if self.req_in_win[i] and self.req_in_win[i] > t - 3000:
                res += 1
        return res


"""
Java方法：
1. TreeMap
    TreeMap<Integer, Integer> tm;

    public RecentCounter() {
        tm = new TreeMap<>();
    }
    
    public int ping(int t) {
        tm.put(t, 1 + tm.size());
        return tm.tailMap(t - 3000).size();
    }

2. TreeSet
    TreeSet<Integer> ts;

    public RecentCounter() {
        ts = new TreeSet<>();
    }
    
    public int ping(int t) {
        ts.add(t);
        return ts.tailSet(t - 3000).size();
    }

3. ArrayList (binarySearch)
    List<Integer> list;

    public RecentCounter() {
        list = new ArrayList<>();
    }
    
    public int ping(int t) {
        list.add(t);
        int index = Collections.binarySearch(list, t - 3000); // search the index of t - 3000.
        if (index < 0) { index = ~index; } // if t - 3000 is not in list, use the index of the ceiling of t - 3000.
        return list.size() - index;
    }

4. Queue
    Queue<Integer> q;

    public RecentCounter() {
        q = new LinkedList<>();
    }
    
    public int ping(int t) {
        q.offer(t);
        while (q.peek() < t - 3000) { q.poll(); }
        return q.size();
    }
"""