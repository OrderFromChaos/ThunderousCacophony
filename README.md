# ThunderousCacophony
### Hear The Weather

[built for UCR Physics Hack Day 2017]

### ------------=--=-=-=-========= Group Members =========-=-=-=--=------------

Peter Bautista (github: pbaut002)

Jesus Negrete (github: jesusneg)

Syris Norelli (github: OrderFromChaos)

Andrew Holman

### -------------=--=-=-=-========= Project Goal =========-=-=-=--=-------------

The goal of this project is to form a sonification library for weather data. Since weather data varies significantly from time to time, it makes sense to map a frequency modulation to the absolute temperature. As such, the presentation example corresponding with this code is built for frequency modulation. Included as well is a general mapping function and a method to modify volume/timbre based on data. We have included a data feeding program plus example weather data from a few different locations.

### ------------=--=-=-=-========= Dependencies =========-=-=-=--=------------

numpy (data pulls/text file reads)

math (helper to applyMapping() and converter for frequency -> MIDI)

midiutil (writing MIDI files)

pygame (playing MIDI files)

matplotlib.pyplot (visualization)

#### [Depreciated]

audiolazy (synethizing string plucking using [Karplus-Strong algorithm](https://en.wikipedia.org/wiki/Karplus%E2%80%93Strong_string_synthesis))

pyaudio (playing sounds from audiolazy

### -----------=--=-=-=-========= Interior Structure =========-=-=-=--=-----------

Data is fed from the text files through WDataPull.py using numpy and some reorganization methods. Unusable data is cut out. WDataPull.py is imported into MainProject.ipynb, which acts as a controller for the lower level functions.

Once this data is formatted correctly, it is fed into Sonification.py. Sonification takes advantage of three primary functions to turn the data into sound:

    applyMapping(data, ranges, equ)

This function takes data from an array with some range, say [1,2,3,4,5] with range 1-5 and maps it into a new range, say 1-3. The final output array would be [1, 1.5 ,2 ,2.5 ,3]. This is especially useful because temperature data is all over the place. Using this, we can map our temperature ranges (which could be negative or in some range like 50-80) to frequency ranges. The frequency ranges that MIDI accepts (according to [this webpage](http://glassarmonica.com/science/frequency_midi.php)) are 27.5-4186 Hz, so this is our new mapping.

Equ is a flag which tells the function whether or not to apply an equation to the data before mapping. This equation is hard-coded in, but can be changed before runtime. The function can be arbitrarily complex.

    toMultiMIDI(data, bpm, filename, n_tracks)

This function accepts data in the format [[1,2,3,4],...]. Each data point in the inner array is put on a different track, and each inner array corresponds to a beat. The beat speed can be controlled by the bpm argument.

n_tracks should later be rewritten to be automatically inferred from len(data[0]) in the future.

    playMIDI(filename)

This is a simple pygame player which plays the MIDI file just made by toMultiMIDI().


### -----------=--=-=-=-========= Program Testing =========-=-=-=--=-----------

Try using the samples() function in Sonification.py, especially samples(2) and samples(4).
