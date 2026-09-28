import unittest, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from client import RealtimeVoiceLatencyTelemetry

class CoreTests(unittest.TestCase):
    def setUp(self):self.c=RealtimeVoiceLatencyTelemetry()

    def test_percentiles_and_duplicate_transitions(self):
        for tid,end in [('a',650),('b',920)]:
            self.c.record_pipeline_event(tid,'start',0)
            self.c.record_pipeline_event(tid,'end',end)
        report=self.c.generate_sla_diagnostic_report()
        self.assertEqual(report['p50_latency_ms'],650)
        self.assertEqual(report['p90_latency_ms'],920)
        self.assertEqual(report['sla_compliance_rate_percent'],50)
        for stage,ts in [('A',0),('B',10),('A',20),('B',40)]:self.c.record_pipeline_event('c',stage,ts)
        self.assertEqual(self.c.compute_turn_latency_breakdown('c')['stage_breakdown_ms']['A_TO_B'],30)
    def test_empty_and_benchmark(self):
        self.assertEqual(self.c.generate_sla_diagnostic_report()['status'],'NO_DATA')
        self.assertEqual(self.c.run_benchmark_telemetry_profiling()['turn_101_e2e_ms'],650)
