# main.py

from login import login_user
from Scan_Results import display_result
from History import add_history, view_history
from Text_To_Speech import speak

# STEP 1: Login
success, message = login_user("G123", "pass123")
print(message)

if success:
    # STEP 2: Simulate scan
    asset = {"student": "S001", "type": "Laptop"}
    student_id = "S001"

    # STEP 3: Get result
    result = display_result(asset, student_id)

    # STEP 4: Save history
    record = {
        "student": student_id,
        "result": result
    }
    add_history(record)

    # STEP 5: Output
    print("Scan Result:", result)

    # STEP 6: Speak result
    speak(result)

    # STEP 7: Show history
    print("History:", view_history())
