# Chord Recognizer

***

## Install

```
!pip install git+https://github.com/asigalov61/chord_recognizer.git
```

***

## Usage example

```
!wget https://github.com/asigalov61/chord_recognizer/raw/master/test_data/17%20Moments%20of%20Spring.mid

import os
from chord_recognizer import recognize_chords

midi_path = './17 Moments of Spring.mid'

result = recognize_chords(midi_path, note_precision=0.125)
result.to_csv(os.path.splitext(midi_path)[0] + ".csv", index=False)
result
```

***

### Project Los Angeles
### Tegridy Code 2024
