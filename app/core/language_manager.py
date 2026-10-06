SUPPORTED_LANGUAGES = {
    "1": "en",
    "2": "ta",
    "3": "hi"
}


MESSAGES = {
    "en": {
        "welcome": "Welcome to Smart Bus Tracking.",
        "ask_source": "Please tell me your current location.",
        "ask_destination": "Please tell me your destination.",
        "location_not_found": "Sorry, I could not recognize that location.",
        "bus_not_found": "Sorry, no suitable bus was found."
    },

    "ta": {
        "welcome": "Smart Bus Tracking-க்கு வரவேற்கிறோம்.",
        "ask_source": "உங்கள் தற்போதைய இடத்தை சொல்லுங்கள்.",
        "ask_destination": "நீங்கள் செல்ல வேண்டிய இடத்தை சொல்லுங்கள்.",
        "location_not_found": "மன்னிக்கவும், அந்த இடத்தை அடையாளம் காண முடியவில்லை.",
        "bus_not_found": "மன்னிக்கவும், பொருத்தமான பேருந்து கிடைக்கவில்லை."
    },

    "hi": {
        "welcome": "Smart Bus Tracking में आपका स्वागत है।",
        "ask_source": "कृपया अपना वर्तमान स्थान बताएं।",
        "ask_destination": "कृपया अपना गंतव्य बताएं।",
        "location_not_found": "क्षमा करें, मैं उस स्थान को पहचान नहीं सका।",
        "bus_not_found": "क्षमा करें, कोई उपयुक्त बस नहीं मिली।"
    }
}


def get_language(choice):
    return SUPPORTED_LANGUAGES.get(choice)


def get_message(language, message_key):
    language_messages = MESSAGES.get(language)

    if language_messages is None:
        return None

    return language_messages.get(message_key)