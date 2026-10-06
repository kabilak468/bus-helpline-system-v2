def calculate_eta(distance_km, speed_kmph):
    if speed_kmph <= 0:
        return None

    eta_hours = distance_km / speed_kmph
    eta_minutes = eta_hours * 60

    return round(eta_minutes)