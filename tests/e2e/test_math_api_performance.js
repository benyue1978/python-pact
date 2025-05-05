import http from 'k6/http';
import { check, sleep } from 'k6';
import { textSummary } from 'https://jslib.k6.io/k6-summary/0.0.1/index.js';

export const options = {
    vus: 10, // 并发用户数
    duration: '10s', // 测试时长
};

export default function () {
    const url = 'http://localhost:8000/api/math/add';
    const payload = JSON.stringify({ a: 2.5, b: 3.5 });
    const params = {
        headers: {
            'Content-Type': 'application/json',
        },
    };
    const res = http.post(url, payload, params);
    check(res, {
        'status is 200': (r) => r.status === 200,
        'result is 6.0': (r) => r.json().result === 6.0,
    });
    sleep(1);
}

export function handleSummary(data) {
    return {
        'summary.json': JSON.stringify(data, null, 2), // 结构化输出
        stdout: textSummary(data, { indent: ' ', enableColors: true }),
    };
} 