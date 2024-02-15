from plyer import notification
import time

if __name__ == '__main__':
    while True:
        # Sending a simple notification
        notification.notify(
            title="Take some rest",
            message="It's time to take a break and relax.",
            app_icon=None,
            timeout=5,
        )
        print("Notification sent.")
        time.sleep(60*15)  # Wait for 15 minutes before sending the next one</

# pythonw  desktop_notifiyer.py  to run in the background
        