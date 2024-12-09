# MSDS-436

# Benchmark Study Design
## Objective
Evaluate and compare the performance of seven web frameworks across two programming languages—Go and Python—on throughput and latency when querying a SQLite database.

### Frameworks to Compare: 
Python Django and Go (tbd, probably echo)

### Performance Metrics: 
Throughput and Latency

## Test Set-Up
* Hardware/Server Environment: Use identical specifications for all tests.
* Database: SQLite with the same dataset and schema.
* Request Payload: Use consistent HTTP requests for all frameworks.
* Query Types:
 * Simple Query: Single-table SELECT with a small result set.
 * Complex Query: Multi-table JOIN with aggregation.


## Progress: 
Installed Django and started setting up a project ("myproject"). Verified in settings.py that it's using SQLite. (I did not use a virtual environment or container.)
Started building a model, thought maybe I could incorporate the fortunes the TechEmpower tests use since that seemed like a good way to generate data.
