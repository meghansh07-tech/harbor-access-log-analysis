Analyze the access log located at `/app/access.log` and generate a summary report containing traffic statistics.

### Task Requirements:
1. Parse the entire log file to calculate the total number of requests.
2. Count the total number of unique client IP addresses.
3. Determine the single most frequently requested path (URL).
4. Save the final results to `/app/report.json`.

### Output Format:
The output file must be a valid JSON object containing exactly these three fields:
- `total_requests`: (Integer) The total request count.
- `unique_ips`: (Integer) The unique IP count.
- `top_path`: (String) The most popular path string.
