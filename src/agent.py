def analyze_risk(message):

    message = message.lower()

    if "payment" in message or "checkout" in message:
        return {
            "Risk Type": "Product Failure",
            "Risk Level": "High",
            "Probability": "75%",
            "Summary": "Customer complaints suggest a potential payment outage."
        }

    elif "vendor" in message or "shipment" in message:
        return {
            "Risk Type": "Vendor Risk",
            "Risk Level": "Medium",
            "Probability": "60%",
            "Summary": "Repeated vendor delays detected."
        }

    elif "burnout" in message or "overworked" in message:
        return {
            "Risk Type": "Employee Burnout",
            "Risk Level": "Medium",
            "Probability": "55%",
            "Summary": "Employee workload complaints detected."
        }

    else:
        return {
            "Risk Type": "Low Risk",
            "Risk Level": "Low",
            "Probability": "20%",
            "Summary": "No major operational risk detected."
        }


print("ShadowRisk AI Agent")

message = input("Enter enterprise message: ")

result = analyze_risk(message)

print("\nRisk Analysis")

for key, value in result.items():
    print(key + ":", value)
