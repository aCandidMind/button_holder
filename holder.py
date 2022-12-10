import mouse
import keyboard
import time

BUTTONS = ['left', 'right']  # valid button names
START_DELAY = 3
KEY = 'Scroll_Lock'


def main():
	button = 'left'# input('Enter right or left: ')

	if button in BUTTONS:
		print('Will start in:')
		for i in range(START_DELAY, 0, -1):  # count START_DELAY seconds and start
			print(i)
			time.sleep(1)
		mouse.press(button=button)  # hold the button

		print('Waiting for %s key in order to stop...' % KEY)
		keyboard.wait(KEY)  # wait for key to be pressed
		mouse.release(button=button)  # stop holding
		print('Done!')
	else:
		print('Not a button...')


if __name__ == "__main__":
	main()
