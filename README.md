a simple pomodoro timer GUI using PySide6's Qt. It prompts the user to set a work session duration in minutes using either a slider or a spinbox, lets the user start and reset the timer, rename the session name and automatically switch between work and break mode, where break mode is activated after the work duration is over, and runs for 5mins. After 5mins, the user can set a new duration or continue the same duration, which is remembered by the JSON file the timer saves to. This also allows the timer to remember how much time was set the last time when closed and reopened.

WIDGETS USED:
QLabel: used for the title and to label if its work mode or break mode
QPushButton: used for start, reset, and rename buttons
QSpinBox: allows the user to enter the work duration in minutes with up/down arrows
QSlider: gives the user another way to adjust the work duration with a mouse in a more intuitive way
QProgressBar: shows the percentage of time passed in the timer
QMessageBox: shows popups when work timer and break timer is up
QInputDialog: allows users to change the name of the session

SIGNALS:
All 3 push buttons (start, reset, and rename) have signals
QSpinBox and QSlider updates each other and saves the time selected to the JSON file
Timeout signal by QTimer.

Other requirements:
Size: 400, 300
Structured with nested layouts.
Styled with Qt Stylesheet.
Persists timer data with JSON.

SCREENSHOTS:

Normal work mode:
<img width="515" height="412" alt="Screenshot 2026-05-31 203047" src="https://github.com/user-attachments/assets/3772ebab-6fa6-47bb-bea7-d8535ec8bda5" />

Work mode ended:
<img width="515" height="401" alt="Screenshot 2026-05-31 203059" src="https://github.com/user-attachments/assets/dda757c7-77bc-4488-be50-45e3d4c9d220" />

Normal break mode:
<img width="528" height="414" alt="Screenshot 2026-05-31 203454" src="https://github.com/user-attachments/assets/2590a882-cd0c-4cf8-8c0b-eab3fbb05927" />

Break mode over:
<img width="534" height="412" alt="Screenshot 2026-05-31 203616" src="https://github.com/user-attachments/assets/3f75a989-823c-43ad-a94f-dde6fe7e26df" />
