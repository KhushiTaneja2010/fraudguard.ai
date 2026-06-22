import re
import random
import time

# ===================== SCAM INTELLIGENCE ENGINE =====================

SCAM_KEYWORDS = {
    "otp": "OTP Fraud",
    "upi": "UPI Fraud",
    "account blocked": "Account Scam",
    "kyc": "KYC Scam",
    "rbi": "Govt Scam",
    "refund": "Refund Scam",
    "arrest": "Digital Arrest Scam",
    "urgent": "Urgency Scam",
    "immediately": "Pressure Scam",
    "click": "Phishing Attempt",
    "win": "Prize Scam",
    "lottery": "Lottery Scam",
    "bank": "Bank Scam",
    "password": "Credential Theft",
    "verify": "Verification Scam"
}

SCAM_TEMPLATES = [
    "package could not be delivered",
    "update your details",
    "suspicious activity detected",
    "final notice",
    "legal action",
    "your account will be blocked",
    "verify your identity",
    "click the link below",
    "you have won",
    "claim your reward",
    "urgent action required",
    "rbi wants you to transfer money",
]

# ===================== CORE ANALYSIS =====================

def analyze(text):
    text = text.lower()

    score = 0
    detected = []

    # keyword scoring
    for k, v in SCAM_KEYWORDS.items():
        if k in text:
            score += 12
            detected.append(v)

    # template scoring
    for t in SCAM_TEMPLATES:
        if t in text:
            score += 20
            detected.append("Template Match: " + t)

    # heuristic rules
    if re.search(r"http|www|bit\.ly", text):
        score += 25
        detected.append("Suspicious Link Detected")

    if "urgent" in text and "account" in text:
        score += 25

    if "rbi" in text and "transfer" in text:
        score += 30

    score = min(score, 100)

    if score >= 70:
        status = "🔴 HIGH RISK"
    elif score >= 40:
        status = "🟠 SUSPICIOUS"
    else:
        status = "🟢 SAFE"

    return score, status, detected


import random
import time

def animated_heatmap(frames=5):

    cities = ["Delhi", "Mumbai", "Bengaluru", "Chennai", "Kolkata"]

    for frame in range(frames):

        print("\n" + "="*60)
        print(f"🌐 FRAUD HEATMAP FRAME {frame+1}")
        print("="*60)

        for city in cities:
            risk = random.randint(10, 100)

            if risk > 75:
                bar = "██████████"
                level = "🔴 CRITICAL"
            elif risk > 50:
                bar = "███████░░░"
                level = "🟠 HIGH"
            elif risk > 30:
                bar = "████░░░░░░"
                level = "🟡 MEDIUM"
            else:
                bar = "██░░░░░░░░"
                level = "🟢 LOW"

            print(f"{city:10} | {bar} | {risk}/100 {level}")

        print("\nUpdating intelligence layer...\n")
        time.sleep(1)

        print("\nUpdating national fraud intelligence layer...")
        time.sleep(1.2)

    print("\n✅ Heatmap stabilized. Intelligence cycle complete.\n")


# ===================== MAIN SYSTEM =====================

print("\n🛡️ FRAUDGUARD AI - DIGITAL PUBLIC SAFETY SYSTEM")
print("Type 'heatmap' for geospatial simulation")
print("Type 'exit' to stop\n")

while True:
    msg = input("Enter message: ")

    if msg.lower() == "exit":
        break

    if msg.lower() == "heatmap":
        animated_heatmap(6)
        continue

    print("\nAnalyzing...\n")

    score, status, detected = analyze(msg)

    print("===== FRAUD REPORT =====")
    print(f"Risk Score: {score}/100")
    print(f"Status: {status}")
    print("\nDetected Patterns:")

    if detected:
        for d in detected:
            print("-", d)
    else:
        print("- No strong scam indicators")

    print("\nAI Reasoning:")
    print("Hybrid system using keyword + template + heuristic detection")

    print("\nGeolocation Layer:")
    print("India Cyber Grid (simulated intelligence layer)")

    print("\n========================\n")