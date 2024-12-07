//for testing git
// does this also get updated??
//acidently added audio_capture system

from plyer import notification

def alert_user(message):
    notification.notify(
        title="Vishing Detection Alert",
        message=message,
        app_name="Vishing Detector",
        timeout=5,
    )
