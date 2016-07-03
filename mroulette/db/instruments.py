# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from mroulette.types import (
    aumf, aumu, kontakt, reaktor, logic, live, uvi, product,
)
from mroulette.tags import t, tags

#: ---------------------------- INSTRUMENTS
INST = {
    # -8dio-
    product('8dio', 'Mini', kontakt, tags(
        t.DRUMS, t.KONTAKT, t.ACOUSTIC, 'impulses',
    )),

    # -AAS-
    product('AAS', 'Chromaphone 2', aumu('AAS ', 'TBBV'), tags(
        t.SYNTH, t.PHYSMOD, t.MALLET, t.STRINGS, t.BELL,
    )),

    # -Ableton-
    product('Ableton', 'Sampler', live, tags(
        t.SAMPLER,
    )),
    product('Ableton', 'Operator', live, tags(
        t.SYNTH, t.FM,
    )),
    product('Ableton', 'Tension', live, tags(
        t.SYNTH, t.PHYSMOD, t.PLUCKED, t.STRINGS,
    )),
    product('Ableton', 'Analog', live, tags(
        t.SYNTH, t.ANALOG, t.SUBTRACTIVE,
    )),
    product('Ableton', t.ELECTRIC, live, tags(
        t.SYNTH, t.KEYS,
    )),
    product('Ableton', 'Collision', live, tags(
        t.SYNTH, t.PHYSMOD, t.PERC, t.MALLET,
    )),

    # -Acousticsamples-
    product('Acousticsamples', 'Bassysm-F', uvi, tags(
        t.BASS, t.ACOUSTIC,
    )),
    product('Acousticsamples', 'Bassysm-J', uvi, tags(
        t.BASS, t.ACOUSTIC,
    )),
    product('Acousticsamples', 'Bassysm-M', uvi, tags(
        t.BASS, t.ACOUSTIC,
    )),
    product('Acousticsamples', 'Bassysm-S', uvi, tags(
        t.BASS, t.ACOUSTIC,
    )),
    product('Acousticsamples', 'J-Bass', uvi, tags(
        t.BASS, t.ACOUSTIC,
    )),
    product('Acousticsamples', 'TheUpright', uvi, tags(
        t.BASS, t.ACOUSTIC, t.DOUBLEBASS,
    )),
    product('Acousticsamples', 'GD-6', uvi, tags(
        t.GUITAR, t.ACOUSTIC, t.PLUCKED,
    )),
    product('Acousticsamples', 'Sunbird', uvi, tags(
        t.GUITAR, t.ACOUSTIC, t.PLUCKED,
    )),
    product('Acousticsamples', 'Telematic', uvi, tags(
        t.GUITAR, t.ACOUSTIC, t.PLUCKED, 'telecaster',
    )),
    product('Acousticsamples', 'F Grand 278', uvi, tags(
        t.PIANO, 'grand', t.ACOUSTIC, t.SOLD,
    )),
    product('Acousticsamples', 'Mark 79', uvi, tags(
        t.ORGAN, t.ELECTRIC, t.SOLD,
    )),
    product('Acousticsamples', 'Percussiv', uvi, tags(
        t.DRUMS, t.PERC, t.ACOUSTIC, t.SOLD,
    )),
    product('Acousticsamples', 'UKU', uvi, tags(
        t.UKULELE, t.ACOUSTIC, t.PLUCKED,
    )),

    # -Admiral Quality-
    product('Admiral Quality', 'Poly-Ana', aumu('AdmQ', 'AQI2'), tags(
        t.SUBTRACTIVE, t.DIGITAL, t.ANALOG,
    )),

    # -Air Music Tech-
    product('Air', 'Loom', aumu('Wzoo', 'Loom'), tags(
        t.ADDITIVE, t.DIGITAL,
    )),
    product('Air', 'Vacuum Pro', aumu('Wzoo', 'VacP'), tags(
        t.SUBTRACTIVE, t.ANALOG,
    )),
    product('Air', 'Hybrid', aumu('Wzoo', 'Thun'), tags(
        t.WAVETABLE, t.DIGITAL,
    )),
    product('Air', 'Strike', aumu('Wzoo', 'UVD1'), tags(
        t.DRUMS, t.SAMPLER,
    )),
    product('Air', 'Structure', aumu('Wzoo', 'DSpl'), tags(
        t.SAMPLER,
    )),
    product('Air', 'Velvet', aumu('Wzoo', 'StgP'), tags(
        t.KEYS,
    )),
    product('Air', 'theRiser', aumu('Wzoo', 'tRsr'), tags(
        t.FX, t.SPECIAL,
    )),
    product('Air', 'Transfuser', aumu('Wzoo', 'Trfr'), tags(
        'loop', t.SAMPLER,
    )),
    product('Air', 'Xpand!2', aumu('Wzoo', 'WSL1'), tags(
        t.ROMPLER,
    )),

    # -AlyJamesLab-
    product('AlyJamesLab', 'VLINN 2.0', aumu('AlyJ', 'VLn2'), tags(
        t.DRUMS, t.SYNTH, t.DIGITAL, 'linndrum',
    )),

    # -Amazing Noises-
    product('Amazing Noises', 'Dark Synth', live, tags(
        t.SPECIAL, t.ADDITIVE, t.CREATIVE, t.ABLETON, t.M4L,
    )),
    product('Amazing Noises', 'Density', live, tags(
        t.GRAIN, t.SPECIAL, t.CREATIVE, t.SAMPLER, t.ABLETON, t.M4L,
    )),
    product('Amazing Noises', 'Pulsaret', live, tags(
        t.GRAIN, t.ADDITIVE, t.SPECIAL, t.CREATIVE, t.ABLETON, t.M4L,
    )),
    product('Amazing Noises', 'Pulsor', live, tags(
        t.SPECIAL, t.SUBTRACTIVE, t.CREATIVE, t.ABLETON, t.M4L,
    )),

    # -Analogue Drums-
    product('Analogue Drums', 'Boxer', kontakt, tags(
        t.DRUMS, t.KONTAKT, t.ACOUSTIC,
    )),
    product('Analogue Drums', 'FatStacks', kontakt, tags(
        t.DRUMS, t.KONTAKT, t.ACOUSTIC,
    )),
    product('Analogue Drums', 'Kingpin', kontakt, tags(
        t.DRUMS, t.KONTAKT, t.ACOUSTIC,
    )),
    product('Analogue Drums', 'Monotown', kontakt, tags(
        t.DRUMS, t.KONTAKT, t.ACOUSTIC,
    )),
    product('Analogue Drums', 'Pizazz', kontakt, tags(
        t.DRUMS, t.KONTAKT, t.ACOUSTIC,
    )),
    product('Analogue Drums', 'Royale', kontakt, tags(
        t.DRUMS, t.KONTAKT, t.ACOUSTIC,
    )),
    product('Analogue Drums', 'Smoker', kontakt, tags(
        t.DRUMS, t.KONTAKT, t.ACOUSTIC,
    )),

    # -Apple Logic Pro X-
    product('Apple', 'Ultrabeat', logic, tags(
        t.LOGIC, t.DRUMS, t.SYNTH, t.LOGIC_INST,
    )),
    product('Apple', 'Sculpture', logic, tags(
        t.LOGIC, t.PHYSMOD, t.SYNTH, t.LOGIC_INST,
    )),
    product('Apple', 'EVOC 20 PS', logic, tags(
        t.LOGIC, t.VOCODER, t.DIGITAL, t.LOGIC_INST,
    )),
    product('apple', 'EFM1', logic, tags(
        t.LOGIC, t.FM, t.DIGITAL, t.SYNTH, t.LOGIC_INST,
    )),
    product('apple', 'ES M', logic, tags(
        t.LOGIC, t.SUBTRACTIVE, t.MONO, t.DIGITAL, t.SYNTH, t.LOGIC_INST,
    )),
    product('apple', 'ES P', logic, tags(
        t.LOGIC, t.SUBTRACTIVE, t.DIGITAL, t.SYNTH, t.LOGIC_INST,
    )),
    product('apple', 'ES1', logic, tags(
        t.LOGIC, t.SUBTRACTIVE, t.DIGITAL, t.SYNTH, t.LOGIC_INST,
    )),
    product('apple', 'ES2', logic, tags(
        t.LOGIC, t.SUBTRACTIVE, t.DIGITAL, t.SYNTH, t.LOGIC_INST,
    )),

    # -Aria Sounds-
    product('Aria Sounds', 'London Symphonic Strings', kontakt, tags(
        t.STRINGS, t.KONTAKT, t.ACOUSTIC, t.VIOLIN, t.BOWED,
    )),

    # -Arturia-
    product('Arturia', 'Analog Lab', aumu('Artu', 'ALab'), tags(
        t.ANALOG,
    )),
    product('Arturia', 'ARP 2600 V2', aumu('Artu', 'arpW'), tags(
        t.ANALOG, t.SUBTRACTIVE, t.SOLD,
    )),
    product('Arturia', 'CS-80 V2', aumu('ArTu', 'Cs82'), tags(
        t.ANALOG, t.SUBTRACTIVE, t.SOLD,
    )),
    product('Arturia', 'Jupiter-8 V2', aumu('Artu', 'Ju82'), tags(
        t.ANALOG, t.SUBTRACTIVE, t.SOLD,
    )),
    product('Arturia', 'Matrix-12 V', aumu('Artu', 'Matr'), tags(
        t.ANALOG, t.SUBTRACTIVE, t.SOLD,
    )),

    product('Arturia', 'Mini V', aumu('Artu', 'mini'), tags(
        t.ANALOG, t.SUBTRACTIVE, t.SOLD,
    )),
    product('Arturia', 'Modular V', aumu('Artu', 'mmv2'), tags(
        t.ANALOG, t.MODULAR, t.SOLD,
    )),
    product('Arturia', 'Oberheim SEM V', aumu('Artu', 'ObsV'), tags(
        t.ANALOG, t.SUBTRACTIVE, t.SOLD,
    )),
    product('Arturia', 'Prophet V2', aumu('Artu', 'P5V2'), tags(
        t.ANALOG, t.SUBTRACTIVE, t.SOLD,
    )),
    product('Arturia', 'Solina V', aumu('Artu', 'Soli'), tags(
        'organ', t.ANALOG, t.SOLD,
    )),
    product('Arturia', 'Spark', aumu('Artu', 'ArDS'), tags(
        t.DRUMS, t.ELECTRONIC, t.SOLD,
    )),
    product('Arturia', 'Spark Dubstep', aumu('Artu', 'ArDD'), tags(
        t.DRUMS, t.ELECTRONIC, t.SOLD,
    )),
    product('Arturia', 'Spark Vintage', aumu('Artu', 'ArDV'), tags(
        t.DRUMS, t.ELECTRONIC, t.SOLD,
    )),
    product('Arturia', 'Vox V', aumu('Artu', 'VoxA'), tags(
        'organ', t.ANALOG, t.SOLD,
    )),
    product('Arturia', 'Wurlitzer V', aumu('Artu', 'WurV'), tags(
        t.KEYS, t.ANALOG, t.SOLD,
    )),

    # -Atom Hub-
    product('Atom Hub', 'A day in the park', kontakt, tags(
        t.KONTAKT, t.DRUMS, t.ACOUSTIC,
    )),
    product('Atom Hub', 'Drunkeytar', kontakt, tags(
        t.KONTAKT, t.GUITAR, t.ACOUSTIC, t.PLUCKED,
    )),
    product('Atom Hub', 'Harmogeddon', kontakt, tags(
        t.KONTAKT, t.HARMONICA, t.ACOUSTIC,
    )),
    product('Atom Hub', 'Old Mandolin v2', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC,
    )),
    product('Atom Hub', 'Bell from Shelf v2', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC,
    )),
    product('Atom Hub', 'Toolshed', kontakt, tags(
        t.KONTAKT, t.DRUMS, t.ACOUSTIC,
    )),

    # -Audio Damage-
    product('Audio Damage', 'Basic', aumu('AuDa', 'ADba'), tags(
        t.SYNTH, t.SUBTRACTIVE,
    )),
    product('Audio Damage', 'Phosphor', aumu('AuDa', 'ADph'), tags(
        t.SYNTH, t.ADDITIVE,
    )),
    product('Audio Damage', 'Tattoo', aumu('AuDa', 'Tatt'), tags(
        t.DRUMS, t.SYNTH, t.SOLD,
    )),

    # -Audio Realism-
    product('Audio Realism', 'ABL2x', aumu('AuRe', 'abl3'), tags(
        t.SYNTH, t.SUBTRACTIVE, '303', t.SOLD,
    )),
    product('Audio Realism', 'ADMx', aumu('AuRe', 'aadm'), tags(
        t.DRUMS, t.SYNTH, '606', '808', '909',
    )),
    product('Audio Realism', 'ReDominator', aumu('AuRe', 'ReDo'), tags(
        t.SYNTH, t.SUBTRACTIVE, 'juno',
    )),

    # -Audiothing-
    product('Audiothing', 'Organetta', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC,
    )),
    product('Audiothing', 'miniBit', aumu('AdTg', 'mIbt'), tags(
        t.SYNTH, t.CHIP, t.SUBTRACTIVE,
    )),

    # -Audiowarp-
    product('Audiowarp', 'BOCS3', kontakt, tags(
        t.SYNTH, 'lofi', 'tape',
    )),

    # -Beepstreet-
    product('Beepstreet', 'Sunrizer', aumu('BSTR', 'SNRZ'), tags(
        t.SYNTH, t.SUBTRACTIVE,
    )),

    # -Bolder Sounds-
    product('Bolder Sounds', 'Harmoniums of the Opera', kontakt, tags(
        t.HARMONIUM, t.KONTAKT, t.ACOUSTIC,
    )),

    # -Camel Audio-
    product('Camel Audio', 'Alchemy', aumu('CamA', 'CaC2'), tags(
        t.SYNTH, t.GRAIN, t.ADDITIVE, t.SUBTRACTIVE,
    )),

    # -Drumdrops-
    product('Drumdrops', '1970s Rogers Dub Kit', kontakt, tags(
        t.DRUMS, t.KONTAKT, t.ACOUSTIC,
    )),
    product('Drumdrops', 'Ludwig Super Classic Kit', kontakt, tags(
        t.DRUMS, t.KONTAKT, t.ACOUSTIC,
    )),
    product('Drumdrops', 'Gretsch Soul Kit', kontakt, tags(
        t.DRUMS, t.KONTAKT, t.ACOUSTIC,
    )),

    # -Elektron-
    product('Elektron', 'Analog Keys', aumu('ELEK', 'ELAK'), tags(
        t.EDITOR, t.SYNTH, t.ANALOG,
    )),
    product('Elektron', 'Analog Rytm', aumu('ELEK', 'ELAR'), tags(
        t.EDITOR, t.DRUMS, t.SYNTH, t.ANALOG, t.SAMPLER,
    )),

    # -Expert Sleepers-
    product(
        'Expert Sleepers', 'Crossfade Loop Synth',
        aumu('ExSl', 'XFls'),
        tags(t.CREATIVE, t.SAMPLER, t.SPECIAL, 'mfx'),
    ),
    product('Expert Sleepers', 'Minky Starshine', aumu('ExSl', 'MiSt'), tags(
        t.SYNTH, t.DIGITAL, t.ADDITIVE,
    )),

    # -Facets of Sound-
    product('Facets of Sound', 'LOVELY Drumkit', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC, t.DRUMS,
    )),

    # -Fairly Confusing-
    product('Fairly Confusing', 'Alimchord PE', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC,
    )),

    # -Fluffy Audio-
    product('Fluffy Audio', 'Simple Flute', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC, t.FLUTE, t.FREE,
    )),

    # -FXpansion-
    product('FXpansion', 'Amber', aumu('FXPN', 'AMBR'), tags(
        t.ANALOG, t.STRINGS, t.ENSEMBLE,
    )),
    product('FXpansion', 'Cypher', aumu('FXPN', 'CYPH'), tags(
        t.ANALOG, t.FM,
    )),
    product('FXpansion', 'Geist', aumu('FXPN', 'FXGR'), tags(
        t.DRUMS, t.SAMPLER, 'loop', 'rex',
    )),
    product('FXpansion', 'Strobe', aumu('FXPN', 'STRO'), tags(
        t.ANALOG, t.SUBTRACTIVE, t.MONO, t.POLY,
    )),
    product('FXpansion', 'Tremor', aumu('FXPN', 'FXBS'), tags(
        t.DRUMS, t.SYNTH,
    )),

    # -GForce-
    product('GForce', 'impOSCar2', aumu('VST ', 'imp2'), tags(
        t.SYNTH, t.VA, 'OSCar',
    )),


    # -Goldbaby-
    product('Goldbaby', 'SP1200 Vol.2', kontakt, tags(
        t.DRUMS, t.SAMPLED, 'SP1200', t.KONTAKT, t.BATTERY, t.GEIST,
    )),
    product('Goldbaby', 'Urban Cookbook Vol.3', kontakt, tags(
        t.DRUMS, t.SAMPLED, t.KONTAKT, t.BATTERY, t.GEIST,
    )),

    # -IRCAM-
    product('IRCAM', 'IM-SuperVPSynth', live, tags(
        t.SPECIAL, t.CREATIVE, t.SAMPLER, 'stretch', 'IRCAM',
        t.ABLETON, t.M4L, 'latency',
    )),

    # -iZotope-
    product('iZotope', 'IRIS 2', aumu('iZtp', 'Zir2'), tags(
        t.SYNTH, t.SPECTRAL, t.SAMPLER,
    )),

    # -Klevgränd Produktion-
    product('Klevgränd Produktion', 'Enkl', aumu('Klev', 'Enkl'), tags(
        t.SYNTH, t.MONO,
    )),

    # -Korg-
    product('Korg', 'M1', aumu('KORG', 'KLM1'), tags(
        t.SYNTH, t.DIGITAL, t.SOLD,
    )),
    product('Korg', 'Mono-poly', aumu('KORG', 'KLMP'), tags(
        t.ANALOG, t.SUBTRACTIVE, t.SOLD,
    )),
    product('Korg', 'MS-20', aumu('KORG', 'KLMV'), tags(
        t.ANALOG, t.SUBTRACTIVE, t.SOLD,
    )),
    product('Korg', 'Polysix', aumu('KORG', 'KLPV'), tags(
        t.ANALOG, t.SUBTRACTIVE, t.SOLD,
    )),
    product('Korg', 'Wavestation', aumu('KORG', 'KLWV'), tags(
        t.DIGITAL, t.SYNTH, t.WAVETABLE, t.SOLD,
    )),

    # -Loops De La Creme-
    product('Loops De La Creme', 'Bell Empire', kontakt, tags(
        'bell', t.ACOUSTIC, t.SYNTH,
    )),
    product('Loops De La Creme', 'Booga Rocket Drums', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC, t.DRUMS,
    )),
    product('Loops De La Creme', 'Cymbal Rolls', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC, t.DRUMS,
    )),
    product('Loops De La Creme', 'Organic Transitions', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC, t.PERC,
    )),

    # -Lux/Nox-
    product('Lux/Nox', 'PERC+', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC, t.DRUMS,
    )),

    # -Madrona Labs-
    product('Madrona Labs', 'AAlto', aumu('MLbs', 'Aalt'), tags(
        t.ANALOG, t.MONO, t.POLY, t.SUBTRACTIVE,
    )),
    product('Madrona Labs', 'Kaivo', aumu('MLbs', 'Kaiv'), tags(
        t.GRAIN, t.PHYSMOD,
    )),

    # -Max for Cats-
    product('Max for Cats', t.DIGITAL, live, tags(
        t.DIGITAL, t.SYNTH, t.ADDITIVE, t.ABLETON, t.M4L,
    )),
    product('Max for Cats', 'Oscillot', live, tags(
        t.MODULAR, t.SYNTH, t.ABLETON, t.M4L,
    )),

    # -Modartt-
    product('Modartt', 'Pianoteq 5 PRO', aumu('Mdrt', 'Pt5q'), tags(
        t.PIANO, t.ACOUSTIC, t.PHYSMOD, t.KEYS, 'chromatic', 'microtonal',
    )),

    # -Modwheel-
    product('Modwheel', 'Angklung', kontakt, tags(
        t.KONTAKT, t.PERC, t.ACOUSTIC,
    )),
    product('Modwheel', 'Biscuit Tin Guitar', kontakt, tags(
        t.KONTAKT, t.GUITAR, t.ACOUSTIC, t.PLUCKED,
    )),
    product('Modwheel', 'Hum Drum', kontakt, tags(
        t.KONTAKT, t.DRUMS, t.ACOUSTIC, t.PERC,
    )),
    product('Modwheel', 'The Bends', kontakt, tags(
        t.PERC, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Modwheel', 'The Lowdown', kontakt, tags(
        t.BASS, t.STRINGS, t.BOWED, t.ACOUSTIC, t.KONTAKT, t.DOUBLEBASS,
        t.PLUCKED, t.BOWED,
    )),

    # -MOTU-
    product('MOTU', 'MachFive3', aumu('MOTU', 'MCH3'), tags(
        t.SAMPLER, t.GRAIN, 'stretch', 'IRCAM', t.SOLD,
    )),

    # -Native Instruments-
    product('Native Instruments', 'Absynth 5', aumu('-NI-', 'Clm5'), tags(
        t.GRAIN,
    )),
    product('Native Instruments', 'Battery 4', aumu('-NI-', 'NBa4'), tags(
        t.DRUMS, t.SAMPLER,
    )),
    product('Native Instruments', 'FM8', aumu('-NI-', 'Nif8'), tags(
        t.FM, t.DIGITAL, t.LOFI,
    )),
    product('Native Instruments', 'Kontakt 5', aumu('-NI-', 'NiO5'), tags(
        t.SAMPLER,
    )),
    product('Native Instruments', 'Massive', aumu('-NI-', 'NiMa'), tags(
        t.SYNTH, t.DIGITAL, t.WAVETABLE,
    )),
    product('Native Instruments', 'Reaktor 6', aumu('-NI-', 'NiR6'), tags(
        t.MODULAR,
    )),
    product('Native Instruments', 'Reaktor 5', aumu('-NI-', 'NiR5'), tags(
        t.MODULAR,
    )),
    product('Native Instruments', 'Monark', reaktor, tags(
        t.SYNTH, t.MONO, t.SUBTRACTIVE, t.ANALOG, t.REAKTOR,
    )),
    product('Native Instruments', 'Polyplex', reaktor, tags(
        t.DRUMS, t.SAMPLED, t.REAKTOR,
    )),
    product('Native Instruments', 'Rounds', reaktor, tags(
        t.SYNTH, t.DIGITAL, t.REAKTOR,
    )),
    product('Native Instruments', 'Kontour', reaktor, tags(
        t.SYNTH, t.PHYSMOD, t.REAKTOR,
    )),
    product('Native Instruments', 'Spark R2', reaktor, tags(
        t.SYNTH, t.DIGITAL, t.REAKTOR,
    )),
    product('Native Instruments', 'Prism', reaktor, tags(
        t.SYNTH, t.PHYSMOD, t.REAKTOR,
    )),
    product('Native Instruments', 'Razor', reaktor, tags(
        t.SYNTH, t.ADDITIVE, t.REAKTOR,
    )),
    product('Native Instruments', 'Skanner XT', reaktor, tags(
        t.SYNTH, t.GRAIN, 'morph', t.REAKTOR, t.SPECIAL,
    )),
    product('Native Instruments', 'Carbon', reaktor, tags(
        t.SYNTH, t.DIGITAL, t.REAKTOR,
    )),
    product('Native Instruments', 'Junatik', reaktor, tags(
        t.SYNTH, t.SUBTRACTIVE, t.REAKTOR,
    )),
    product('Native Instruments', 'Steam Pipe', reaktor, tags(
        t.SYNTH, t.PHYSMOD, t.REAKTOR,
    )),
    product('Native Instruments', 'Grobian', reaktor, tags(
        t.SYNTH, 'acid', t.REAKTOR,
    )),
    product('Native Instruments', 'Titan', reaktor, tags(
        t.SYNTH, t.DIGITAL, t.REAKTOR,
    )),
    product('Native Instruments', 'Akkord', reaktor, tags(
        t.SYNTH, t.DIGITAL, t.REAKTOR,
    )),
    product('Native Instruments', 'Metaphysical Function A', reaktor, tags(
        t.SYNTH, t.DIGITAL, t.SPECIAL,
    )),
    product('Native Instruments', 'Metaphysical Function B', reaktor, tags(
        t.SYNTH, t.DIGITAL, t.SPECIAL,
    )),
    product('Native Instruments', 'Photone', reaktor, tags(
        t.SYNTH, t.DIGITAL,
    )),
    product('Native Instruments', 'Abbey Road 50s Drummer', kontakt, tags(
        t.DRUMS, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Native Instruments', 'Abbey Road 60s Drummer', kontakt, tags(
        t.DRUMS, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Native Instruments', 'Abbey Road 70s Drummer', kontakt, tags(
        t.DRUMS, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Native Instruments', 'Abbey Road 80s Drummer', kontakt, tags(
        t.DRUMS, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Native Instruments', 'Abbey Road Vintage Drummer', kontakt, tags(
        t.DRUMS, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Native Instruments', 'Abbey Road Modern Drummer', kontakt, tags(
        t.DRUMS, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Native Instruments', 'Action Strikes', kontakt, tags(
        t.CINEMATIC, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Native Instruments', 'Action Strings', kontakt, tags(
        t.CINEMATIC, t.ACOUSTIC, t.KONTAKT, t.DISABLED,
    )),
    product('Native Instruments', 'Alicias Keys', kontakt, tags(
        t.PIANO, t.ACOUSTIC, t.KONTAKT, t.DISABLED,
    )),
    product('Native Instruments', 'Balinese Gamelan', kontakt, tags(
        'gamelan', t.PERC, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Native Instruments', 'Cuba', kontakt, tags(
        t.PERC, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Native Instruments', 'Damage', kontakt, tags(
        t.CINEMATIC, t.PERC, t.ACOUSTIC, t.KONTAKT, t.DISABLED,
    )),
    product('Native Instruments', 'Evolve', kontakt, tags(
        t.CINEMATIC, t.KONTAKT, t.DISABLED,
    )),
    product('Native Instruments', 'Evolve Mutations', kontakt, tags(
        t.CINEMATIC, t.KONTAKT, t.DISABLED,
    )),
    product('Native Instruments', 'Evolve Mutations II', kontakt, tags(
        t.CINEMATIC, t.KONTAKT, t.DISABLED,
    )),
    product('Native Instruments', 'Drum Lab', kontakt, tags(
        t.DRUMS, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Native Instruments', 'George Duke Soul Treasures', kontakt, tags(
        t.ACOUSTIC, t.KONTAKT, t.DISABLED,
    )),
    product('Native Instruments', 'Kinetic Metal', kontakt, tags(
        t.CINEMATIC, t.KONTAKT,
    )),
    product('Native Instruments', 'Machine Drum Selection', kontakt, tags(
        t.DRUMS, t.SYNTH, t.SAMPLED, t.KONTAKT,
    )),
    product('Native Instruments', 'Retro Machines MK2', kontakt, tags(
        t.SYNTH, t.ANALOG, t.KONTAKT, t.DISABLED,
    )),
    product('Native Instruments', 'Rise & Hit', kontakt, tags(
        t.CINEMATIC, t.KONTAKT, t.DISABLED,
    )),
    product('Native Instruments', 'Scarbee Funk Guitarist', kontakt, tags(
        t.GUITAR, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Native Instruments', 'Scarbee Jay Bass', kontakt, tags(
        t.BASS, t.ELECTRIC, 'funk', t.ACOUSTIC, t.KONTAKT,
    )),
    product('Native Instruments', 'Scarbee MM Bass', kontakt, tags(
        t.BASS, t.ELECTRIC, 'funk', t.ACOUSTIC, t.KONTAKT,
    )),
    product('Native Instruments', 'Scarbee MM Bass Amped', kontakt, tags(
        t.BASS, t.ELECTRIC, 'funk', t.ACOUSTIC, t.KONTAKT,
    )),
    product('Native Instruments', 'Scarbee Pre Bass', kontakt, tags(
        t.BASS, t.ELECTRIC, 'funk', t.ACOUSTIC, t.KONTAKT,
    )),
    product('Native Instruments', 'Scarbee Pre Bass Amped', kontakt, tags(
        t.BASS, t.ELECTRIC, 'funk', t.ACOUSTIC, t.KONTAKT,
    )),
    product('Native Instruments', 'Scarbee Rickenbacker Bass', kontakt, tags(
        t.BASS, t.ELECTRIC, 'funk', t.ACOUSTIC, t.KONTAKT,
    )),
    product('Native Instruments', 'Scarbee Vintage Keys', kontakt, tags(
        'Mark I', 'A-200', 'clavinet', 'pianet', t.ELECTRIC, t.KONTAKT,
        t.DISABLED,
    )),
    product('Native Instruments', 'Session Horns Pro', kontakt, tags(
        t.BRASS, t.ENSEMBLE,  t.TROMBONE, t.TENOR, t.SAX, t.TRUMPET,
        t.ACOUSTIC, t.KONTAKT, t.WOODWINDS,
    )),
    product('Native Instruments', 'Session Strings Pro', kontakt, tags(
        t.STRINGS, 'ensemble', t.ACOUSTIC, t.KONTAKT, t.BOWED,
        t.DISABLED,
    )),
    product('Native Instruments', 'Studio Drummer', kontakt, tags(
        t.DRUMS, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Native Instruments', 'The Gentleman', kontakt, tags(
        t.PIANO, 'upright', t.ACOUSTIC, t.KONTAKT, t.DISABLED,
    )),
    product('Native Instruments', 'The Giant', kontakt, tags(
        t.PIANO, t.ACOUSTIC, t.KONTAKT, 'upright', t.DISABLED,
    )),
    product('Native Instruments', 'The Grandeur', kontakt, tags(
        t.PIANO, 'grand', t.ACOUSTIC, t.KONTAKT, t.DISABLED,
    )),
    product('Native Instruments', 'The Maverick', kontakt, tags(
        t.PIANO, 'grand', t.ACOUSTIC, t.KONTAKT, t.DISABLED,
    )),
    product('Native Instruments', 'Vintage Organs', kontakt, tags(
        t.ORGAN, 'hammond B3', 'hammond C3', 'hammond M3',
        'vox continental ii', 'farfisa compact',
        t.ELECTRIC, t.ACOUSTIC, t.KONTAKT, t.DISABLED,
    )),
    product('Native Instruments', 'West Africa', kontakt, tags(
        t.DRUMS, t.PERC, t.ACOUSTIC, t.KONTAKT, t.KALIMBA,
    )),

    # -New Sonic Arts-
    product('New Sonic Arts', 'Granite', aumu('NSA_', 'NSA0'), tags(
        t.GRAIN, 'simple',
    )),
    product('New Sonic Arts', 'Nuance', aumu('NSA_', 795658), tags(
        t.SAMPLER, 'simple',
    )),
    product('New Sonic Arts', 'Vice', aumu('NSA_', 833665), tags(
        t.SAMPLER, 'loop', 'rex', 'simple',
    )),

    # -Olli Larkin-
    product('Olli Larkin', 'Endless Series', aumf('oliL', 'Oles'), tags(
        t.CREATIVE, 'mfx', t.SPECIAL, 'generator',
    )),

    # -Orange Tree-
    product('Orange Tree', 'Angelic Harp', kontakt, tags(
        t.PLUCKED, t.ACOUSTIC, t.KONTAKT, t.HARP,
    )),
    product('Orange Tree', 'Angelic Chimes', kontakt, tags(
        t.ACOUSTIC, t.KONTAKT, t.CHIMES,
    )),
    product('Orange Tree', 'Angelic Zither', kontakt, tags(
        t.PLUCKED, t.ACOUSTIC, t.KONTAKT, t.ZITHER,
    )),
    product('Orange Tree', 'CoreBass Pear', kontakt, tags(
        t.PLUCKED, t.ACOUSTIC, t.KONTAKT, t.DOUBLEBASS,
    )),
    product('Orange Tree', 'EAG - Steel Strings KP', kontakt, tags(
        t.GUITAR, t.PLUCKED, t.ACOUSTIC,
    )),
    product('Orange Tree', 'Grand Kalimba', kontakt, tags(
        t.PLUCKED, t.ACOUSTIC, t.KONTAKT, t.KALIMBA,
    )),
    product('Orange Tree', 'Tiny Box', kontakt, tags(
        t.PLUCKED, t.ACOUSTIC, t.KONTAKT, t.MUSICBOX,
    )),

    # -Origins of Audio-
    product('Origins of Audio', 'Dark Kalimba', kontakt, tags(
        t.PLUCKED, t.ACOUSTIC, t.KONTAKT, t.KALIMBA,
    )),

    # -Plogue-
    product('Plogue', 'chipsounds', aumu('PLOG', 'PLGO'), tags(
        t.SYNTH, t.CHIP, t.DIGITAL,
    )),
    product('Plogue', 'chipspeech', aumu('PLOG', 'PLGS'), tags(
        t.VOCAL, t.CHIP, t.SPECIAL,
    )),

    # -Pluginboutique-
    product('Pluginboutique', 'VirtualCZ', aumu('pibT', 'vcz1'), tags(
        t.SYNTH, t.PHASEDIST, t.DIGITAL,
    )),

    # -PPG-
    product('PPG', 'Phonem', aumu('PpgW', 'Phnm'), tags(
        t.VOCAL, t.SYNTH, t.WAVETABLE,
    )),

    # -Prodyon-
    product('Prodyon', 'Shortnoise', kontakt, tags(
        t.SYNTH, t.SAMPLED, t.KONTAKT,
    )),
    product('Prodyon', 'Shortnoise II', kontakt, tags(
        t.SYNTH, t.SAMPLED, t.KONTAKT,
    )),
    product('Prodyon', 'Elektrono', kontakt, tags(
        t.SYNTH, t.SAMPLED, t.KONTAKT,
    )),

    # -Psound-
    product('Psound', 'Vintage Accordion', uvi, tags(
        t.ACCORDION, t.ACOUSTIC,
    )),

    # -ReFX-
    product('ReFX', 'QuadraSID', aumu('reFX', 'QSID'), tags(
        t.SYNTH, 'sid', t.DIGITAL, t.LOFI, t.CHIP, t.DISABLED,
    )),

    # -Renoise-
    product('Renoise', 'Redux', aumu('ReNS', 'RRDX'), tags(
        t.SAMPLER, 'tracker',
    )),

    # -Rhythmic Robot-
    product('Rhythmic Robot', 'Grit Kit', kontakt, tags(
        t.KONTAKT, t.DRUMS, t.ELECTRONIC,
    )),
    product('Rhythmic Robot', 'LAMBDA', kontakt, tags(
        t.KONTAKT, t.SYNTH, t.SAMPLED,
    )),

    # -Roland-
    product('Roland', 'PROMARS', aumu('Rlnd', 'Vas2'), tags(
        t.MONO, t.ANALOG, t.SUBTRACTIVE, 'promars',
    )),
    product('Roland', 'SH-2', aumu('Rlnd', 'Vas1'), tags(
        t.MONO, t.ANALOG, t.SUBTRACTIVE, 'sh-2',
    )),
    product('Roland', 'SH-101', aumu('Rlnd', 'Vas0'), tags(
        t.MONO, t.ANALOG, t.SUBTRACTIVE, 'sh-101',
    )),

    # -Skinnerbox-
    product('Skinnerbox', 'Time & Timbre', live, tags(
        t.DRUMS, t.SYNTH, t.ABLETON, t.M4L,
    )),

    # -Softube-
    product('Softube', 'Heartbeat', aumu('SfTb', 'r9z8'), tags(
        t.DRUMS, t.SYNTH, t.ANALOG,
    )),
    product('Softube', 'Modular', aumu('SfTb', 'hs9z'), tags(
        t.SYNTH, t.ANALOG, t.MODULAR,
    )),

    # -Sonic Charge-
    product('Sonic Charge', 'Microtonic', aumu('NuEd', 'NuMT'), tags(
        t.DRUMS, t.SYNTH,
    )),
    product('Sonic Charge', 'Synplant', aumu('NuEd', 'NuSP'), tags(
        t.SYNTH, t.SPECIAL,
    )),

    # -Soniccouture-
    product('Soniccouture', 'Array Mbira', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC, t.KALIMBA, t.PLUCKED,
    )),
    product('Soniccouture', 'Bag of Tricks', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC, t.KALIMBA, t.DRUMS, t.PERC, t.MALLET,
    )),
    product('Soniccouture', 'Broken Wurli', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC, t.KEYS, t.ELECTRIC, t.TINES,
    )),
    product('Soniccouture', 'EP73 Deconstructed', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC, t.KEYS, t.ELECTRIC, t.TINES,
    )),
    product('Soniccouture', 'Giant Bass Tongue Drum', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC, t.DRUMS, t.PERC, t.TUNED,
    )),
    product('Soniccouture', 'Glass Works', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC, t.PERC, t.MALLET,
    )),
    product('Soniccouture', 'Grand Marimba', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC, t.MARIMBA, t.PERC, t.TUNED, t.MALLET,
    )),
    product('Soniccouture', 'KIM', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC, t.PLUCKED,
    )),
    product('Soniccouture', 'Konkrete Drums 1', live, tags(
        t.DRUMS, t.ABLETON,
    )),
    product('Soniccouture', 'Konkrete Drums 2', live, tags(
        t.DRUMS, t.ABLETON,
    )),
    product('Soniccouture', 'Konkrete Drums 3', live, tags(
        t.DRUMS, t.ABLETON,
    )),
    product('Soniccouture', 'Novachord', kontakt, tags(
        t.KONTAKT, t.SYNTH, t.ANALOG, t.SAMPLED, t.SPECIAL,
    )),
    product('Soniccouture', 'Ondes', kontakt, tags(
        t.KONTAKT, t.SYNTH, t.ANALOG, t.SAMPLED, t.SPECIAL,
    )),
    product('Soniccouture', 'Ondioline', kontakt, tags(
        t.KONTAKT, t.SYNTH, t.ANALOG, t.SAMPLED, t.SPECIAL,
    )),
    product('Soniccouture', 'Pan Drums', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC, t.PERC, t.MALLET,
    )),
    product('Soniccouture', 'The Attic', kontakt, tags(
        t.KONTAKT, t.SYNTH, t.ANALOG, t.SAMPLED, t.SPECIAL,
    )),
    product('Soniccouture', 'The Conservatoire Collection', kontakt, tags(
        t.KONTAKT, t.HARPSICHORD, t.ACOUSTIC, t.PERC, t.PLUCKED,
    )),
    product('Soniccouture', 'The Hammersmith PRO', kontakt, tags(
        t.KONTAKT, t.PIANO, t.ACOUSTIC,
    )),
    product('Soniccouture', 'Vibraphone', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC, t.VIBRAPHONE, t.PERC, t.TUNED, t.MALLET,
    )),
    product('Soniccouture', 'Xtended Piano', kontakt, tags(
        t.KONTAKT, t.PIANO, t.ACOUSTIC, t.SPECIAL,
    )),

    # -Sonokinetic-
    product('Sonokinetic', 'Hurdy Gurdy', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC,
    )),

    # -SoundDUST-
    product('SoundDUST', 'Cloud Cello', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC, t.STRINGS, t.CELLO,
    )),
    product('SoundDUST', 'Cloud Viola', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC, t.STRINGS, t.VIOLA,
    )),
    product('SoundDUST', 'Dulcitone 1884x2', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC, t.DULCITONE, t.KEYS,
    )),
    product('SoundDUST', 'Dulcitone 1900x2', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC, t.DULCITONE, t.KEYS,
    )),
    product('SoundDUST', 'Flutter EP', kontakt, tags(
        t.KONTAKT, t.KEYS,
    )),
    product('SoundDUST', 'Ghost Dulcitone 1900', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC, t.DULCITONE, t.KEYS, t.SPECIAL,
    )),
    product('SoundDUST', 'GrandThrift AutoHarp2', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC, t.AUTOHARP, t.SPECIAL,
    )),
    product('SoundDUST', 'Hammr+', kontakt, tags(
        t.KONTAKT, 'hammond', t.ORGAN,
    )),
    product('SoundDUST', 'Hammr Growler', kontakt, tags(
        t.KONTAKT, 'hammond', t.ORGAN,
    )),
    product('SoundDUST', 'idstrument suite', kontakt, tags(
        'div', t.KONTAKT, t.DRUMS, t.SYNTH, t.GUITAR,
    )),
    product('SoundDUST', 'Orgone', kontakt, tags(
        t.KONTAKT, t.SYNTH, t.SAMPLED,
    )),
    product('SoundDUST', 'Plastic Ghost Piano', kontakt, tags(
        t.KONTAKT, t.SYNTH, t.SAMPLED, t.PIANO,
    )),
    product('SoundDUST', 'Rubber Bass', kontakt, tags(
        t.KONTAKT, t.ACOUSTIC, t.BASS,
    )),
    product('SoundDUST', 'Ships Piano MK2', kontakt, tags(
        t.KONTAKT, t.SAMPLED, t.PIANO,
    )),

    # -Soundguru-
    product('Soundguru', 'The Mangle', aumu('Sgru', 'Mngl'), tags(
        t.GRAIN,
    )),

    # -Soundsdivine-
    product('Soundsdivine', 'MM+', kontakt, tags(
        t.SYNTH, t.SUBTRACTIVE, t.KONTAKT, t.ANALOG,
    )),
    product('Soundsdivine', 'The2600', kontakt, tags(
        t.SYNTH, t.SUBTRACTIVE, t.KONTAKT, t.ANALOG,
    )),

    # -Soundprovocation-
    product('Soundprovocation', 'Vocalotheque', kontakt, tags(
        t.VOCAL, 'male', 'female', t.SAMPLED, t.KONTAKT,
    )),

    # -Spaectrum Arts-
    product('Spaectrum Arts', 'Percussion Hits', kontakt, tags(
        t.PERC, t.FX, t.ACOUSTIC, t.SPECIAL,
    )),
    product('Spaectrum Arts', 'The Container', kontakt, tags(
        t.DRUMS, t.PERC, t.FX, t.ACOUSTIC, t.SPECIAL,
    )),

    # -SPC Plugins-
    product('SPC Plugins', 'ArcSyn', aumu('SPCP', 'SPCa'), tags(
        t.SYNTH, t.WAVETABLE, t.DIGITAL,t.SPECIAL,
    )),

    # -Spitfire Audio-
    product('Spitfire Audio', 'Artisan Cello', kontakt, tags(
        t.STRINGS, t.CELLO, t.SOLO, t.ACOUSTIC, t.KONTAKT, t.BOWED,
    )),
    product('Spitfire Audio', 'Artisan Violins', kontakt, tags(
        t.STRINGS, t.VIOLIN, t.SOLO, t.ACOUSTIC, t.KONTAKT, t.BOWED,
    )),
    product('Spitfire Audio', 'Chrysalis', kontakt, tags(
        t.HARP, t.PLUCKED, t.SOLO, t.ACOUSTIC, t.KONTAKT, t.BOWED, t.SPECIAL,
    )),
    product('Spitfire Audio', 'EVO Grid 2: Strings', kontakt, tags(
        t.STRINGS, t.KONTAKT, t.ACOUSTIC,
    )),
    product('Spitfire Audio', 'EVO Grid 4: Woodwinds', kontakt, tags(
        t.BRASS, t.WOODWINDS, t.KONTAKT, t.ACOUSTIC,
    )),
    product('Spitfire Audio', 'Olafur Arnalds Evolutions', kontakt, tags(
        t.STRINGS, t.ACOUSTIC, t.KONTAKT, t.VIOLIN, t.CELLO, t.VIOLA, t.BASS,
    )),
    product('Spitfire Audio', 'Orstphone', kontakt, tags(
        'orstphone', t.IDIOPHONE, t.SOLO, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Spitfire Audio', 'Sable Chamber Strings Vol1', kontakt, tags(
        t.STRINGS, t.ACOUSTIC, t.KONTAKT, t.VIOLIN, t.CELLO,
    )),
    product('Spitfire Audio', 'Sable Chamber Strings Vol3', kontakt, tags(
        t.STRINGS, t.ACOUSTIC, t.KONTAKT, t.VIOLIN, t.CELLO, t.BASS, t.VIOLA,
    )),
    product('Spitfire Audio', 'Sable Chamber Strings Vol4', kontakt, tags(
        t.STRINGS, t.ACOUSTIC, t.KONTAKT, t.VIOLIN, t.CELLO, t.BASS, t.VIOLA,
    )),
    product('Spitfire Audio', 'Sable Chamber Strings Ensembles', kontakt, tags(
        t.STRINGS, t.ACOUSTIC, t.KONTAKT, t.VIOLIN, t.CELLO, t.ENSEMBLE,
    )),
    product('Spitfire Audio', 'Sacconi Quartet Vol2 - Cello', kontakt, tags(
        t.STRINGS, t.ACOUSTIC, t.KONTAKT, t.CELLO,
    )),
    product('Spitfire Audio', 'Sacconi Quartet Vol1 - Viola 1', kontakt, tags(
        t.STRINGS, t.ACOUSTIC, t.KONTAKT, t.VIOLA,
    )),
    product('Spitfire Audio', 'Sacconi Quartet Vol1 - Violin 1', kontakt, tags(
        t.STRINGS, t.ACOUSTIC, t.KONTAKT, t.VIOLIN,
    )),
    product('Spitfire Audio', 'Sacconi Quartet Vol1 - Violin 2', kontakt, tags(
        t.STRINGS, t.ACOUSTIC, t.KONTAKT, t.VIOLIN,
    )),
    product('Spitfire Audio', 'Swarm Harp', kontakt, tags(
        t.HARP, t.SOLO, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Spitfire Audio', 'Swarm Mandolins', kontakt, tags(
        t.MANDOLIN, t.SOLO, t.ACOUSTIC, t.KONTAKT,
    )),

    # -Spitfire LABS-
    product('Spitfire LABS', 'Bedlam Piano', kontakt, tags(
        t.PIANO, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Spitfire LABS', 'Bike Bells', kontakt, tags(
        'bell', t.ACOUSTIC, t.KONTAKT,
    )),
    product('Spitfire LABS', 'Drums', kontakt, tags(
        t.DRUMS, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Spitfire LABS', 'Fingered Dulcimer', kontakt, tags(
        t.PLUCKED, t.DULCIMER, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Spitfire LABS', 'Hamster Cage', kontakt, tags(
        t.PERC, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Spitfire LABS', 'Harmonic Piano', kontakt, tags(
        t.PIANO, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Spitfire LABS', 'Henson\'s Frozen Strings', kontakt, tags(
        t.STRINGS, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Spitfire LABS', 'Kalimba', kontakt, tags(
        'kalimba', t.ACOUSTIC, t.KONTAKT,
    )),
    product('Spitfire LABS', 'Kitchen Sink', kontakt, tags(
        t.PERC, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Spitfire LABS', 'Mandolin', kontakt, tags(
        'mandolin', t.ACOUSTIC, t.KONTAKT,
    )),
    product('Spitfire LABS', 'Melodica', kontakt, tags(
        'melodica', t.ACOUSTIC, t.KONTAKT,
    )),
    product('Spitfire LABS', 'Metal Fan', kontakt, tags(
        'tuned', t.PERC, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Spitfire LABS', 'Mini Harp', kontakt, tags(
        t.HARP, t.PLUCKED, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Spitfire LABS', 'Music Box', kontakt, tags(
        t.PLUCKED, t.ACOUSTIC, t.KONTAKT, t.MUSICBOX,
    )),
    product('Spitfire LABS', 'Nylon Guitar', kontakt, tags(
        t.PLUCKED, t.GUITAR, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Spitfire LABS', 'Office Lightshades', kontakt, tags(
        t.TUNED, t.PERC, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Spitfire LABS', 'Peel Guitar', kontakt, tags(
        t.GUITAR, t.ELECTRIC, t.ACOUSTIC, t.KONTAKT, t.PLUCKED,
    )),
    product('Spitfire LABS', 'Plastic Pipes', kontakt, tags(
        t.TUNED, t.PERC, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Spitfire LABS', 'Plucked Piano', kontakt, tags(
        t.PIANO, t.PLUCKED, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Spitfire LABS', 'Scary Strings', kontakt, tags(
        t.STRINGS, t.ACOUSTIC, t.KONTAKT, 'eerie', t.BOWED,
    )),
    product('Spitfire LABS', 'Small Pan', kontakt, tags(
        t.IDIOPHONE, t.TUNED, t.MALLET, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Spitfire LABS', 'Thundervox', kontakt, tags(
        t.VOCAL, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Spitfire LABS', 'Trumpet Fiddle', kontakt, tags(
        t.STRINGS, t.BOWED, t.ACOUSTIC, t.KONTAKT,
    )),

    # -Steinberg-
    product('Steinberg', 'Padshop Pro', aumu('Stbg', 'pads'), tags(
        t.GRAIN, t.SYNTH, t.SAMPLER,
    )),

    # -TAL-
    product('TAL', 'TAL Sampler', aumu('TOGU', 'hEl1'), tags(
        t.SAMPLER, t.LOFI, t.CREATIVE,
    )),

    # -Twisted Tools-
    product('Twisted Tools', 'Ultraloop', reaktor, tags(
        'loop', t.CREATIVE, t.FSU, t.DRUMS, t.PERC, t.SAMPLER,
    )),
    product('Twisted Tools', 'Vortex', reaktor, tags(
        'loop', t.CREATIVE, t.FSU, t.DRUMS, t.PERC, t.SAMPLER,
    )),

    # -Uhe-
    product('u-he', 'ACE', aumu('UHfX', 'acEU'), tags(
        t.SYNTH, t.ANALOG, t.MODULAR,
    )),
    product('u-he', 'Bazille', aumu('UHfX', 'UpH4'), tags(
        t.SYNTH, t.ANALOG, t.PHASEMOD, t.FM, t.MODULAR,
    )),
    product('u-he', 'Diva', aumu('UHfX', 'DiVa'), tags(
        t.SYNTH, t.ANALOG, t.DIGITAL, t.SUBTRACTIVE,
    )),
    product('u-he', 'FilterscapeVA', aumu('UHfX', 'FSVA'), tags(
        t.SYNTH, t.DIGITAL, t.SUBTRACTIVE, t.SPECIAL,
    )),
    product('u-he', 'Podolski', aumu('UHfX', 'Podo'), tags(
        t.DIGITAL, t.FREE, t.DISABLED,
    )),
    product('u-he', 'Triple Cheese', aumu('UHfX', 'cbSy'), tags(
        t.DIGITAL, t.FREE, t.DISABLED,
    )),

    # -Utami-
    product('Utami', 'Geisterwelt', live, tags(
        t.SAMPLER, t.SPECTRAL, t.ABLETON, t.M4L,
    )),

    # -UVI-
    product('UVI', 'Acoustic Toy Museum', uvi, tags(
        t.ACOUSTIC, t.SAMPLED,
    )),
    product('UVI', 'Electric Toy Museum', uvi, tags(
        t.SAMPLED,
    )),
    product('UVI', 'Falcon', aumu('UVI ', 'Flcn'), tags(
        t.GRAIN, t.SYNTH, t.SAMPLER, t.DIGITAL, t.ANALOG, t.WAVETABLE,
    )),
    product('UVI', 'IRCAM Prepared Piano', uvi, tags(
        t.PIANO, t.ACOUSTIC, t.SPECIAL, 'avant', 'IRCAM',
    )),
    product('UVI', 'IRCAM Solo Strings', uvi, tags(
        t.FLUTE, 'oboe', 'clarinet', 'bassoon', t.TRUMPET,
        'alto saxophone', 'french horn', t.TROMBONE, 'bass tuba', t.CHIP,
        t.ACCORDION, t.GUITAR, t.HARP, t.VIOLIN, t.VIOLA, 'violincello',
        t.DOUBLEBASS, t.ACOUSTIC, t.SPECIAL, 'avant', 'IRCAM', t.BOWED,
        t.CHIP, t.SOLD,
    )),
    product('UVI', 'Digital Synsations', uvi, tags(
        t.DIGITAL, t.SYNTH, t.SAMPLED,
    )),
    product('UVI', 'Emulation One', uvi, tags(
        t.DIGITAL, t.LOFI, t.SAMPLED,
    )),
    product('UVI', 'Grand Piano Model D', uvi, tags(
        t.PIANO, t.SAMPLED,
    )),
    product('UVI', 'Mello', uvi, tags(
        t.LOFI, t.SAMPLED,
    )),
    product('UVI', 'MachFive3 Biosphere', uvi, tags(
        t.SYNTH, t.DRUMS, 'atmo', t.SAMPLED,
    )),
    product('UVI', 'Analogic Piano 09', uvi, tags(
        t.PIANO, t.SAMPLED,
    )),
    product('UVI', 'Scratch Machines', uvi, tags(
        t.DRUMS, t.PERC, t.VOCAL, 'vinyl', t.SAMPLED,
    )),
    product('UVI', 'X-Treme FX', uvi, tags(
        'fx', 'samples',
    )),

    # -Waldorf-
    product('Waldorf', 'Attack', aumu('3E00', '3EDr'), tags(
        t.DRUMS, t.SYNTH,
    )),
    product('Waldorf', 'Largo', aumu('3E00', '3E80'), tags(
        t.SYNTH, t.WAVETABLE, t.DIGITAL,
    )),
    product('Waldorf', 'Nave', aumu('Wald', 'nave'), tags(
        t.SYNTH, t.WAVETABLE, t.DIGITAL,
    )),
    product('Waldorf', 'PPG Wave 2.V', aumu('3E00', '2900'), tags(
        t.SYNTH, t.WAVETABLE, t.DIGITAL,
    )),
    product('Waldorf', 'PPG Wave 3.V', aumu('3E00', '2901'), tags(
        t.SYNTH, t.WAVETABLE, t.DIGITAL,
    )),

    # -Wave Alchemy-
    product('Wave Alchemy', 'Digital Revolution', kontakt, tags(
        t.DRUMS, t.SAMPLED, t.KONTAKT, t.SOLD,
    )),
    product('Wave Alchemy', 'Revolution-606', kontakt, tags(
        t.DRUMS, '606', t.SAMPLED, t.KONTAKT,
    )),
    product('Wave Alchemy', 'Transistor Revolution MKII', kontakt, tags(
        t.DRUMS, '808', '909', t.SAMPLED, t.KONTAKT, t.SOLD,
    )),

    # -Wavesfactory-
    product('Wavesfactory', 'Little Harmonium', kontakt, tags(
        'melodica', t.ACOUSTIC, t.KONTAKT,
    )),
    product('Wavesfactory', 'Newmello 1', kontakt, tags(
        t.ACOUSTIC, t.KONTAKT, 'tape',
    )),
    product('Wavesfactory', 'Suspended Cymbals', kontakt, tags(
        t.DRUMS, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Wavesfactory', 'Tea Towl Drums 2.0', kontakt, tags(
        t.DRUMS, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Wavesfactory', 'VQ Drums', kontakt, tags(
        t.DRUMS, t.ACOUSTIC, t.KONTAKT,
    )),
    product('Wavesfactory', 'W-Buzz', kontakt, tags(
        t.BASS, t.SPECIAL, 'snare', t.DRUMS, t.ACOUSTIC, t.KONTAKT,
    )),

    # -XILS Labs-
    product('XILS Labs', 'miniSyn-X', aumu('XSyL', 'XSyL'), tags(
        t.SYNTH, t.ANALOG, t.SUBTRACTIVE,
    )),
    product('XILS Labs', 'PolyKB II', aumu('Xils', 'pKB2'), tags(
        t.SYNTH, t.ANALOG, t.SUBTRACTIVE,
    )),
    product('XILS Labs', 'SynX2', aumu('Xils', 'XSy2'), tags(
        t.SYNTH, t.ANALOG, t.SUBTRACTIVE,
    )),
    product('XILS Labs', 'XILS 3.2', aumu('Xils', 'XVc2'), tags(
        t.SYNTH, t.ANALOG, t.SUBTRACTIVE,
    )),
    product('XILS Labs', 'XILS 4', aumu('Xils', 'x3Di'), tags(
        t.SYNTH, t.ANALOG, t.SUBTRACTIVE,
    )),
}
