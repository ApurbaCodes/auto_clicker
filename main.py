
import pyautogui
import time


class Clicker:
    def __init__(self):
        self.running = True
    def starter(self):
        start=pyautogui.confirm(text="Auto Clicker Started. Please set the cursor position within 5 sec.",
                                  title="Auto Clicker",
                                   buttons=['Continue','Cancle'] )
        return start =="Continue"


    def get_cursor_position(self):
        time.sleep(5)
        cursor_x, cursor_y = pyautogui.position()
        print(f"Cursor Position: ({cursor_x}, {cursor_y})")
        return cursor_x, cursor_y

    def confirm_cursor_position(self, cursor_x, cursor_y):
        cursor_position_correct = pyautogui.confirm(text=f"Cursor Position is: ({cursor_x}, {cursor_y})\n\n If cursor position is correct click Yes and continue",
                                                     title='Cursor Position Confirmation',
                                                       buttons=['Yes', 'No'])
        return cursor_position_correct=="Yes"

    def click_at_position(self, cursor_x, cursor_y, num_clicks):
        for i in range(num_clicks):
            pyautogui.click(cursor_x, cursor_y)
            time.sleep(2)

    def run(self):
            while self.running:
                if  not self.starter():
                    break
                cursor_x, cursor_y = self.get_cursor_position()
                if self.confirm_cursor_position(cursor_x, cursor_y):
                    while True:
                        try:
                            num_clicks=int(pyautogui.prompt(text="Please enter how many times you want to click.\n\n ",
                                        title="Number Click",
                                        default=1))
                        except:
                            break
                        self.click_at_position(cursor_x, cursor_y, num_clicks)
                        user_choice =pyautogui.confirm(text=f"{num_clicks} clicks completed.\n\n  Do you want to continue?(Y/N)",
                                                        title='Want To Continue',
                                                        buttons=['Yes', 'No'])
                        if user_choice=="Yes":
                            continue
                        else:
                            print("See you!!")
                            self.running = False
                            exit()

if __name__ == "__main__":
    clicker = Clicker()
    clicker.run()
