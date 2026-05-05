### PROD-LLM-API-SERVER
# 1. Setup the virtual env
# 2. Install , fastapi
# 3. Set github and commit
# 4. Create fastapi server - api created
# 5. Performance testing 



### Authetication
### JWT, (JWT, refrest token), AUTH2.0 , 2.0

/predict --> safety mesures , authictae, rate limiting( DDOs), 



### LLM Parrellism

### Data parallelism - in production
## -->  Qwen/Qwen3.6-27B - 55GB (FP16)
## When -->. throughput, latency,  
### Quantization --> which one ? -->


## How to reduce latency ---> 
- TTFT (Time to First Token) → responsiveness (most important for UX)
- TPOT (Time per Output Token) → generation speed
- End-to-end latency
  
Optimize TTFT 
 - Use continuous batching (vLLM default)
 - Prefix Caching
Optimize TPOT: 
 - Tensor Parallelism
 - Use Faster Kernels (flash attention 2)
 - KV Cache Optimization


Practical for Latency
 - Qwen/Qwen3.5-4B (9.34 GB)
 -  Which GPU we need : 
    -  model size(9.34) + KV(12 -16GB) -->24 GPU is enough
    - if we need higher concuurency use a100 --> 
- Test 1 : RTX4090/L4 - 24GB -  full precision
  - check latency - guidellm
  - Maximum concurrency for 262,144 tokens per request: 1.14x
- ℹ Request Latency Statistics Table-1 (Completed Requests)
|=============|=========|========|========|========|=======|=======|=======|=======|
| Benchmark   | Request Latency || TTFT           || ITL          || TPOT         ||
| Strategy    | Sec             || ms             || ms           || ms           ||
|             | Mdn     | p95    | Mdn    | p95    | Mdn   | p95   | Mdn   | p95   |
|-------------|---------|--------|--------|--------|-------|-------|-------|-------|
| synchronous | 4.5     | 7.7    | 78.9   | 3233.2 | 35.0  | 35.1  | 35.4  | 60.0  |
| throughput  | 27.0    | 30.1   | 3912.1 | 6255.4 | 182.0 | 187.6 | 211.1 | 235.1 |
| constant    | 4.9     | 4.9    | 140.2  | 157.1  | 37.5  | 37.5  | 38.3  | 38.4  |
| constant    | 5.0     | 5.0    | 133.4  | 150.3  | 38.6  | 38.6  | 39.3  | 39.4  |
| constant    | 5.2     | 5.3    | 146.1  | 165.2  | 40.2  | 40.3  | 41.0  | 41.2  |
| constant    | 5.5     | 5.5    | 148.7  | 168.4  | 41.9  | 42.0  | 42.8  | 42.9  |
| constant    | 5.7     | 5.7    | 153.8  | 176.1  | 43.5  | 43.5  | 44.4  | 44.6  |
| constant    | 5.9     | 6.0    | 162.9  | 187.0  | 45.6  | 45.6  | 46.5  | 46.7  |
| constant    | 6.1     | 6.2    | 162.0  | 182.4  | 47.2  | 47.2  | 48.0  | 48.2  |
| constant    | 7.0     | 7.2    | 177.7  | 200.9  | 53.3  | 55.2  | 54.4  | 56.3  |
|=============|=========|========|========|========|=======|=======|=======|=======|



ℹ Request Latency Statistics Table-2 (Completed Requests)
|=============|=========|========|=========|=========|======|======|=======|=======|
| Benchmark   | Request Latency || TTFT             || ITL        || TPOT         ||
| Strategy    | Sec             || ms               || ms         || ms           ||
|             | Mdn     | p95    | Mdn     | p95     | Mdn  | p95  | Mdn   | p95   |
|-------------|---------|--------|---------|---------|------|------|-------|-------|
| synchronous | 3.1     | 5.8    | 94.6    | 2843.1  | 23.5 | 26.2 | 24.4  | 45.5  |
| throughput  | 21.4    | 29.6   | 13575.3 | 21702.9 | 61.4 | 78.2 | 166.9 | 231.1 |
| constant    | 3.1     | 4.1    | 174.4   | 369.7   | 23.4 | 30.2 | 24.6  | 31.6  |
| constant    | 3.1     | 3.4    | 178.2   | 200.9   | 23.3 | 25.4 | 24.6  | 26.8  |
| constant    | 3.5     | 4.1    | 178.6   | 203.1   | 26.1 | 30.9 | 27.2  | 32.2  |
| constant    | 3.6     | 3.9    | 186.1   | 215.7   | 26.8 | 29.5 | 28.1  | 30.7  |
| constant    | 3.9     | 4.3    | 190.8   | 221.7   | 28.9 | 32.4 | 30.2  | 33.8  |
| constant    | 4.0     | 4.6    | 194.6   | 229.0   | 29.7 | 34.9 | 31.0  | 36.3  |
| constant    | 4.3     | 4.8    | 204.1   | 232.5   | 31.9 | 35.6 | 33.3  | 37.2  |
| constant    | 4.4     | 4.9    | 211.3   | 243.1   | 33.2 | 36.7 | 34.7  | 38.1  |
|=============|=========|========|=========|=========|======|======|=======|=======|


