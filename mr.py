from __future__ import print_function

import os
import sys
import random

from collections import Counter, defaultdict, namedtuple
from functools import partial

product = namedtuple('product', ('brand', 'name', 'au', 'tags'))
AUid = namedtuple('AUid', ('type', 'manufacturer', 'name'))
aufx = partial(AUid, 'aufx')
aumf = partial(AUid, 'aumf')
aumu = partial(AUid, 'aumu')
kontakt = aumu('-NI-', 'NiO5')
reaktor = aumu('-NI-', 'NiR5')
logic = aumu('x', 'x')
live = aumu('y', 'y')
livefx = aufx('yfx', 'yfx')
uvi = aumu('UVI ', 'UVIW')
tags = lambda *x: x

FMT = """\
------------------------------------------
{inst}
------------------------------------------
reverb:    {reverb}
delay:     {delay}
special:   {special}
character: {character}
dynamics:  {dynamics}
eq:        {eq}
"""

MFX = {
    product('accSone', 'CrusherX', aumf('bsCX', 'cXs1'), tags(
        'granular', 'special', 'mfx',
    )),
    product('Antares', 'Harmony Engine EVO', aumf('VST ', 'VZr2'), tags(
        'vocal', 'special', 'mfx',
    )),
    product('Cytomic', 'The Drop', aumf('Cyto', 'Drp1'), tags(
        'filter', 'special', 'eq', 'mfx', 'character', 'sidechain',
    )),
    product('Expert Sleepers', 'Crossfade Loop Synth',
        aumu('ExSl', 'XFls'), tags(
            'fx', 'sampler', 'special', 'mfx',
        ),
    ),
    product('Olli Larkin', 'Endless Series', aumf('oliL', 'Oles'), tags(
        'mfx', 'special', 'generator',
    )),
    product('Soundhack', '+pvocloop (pvoc)', aumf('SDHK', '+pvt'), tags(
        'special', 'granular', 'mfx',
    )),
    product('XILS', 'XILS 5000', aumf('Xils', 'XiE5'), tags(
        'vocoder', 'special', 'mfx', 'sidechain',
    )),
}

