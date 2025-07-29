# threat_detection/model.py

import json
from stix2 import FileSystemSource, Filter

class ThreatDetector:
    """
    Scans telemetry logs (JSONL) for APT/ransomware technique IDs
    based on MITRE CTI intrusion-set 'uses' relationships.
    """
    def __init__(self, cti_path="cti/enterprise-attack"):
        fs = FileSystemSource(cti_path)
        intrusion_sets = fs.query([Filter("type","=","intrusion-set")])
        self.group_map = {i.id: i.name for i in intrusion_sets}
        rels = fs.query([Filter("type","=","relationship")])
        self.mapping = {}
        for r in rels:
            if r.relationship_type == "uses" and r.source_ref in self.group_map:
                self.mapping.setdefault(r.source_ref, []).append(r.target_ref)

    def detect_from_logs(self, log_file):
        detections = []
        for line in log_file:
            entry = json.loads(line)
            tech = entry.get("technique_id")
            ts   = entry.get("timestamp")
            for gid, techniques in self.mapping.items():
                if tech in techniques:
                    detections.append({
                        "timestamp": ts,
                        "group":     self.group_map[gid],
                        "technique_id": tech
                    })
        return detections
