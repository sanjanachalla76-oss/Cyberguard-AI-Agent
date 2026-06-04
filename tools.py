def log_analyzer(log_data):
    failed_count = log_data.lower().count("failed login")

    if failed_count >= 3:
        return "Potential brute-force attack detected."

    return "No suspicious activity detected."


def threat_intelligence(ip):
    malicious_ips = [
        "10.0.0.5",
        "192.168.1.100",
        "172.16.1.50"
    ]

    if ip in malicious_ips:
        return "Threat Score: HIGH | Known malicious IP."

    return "Threat Score: LOW | No threat intelligence found."


def incident_response(alert_type):
    recommendations = {
        "brute force": [
            "Block source IP",
            "Enable MFA",
            "Reset compromised passwords"
        ],

        "malware": [
            "Isolate affected system",
            "Run antivirus scan",
            "Review processes"
        ]
    }

    return recommendations.get(
        alert_type.lower(),
        ["Investigate manually"]
    )