INST = {
    # -8dio-
    product('8dio', 'Mini', kontakt, tags(
        'drums', 'kontakt', 'acoustic', 'impulses',
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
        'guitar', 'acoustic',
    )),
    product('Acousticsamples', 'Sunbird', uvi, tags(
        'guitar', 'acoustic',
    )),
    product('Acousticsamples', 'Telematic', uvi, tags(
        'guitar', 'acoustic',
    )),
    product('Acousticsamples', 'F Grand 278', uvi, tags(
        'piano', 'grand', 'acoustic',
    )),
    product('Acousticsamples', 'Mark 79', uvi, tags(
        'organ', 'electric',
    )),
    product('Acousticsamples', 'Percussive', uvi, tags(
        'drums', 'percussion', 'acoustic', 'acoustic',
    )),
    product('Acousticsamples', 'Star Drums', uvi, tags(
        'drums', 'acoustic',
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
        'strings', 'kontakt', 'acoustic', 'violin',
    )),

    # -Arturia-
    product('Arturia', 'Analog Lab', aumu('Artu', 'ALab'), tags(
        'analog',
    )),
    product('Arturia', 'Analog Labratory', aumu('Artu', 'ArLa'), tags(
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
    product('Arturia', 'Wurlitzer V', aumu('Artu', 'WurV'), tags(
        'keys', 'analog',
    )),

    # -Atom Hub-
    product('Atom Hub', 'A day in the park', kontakt, tags(
        'kontakt', 'drums', 'acoustic',
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

    # -Bolder Sounds-
    product('Bolder Sounds', 'Harmoniums of the Opera', kontakt, tags(
        'harmonium', 'kontakt', 'acoustic',
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

    # -Fluffy Audio-
    product('Fluffy Audio', 'Simple Flute', kontakt, tags(
        'kontakt', 'acoustic', 'flute', 'free',
    )),

    # -FXpansion-
    product('FXpansion', 'Amber', aumu('FXPN', 'AMBR'), tags(
        'analog', 'string', 'ensemble',
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

    # -IRCAM-
    product('IRCAM', 'IM-SuperVPSynth', livefx, tags(
        'special', 'creative', 'sampler', 'stretch', 'IRCAM',
        'Live', 'maxforlive', 'latency',
    )),

    # -iZotope-
    product('iZotope', 'IRIS 2', aumu('iZtp', 'Zir2'), tags(
        'synth', 'spectral', 'sampler',
    )),

    # -Korg-
    product('Korg', 'M1', aumu('KORG', 'KLM1'), tags(
        'synth', 'digital',
    )),
    product('Korg', 'Mono/poly', aumu('KORG', 'KLMP'), tags(
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

    # -Modartt-
    product('Modartt', 'Pianoteq 5', aumu('Mdrt', 'Pt5q'), tags(
        'piano', 'acoustic', 'physmod', 'keys', 'chromatic', 'microtonal',
    )),
    product('Modartt', 'Electric Pianos', aumu('Mdrt', 'Pt5q'), tags(
        'keys',
    )),
    product('Modartt', 'Celeste', aumu('Mdrt', 'Pt5q'), tags(
        'chromatic', 'acoustic',
    )),
    product('Modartt', 'Xylo', aumu('Mdrt', 'Pt5q'), tags(
        'chromatic', 'acoustic',
    )),
    product('Modartt', 'Vibes', aumu('Mdrt', 'Pt5t'), tags(
        'chromatic', 'acoustic',
    )),

    # -Modwheel-
    product('Modwheel', 'The Lowdown', kontakt, tags(
        'bass', 'string', 'bow', 'acoustic', 'kontakt', 'upright',
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
    product('Native Instruments', 'Kontakt 5', kontakt, tags(
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
        'strings', 'ensemble', 'acoustic', 'kontakt',
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
    product('New Sonic Arts', 'Nuance', aumu('NSA_', '000C240A'), tags(
        'sampler', 'simple',
    )),
    product('New Sonic Arts', 'Vice', aumu('NSA_', '000CB881'), tags(
        'sampler', 'loop', 'rex', 'simple',
    )),

    # -Orange Tree-
    product('Orange Tree', 'Angelic Harp', kontakt, tags(
        'string', 'acoustic', 'kontakt', 'harp',
    )),
    product('Orange Tree', 'Angelic Zither', kontakt, tags(
        'string', 'acoustic', 'kontakt', 'zither',
    )),
    product('Orange Tree', 'Grand Kalimba', kontakt, tags(
        'string', 'acoustic', 'kontakt', 'kalimba',
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
    product('ReFX', 'QuadraSID', aumu('reFX', 'QSID'), tags(
        'synth', 'sid', 'digital', 'retro',
    )),

    # -Roland-
    product('Roland', 'SH-2', aumu('Rlnd', 'Vas1'), tags(
        'mono', 'analog', 'subtractive',
    )),

    product('Roland', 'SH-101', aumu('Rlnd', 'Vas0'), tags(
        'mono', 'analog', 'subtractive',
    )),

    # -Skinnerbox-
    product('Skinnerbox', 'Time & Timbre', live, tags(
        'drums', 'synth', 'Live', 'maxforlive'
    )),

    # -Soniccharge-
    product('Soniccharge', 'Microtonic', aumu('NuEd', 'NuMT'), tags(
        'drums', 'synth',
    )),

    # -Soniccouture-
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
    product('SoundDUST', 'idstrument suite', kontakt, tags(
        'div', 'kontakt', 'drums', 'synth', 'guitar',
    )),
    product('SoundDUST', 'Orgone', kontakt, tags(
        'kontakt', 'synth', 'sampled',
    )),
    product('SoundDUST', 'Plastic Ghost Piano', kontakt, tags(
        'kontakt', 'synth', 'sampled', 'piano',
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

    # -Spitfire-
    product('Spitfire', 'Artisan Cello', kontakt, tags(
        'strings', 'cello', 'solo', 'acoustic', 'kontakt',
    )),
    product('Spitfire', 'LABS Bike Bells', kontakt, tags(
        'bell', 'acoustic', 'kontakt',
    )),
    product('Spitfire', 'LABS Mandolin', kontakt, tags(
        'mandolin', 'acoustic', 'kontakt',
    )),
    product('Spitfire', 'LABS Melodica', kontakt, tags(
        'melodica', 'acoustic', 'kontakt',
    )),
    product('Spitfire', 'LABS Scary Strings', kontakt, tags(
        'strings', 'acoustic', 'kontakt', 'eerie',
    )),

    # -Twisted Tools-
    product('Twisted Tools', 'Ultraloop', reaktor, tags(
        'loop', 'creative', 'FSU', 'drums', 'percussion', 'sampler',
    )),
    product('Twisted Tools', 'Vortex', reaktor, tags(
        'loop', 'creative', 'FSU', 'drums', 'percussion', 'sampler',
    )),


    # -Uhe-
    product('u-he', 'Bazille', aumu('UHfX', 'UpH4'), tags(
        'synth', 'analog', 'phase modulation', 'FM', 'modular',
    )),
    product('u-he', 'Diva', aumu('UHfX', 'DiVa'), tags(
        'synth', 'analog', 'digital', 'subtractive',
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
        'contrabass', 'acoustic', 'special', 'avant', 'IRCAM',
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

    # -Wave Alchemy-
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
    product('XILS', 'PolyKB II', aumu('Xils', 'pKB2'), tags(
        'synth', 'analog',
    )),
    product('XILS', 'SynX', aumu('Xils', 'XiSy'), tags(
        'synth', 'analog',
    )),
    product('XILS', 'XILS 3.2', aumu('Xils', 'XVc2'), tags(
        'synth', 'analog',
    )),
    product('XILS', 'XILS 4', aumu('Xils', 'x3Di'), tags(
        'synth', 'analog',
    )),
}


FX = {
    # -2c Audio-
    product('2c Audio', 'Kaleidoscope', aufx('2cau', '2cks'), tags(
        'special', 'creative', 'granular', 'spectral', 'resonator',
    )),


    # -Abbey Road-
    product('Abbey Road', 'EMI RS 124 LE', aufx('AbRd', 'R124'), tags(
        'dynamics', 'character', 'compressor',
    )),
    product('Abbey Road', 'EMI TG12412', aufx('AbRd', 'TGeq'), tags(
        'eq', 'character',
    )),
    product('Abbey Road', 'EMI TG12414', aufx('AbRd', 'TGfi'), tags(
        'eq', 'character', 'filter',
    )),
    product('Abbey Road', 'EMI TG12413 1969', aufx('AbRd', 'TG69'), tags(
        'dynamics', 'compressor', 'limiter',
    )),
    product('Abbey Road', 'EMI TG12413 2005', aufx('AbRd', 'TG05'), tags(
        'dynamics', 'compressor', 'limiter',
    )),

    # -Airwindows-
    product('Airwindows', 'Pressure 3', aufx('Dthr', 'prs3'), tags(
        'dynamics', 'free', 'compressor',
    )),
    product('Airwindows', 'Channel 4', aufx('Dthr', 'cha4'), tags(
        'character', 'free', 'analog',
    )),
    product('Airwindows', 'DeRez', aufx('Dthr', 'derz'), tags(
        'character', 'distortion', 'bitcrusher', 'free',
    )),
    product('Airwindows', 'DustBunny', aufx('Dthr', 'dbny'), tags(
        'character', 'distortion', 'vinyl', 'free',
    )),
    product('Airwindows', 'TapeFat', aufx('Dthr', 'tayp'), tags(
        'character', 'filter', 'tape', 'free',
    )),

    # -Amazing Noises-
    product('Amazing Noises', 'Grip', livefx, tags(
        'special', 'spectral', 'creative', 'Live', 'maxforlive',
    )),
    product('Amazing Noises', 'Spectrum Runner', livefx, tags(
        'special', 'spectral', 'creative', 'Live', 'maxforlive',
    )),

    # -Apple-
    product('Apple', 'AUDistortion', aufx('aapl', '????'), tags(
        'distortion', 'character', 'free', 'bitcrusher', 'special',
    )),

    # -Apple Logic Pro X-
    product('Apple', 'Delay Designer', logic, tags(
        'logic', 'delay',
        'logic:delay',
    )),
    product('Apple', 'Bitcrusher', logic, tags(
        'logic', 'bitcrusher', 'distortion', 'character',
        'logic:distortion',
    )),
    product('Apple', 'EVOC Filterbank', logic, tags(
        'logic', 'vocoder', 'special', 'filter',
        'logic:filter',
    )),
    product('Apple', 'EVOC Track Oscillator', logic, tags(
        'logic', 'vocoder', 'special', 'filter', 'sidechain',
        'logic:filter',
    )),
    product('Apple', 'Modulation Delay', logic, tags(
        'logic', 'modulation', 'special', 'zipper-noise',
        'logic:modulation',
    )),
    product('Apple', 'Ringshifter', logic, tags(
        'logic', 'modulation', 'special', 'ringmod', 'delay',
        'logic:modulation', 'sidechain',
    )),
    product('Apple', 'Rotor Cabinet', logic, tags(
        'logic', 'amp', 'cabinet', 'modulation', 'character',
        'logic:modulation',
    )),
    product('Apple', 'Scanner Vibrato', logic, tags(
        'logic', 'modulation', 'vibrato', 'character',
        'logic:modulation',
    )),
    product('Apple', 'Spreader', logic, tags(
        'logic', 'modulation', 'chorus', 'character', 'imaging',
        'logic:modulation',
    )),
    product('Apple', 'Vocal Transformer', logic, tags(
        'logic', 'special', 'vocal', 'pitch',
        'logic:pitch',
    )),
    product('Apple', 'SubBass', logic, tags(
        'logic', 'special', 'pitch', 'bass',
        'logic:specialized',
    )),
    product('Apple', 'Denoiser', logic, tags(
        'logic', 'special', 'noise', 'spectral',
        'logic:specialized',
    )),
    product('Apple', 'Exciter', logic, tags(
        'logic', 'special', 'zipper-noise',
        'logic:specialized',
    )),
    product('Apple', 'Phase Distortion', logic, tags(
        'logic', 'distortion', 'monitor-option',
        'logic:distortion',
    )),

    # -Audio Ease-
    product('Audio Ease', 'Altiverb 7', aufx('AEas', 'AVr5'), tags(
        'reverb', 'delay', 'special',
    )),
    product('Audio Ease', 'Speakerphone 2', aufx('AEas', 'SpVl'), tags(
        'special', 'character', 'eq',
    )),

    # -Brainworx-
    product('Brainworx', 'bx_solo', aufx('Brwx', 'bxs2'), tags(
        'imaging', 'free',
    )),
    product('Brainworx', 'bx_cleansweep', aufx('Brwx', 'bxsl'), tags(
        'eq', 'filter',
    )),

    # -Celemony-
    product('Celemony', 'Melodyne Editor', aumf('CLMY', 'MPLG'), tags(
        'vocal', 'special', 'creative', 'pitch',
    )),

    # -Eiosis-
    product('Eiosis', 'AirEQ', aufx('Eios', 'AEq5'), tags(
        'eq', 'character',
    )),

    # -Eventide-
    product('Eventide', '2016 Stereo Room', aufx('TIDE', '22SR'), tags(
        'reverb',
    )),
    product('Eventide', 'Blackhole', aufx('TIDE', 'HOLE'), tags(
        'reverb', 'delay', 'special',
    )),
    product('Eventide', 'H3000 Factory', aufx('TIDE', 'Fact'), tags(
        'pitch', 'delay', 'special', 'sidechain',
    )),
    product('Eventide', 'Omnipressor', aufx('TIDE', 'Omni'), tags(
        'dynamics', 'special', 'compressor', 'expander', 'character',
        'saturation', 'sidechain',
    )),
    product('Eventide', 'UltraChannel', aufx('Tide', 'UlCh'), tags(
        'dynamics', 'delay', 'eq', 'character', 'saturation', 'pitch',
        'compressor', 'sidechain',
    )),
    product('Eventide', 'UltraReverb', aufx('Tide', 'Revb'), tags(
        'reverb', 'delay', 'special', 'compressor', 'character',
        'distortion', 'sidechain',
    )),

    # -Exponential Audio-
    product('Exponential Audio', 'PhoenixVerb', aufx('EXPa', 'MCsr'), tags(
        'reverb',
    )),
    product('Exponential Audio', 'R2', aufx('EXPa', 'MCs2'), tags(
        'reverb',
    )),

    # -Flux-
    product('Flux', 'Alchemist', aufx('Fspd', 'fxAl'), tags(
        'dynamics', 'special', 'multiband', 'compressor', 'mix', 'mastering',
    )),
    product('Flux', 'Elixir', aufx('Fspd', 'Flxr'), tags(
        'dynamics', 'limiter', 'mix', 'mastering',
    )),
    product('Flux', 'Epure', aufx('Fspd', 'Ftst'), tags(
        'eq', 'mix', 'mastering',
    )),
    product('Flux', 'Pure Compressor', aufx('Fspd', 'fxPc'), tags(
        'dynamics', 'compressor', 'mix', 'sidechain',
    )),
    product('Flux', 'Pure DCompressor', aufx('Fspd', 'fxDc'), tags(
        'dynamics', 'decompressor', 'mix', 'sidechain',
    )),
    product('Flux', 'Pure DExpander', aufx('Fspd', 'fxDx'), tags(
        'dynamics', 'deexpander', 'mix', 'sidechain',
    )),
    product('Flux', 'Pure Expander', aufx('Fspd', 'fxEx'), tags(
        'dynamics', 'expander', 'mix', 'sidechain',
    )),
    product('Flux', 'Pure Limiter', aufx('Fspd', 'fxPl'), tags(
        'dynamics', 'limiter', 'mix',
    )),
    product('Flux', 'Solera', aufx('Fspd', 'fxSo'), tags(
        'dynamics', 'compressor', 'decompressor', 'expander', 'deexpander',
        'mix', 'mastering', 'sidechain',
    )),
    product('Flux', 'StereoToolV3', aufx('Fspd', 'fxSt'), tags(
        'imaging', 'free',
    )),
    product('Flux', 'Syrah', aufx('Fspd', 'fxSy'), tags(
        'dynamics', 'mix', 'mastering', 'bus', 'track', 'compression',
        'special', 'M/S'
    )),

    # -Focusrite-
    product('Focusrite', 'RED 2 EQ', aufx('FCUS', 'rd2E'), tags(
        'eq',
    )),
    product('Focusrite', 'RED 3 Compressor', aufx('FCUS', 'rd3C'), tags(
        'compressor', 'character', 'dynamics',
    )),


    # -FXpansion-
    product('FXpansion', 'Bloom', aumf('FXPN', 'FXBL'), tags(
        'delay', 'special',
    )),
    product('FXpansion', 'Etch', aumf('FXPN', 'FXET'), tags(
        'filter', 'special',
    )),
    product('FXpansion', 'Maul', aumf('FXPN', 'FXMA'), tags(
        'distortion', 'special',
    )),

    # -Goodhertz-
    product('Goodhertz', 'Faraday Limiter', aufx('GDHZ', 'FDLM'), tags(
        'dynamics', 'limiter', 'character',
    )),
    product('Goodhertz', 'Lossy', aufx('GDHZ', 'LSSY'), tags(
        'special', 'character',
    )),

    # -Illformed-
    product('Illformed', 'Glitch2', aumu('DBlu', 'igl2'), tags(
        'special', 'FSU', 'mfx',
    )),

    # -Ina-GRM-
    product('Ina-GRM', 'Band pass', aumf('Grm ', 'BaPS'), tags(
        'special', 'filter', 'grm',
    )),
    product('Ina-GRM', 'Comb filters', aumf('Grm ', 'Comb'), tags(
        'special', 'filter', 'grm',
    )),
    product('Ina-GRM', 'Contrast', aumf('Grm ', 'ctrG'), tags(
        'special', 'spectral', 'grm',
    )),
    product('Ina-GRM', 'Delays', aumf('Grm ', 'Dely'), tags(
        'special', 'delay', 'grm',
    )),
    product('Ina-GRM', 'Doppler', aumf('Grm ', 'DopS'), tags(
        'special', 'delay', 'imaging', 'grm',
    )),
    product('Ina-GRM', 'Evolution', aumf('Grm ', 'GrEv'), tags(
        'special', 'grm',
    )),
    product('Ina-GRM', 'Equalize', aumf('Grm ', 'EquS'), tags(
        'special', 'spectral', 'grm',
    )),
    product('Ina-GRM', 'Freeze', aumf('Grm ', 'Free'), tags(
        'special', 'granular', 'grm',
    )),
    product('Ina-GRM', 'Fusion', aumf('Grm ', 'GFus'), tags(
        'special', 'grm',
    )),
    product('Ina-GRM', 'Grinder', aumf('Grm ', 'Cruh'), tags(
        'special', 'grm', 'sidechain',
    )),
    product('Ina-GRM', 'Pitch Accum', aumf('Grm ', 'Pitc'), tags(
        'special', 'grm',
    )),
    product('Ina-GRM', 'Reson', aumf('Grm ', 'Reso'), tags(
        'special', 'grm',
    )),
    product('Ina-GRM', 'FreqShift', aumf('Grm ', 'FrsG'), tags(
        'special', 'spectral', 'grm',
    )),
    product('Ina-GRM', 'Shuffling', aumf('Grm ', 'Shuf'), tags(
        'special', 'delay', 'grm', 'sidechain',
    )),
    product('Ina-GRM', 'FreqWarp', aumf('Grm ', 'Fw G'), tags(
        'special', 'spectral', 'grm',
    )),

    # -IRCAM-
    product('IRCAM', 'IM-FXSequencer', livefx, tags(
        'special', 'creative', 'FSU', 'Live', 'maxforlive',
    )),
    product('IRCAM', 'IM-MultibandDelay', livefx, tags(
        'special', 'creative', 'spectral', 'delay', 'IRCAM',
        'Live', 'maxforlive',
    )),
    product('IRCAM', 'IM-SimpleTransp', livefx, tags(
        'special', 'creative', 'pitch', 'stretch', 'IRCAM',
        'Live', 'maxforlive',
    )),
    product('IRCAM', 'IM-Scrub', livefx, tags(
        'special', 'creative', 'pitch', 'stretch', 'IRCAM',
        'Live', 'maxforlive',
    )),
    product('IRCAM', 'IM-Mover', livefx, tags(
        'special', 'creative', 'pitch', 'stretch', 'IRCAM',
        'Live', 'maxforlive',
    )),

    # -iZotope-
    product('iZotope', 'RX 4 Declicker', aufx('iZtp', 'Zn4K'), tags(
        'special', 'creative', 'restoration',
    )),
    product('iZotope', 'RX 4 Decrackler', aufx('iZtp', 'Zn4C'), tags(
        'special', 'creative', 'restoration',
    )),
    product('iZotope', 'RX 4 Denoiser', aufx('iZtp', 'Zn4N'), tags(
        'special', 'creative', 'restoration',
    )),
    product('iZotope', 'Nectar Elements', aufx('iZtp', 'ZnNE'), tags(
        'vocal', 'strip',
    )),
    product('iZotope', 'Vinyl', aufx('iZtp', 'Vnyl'), tags(
        'special', 'character', 'free',
    )),

    # -K-Devices-
    product('K-Devices', 'Holder', livefx, tags(
        'special', 'spectral', 'creative', 'freeze', 'Live', 'maxforlive',
    )),
    product('K-Devices', 'Alter Echo', livefx, tags(
        'special', 'creative', 'delay', 'Live', 'maxforlive',
    )),

    # -Kush Audio-
    product('Kush Audio', 'Clariphonic', aufx('Kush', 'clar'), tags(
        'eq', 'exciter'
    )),
    product('Kush Audio', 'Pusher', aufx('Kush', 'Push'), tags(
        'distortion', 'character',
    )),
    product('Kush Audio', 'UBK-1', aufx('KuSh', 'dcmp'), tags(
        'dynamics', 'character', 'special', 'compressor', 'saturation',
    )),

    # -Lexicon-
    product('Lexicon', 'Chamber PCM', aufx('Lexi', 'Lcm1'), tags(
        'reverb',
    )),
    product('Lexicon', 'Chorus', aufx('Lexi', 'Lcr1'), tags(
        'chorus', 'delay',
    )),
    product('Lexicon', 'Concert Hall PCM', aufx('Lexi', 'Lch1'), tags(
        'reverb',
    )),
    product('Lexicon', 'DualDelay', aufx('Lexi', 'Ldd1'), tags(
        'delay',
    )),
    product('Lexicon', 'Hall PCM', aufx('Lexi', 'Lhl1'), tags(
        'reverb',
    )),
    product('Lexicon', 'MultivoiceShift', aufx('Lexi', 'Lmp1'), tags(
        'pitch', 'special', 'delay',
    )),
    product('Lexicon', 'Pitchshift', aufx('Lexi', 'Lsp1'), tags(
        'pitch', 'special',
    )),
    product('Lexicon', 'Plate PCM', aufx('Lexi', 'Lpl1'), tags(
        'reverb',
    )),
    product('Lexicon', 'RandomDelay', aufx('Lexi', 'Lrd1'), tags(
        'delay', 'special',
    )),
    product('Lexicon', 'RandomHall PCM', aufx('Lexi', 'Lrh1'), tags(
        'reverb',
    )),
    product('Lexicon', 'ResonantChords', aufx('Lexi', 'Lrc1'), tags(
        'delay', 'pitch', 'special',
    )),
    product('Lexicon', 'Room PCM', aufx('Lexi', 'Lrm1'), tags(
        'reverb',
    )),
    product('Lexicon', 'StringBox', aufx('Lexi', 'Sbx1'), tags(
        'reverb', 'pitch', 'special',
    )),
    product('Lexicon', 'VintagePlate PCM', aufx('Lexi', 'Lpl0'), tags(
        'reverb',
    )),

    # -Little Endian-
    product('Little Endian', 'SpectrumWorx', aufx('LE00', 'SW00'), tags(
        'spectral', 'special', 'sidechain',
    )),

    # -McDSP-
    product('McDSP', 'Analog Channel AC101', aufx('McDP', 'AC01'), tags(
        'distortion', 'character',
    )),
    product('McDSP', 'Analog Channel AC202', aufx('McDP', 'AC02'), tags(
        'distortion', 'character', 'tape',
    )),
    product('McDSP', 'FutzBox', aufx('McDP', 'Futz'), tags(
        'special', 'eq', 'distortion', 'character',
    )),

    # -MeldaProduction-
    product('MeldaProduction', 'MMultibandGranular', aumf('Meld', 'MMGr'), tags(
        'granular', 'special', 'sidechain',
    )),

    # -Metric Halo-
    product('Metric Halo', 'Dirty Delay', aufx('MHL ', 'DELY'), tags(
        'delay',
    )),

    # -Native Instruments-
    product('Native Instruments', 'Driver', aufx('-NI-', 'Ni$='), tags(
        'distortion', 'character', 'sidechain',
    )),
    product('Native Instruments', 'Reaktor 5 FX', aumf('-NI-', 'NiR5'), tags(
        'modular', 'sidechain',
    )),
    product('Native Instruments', 'Guitar Rig 5', aumf('-NI-', 'NiG5'), tags(
        'guitar', 'strip', 'sidechain', 'amp',
    )),
    product('Native Instruments', 'Solid Bus Comp', aufx('-NI-', 'Ni$6'), tags(
        'compression', 'dynamics',
    )),
    product('Native Instruments', 'Solid Dynamics', aufx('-NI-', 'Ni$7'), tags(
        'dynamics',
    )),
    product('Native Instruments', 'Solid EQ', aufx('-NI-', 'Ni$8'), tags(
        'eq',
    )),
    product('Native Instruments', 'Supercharger GT', aufx('-NI-', 'Ni$A'), tags(
        'compression', 'character', 'distortion', 'dynamics', 'sidechain',
    )),
    product('Native Instruments', 'Transient Master', aufx('-NI-', 'Ni$5'), tags(
        'dynamics', 'transient shaper',
    )),
    product('Native Instruments', 'Replika', aufx('-NI-', 'Ni$B'), tags(
        'delay', 'reverb'
    )),

    # -Plogue-
    product('Plogue', 'Chipcrusher', aufx('PLOG', 'PLGP'), tags(
        'character', 'distortion', 'bitcrush', 'latency',
    )),

    # -Relab-
    product('Relab', 'LX480 Complete', aufx('RELB', 'LX4C'), tags(
        'reverb', 'delay', 'retro',
    )),

    # -SampleSumo-
    product('SampleSumo', 'SaltyGrain', aumf('SaSu', 'StGr'), tags(
        'granular', 'delay', 'pitch', 'mfx',
    )),

    # -Slate Digital-
    product('Slate Digital', 'FG-116 (VMR)', aufx('SlDg', 'VMXR'), tags(
        'dynamics', 'character', 'compressor',
    )),
    product('Slate Digital', 'FG-401 (VMR)', aufx('SlDg', 'VMXR'), tags(
        'dynamics', 'character', 'compressor',
    )),
    product('Slate Digital', 'FG-N (VMR)', aufx('SlDg', 'VMXR'), tags(
        'eq', 'character',
    )),
    product('Slate Digital', 'FG-S (VMR)', aufx('SlDg', 'VMXR'), tags(
        'eq', 'character',
    )),
    product('Slate Digital', 'Revival (VMR)', aufx('SlDg', 'VMXR'), tags(
        'exciter', 'character', 'free',
    )),
    product('Slate Digital', 'FG-Grey (VBC)', aufx('SlDg', 'VBCg'), tags(
        'dynamics', 'mix', 'compressor',
    )),
    product('Slate Digital', 'FG-MU (VBC)', aufx('SlDg', 'VBCm'), tags(
        'dynamics', 'mix', 'compressor',
    )),
    product('Slate Digital', 'FG-Red (VBC)', aufx('SlDg', 'VBCr'), tags(
        'dynamics', 'mix', 'compressor',
    )),

    # -Smartelectronix-
    product('Smartelectronix', 'Ambience', aufx('MagJ', '07C0BCD2'), tags(
        'reverb', 'free',
    )),
    product('Smartelectronix', 'Bouncy', aufx('BrDJ', 'BNCY'), tags(
        'delay', 'special', 'free', 'zipper-noise',
    )),
    product('Smartelectronix', 'Buffer Override', aumf('DFX!', 'buff'), tags(
        'special', 'free', 'FSU',
    )),
    product('Smartelectronix', 'Geometer', aumf('DFX!', 'DFgr'), tags(
        'special', 'character', 'free', 'distoration', 'waveshaper',
    )),
    product('Smartelectronix', 'Monomaker', aufx('DFX!', 'mono'), tags(
        'imaging', 'character', 'free', 'zipper-noise',
    )),
    product('Smartelectronix', 'Polarizer', aufx('DFX!', 'pola'), tags(
        'character', 'bitcrusher', 'free', 'distortion',
    )),
    product('Smartelectronix', 'Scrubby', aumf('DFX!', 'scub'), tags(
        'special', 'free', 'pitch',
    )),
    product('Smartelectronix', 'Skidder', aumf('DFX!', 'skid'), tags(
        'tremolo', 'special', 'free',
    )),
    product('Smartelectronix', 'Transverb', aumf('DFX!', 'DFtv'), tags(
        'delay', 'special', 'pitch', 'free',
    )),

    # -Softube-
    product('Softube', 'Abbey Road RS137 Box', aufx('AbRd', 'r127'), tags(
        'eq', 'character', 'exciter',
    )),
    product('Softube', 'Abbey Road RS137 Rack', aufx('AbRd', 'g127'), tags(
        'eq', 'character', 'exciter',
    )),
    product('Softube', 'Abbey Road RS135', aufx('AbRd', '8kbx'), tags(
        'eq', 'character', 'exciter',
    )),
    product('Softube', 'Acoustic Feedback', aufx('SfTb', 'FbAU'), tags(
        'guitar', 'special',
    )),
    product('Softube', 'Active Equalizer', aufx('SfTb', 'AcEQ'), tags(
        'eq', 'character',
    )),
    product('Softube', 'Bass Amp Room', aufx('SfTb', 'BARn'), tags(
        'amp', 'distortion', 'character',
    )),
    product('Softube', 'FET Compressor', aufx('SfTb', 'FcPn'), tags(
        'character', 'dynamics', 'compressor', 'saturation',
        'sidechain',
    )),
    product('Softube', 'Focusing Equalizer', aufx('SfTb', 'ChEq'), tags(
        'eq', 'character',
    )),
    product('Softube', 'Metal Amp Room', aufx('SfTb', 'Mtal'), tags(
        'amp', 'distortion', 'character',
    )),
    product('Softube', 'Mutronics Mutator', aufx('SfTb', 'z9x7'), tags(
        'character', 'filter', 'eq', 'sidechain',
    )),
    product('Softube', 'Passive-Active Pack', aufx('SfTb', 'PvEQ'), tags(
        'character', 'eq',
    )),
    product('Softube', 'Saturation Knob', aufx('SfTb', 'satn'), tags(
        'character',
    )),
    product('Softube', 'Spring Reverb', aufx('SfTb', 'SpRn'), tags(
        'reverb',
    )),
    product('Softube', 'Summit Audio EQF-100', aufx('SfTb', 'e100'), tags(
        'character', 'eq',
    )),
    product('Softube', 'Summit Audio Grand Channel', aufx('SfTb', 'SAGC'), tags(
        'character', 'eq', 'dynamics', 'compressor', 'saturation',
        'sidechain',
    )),
    product('Softube', 'Summit Audio TLA-100A', aufx('SfTb', 't100'), tags(
        'character', 'dynamics', 'compressor', 'saturation',
        'sidechain',
    )),
    product('Softube', 'Tonelux Tilt', aufx('SfTb', 'Tilt'), tags(
        'eq',
    )),
    product('Softube', 'Transient Shaper', aufx('SfTb', 'Shpe'), tags(
        'eq',
    )),
    product('Softube', 'Trident A-Range', aufx('SfTb', 'Aran'), tags(
        'character', 'eq', 'saturation',
    )),
    product('Softube', 'TSAR-1', aufx('SfTb', 'tsar'), tags(
        'reverb',
    )),
    product('Softube', 'TSAR-1R', aufx('SfTb', 'ts1r'), tags(
        'reverb',
    )),
    product('Softube', 'Tube Delay', aufx('SfTb', 'TbDe'), tags(
        'delay', 'character', 'saturation',
    )),
    product('Softube', 'Tube-Tech CL 1B', aufx('SfTb', 'clST'), tags(
        'character', 'dynamics', 'compressor', 'saturation',
        'sidechain',
    )),
    product('Softube', 'Tube-Tech Classic Channel', aufx('SfTb', 'TTCC'), tags(
        'character', 'dynamics', 'eq', 'compressor', 'saturation',
        'sidechain',
    )),
    product('Softube', 'Tube-Tech ME 1B', aufx('SfTb', 'ME1B'), tags(
        'character', 'eq', 'saturation',
    )),
    product('Softube', 'Tube-Tech PE 1C', aufx('SfTb', 'PE1C'), tags(
        'character', 'eq', 'saturation',
    )),
    product('Softube', 'Valley People Dyna-mite', aufx('SfTb', 'DaMt'), tags(
        'character', 'dynamics', 'gate', 'expander', 'ducking', 'keying',
        'compressor', 'saturation', 'sidechain',
    )),
    product('Softube', 'Vintage Amp Room', aufx('SfTb', 'ViAU'), tags(
        'amp', 'distortion', 'character',
    )),
    product('Softube', 'White Amp', aufx('SfTb', 'WAmp'), tags(
        'amp', 'distortion', 'character',
    )),

    # -Soniccharge-
    product('Soniccharge', 'Bitspeek', aumf('NuEd', 'NuSq'), tags(
        'vocal', 'special',
    )),
    product('Soniccharge', 'Permut8', aumf('NuEd', 'NuPR'), tags(
        'FSU', 'special',
    )),

    # -Sonnox-
    product('Sonnox', 'Oxford Dynamics', aufx('Sony', 'OxDy'), tags(
        'dynamics', 'character', 'compressor', 'gate', 'expander', 'limiter',
        'saturation', 'sidechain',
    )),
    product('Sonnox', 'Oxford Inflator', aufx('Sony', 'Oxln'), tags(
        'dynamics', 'exciter', 'character',
    )),
    product('Sonnox', 'Oxford Limiter', aufx('Sony', 'OxLm'), tags(
        'dynamics', 'character', 'limiter',
    )),
    product('Sonnox', 'Oxford TransMod', aufx('Sony', 'OxTM'), tags(
        'character', 'dynamics', 'transient shaper', 'distortion',
    )),

    # -Soundhack-
    product('Soundhack', '+bubbler', aumf('SDHK', '+bub'), tags(
        'granular', 'delay', 'special',
    )),
    product('Soundhack', '+chebyshev', aufx('SDHK', '+chb'), tags(
        'distortion', 'special',
    )),
    product('Soundhack', '+compand', aufx('SDHK', 'ercm'), tags(
        'dynamics', 'free',
    )),
    product('Soundhack', '+decimate', aufx('SDHK', 'er10'), tags(
        'character', 'bitcrush', 'free',
    )),
    product('Soundhack', '+delay', aumf('SDHK', '+dla'), tags(
        'delay', 'free',
    )),
    product('Soundhack', '+matrix', aufx('SDHK', '+mtx'), tags(
        'special', 'free',
    )),
    product('Soundhack', '+morphfilter', aumf('SDHK', '+mrf'), tags(
        'spectral', 'special', 'filter',
    )),
    product('Soundhack', '+phasemash (pvoc)', aumf('SDHK', '+pvx'), tags(
        'special',
    )),
    product('Soundhack', '+phasor', aumf('SDHK', '+phz'), tags(
        'special', 'phaser', 'free',
    )),
    product('Soundhack', '+pitchdelay', aumf('SDHK', '+pdl'), tags(
        'delay', 'pitch', 'special',
    )),
    product('Soundhack', '+pitchsift (pvoc)', aumf('SDHK', '+pvp'), tags(
        'vocoder', 'pitch', 'harmonics', 'special',
    )),
    product('Soundhack', '+spectralcompand', aumf('SDHK', '+spx'), tags(
        'spectral', 'special', 'eq',
    )),
    product('Soundhack', '+spectralgate', aumf('SDHK', '+spg'), tags(
        'spectral', 'special', 'dynamics', 'gate',
    )),
    product('Soundhack', '+spiralstretch (pvoc)', aumf('SDHK', '+pvm'), tags(
        'granular', 'special',
    )),

    # -Soundtoys-
    product('Soundtoys', 'Crystallizer', aufx('SToy', 'CR  '), tags(
        'granular', 'delay', 'special',
    )),
    product('Soundtoys', 'Decapitator', aufx('SToy', 'DEC '), tags(
        'character', 'distortion',
    )),
    product('Soundtoys', 'DevilLoc', aufx('SToy', 'DVL '), tags(
        'dynamics', 'character', 'distortion', 'limiter', 'compressor',
    )),
    product('Soundtoys', 'DevilLoc Deluxe', aufx('SToy', 'DLD '), tags(
        'dynamics', 'character', 'distortion', 'limiter', 'compressor',
    )),
    product('Soundtoys', 'Echoboy', aufx('SToy', 'EB  '), tags(
        'character', 'delay', 'distortion',
    )),
    product('Soundtoys', 'Filterfreak1', aufx('SToy', 'FF1 '), tags(
        'character', 'filter', 'special',
    )),
    product('Soundtoys', 'Filterfreak2', aufx('SToy', 'FF2 '), tags(
        'character', 'filter', 'special',
    )),
    product('Soundtoys', 'Little Microshift', aufx('SToy', 'LMS '), tags(
        'delay', 'pitch',
    )),
    product('Soundtoys', 'Little Primaltap', aufx('SToy', 'LPT '), tags(
        'delay', 'special', 'character', 'zipper-noise',
    )),
    product('Soundtoys', 'Little Radiator', aufx('SToy', 'LRD '), tags(
        'character', 'amp',
    )),
    product('Soundtoys', 'Microshift', aufx('SToy', 'MCS '), tags(
        'delay', 'pitch',
    )),
    product('Soundtoys', 'Panman', aufx('SToy', 'PMN '), tags(
        'imaging', 'character',
    )),
    product('Soundtoys', 'Phase Mistress', aufx('SToy', 'PM  '), tags(
        'special', 'character',
    )),
    product('Soundtoys', 'Radiator', aufx('SToy', 'RAD '), tags(
        'character', 'amp',
    )),
    product('Soundtoys', 'Tremolator', aufx('SToy', 'TRM '), tags(
        'special', 'character',
    )),

    # -SPL-
    product('SPL', 'DeVerb', aufx('SPL1', 'SPDV'), tags(
        'dynamics', 'transient shaper',
    )),

    # -Twisted Tools-
    product('Twisted Tools', 'Buffeater', reaktor, tags(
        'midi', 'creative', 'FSU', 'special',
    )),

    # -Unfiltered Audio-
    product('Unfiltered Audio', 'G8 Gate', aumf('UnAu', 'Gate'), tags(
        'dynamics', 'special', 'gate', 'granular',
    )),
    product('Unfiltered Audio', 'Sandman', aufx('UnAu', 'snDM'), tags(
        'delay', 'special',
    )),

    # -Valhalla-
    product('Valhalla', 'Shimmer', aufx('oDin', 'shmr'), tags(
        'reverb', 'special', 'pitch',
    )),

    # -Waves-
    product('Waves', 'The Kings Microphones', aufx('ksWV', 'TKMS'), tags(
        'character', 'special', 'vocal',
    )),


}

INST.update(MFX)
FX.update(MFX)

fx_by_tag = defaultdict(set)
inst_by_tag = defaultdict(set)
fx_by_brand = defaultdict(set)
inst_by_brand = defaultdict(set)

for f in FX:
    fx_by_brand[f.brand].add(f)
    for tag in f.tags:
        fx_by_tag[tag].add(f)
for i in INST:
    inst_by_brand[i.brand].add(i)
    for tag in i.tags:
        inst_by_tag[tag].add(f)


class Collection(object):

    def __init__(self, db):
        self.db = db
        self.by_tag = defaultdict(set)
        self.by_brand = defaultdict(set)
        self._rand_by_tag = None
        self._rand_by_brand = None
        self._most_common = None
        self.update_indices()

    def __iter__(self):
        return iter(self.db)

    def update_indices(self):
        self.by_tag.clear()
        self.by_brand.clear()

        for product in self.db:
            self.by_brand[product.brand].add(product)
            for tag in f.tags:
                self.by_tag[tag].add(product)
        self._rand_by_tag = defaultdict(list)
        self._rand_by_brand = self._prepare_randomness()
        for brand, products in self._rand_by_brand.iteritems():
            for product in products:
                for tag in product.tags:
                    self._rand_by_tag[tag].append(product)

    def _prepare_randomness(self):
        result = defaultdict(list)
        brands = self._most_common = Counter(p.brand for p in self)
        most_total = None
        for i, (brand, total) in enumerate(brands.most_common()):
            if i:
                diff = most_total - total
                products = list(self.by_brand[brand])
                result[brand].extend(products)
                result[brand].extend(
                    products[j % total]
                    for j in range(min(diff, max(total, 8)))
                )
                random.shuffle(result[brand])
            else:
                most_total = total
        return result

    def random_by_tag(self, tag):
        return random.choice(self._rand_by_tag[tag])


effects = Collection(FX)
instruments = Collection(INST)


def find_info(p, key, sep=':'):
    return [t.split(sep) for t in p.tags if t.startswith(key + sep)]


def hp(p, cat=''):
    if 'logic' in p.tags:
        tag, menu = find_info(p, 'logic')[0]
        cat = '({0}:{1})'.format(tag, menu.capitalize())
    return '{0.brand} {0.name} {cat}'.format(p, cat=cat)


def select():
    seen = set()

    def uniq_fx_by_tag(tag):
        while 1:
            r = effects.random_by_tag(tag)
            if r not in seen:
                seen.add(r)
                return r

    return FMT.format(
        inst=hp(random.choice(list(INST))),
        reverb=hp(uniq_fx_by_tag('reverb')),
        delay=hp(uniq_fx_by_tag('delay')),
        special=hp(uniq_fx_by_tag('special')),
        character=hp(uniq_fx_by_tag('character')),
        eq=hp(uniq_fx_by_tag('eq')),
        dynamics=hp(uniq_fx_by_tag('dynamics')),
    )


def main(argv=sys.argv, env=os.environ):
    print(select())


if __name__ == '__main__':
    main()
