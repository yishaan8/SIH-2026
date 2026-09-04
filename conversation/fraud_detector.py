import re


def detect_fraud_signals(text: str):

    text = text.lower()

   
    money_keywords = [
        "money", "rupees", "₹", "rs", "transfer",
        "upi", "payment", "send", "account"
    ]

   
    urgency_keywords = [
        "urgent", "urgently", "immediately",
        "emergency", "right now", "asap",
        "abhi", "turant", "jaldi"
    ]


    otp_keywords = [
        "otp", "password", "pin", "cvv",
        "verification code", "passcode"
    ]

    
    secrecy_keywords = [
        "secret", "don't tell", "do not tell",
        "kisi ko mat batana", "kisi ko mat batao"
    ]


    authority_keywords = [
        "boss", "manager", "police",
        "bank officer", "bank manager",
        "government officer", "officer"
    ]

    money_request = any(
        keyword in text for keyword in money_keywords
    )

    urgency_detected = any(
        keyword in text for keyword in urgency_keywords
    )

    otp_request = any(
        keyword in text for keyword in otp_keywords
    )

    secrecy_detected = any(
        keyword in text for keyword in secrecy_keywords
    )

    authority_claim = any(
        keyword in text for keyword in authority_keywords
    )

    impersonation_keywords = [
        "i am your",
        "i'm your",
        "main tumhara",
        "main aapka",
        "this is your"
    ]

    impersonation = any(
        keyword in text for keyword in impersonation_keywords
    ) or authority_claim

    return {
        "moneyRequest": money_request,
        "urgency": "High" if urgency_detected else "Low",
        "otpRequest": otp_request,
        "secrecy": secrecy_detected,
        "impersonation": impersonation,
        "authorityClaim": authority_claim
    }


if __name__ == "__main__":

    sample_text = """
    Hello, I am your brother.
    There is an emergency.
    Please send me 25000 rupees immediately.
    Do not tell anyone about this.
    """

    result = detect_fraud_signals(sample_text)

    print("\n==============================")
    print("Fraud Detection Result")
    print("==============================")

    for key, value in result.items():
        print(f"{key:20}: {value}")

    print("==============================")