# genpark-voice-latency

Record supplied voice pipeline timestamps in session memory and calculate latency, bottlenecks and nearest-rank percentiles. No automatic instrumentation.

Python 3.9+; standard library runtime; MIT license.

## Install and run

Download `genpark-voice-latency.mcpb` from [GitHub Releases](https://github.com/Alpha-Park/genpark-realtime-voice-agent-latency-telemetry-skill/releases/tag/v1.0.1) and install with an MCPB-compatible client. Python must be installed and available as `python`.

Alternatively clone this repository and configure an MCP stdio server with command `python` and arguments containing the absolute path to `mcp_server.py`.

[Smithery listing](https://smithery.ai/servers/krispang1020/genpark-voice-latency)

## Tools

- `record_pipeline_event`
- `compute_turn_latency_breakdown`
- `generate_sla_diagnostic_report`
- `run_benchmark_telemetry_profiling`

Run `python -m unittest discover -s tests` for regression checks. The official MCP SDK integration check uses the development dependency `mcp`: `python tests/check_mcp.py`.

## Limitations

These are deterministic helpers operating on supplied structured data, not machine-learning models. Input and output remain in the local process. No hosted endpoint, automatic file access or network access is required. State lasts only for the current process. Benchmark tools run synthetic examples in isolated state; their status is not a production-quality certification.

Explicit timestamps must share a clock and unit (milliseconds); repeated stage-pair durations are summed. Default SLA is 800 ms. No persistence or telemetry collection occurs automatically.
