import json
from pathlib import Path

def test_total_requests_criterion():
    """Verifies Task Requirement 1: Parse the entire log file to calculate the total number of requests."""
    report_path = Path("/app/report.json")
    assert report_path.exists(), "no report.json found"
    
    with open(report_path, "r") as f:
        data = json.load(f)
        
    assert "total_requests" in data, "Missing key 'total_requests' in output report"
    assert isinstance(data["total_requests"], int), "'total_requests' must be an integer"
    # Ensure the value matches the mathematically expected ground truth from the log file
    assert data["total_requests"] == 100, f"Expected 100 total requests, got {data['total_requests']}"


def test_unique_ips_criterion():
    """Verifies Task Requirement 2: Count the total number of unique client IP addresses."""
    report_path = Path("/app/report.json")
    assert report_path.exists(), "no report.json found"
    
    with open(report_path, "r") as f:
        data = json.load(f)
        
    assert "unique_ips" in data, "Missing key 'unique_ips' in output report"
    assert isinstance(data["unique_ips"], int), "'unique_ips' must be an integer"
    # Ensure the value matches the mathematically expected ground truth from the log file
    assert data["unique_ips"] == 15, f"Expected 15 unique IPs, got {data['unique_ips']}"


def test_top_path_criterion():
    """Verifies Task Requirement 3: Determine the single most frequently requested path (URL)."""
    report_path = Path("/app/report.json")
    assert report_path.exists(), "no report.json found"
    
    with open(report_path, "r") as f:
        data = json.load(f)
        
    assert "top_path" in data, "Missing key 'top_path' in output report"
    assert isinstance(data["top_path"], str), "'top_path' must be a string"
    # Ensure the value matches the mathematically expected ground truth from the log file
    assert data["top_path"] == "/index.html", f"Expected '/index.html', got {data['top_path']}"


def test_output_file_location_criterion():
    """Verifies Task Requirement 4: Save the final results to /app/report.json as a valid JSON object."""
    report_path = Path("/app/report.json")
    assert report_path.exists(), "The report file was not saved at the mandatory path: /app/report.json"
    
    try:
        with open(report_path, "r") as f:
            json.load(f)
    except json.JSONDecodeError:
        assert False, "/app/report.json is not a valid JSON structure"
