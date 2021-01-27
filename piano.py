from tkinter import Tk, Frame, BOTH, Label, PhotoImage
import simpleaudio as sa
import time as t
import _thread
from _thread import start_new_thread
import sys
sys.path.insert(1, '/Users/keith/Desktop/Ear Training')
import metronome

recordedNotes = []
keyboardPromptTime = 20
metronomeTimeStamps = []
start = t.time()
recording = True

class CancellationToken:
   def __init__(self):
       self.is_cancelled = False

   def cancel(self):
       self.is_cancelled = True

def on_closing(root):
   if t.time() - start > 0:
       global cancellationToken
       cancellationToken.cancel()
       root.destroy()

cancellationToken = CancellationToken()

def label_pressed(event):
    if len(event.widget.name) == 2:
        img = 'pictures/white_key_pressed.gif'
    elif len(event.widget.name) == 3:
        img = 'pictures/black_key_pressed.gif'
    elif event.widget.name == 'red_button':
        img = 'pictures/red_button_pressed.gif'
    else:
        img = 'pictures/green_button_pressed.gif'
    key_img = PhotoImage(file=img)
    event.widget.configure(image=key_img)
    event.widget.image = key_img

def label_released(event):
    if len(event.widget.name) == 2:
        img = 'pictures/white_key.gif'
    elif len(event.widget.name) == 3:
        img = 'pictures/black_key.gif'
    elif event.widget.name == 'red_button':
        img = 'pictures/red_button.gif'
    else:
        img = 'pictures/green_button.gif'
    key_img = PhotoImage(file=img)
    event.widget.configure(image=key_img)
    event.widget.image = key_img

def record_on_off(event):
    global recording
    recording = not recording
    if recording:
        label_pressed(event)
    else:
        label_released(event)


def record(note):
    end = t.time()
    time = end - start
    recordedNotes.append((note, time))

def find_label(name, array):
    for x in range(len(array)):
        # checks against the name component in keys
        if name == array[x][1]:
            # returns the Label component in keys
            return array[x][2]


def key_pressed(event):
    # This is so that if a key that is not in KEYS_TO_NOTES
    # is pressed, it will not return an error.
    note = KEYS_TO_NOTES.get(event.char, None)
    if note:
        wave_obj = sa.WaveObject.from_wave_file('sounds/' + note + '.wav')
        wave_obj.play()
        if recording:
            record(note)
        if len(note) == 2:
            img = 'pictures/white_key_pressed.gif'
        else:
            img = 'pictures/black_key_pressed.gif'
        key_img = PhotoImage(file=img)
        find_label(note, event.widget.keys).configure(image=key_img)
        find_label(note, event.widget.keys).image = key_img


def key_released(event):
    note = KEYS_TO_NOTES.get(event.char, None)
    if note:
        if len(note) == 2:
            img = 'pictures/white_key.gif'
        else:
            img = 'pictures/black_key.gif'
        key_img = PhotoImage(file=img)
        find_label(note, event.widget.keys).configure(image=key_img)
        find_label(note, event.widget.keys).image = key_img


def button_pressed(event):
    wave_obj = sa.WaveObject.from_wave_file('sounds/' + event.widget.name + '.wav')
    wave_obj.play()
    if recording:
        record(event.widget.name)
    label_pressed(event)

def deepCopyNotesAndMetronomeLists():
    global recordedNotes
    global metronomeTimeStamps
    recNotes = recordedNotes.copy()
    metroStamps = metronomeTimeStamps.copy()
    recordedNotes = []
    metronomeTimeStamps = []
    return recNotes, metroStamps

KEYS_TO_NOTES = {
    'z': 'C1',
    'x': 'D1',
    'c': 'E1',
    'v': 'F1',
    'b': 'G1',
    'n': 'A1',
    'm': 'B1',
    's': 'C#1',
    'd': 'D#1',
    'g': 'F#1',
    'h': 'G#1',
    'j': 'A#1',
    'Z': 'C2',
    'X': 'D2',
    'C': 'E2',
    'V': 'F2',
    'B': 'G2',
    'N': 'A2',
    'M': 'B2',
    'S': 'C#2',
    'D': 'D#2',
    'G': 'F#2',
    'H': 'G#2',
    'J': 'A#2',
}


class Piano(Frame):

    def __init__(self, parent):

        Frame.__init__(self, parent, background='SkyBlue3')

        start_new_thread(metronome.executeMetronome, (metronomeTimeStamps, cancellationToken, keyboardPromptTime))

        self.parent = parent

        self.init_user_interface()

    def init_user_interface(self):

        keys = [
            [0, 'C1'],
            [35, 'C#1'],
            [50, 'D1'],
            [85, 'D#1'],
            [100, 'E1'],
            [150, 'F1'],
            [185, 'F#1'],
            [200, 'G1'],
            [235, 'G#1'],
            [250, 'A1'],
            [285, 'A#1'],
            [300, 'B1'],
            [350, 'C2'],
            [385, 'C#2'],
            [400, 'D2'],
            [435, 'D#2'],
            [450, 'E2'],
            [500, 'F2'],
            [535, 'F#2'],
            [550, 'G2'],
            [585, 'G#2'],
            [600, 'A2'],
            [635, 'A#2'],
            [650, 'B2']
        ]

        for key in keys:
            if len(key[1]) == 2:
                img = 'pictures/white_key.gif'
                key.append(self.create_key(img, key))

        for key in keys:
            if len(key[1]) > 2:
                img = 'pictures/black_key.gif'
                key.append(self.create_key(img, key))


        self.parent.title('The Piano')

        w = 700
        h = 200
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.parent.keys = keys
        self.parent.bind('<KeyPress>', key_pressed)
        self.parent.bind('<KeyRelease>', key_released)


        self.pack(fill=BOTH, expand=1)

    def create_key(self, img, key):
        key_image = PhotoImage(file=img)
        label = Label(self, image=key_image, bd=0)
        label.image = key_image
        label.place(x=key[0], y=0)
        label.name = key[1]
        label.bind('<Button-1>', button_pressed)
        label.bind('<ButtonRelease-1>', label_released)
        return label

def main(pianoPromptTime):
    global keyboardPromptTime
    keyboardPromptTime = int(pianoPromptTime / 1000)
    root = Tk()
    app = Piano(root)
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))
    #root.after(pianoPromptTime, lambda: root.destroy())
    app.mainloop()
    return deepCopyNotesAndMetronomeLists()

if __name__ == "__main__":
    main(5000)

