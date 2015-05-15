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
        'drums', 'kontakt', 'acoustic', 'impulses',
    )),

    # -Ableton-
    product('Ableton', 'Sampler', live, tags(
        'sampler',
    )),
    product('Ableton', 'Operator', live, tags(
        'synth', 'fm',
    )),
    product('Ableton', 'Tension', live, tags(
        'synth', 'physmod', 'plucked', 'strings',
    )),
    product('Ableton', 'Analog', live, tags(
        'synth', 'analog', 'subtractive',
    )),
    product('Ableton', 'Electric', live, tags(
        'synth', 'keys',
    )),
    product('Ableton', 'Collision', live, tags(
        'synth', 'physmod', 'percussion', 'mallet',
    )),

    # -Acousticsamples-
    product('Acousticsamples', 'Bassysm-F', uvi, tags(
        'bass', 'acoustic',
    )),
    product('Acousticsamples', 'Bassysm-J', uvi, tags(
        'bass', 'acoustic',
    )),
    product('Acousticsamples', 'Bassysm-M', uvi, tags(
        'bass', 'acoustic',
    )),
    product('Acousticsamples', 'Bassysm-S', uvi, tags(
        'bass', 'acoustic',
    )),
    product('Acousticsamples', 'J-Bass', uvi, tags(
        'bass', 'acoustic',
    )),
    product('Acousticsamples', 'TheUpright', uvi, tags(
        'bass', 'acoustic',
    )),
    product('Acousticsamples', 'GD-6', uvi, tags(
        'guitar', 'acoustic', 'plucked',
    )),
    product('Acousticsamples', 'Sunbird', uvi, tags(
        'guitar', 'acoustic', 'plucked',
    )),
    product('Acousticsamples', 'Telematic', uvi, tags(
        'guitar', 'acoustic', 'plucked', 'telecaster',
    )),
    product('Acousticsamples', 'F Grand 278', uvi, tags(
        'piano', 'grand', 'acoustic',
    )),
    product('Acousticsamples', 'Mark 79', uvi, tags(
        'organ', 'electric',
    )),
    product('Acousticsamples', 'Percussiv', uvi, tags(
        'drums', 'percussion', 'acoustic', 'acoustic',
    )),
    product('Acousticsamples', 'Star Drums', uvi, tags(
        'drums', 'acoustic',
    )),
    product('Acousticsamples', 'UKU', uvi, tags(
        'ukulele', 'acoustic', 'plucked',
    )),

    # -Admiral Quality-
    product('Admiral Quality', 'Poly-Ana', aumu('AdmQ', 'AQI2'), tags(
        'subtractive', 'digital', 'analog',
    )),

    # -Air Music Tech-
    product('Air', 'Loom', aumu('Wzoo', 'Loom'), tags(
        'additive', 'digital',
    )),
    product('Air', 'Vacuum Pro', aumu('Wzoo', 'VacP'), tags(
        'subtractive', 'analog',
    )),
    product('Air', 'Hybrid', aumu('Wzoo', 'Thun'), tags(
        'wavetable', 'digital',
    )),
    product('Air', 'Strike', aumu('Wzoo', 'UVD1'), tags(
        'drums', 'sampler',
    )),
    product('Air', 'Structure', aumu('Wzoo', 'DSpl'), tags(
        'sampler',
    )),
    product('Air', 'Velvet', aumu('Wzoo', 'StgP'), tags(
        'keys',
    )),
    product('Air', 'theRiser', aumu('Wzoo', 'tRsr'), tags(
        'fx', 'special',
    )),
    product('Air', 'Transfuser', aumu('Wzoo', 'Trfr'), tags(
        'loop', 'sampler',
    )),
    product('Air', 'Xpand!2', aumu('Wzoo', 'WSL1'), tags(
        'rompler',
    )),

    # -Amazing Noises-
    product('Amazing Noises', 'Dark Synth', live, tags(
        'special', 'additive', 'creative', 'Live', 'maxforlive',
    )),
    product('Amazing Noises', 'Density', live, tags(
        'granular', 'special', 'creative', 'sampler', 'Live', 'maxforlive',
    )),
    product('Amazing Noises', 'Pulsaret', live, tags(
        'granular', 'additive', 'special', 'creative', 'Live', 'maxforlive',
    )),
    product('Amazing Noises', 'Pulsor', live, tags(
        'special', 'subtractive', 'creative', 'Live', 'maxforlive',
    )),

    # -Analogue Drums-
    product('Analogue Drums', 'Boxer', kontakt, tags(
        'drums', 'kontakt', 'acoustic',
    )),
    product('Analogue Drums', 'FatStacks', kontakt, tags(
        'drums', 'kontakt', 'acoustic',
    )),
    product('Analogue Drums', 'Kingpin', kontakt, tags(
        'drums', 'kontakt', 'acoustic',
    )),
    product('Analogue Drums', 'Monotown', kontakt, tags(
        'drums', 'kontakt', 'acoustic',
    )),
    product('Analogue Drums', 'Pizazz', kontakt, tags(
        'drums', 'kontakt', 'acoustic',
    )),
    product('Analogue Drums', 'Royale', kontakt, tags(
        'drums', 'kontakt', 'accoustic',
    )),
    product('Analogue Drums', 'Smoker', kontakt, tags(
        'drums', 'kontakt', 'acoustic',
    )),

    # -Apple Logic Pro X-
    product('Apple', 'Ultrabeat', logic, tags(
        'logic', 'drums', 'synth', 'logic:inst',
    )),
    product('Apple', 'Sculpture', logic, tags(
        'logic', 'physmod', 'synth', 'logic:inst',
    )),
    product('Apple', 'EVOC 20 PS', logic, tags(
        'logic', 'vocoder', 'digital', 'logic:inst',
    )),
    product('apple', 'EFM1', logic, tags(
        'logic', 'FM', 'digital', 'synth', 'logic:inst',
    )),
    product('apple', 'ES M', logic, tags(
        'logic', 'subtractive', 'mono', 'digital', 'synth', 'logic:inst',
    )),
    product('apple', 'ES P', logic, tags(
        'logic', 'subtractive', 'digital', 'synth', 'logic:inst',
    )),
    product('apple', 'ES1', logic, tags(
        'logic', 'subtractive', 'digital', 'synth', 'logic:inst',
    )),
    product('apple', 'ES2', logic, tags(
        'logic', 'subtractive', 'digital', 'synth', 'logic:inst',
    )),

    # -Aria Sounds-
    product('Aria Sounds', 'London Symphonic Strings', kontakt, tags(
        'strings', 'kontakt', 'acoustic', 'violin', 'bowed',
    )),

    # -Arturia-
    product('Arturia', 'Analog Lab', aumu('Artu', 'ALab'), tags(
        'analog',
    )),
    product('Arturia', 'ARP 2600 V2', aumu('Artu', 'arpW'), tags(
        'analog', 'subtractive',
    )),
    product('Arturia', 'CS-80 V2', aumu('ArTu', 'Cs82'), tags(
        'analog', 'subtractive',
    )),
    product('Arturia', 'Jupiter-8 V2', aumu('Artu', 'Ju82'), tags(
        'analog', 'subtractive',
    )),
    product('Arturia', 'Matrix-12 V', aumu('Artu', 'Matr'), tags(
        'analog', 'subtractive',
    )),

    # XXX Crashing:
    product('Arturia', 'Mini V', aumu('Artu', 'mini'), tags(
        'analog', 'subtractive',
    )),
    product('Arturia', 'Modular V', aumu('Artu', 'mmv2'), tags(
        'analog', 'modular',
    )),
    product('Arturia', 'Oberheim SEM V', aumu('Artu', 'ObsV'), tags(
        'analog', 'subtractive',
    )),
    product('Arturia', 'Prophet V2', aumu('Artu', 'P5V2'), tags(
        'analog', 'subtractive',
    )),
    product('Arturia', 'Solina V', aumu('Artu', 'Soli'), tags(
        'organ', 'analog',
    )),
    product('Arturia', 'Spark', aumu('Artu', 'ArDS'), tags(
        'drums',
    )),
    product('Arturia', 'Spark Dubstep', aumu('Artu', 'ArDD'), tags(
        'drums',
    )),
    product('Arturia', 'Spark Vintage', aumu('Artu', 'ArDV'), tags(
        'drums',
    )),
    product('Arturia', 'Vox V', aumu('Artu', 'VoxA'), tags(
        'organ', 'analog',
    )),
    # XXX Crashing:
    product('Arturia', 'Wurlitzer V', aumu('Artu', 'WurV'), tags(
        'keys', 'analog',
    )),

    # -Atom Hub-
    product('Atom Hub', 'A day in the park', kontakt, tags(
        'kontakt', 'drums', 'acoustic',
    )),
    product('Atom Hub', 'Drunkeytar', kontakt, tags(
        'kontakt', 'guitar', 'acoustic', 'plucked',
    )),
    product('Atom Hub', 'Harmogeddon', kontakt, tags(
        'kontakt', 'harmonica', 'acoustic',
    )),
    product('Atom Hub', 'Old Mandolin v2', kontakt, tags(
        'kontakt', 'acoustic',
    )),
    product('Atom Hub', 'Bell from Shelf v2', kontakt, tags(
        'kontakt', 'acoustic',
    )),
    product('Atom Hub', 'Toolshed', kontakt, tags(
        'kontakt', 'drums', 'acoustic',
    )),

    # -Audio Damage-
    product('Audio Damage', 'Basic', aumu('AuDa', 'ADba'), tags(
        'synth', 'subtractive',
    )),
    product('Audio Damage', 'Phosphor', aumu('AuDa', 'ADph'), tags(
        'synth', 'additive',
    )),
    product('Audio Damage', 'Tattoo', aumu('AuDa', 'Tatt'), tags(
        'drums', 'synth',
    )),

    # -Audio Realism-
    product('Audio Realism', 'ABL2x', aumu('AuRe', 'abl3'), tags(
        'synth', 'subtractive', '303',
    )),
    product('Audio Realism', 'ADMx', aumu('AuRe', 'aadm'), tags(
        'drums', 'synth', '606', '808', '909',
    )),
    product('Audio Realism', 'ReDominator', aumu('AuRe', 'ReDo'), tags(
        'synth', 'subtractive', 'juno',
    )),

    # -Audiothing-
    product('Audiothing', 'Organetta', kontakt, tags(
        'kontakt', 'acoustic',
    )),
    product('Audiothing', 'miniBit', aumu('AdTg', 'mIbt'), tags(
        'synth', 'chip', 'subtractive',
    )),

    # -Audiowarp-
    product('Audiowarp', 'BOCS3', kontakt, tags(
        'synth', 'lofi', 'tape',
    )),

    # -Beepstreet-
    product('Beepstreet', 'Sunrizer', aumu('BSTR', 'SNRZ'), tags(
        'synth', 'subtractive',
    )),

    # -Bolder Sounds-
    product('Bolder Sounds', 'Harmoniums of the Opera', kontakt, tags(
        'harmonium', 'kontakt', 'acoustic',
    )),

    # -Camel Audio-
    product('Camel Audio', 'Alchemy', aumu('CamA', 'CaC2'), tags(
        'synth', 'granular', 'additive', 'subtractive',
    )),

    # -Drumdrops-
    product('Drumdrops', '1970s Rogers Dub Kit', kontakt, tags(
        'drums', 'kontakt', 'acoustic',
    )),
    product('Drumdrops', 'Ludwig Super Classic Kit', kontakt, tags(
        'drums', 'kontakt', 'acoustic',
    )),
    product('Drumdrops', 'Gretsch Soul Kit', kontakt, tags(
        'drums', 'kontakt', 'acoustic',
    )),

    # -Expert Sleepers-
    product(
        'Expert Sleepers', 'Crossfade Loop Synth',
        aumu('ExSl', 'XFls'),
        tags(t.CREATIVE, 'sampler', 'special', 'mfx'),
    ),
    product('Expert Sleepers', 'Minky Starshine', aumu('ExSl', 'MiSt'), tags(
        'synth', 'digital', 'additive',
    )),

    # -Facets of Sound-
    product('Facets of Sound', 'LOVELY Drumkit', kontakt, tags(
        'kontakt', 'acoustic', 'drums',
    )),

    # -Fairly Confusing-
    product('Fairly Confusing', 'Alimchord PE', kontakt, tags(
        'kontakt', 'acoustic',
    )),

    # -Fluffy Audio-
    product('Fluffy Audio', 'Simple Flute', kontakt, tags(
        'kontakt', 'acoustic', 'flute', 'free',
    )),

    # -FXpansion-
    product('FXpansion', 'Amber', aumu('FXPN', 'AMBR'), tags(
        'analog', 'strings', 'ensemble',
    )),
    product('FXpansion', 'Cypher', aumu('FXPN', 'CYPH'), tags(
        'analog', 'FM',
    )),
    product('FXpansion', 'Geist', aumu('FXPN', 'FXGR'), tags(
        'drums', 'sampler', 'loop', 'rex',
    )),
    product('FXpansion', 'Strobe', aumu('FXPN', 'STRO'), tags(
        'analog', 'subtractive', 'mono', 'poly',
    )),
    product('FXpansion', 'Tremor', aumu('FXPN', 'FXBS'), tags(
        'drums', 'synth',
    )),

    # -Goldbaby-
    product('Goldbaby', 'SP1200 Vol.2', kontakt, tags(
        'drums', 'sampled', 'SP1200', 'kontakt', 'battery', 'geist',
    )),
    product('Goldbaby', 'Urban Cookbook Vol.3', kontakt, tags(
        'drums', 'sampled', 'kontakt', 'battery', 'geist',
    )),

    # -IRCAM-
    product('IRCAM', 'IM-SuperVPSynth', live, tags(
        'special', 'creative', 'sampler', 'stretch', 'IRCAM',
        'Live', 'maxforlive', 'latency',
    )),

    # -iZotope-
    product('iZotope', 'IRIS 2', aumu('iZtp', 'Zir2'), tags(
        'synth', 'spectral', 'sampler',
    )),

    # -Klevgränd Produktion-
    product('Klevgränd Produktion', 'Enkl', aumu('Klev', 'Enkl'), tags(
        'synth', 'mono',
    )),

    # -Korg-
    product('Korg', 'M1', aumu('KORG', 'KLM1'), tags(
        'synth', 'digital',
    )),
    product('Korg', 'Mono-poly', aumu('KORG', 'KLMP'), tags(
        'analog', 'subtractive',
    )),
    product('Korg', 'MS-20', aumu('KORG', 'KLMV'), tags(
        'analog', 'subtractive',
    )),
    product('Korg', 'Polysix', aumu('KORG', 'KLPV'), tags(
        'analog', 'subtractive',
    )),
    product('Korg', 'Wavestation', aumu('KORG', 'KLWV'), tags(
        'digital', 'synth', 'wavetable',
    )),

    # -Loops De La Creme-
    product('Loops De La Creme', 'Bell Empire', kontakt, tags(
        'bell', 'acoustic', 'synth',
    )),
    product('Loops De La Creme', 'Booga Rocket Drums', kontakt, tags(
        'kontakt', 'acoustic', 'drums',
    )),
    product('Loops De La Creme', 'Cymbal Rolls', kontakt, tags(
        'kontakt', 'acoustic', 'drums',
    )),

    # -Lux/Nox-
    product('Lux/Nox', 'PERC+', kontakt, tags(
        'kontakt', 'acoustic', 'drums',
    )),

    # -Madrona Labs-
    product('Madrona Labs', 'AAlto', aumu('MLbs', 'Aalt'), tags(
        'analog', 'mono', 'poly', 'subtractive',
    )),
    product('Madrona Labs', 'Kaivo', aumu('MLbs', 'Kaiv'), tags(
        'granular', 'physmod',
    )),

    # -Max for Cats-
    product('Max for Cats', 'Digital', live, tags(
        'digital', 'synth', 'additive', 'Live', 'maxforlive',
    )),

    # -Modartt-
    product('Modartt', 'Pianoteq 5 PRO', aumu('Mdrt', 'Pt5q'), tags(
        'piano', 'acoustic', 'physmod', 'keys', 'chromatic', 'microtonal',
    )),

    # -Modwheel-
    product('Modwheel', 'Biscuit Tin Guitar', kontakt, tags(
        'kontakt', 'guitar', 'acoustic', 'plucked',
    )),
    product('Modwheel', 'Hum Drum', kontakt, tags(
        'kontact', 'drums', 'accoustic', 'percussion',
    )),
    product('Modwheel', 'The Lowdown', kontakt, tags(
        'bass', 'strings', 'bow', 'acoustic', 'kontakt', 'upright',
        'plucked', 'bowed',
    )),

    # -MOTU-
    product('MOTU', 'MachFive3', aumu('MOTU', 'MCH3'), tags(
        'sampler', 'granular', 'stretch', 'IRCAM',
    )),

    # -Native Instruments-
    product('Native Instruments', 'Absynth 5', aumu('-NI-', 'Clm5'), tags(
        'granular',
    )),
    product('Native Instruments', 'Battery 4', aumu('-NI-', 'NBa4'), tags(
        'drums', 'sampler',
    )),
    product('Native Instruments', 'FM8', aumu('-NI-', 'Nif8'), tags(
        'FM', 'digital', 'retro',
    )),
    product('Native Instruments', 'Kontakt 5', aumu('-NI-', 'NiO5'), tags(
        'sampler',
    )),
    product('Native Instruments', 'Massive', aumu('-NI-', 'NiMa'), tags(
        'synth', 'digital', 'wavetable',
    )),
    product('Native Instruments', 'Reaktor 5', aumu('-NI-', 'NiR5'), tags(
        'modular',
    )),
    product('Native Instruments', 'Monark', reaktor, tags(
        'synth', 'mono', 'subtractive', 'analog', 'reaktor',
    )),
    product('Native Instruments', 'Polyplex', reaktor, tags(
        'drums', 'samples', 'reaktor',
    )),
    product('Native Instruments', 'Rounds', reaktor, tags(
        'synth', 'digital', 'reaktor',
    )),
    product('Native Instruments', 'Kontour', reaktor, tags(
        'synth', 'physmod', 'reaktor',
    )),
    product('Native Instruments', 'Spark R2', reaktor, tags(
        'synth', 'digital', 'reaktor',
    )),
    product('Native Instruments', 'Prism', reaktor, tags(
        'synth', 'physmod', 'reaktor',
    )),
    product('Native Instruments', 'Skanner XT', reaktor, tags(
        'synth', 'granular', 'morph', 'reaktor', 'special',
    )),
    product('Native Instruments', 'Carbon', reaktor, tags(
        'synth', 'digital', 'reaktor',
    )),
    product('Native Instruments', 'Junatik', reaktor, tags(
        'synth', 'subtractive', 'reaktor',
    )),
    product('Native Instruments', 'Steam Pipe', reaktor, tags(
        'synth', 'physmod', 'reaktor',
    )),
    product('Native Instruments', 'Grobian', reaktor, tags(
        'synth', 'acid', 'reaktor',
    )),
    product('Native Instruments', 'Titan', reaktor, tags(
        'synth', 'digital', 'reaktor',
    )),
    product('Native Instruments', 'Akkord', reaktor, tags(
        'synth', 'digital', 'reaktor',
    )),
    product('Native Instruments', 'Metaphysical Function A', reaktor, tags(
        'synth', 'digital', 'special',
    )),
    product('Native Instruments', 'Metaphysical Function B', reaktor, tags(
        'synth', 'digital', 'special',
    )),
    product('Native Instruments', 'Photone', reaktor, tags(
        'synth', 'digital',
    )),
    product('Native Instruments', 'The Giant', kontakt, tags(
        'piano', 'acoustic', 'kontakt', 'upright',
    )),
    product('Native Instruments', 'Drum Lab', kontakt, tags(
        'drums', 'acoustic', 'kontakt',
    )),
    product('Native Instruments', 'Scarbee MM Bass', kontakt, tags(
        'bass', 'electric', 'funk', 'kontakt',
    )),
    product('Native Instruments', 'Scarbee Vintage Keys', kontakt, tags(
        'Mark I', 'A-200', 'clavinet', 'pianet', 'electric', 'kontakt',
    )),
    product('Native Instruments', 'Session Strings', kontakt, tags(
        'strings', 'ensemble', 'acoustic', 'kontakt', 'bowed',
    )),
    product('Native Instruments', 'Vintage Organs', kontakt, tags(
        'organ', 'hammond B3', 'hammond C3', 'hammond M3',
        'vox continental ii', 'farfisa compact',
        'electric', 'acoustic', 'kontakt',
    )),
    product('Native Instruments', 'West Africa', kontakt, tags(
        'drums', 'percussion', 'acoustic', 'kontakt',
    )),
    product('Native Instruments', 'Studio Drummer', kontakt, tags(
        'drums', 'acoustic', 'kontakt',
    )),
    product('Native Instruments', 'Retro Machines MK2', kontakt, tags(
        'synth', 'analogue', 'kontakt',
    )),
    product('Native Instruments', 'Abbey Road 60s Drummer', kontakt, tags(
        'drums', 'acoustic', 'kontakt',
    )),
    product('Native Instruments', 'Abbey Road Vintage Drummer', kontakt, tags(
        'drums', 'acoustic', 'kontakt',
    )),
    product('Native Instruments', 'Session Horns', kontakt, tags(
        'brass', 'ensemble',  'trombone', 'tenor sax', 'trumpet',
        'acoustic', 'kontakt',
    )),
    product('Native Instruments', 'The Maverick', kontakt, tags(
        'piano', 'grand', 'acoustic', 'kontakt',
    )),
    product('Native Instruments', 'The Grandeur', kontakt, tags(
        'piano', 'grand', 'acoustic', 'kontakt',
    )),
    product('Native Instruments', 'The Gentleman', kontakt, tags(
        'piano', 'upright', 'acoustic', 'kontakt',
    )),

    # -New Sonic Arts-
    product('New Sonic Arts', 'Granite', aumu('NSA_', 'NSA0'), tags(
        'granular', 'simple',
    )),
    product('New Sonic Arts', 'Nuance', aumu('NSA_', 795658), tags(
        'sampler', 'simple',
    )),
    product('New Sonic Arts', 'Vice', aumu('NSA_', 833665), tags(
        'sampler', 'loop', 'rex', 'simple',
    )),

    # -Olli Larkin-
    product('Olli Larkin', 'Endless Series', aumf('oliL', 'Oles'), tags(
        t.CREATIVE, 'mfx', 'special', 'generator',
    )),

    # -Orange Tree-
    product('Orange Tree', 'Angelic Harp', kontakt, tags(
        'plucked', 'acoustic', 'kontakt', 'harp',
    )),
    product('Orange Tree', 'Angelic Zither', kontakt, tags(
        'plucked', 'acoustic', 'kontakt', 'zither',
    )),
    product('Orange Tree', 'EAG - Steel Strings', kontakt, tags(
        'guitar', 'plucked', 'accoustic',
    )),
    product('Orange Tree', 'EEG - Stratosphere', kontakt, tags(
        'guitar', 'plucked', 'electric', 'stratocaster',
    )),
    product('Orange Tree', 'Grand Kalimba', kontakt, tags(
        'plucked', 'acoustic', 'kontakt', 'kalimba',
    )),

    # -Plogue-
    product('Plogue', 'chipsounds', aumu('PLOG', 'PLGO'), tags(
        'synth', 'chip', 'digital',
    )),
    product('Plogue', 'chipspeech', aumu('PLOG', 'PLGS'), tags(
        'vocal', 'chip', 'special',
    )),

    # -Pluginboutique-
    product('Pluginboutique', 'VirtualCZ', aumu('pibT', 'vcz1'), tags(
        'synth', 'phase distortion', 'digital',
    )),

    # -Prodyon-
    product('Prodyon', 'Shortnoise', kontakt, tags(
        'synth', 'sampled', 'kontakt',
    )),
    product('Prodyon', 'Shortnoise II', kontakt, tags(
        'synth', 'sampled', 'kontakt',
    )),
    product('Prodyon', 'Elektrono', kontakt, tags(
        'synth', 'sampled', 'kontakt',
    )),

    # -Psound-
    product('Psound', 'Vintage Accordion', uvi, tags(
        'accordion', 'acoustic',
    )),

    # -ReFX-
    #product('ReFX', 'QuadraSID', aumu('reFX', 'QSID'), tags(
    #    'synth', 'sid', 'digital', 'retro',
    #)),

    # -Rhythmic Robot-
    product('Rhythmic Robot', 'Grit Kit', kontakt, tags(
        'kontakt', 'drums', 'electronic',
    )),
    product('Rhythmic Robot', 'LAMBDA', kontakt, tags(
        'kontakt', 'synth', 'sampled',
    )),

    # -Roland-
    product('Roland', 'PROMARS', aumu('Rlnd', 'Vas2'), tags(
        'mono', 'analog', 'subtractive', 'promars',
    )),
    product('Roland', 'SH-2', aumu('Rlnd', 'Vas1'), tags(
        'mono', 'analog', 'subtractive', 'sh-2',
    )),
    product('Roland', 'SH-101', aumu('Rlnd', 'Vas0'), tags(
        'mono', 'analog', 'subtractive', 'sh-101',
    )),

    # -Skinnerbox-
    product('Skinnerbox', 'Time & Timbre', live, tags(
        'drums', 'synth', 'Live', 'maxforlive'
    )),

    # -Sonic Charge-
    product('Sonic Charge', 'Microtonic', aumu('NuEd', 'NuMT'), tags(
        'drums', 'synth',
    )),
    product('Sonic Charge', 'Synplant', aumu('NuEd', 'NuSP'), tags(
        'synth', 'special',
    )),

    # -Soniccouture-
    product('Soniccouture', 'Array Mbira', kontakt, tags(
        'kontakt', 'acoustic', 'kalimba',
    )),
    product('Soniccouture', 'Giant Bass Tongue Drum', kontakt, tags(
        'kontakt', 'accoustic', 'drums', 'percussion', 'tuned',
    )),
    product('Soniccouture', 'The Hammersmith PRO', kontakt, tags(
        'kontakt', 'piano', 'acoustic',
    )),
    product('Soniccouture', 'KIM', kontakt, tags(
        'kontakt', 'acoustic', 'plucked',
    )),
    product('Soniccouture', 'Konkrete Drums 1', live, tags(
        'drums', 'Live',
    )),
    product('Soniccouture', 'Konkrete Drums 2', live, tags(
        'drums', 'Live',
    )),
    product('Soniccouture', 'Konkrete Drums 3', live, tags(
        'drums', 'Live',
    )),

    # -Sonokinetic-
    product('Sonokinetic', 'Hurdy Gurdy', kontakt, tags(
        'kontakt', 'acoustic',
    )),

    # -SoundDUST-
    product('SoundDUST', 'Cloud Viola', kontakt, tags(
        'kontakt', 'acoustic', 'strings',
    )),
    product('SoundDUST', 'Dulcitone 1884x2', kontakt, tags(
        'kontakt', 'acoustic', 'dulcitone', 'keys',
    )),
    product('SoundDUST', 'Dulcitone 1900x2', kontakt, tags(
        'kontakt', 'acoustic', 'dulcitone', 'keys',
    )),
    product('SoundDUST', 'Ghost Dulcitone 1900', kontakt, tags(
        'kontakt', 'acoustic', 'dulcitone', 'keys', 'special',
    )),
    product('SoundDUST', 'idstrument suite', kontakt, tags(
        'div', 'kontakt', 'drums', 'synth', 'guitar',
    )),
    product('SoundDUST', 'Orgone', kontakt, tags(
        'kontakt', 'synth', 'sampled',
    )),
    product('SoundDUST', 'Plastic Ghost Piano', kontakt, tags(
        'kontakt', 'synth', 'sampled', 'piano',
    )),
    product('SoundDUST', 'Ships Piano MK2', kontakt, tags(
        'kontakt', 'sampled', 'piano',
    )),

    # -Soundguru-
    product('Soundguru', 'The Mangle', aumu('Sgru', 'Mngl'), tags(
        'granular',
    )),

    # -Soundsdivine-
    product('Soundsdivine', 'MM+', kontakt, tags(
        'synth', 'subtractive', 'kontakt', 'analog',
    )),
    product('Soundsdivine', 'The2600', kontakt, tags(
        'synth', 'subtractive', 'kontakt', 'analog',
    )),

    # -Soundprovocation-
    product('Soundprovocation', 'Vocalotheque', kontakt, tags(
        'vocal', 'male', 'female', 'sampled', 'kontakt',
    )),

    # -Spaectrum Arts-
    product('Spaectrum Arts', 'The Container', kontakt, tags(
        'drums', 'percussion', 'fx', 'pads', 'acoustic', 'special',
    )),

    # -Spitfire-
    product('Spitfire', 'Artisan Cello', kontakt, tags(
        'strings', 'cello', 'solo', 'acoustic', 'kontakt', 'bowed',
    )),
    product('Spitfire', 'Artisan Violins', kontakt, tags(
        'strings', 'violin', 'solo', 'acoustic', 'kontakt', 'bowed',
    )),
    product('Spitfire', 'EVO Grid 2: Strings', kontakt, tags(
        'strings', 'kontakt', 'acoustic',
    )),
    product('Spitfire', 'Swarm Mandolins', kontakt, tags(
        'mandolin', 'solo', 'acoustic', 'kontakt',
    )),

    # -Spitfire LABS-
    product('Spitfire LABS', 'Bike Bells', kontakt, tags(
        'bell', 'acoustic', 'kontakt',
    )),
    product('Spitfire LABS', 'Hamster Cage', kontakt, tags(
        'percussion', 'acoustic', 'kontakt',
    )),
    product('Spitfire LABS', 'Kalimba', kontakt, tags(
        'kalimba', 'acoustic', 'kontakt',
    )),
    product('Spitfire LABS', 'Kitchen Sink', kontakt, tags(
        'percussion', 'acoustic', 'kontakt',
    )),
    product('Spitfire LABS', 'Mandolin', kontakt, tags(
        'mandolin', 'acoustic', 'kontakt',
    )),
    product('Spitfire LABS', 'Melodica', kontakt, tags(
        'melodica', 'acoustic', 'kontakt',
    )),
    product('Spitfire LABS', 'Metal Fan', kontakt, tags(
        'tuned', 'percussion', 'acoustic', 'kontakt',
    )),
    product('Spitfire LABS', 'Peel Guitar', kontakt, tags(
        'guitar', 'electric', 'acoustic', 'kontakt', 'plucked',
    )),
    product('Spitfire LABS', 'Plucked Piano', kontakt, tags(
        'piano', 'plucked', 'acoustic', 'kontakt',
    )),
    product('Spitfire LABS', 'Scary Strings', kontakt, tags(
        'strings', 'acoustic', 'kontakt', 'eerie', 'bowed',
    )),

    # -Steinberg-
    product('Steinberg', 'Padshop Pro', aumu('Stbg', 'pads'), tags(
        'granular', 'synth', 'sampler',
    )),

    # -Twisted Tools-
    product('Twisted Tools', 'Ultraloop', reaktor, tags(
        'loop', 'creative', 'FSU', 'drums', 'percussion', 'sampler',
    )),
    product('Twisted Tools', 'Vortex', reaktor, tags(
        'loop', 'creative', 'FSU', 'drums', 'percussion', 'sampler',
    )),

    # -Uhe-
    product('u-he', 'ACE', aumu('UHfX', 'acEU'), tags(
        'synth', 'analog', 'modular',
    )),
    product('u-he', 'Bazille', aumu('UHfX', 'UpH4'), tags(
        'synth', 'analog', 'phase modulation', 'FM', 'modular',
    )),
    product('u-he', 'Diva', aumu('UHfX', 'DiVa'), tags(
        'synth', 'analog', 'digital', 'subtractive',
    )),
    product('u-he', 'FilterscapeVA', aumu('UHfX', 'FSVA'), tags(
        'synth', 'digital', 'subtractive', 'special',
    )),
    product('u-he', 'Podolski', aumu('UHfX', 'Podo'), tags(
        'digital', 'free',
    )),
    product('u-he', 'Triple Cheese', aumu('UHfX', 'cbSy'), tags(
        'digital', 'free',
    )),

    # -Utami-
    product('Utami', 'Geisterwelt', live, tags(
        'sampler', 'spectral', 'Live', 'maxforlive'
    )),

    # -UVI-
    product('UVI', 'Acoustic Toy Museum', uvi, tags(
        'acoustic', 'sampled',
    )),
    product('UVI', 'Electric Toy Museum', uvi, tags(
        'sampled',
    )),
    product('UVI', 'IRCAM Prepared Piano', uvi, tags(
        'piano', 'acoustic', 'special', 'avant', 'IRCAM',
    )),
    product('UVI', 'IRCAM Solo Strings', uvi, tags(
        'flute', 'oboe', 'clarinet', 'bassoon', 'trumpet',
        'alto saxophone', 'french horn', 'trombone', 'bass tuba',
        'accordion', 'guitar', 'harp', 'violin', 'viola', 'violincello',
        'contrabass', 'acoustic', 'special', 'avant', 'IRCAM', 'bowed',
    )),
    product('UVI', 'Digital Synsations', uvi, tags(
        'digital', 'synth', 'sampled',
    )),
    product('UVI', 'Emulation One', uvi, tags(
        'digital', 'retro', 'sampled',
    )),
    product('UVI', 'Grand Piano Model D', uvi, tags(
        'piano', 'sampled',
    )),
    product('UVI', 'Mello', uvi, tags(
        'retro', 'sampled',
    )),
    product('UVI', 'MachFive3 Biosphere', uvi, tags(
        'synth', 'drums', 'atomo', 'sampled',
    )),
    product('UVI', 'Analogic Piano 09', uvi, tags(
        'piano', 'sampled',
    )),
    product('UVI', 'Scratch Machines', uvi, tags(
        'drums', 'percussion', 'vocal', 'vinyl', 'sampled',
    )),
    product('UVI', 'X-Treme FX', uvi, tags(
        'fx', 'samples',
    )),

    # -Waldorf-
    product('Waldorf', 'Attack', aumu('3E00', '3EDr'), tags(
        'drums', 'synth',
    )),
    product('Waldorf', 'Largo', aumu('3E00', '3E80'), tags(
        'synth', 'wavetable', 'digital',
    )),
    product('Waldorf', 'Nave', aumu('Wald', 'nave'), tags(
        'synth', 'wavetable', 'digital',
    )),
    product('Waldorf', 'PPG Wave 2.V', aumu('3E00', '2900'), tags(
        'synth', 'wavetable', 'digital',
    )),

    # -Wave Alchemy-
    product('Wave Alchemy', 'Digital Revolution', kontakt, tags(
        'drums', 'sampled', 'kontakt',
    )),
    product('Wave Alchemy', 'Revolution-606', kontakt, tags(
        'drums', '606', 'sampled', 'kontakt',
    )),
    product('Wave Alchemy', 'Transistor Revolution MKII', kontakt, tags(
        'drums', '808', '909', 'sampled', 'kontakt',
    )),

    # -Wavesfactory-
    product('Wavesfactory', 'Little Harmonium', kontakt, tags(
        'melodica', 'acoustic', 'kontakt',
    )),
    product('Wavesfactory', 'Tea Towl Drums 2.0', kontakt, tags(
        'drums', 'acoustic', 'kontakt',
    )),
    product('Wavesfactory', 'W-Buzz', kontakt, tags(
        'bass', 'special', 'snare', 'acoustic', 'kontakt',
    )),

    # -Xfer Records-
    product('Xfer', 'Nerve', aumu('XFER', 'XFRa'), tags(
        'drums', 'sampler',
    )),
    product('Xfer', 'Serum', aumu('XFER', 'XfsX'), tags(
        'synth', 'digital', 'wavetable',
    )),

    # -XILS Labs-
    product('XILS Labs', 'miniSyn-X', aumu('XSyL', 'XSyL'), tags(
        'synth', 'analog', 'subtractive',
    )),
    product('XILS Labs', 'PolyKB II', aumu('Xils', 'pKB2'), tags(
        'synth', 'analog', 'subtractive',
    )),
    product('XILS Labs', 'Syn-X', aumu('Xils', 'XiSy'), tags(
        'synth', 'analog', 'subtractive',
    )),
    product('XILS Labs', 'XILS 3.2', aumu('Xils', 'XVc2'), tags(
        'synth', 'analog', 'subtractive',
    )),
    product('XILS Labs', 'XILS 4', aumu('Xils', 'x3Di'), tags(
        'synth', 'analog', 'subtractive',
    )),
}
