import http from 'k6/http';
import { check } from 'k6';

export const options = {
  stages: [
    { duration: '5s', target: 50 },
    { duration: '20s', target: 200 },
    { duration: '5s', target: 0 },
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};

const BASE = __ENV.BASE_URL || 'http://127.0.0.1:8000';

export default function () {
  const res = http.get(`${BASE}/work?io_ms=50&cpu_iters=80000`);
  check(res, { 'status is 200': (r) => r.status === 200 });
}
