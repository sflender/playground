'''
Various utilities for processing the logs w/ format as follows:

(IP address) - - unix timestamp "HTTP method URL HTTP version" status_code response_size "-" "user_agent" response_time_ms
127.0.0.1 - - 1625152800 "GET /api/v1/feed HTTP/1.1" 200 123 "-" "curl/7.64.1" 48
10.0.0.5 - - 1625152810 "POST /api/v1/login HTTP/1.1" 401 12 "-" "okhttp" 92
127.0.0.1 - - 1625152820 "GET /api/v1/feed HTTP/1.1" 200 99 "-" "curl/7.64.1" 11
'''

from collections import defaultdict, deque
import time
import heapq
import numpy as np

class LogParser:
    def __init__(self):
        self.request_counts = defaultdict(deque)  # ip: deque of timestamps
        self.time_window = 3600  # 1 hour
        self.latencies = deque()  # (timestamp, latency_ms)

        # for session-related metrics
        self.session_timeout = 900  # 15 minutes
        self.sessions = dict()  # ip: (num_sessions, last_request_time)

    def parse_line(self, line):
        ip_address = line.split(' - - ')[0]
        timestamp = line.split(' - - ')[1][:10]
        self.request_counts[ip_address].append(int(timestamp))
        latency_ms = int(line.strip().split(' ')[-1])
        self.latencies.append((int(timestamp), latency_ms))
        
        # update session metrics
        num_sessions, last_request_time = self.sessions.get(ip_address, (0, 0))
        if int(timestamp) - last_request_time > self.session_timeout:
            # count as new session
            num_sessions += 1
        self.sessions[ip_address] = (num_sessions, int(timestamp))

    def get_top_n_ips(self, n=5, now=None):
        ts = time.time() if now is None else now
        cutoff_time = ts - self.time_window  # ignore all prior requests
    
        # evict old requests
        for key in list(self.request_counts.keys()):
            while self.request_counts[key] and self.request_counts[key][0] < cutoff_time:
                self.request_counts[key].popleft()
            if not self.request_counts[key]:
                del self.request_counts[key]

        # get top n ips by request count
        heap = []
        for ip in list(self.request_counts.keys())[:n]:
            heapq.heappush(heap, (-len(self.request_counts[ip]), ip))
        
        for ip in list(self.request_counts.keys())[n:]:
            count = len(self.request_counts[ip])
            if -count > heap[0][0]:  # more requests than the smallest in heap
                heapq.heappushpop(heap, (-count, ip))
        
        return [(ip, abs(count)) for count, ip in sorted(heap)]
    
    def latency_p99(self, now=None):
        ts = time.time() if now is None else now
        cutoff_time = ts - self.time_window  # ignore all prior requests

        # evict old latencies
        while self.latencies and self.latencies[0][0] < cutoff_time:
            self.latencies.popleft()

        if not self.latencies:
            return None  # no data

        latencies = np.array([lat for _, lat in self.latencies])
        return float(np.percentile(latencies, 99))
    
    def get_avg_num_sessions(self):
        # average number of sessions per user ip
        if not self.sessions:
            return 0.0
        total_sessions = sum(num for num, _ in self.sessions.values())
        return total_sessions / len(self.sessions)


if __name__=="__main__":
    parser = LogParser()
    parser.parse_line('127.0.0.1 - - 1625152800 "GET /api/v1/feed HTTP/1.1" 200 123 "-" "curl/7.64.1" 48')
    parser.parse_line('10.0.0.5 - - 1625152810 "POST /api/v1/login HTTP/1.1" 401 12 "-" "okhttp" 92')
    parser.parse_line('127.0.0.1 - - 1625152820 "GET /api/v1/feed HTTP/1.1" 200 99 "-" "curl/7.64.1" 11')
    parser.parse_line('10.0.0.5 - - 1625152830 "GET /api/v1/feed HTTP/1.1" 200 99 "-" "okhttp" 11')
    parser.parse_line('127.0.0.1 - - 1625153740 "GET /api/v1/feed HTTP/1.1" 200 99 "-" "curl/7.64.1" 11')

    now = 1625156400  # some time later
    print("Top IPs:", parser.get_top_n_ips(n=2, now=now))  # should show both IPs with their counts
    print("P99 Latency:", parser.latency_p99(now=now))  # should compute p99 latency
    print("Avg Num Sessions per IP:", parser.get_avg_num_sessions())  # should show average sessions per IP