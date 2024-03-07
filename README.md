# Chord Recognizer

***

## Install

```
!pip install git+https://github.com/asigalov61/chord_recognizer.git
```

***

## Usage example

```
import os
from chord_recognizer import recognize_chords

midi_path = '/usr/local/lib/python3.10/dist-packages/chord_recognizer/17 Moments of Spring.mid'

result = recognize_chords(midi_path, note_precision=0.125)
result.to_csv(os.path.splitext(midi_path)[0] + ".csv", index=False)
result
```

***

### Project Los Angeles
### Tegridy Code 2024