ℹ Request Latency Statistics (Completed Requests)
|=============|=========|========|=========|=========|======|======|=======|=======|
| Benchmark   | Request Latency || TTFT             || ITL        || TPOT         ||
| Strategy    | Sec             || ms               || ms         || ms           ||
|             | Mdn     | p95    | Mdn     | p95     | Mdn  | p95  | Mdn   | p95   |
|-------------|---------|--------|---------|---------|------|------|-------|-------|
| synchronous | 3.2     | 5.5    | 139.8   | 2880.0  | 23.7 | 25.6 | 25.3  | 43.1  |
| throughput  | 21.3    | 29.4   | 13422.9 | 21604.7 | 62.0 | 76.2 | 166.3 | 230.0 |
| constant    | 3.4     | 4.0    | 186.4   | 681.8   | 25.4 | 28.8 | 26.7  | 30.9  |
| constant    | 3.2     | 3.8    | 197.4   | 211.4   | 23.6 | 28.3 | 24.9  | 29.6  |
| constant    | 3.5     | 4.1    | 188.0   | 214.2   | 26.3 | 30.7 | 27.7  | 31.7  |
| constant    | 3.8     | 4.1    | 199.5   | 221.8   | 27.9 | 30.5 | 29.3  | 32.0  |
| constant    | 3.8     | 4.6    | 198.5   | 229.0   | 28.8 | 34.4 | 30.0  | 35.6  |
| constant    | 4.1     | 4.8    | 194.0   | 232.7   | 30.9 | 36.1 | 32.2  | 37.3  |
| constant    | 4.2     | 4.8    | 211.3   | 239.8   | 31.4 | 36.0 | 32.8  | 37.2  |
| constant    | 4.4     | 5.1    | 210.3   | 246.8   | 32.8 | 38.5 | 34.1  | 39.7  |
|=============|=========|========|=========|=========|======|======|=======|=======|



ℹ Request Latency Statistics (Completed Requests)
|=============|=========|========|=========|=========|======|======|=======|=======|
| Benchmark   | Request Latency || TTFT             || ITL        || TPOT         ||
| Strategy    | Sec             || ms               || ms         || ms           ||
|             | Mdn     | p95    | Mdn     | p95     | Mdn  | p95  | Mdn   | p95   |
|-------------|---------|--------|---------|---------|------|------|-------|-------|
| synchronous | 4.5     | 7.7    | 90.5    | 3244.0  | 35.1 | 35.1 | 35.5  | 60.1  |
| throughput  | 20.1    | 26.5   | 14042.8 | 20866.1 | 45.8 | 47.7 | 157.0 | 206.8 |
| constant    | 4.8     | 4.8    | 143.6   | 153.1   | 36.9 | 36.9 | 37.7  | 37.8  |
| constant    | 5.0     | 5.0    | 138.5   | 155.6   | 38.2 | 38.2 | 39.0  | 39.1  |
| constant    | 5.1     | 5.1    | 141.2   | 158.2   | 39.2 | 39.2 | 39.9  | 40.1  |
| constant    | 5.2     | 5.3    | 140.6   | 156.1   | 40.1 | 40.1 | 40.9  | 41.0  |
| constant    | 5.4     | 5.5    | 142.7   | 166.9   | 41.7 | 41.7 | 42.5  | 42.7  |
| constant    | 5.6     | 5.6    | 148.7   | 167.9   | 42.9 | 43.1 | 43.8  | 44.0  |
| constant    | 5.8     | 5.8    | 151.5   | 173.1   | 44.3 | 44.4 | 45.1  | 45.3  |
| constant    | 6.0     | 6.0    | 159.2   | 181.3   | 46.0 | 46.0 | 46.8  | 47.0  |
|=============|=========|========|=========|=========|======|======|=======|=======|