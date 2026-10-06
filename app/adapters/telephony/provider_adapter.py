from app.adapters.telephony.base import TelephonyProvider


class ProviderAdapter(TelephonyProvider):

    def generate_welcome_message(self, language="en"):
        messages = {
            "en": "Welcome to Smart Bus Tracking. Please select your language.",
            "ta": "Smart Bus Tracking-க்கு வரவேற்கிறோம். உங்கள் மொழியை தேர்வு செய்யுங்கள்.",
            "hi": "Smart Bus Tracking में आपका स्वागत है। कृपया अपनी भाषा चुनें।"
        }

        return {
            "action": "speak",
            "text": messages.get(language, messages["en"])
        }

    def generate_language_menu(self):
        return {
            "action": "menu",
            "options": {
                "1": "English",
                "2": "Tamil",
                "3": "Hindi"
            }
        }

    def generate_location_prompt(self, language="en"):
        messages = {
            "en": "Please tell me your current location.",
            "ta": "உங்கள் தற்போதைய இடத்தை சொல்லுங்கள்.",
            "hi": "कृपया अपना वर्तमान स्थान बताएं।"
        }

        return {
            "action": "speak",
            "text": messages.get(language, messages["en"])
        }

    def generate_destination_prompt(self, language="en"):
        messages = {
            "en": "Please tell me your destination.",
            "ta": "நீங்கள் செல்ல வேண்டிய இடத்தை சொல்லுங்கள்.",
            "hi": "कृपया अपना गंतव्य बताएं।"
        }

        return {
            "action": "speak",
            "text": messages.get(language, messages["en"])
        }

    def generate_bus_response(
        self,
        bus_number,
        eta_minutes,
        language="en"
    ):
        messages = {
            "en": (
                f"Bus number {bus_number} will reach you "
                f"in approximately {eta_minutes} minutes."
            ),

            "ta": (
                f"பேருந்து எண் {bus_number}, "
                f"சுமார் {eta_minutes} நிமிடங்களில் உங்களை வந்தடையும்."
            ),

            "hi": (
                f"बस नंबर {bus_number} लगभग "
                f"{eta_minutes} मिनट में आपके पास पहुंचेगी।"
            )
        }

        return {
            "action": "speak",
            "text": messages.get(language, messages["en"])
        }

    def generate_error_response(
        self,
        message,
        language="en"
    ):
        return {
            "action": "speak",
            "text": message
        }