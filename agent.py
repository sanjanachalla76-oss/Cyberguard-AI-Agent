from tools import (
    log_analyzer,
    threat_intelligence,
    incident_response
)

print("=" * 50)
print("CyberGuard AI - SOC Analyst Agent")
print("=" * 50)

while True:

    print("\nOptions:")
    print("1. Analyze Logs")
    print("2. Check Threat Intelligence")
    print("3. Incident Response")
    print("4. Exit")

    choice = input("\nSelect Option: ")

    if choice == "1":

        logs = input("\nPaste Logs:\n")

        result = log_analyzer(logs)

        print("\nAnalysis:")
        print(result)

    elif choice == "2":

        ip = input("\nEnter IP Address: ")

        result = threat_intelligence(ip)

        print("\nThreat Intelligence:")
        print(result)

    elif choice == "3":

        incident = input(
            "\nEnter Incident Type (brute force/malware): "
        )

        actions = incident_response(incident)

        print("\nRecommended Actions:")

        for action in actions:
            print(f"- {action}")

    elif choice == "4":

        print("\nExiting CyberGuard AI...")
        break

    else:
        print("\nInvalid Option")