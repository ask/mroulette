import random

from collections import defaultdict, namedtuple
from functools import partial

product = namedtuple('product', ('brand', 'name', 'tags'))
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
    product('accSone', 'CrusherX', tags('granular', 'special', 'mfx')),
    product('Antares', 'Harmony Engine EVO', tags(
        'vocal', 'special', 'mfx',
    )),
    product('Cytomic', 'The Drop', tags(
        'filter', 'special', 'eq', 'mfx', 'character',
    )),
    product('Expert Sleepers', 'Crossfade Loop Synth', tags(
        'fx', 'sampler', 'special', 'mfx',
    )),
    product('Olli Larkin', 'Endless Series', tags(
        'mfx', 'special', 'generator',
    )),
    product('XILS', 'Vocoder 5000', tags('vocoder', 'special', 'mfx')),
}

INST = {
    product('Acousticsamples', 'Bassysm-F', tags('bass', 'acoustic')),
    product('Acousticsamples', 'Bassysm-J', tags('bass', 'acoustic')),
    product('Acousticsamples', 'Bassysm-M', tags('bass', 'acoustic')),
    product('Acousticsamples', 'Bassysm-S', tags('bass', 'acoustic')),
    product('Acousticsamples', 'J-Bass', tags('bass', 'acoustic')),
    product('Acousticsamples', 'TheUpright', tags('bass', 'acoustic')),
    product('Acousticsamples', 'GD-6', tags('guitar', 'acoustic')),
    product('Acousticsamples', 'Sunbird', tags('guitar', 'acoustic')),
    product('Acousticsamples', 'Telematic', tags('guitar', 'acoustic')),
    product('Acousticsamples', 'IRCAM Prepared Piano', tags(
        'piano', 'acoustic', 'special',
    )),
    product('Admiral-Quality', 'Poly-Ana', tags('subtractive')),
    product('Air', 'Loom', tags('additive', 'digital')),
    product('Air', 'Vacuum Pro', tags('subtractive', 'analog')),
    product('Air', 'Hybrid', tags('wavetable', 'digital')),
    product('Air', 'Strike', tags('drums')),
    product('Air', 'Structure', tags('sampler')),
    product('Air', 'Velvet', tags('keys')),
    product('Air', 'theRiser', tags('fx', 'special')),
    product('Air', 'Xpand!2', tags('rompler')),
    product('Analogue Drums', 'Boxer', tags(
        'drums', 'kontakt', 'acoustic',
    )),
    product('Analogue Drums', 'FatStacks', tags(
        'drums', 'kontakt', 'acoustic',
    )),
    product('Analogue Drums', 'Kingpin', tags('drums', 'kontakt', 'acoustic')),
    product('Analogue Drums', 'Monotown', tags(
        'drums', 'kontakt', 'acoustic',
    )),
    product('Analogue Drums', 'Pizazz', tags('drums', 'kontakt', 'acoustic')),
    product('Analogue Drums', 'Smoker', tags('drums', 'kontakt', 'acoustic')),
    product('Apple', 'Ultrabeat', tags(
        'logic', 'drums', 'synth', 'logic:inst')),
    product('Apple', 'Sculpture', tags(
        'logic', 'physmod', 'synth', 'logic:inst',
    )),
    product('Apple', 'EVOC 20 PS', tags(
        'logic', 'vocoder', 'digital', 'logic:inst',
    ))
    product('apple', 'EFM1', tags(
        'logic', 'FM', 'digital', 'synth', 'logic:inst',
    ))
    product('apple', 'ES M', tags(
        'logic', 'subtractive', 'mono', 'digital', 'synth', 'logic:inst',
    ))
    product('apple', 'ES P', tags(
        'logic', 'subtractive', 'digital', 'synth', 'logic:inst',
    ))
    product('apple', 'ES1', tags(
        'logic', 'subtractive', 'digital', 'synth', 'logic:inst',
    ))
    product('apple', 'ES2', tags(
        'logic', 'subtractive', 'digital', 'synth', 'logic:inst',
    ))
    product('Arturia', 'Analog Lab', tags('analog')),
    product('Arturia', 'Analog Labratory', tags('analog')),
    product('Arturia', 'ARP 2600 V2', tags('analog', 'subtractive')),
    product('Arturia', 'CS-80 V2', tags('analog', 'subtractive')),
    product('Arturia', 'Jupiter-8 V2', tags('analog', 'subtractive')),
    product('Arturia', 'Matrix-12 V', tags('analog', 'subtractive')),
    product('Arturia', 'Mini V', tags('analog', 'subtractive')),
    product('Arturia', 'Modular V', tags('analog', 'modular')),
    product('Arturia', 'Oberheim SEM V', tags('analog', 'subtractive')),
    product('Arturia', 'Prophet V2', tags('analog', 'subtractive')),
    product('Arturia', 'Solina V', tags('organ', 'analog')),
    product('Arturia', 'Spark', tags('drums')),
    product('Arturia', 'Spark Vintage Drum Machines', tags('drums')),
    product('Arturia', 'Spark Dubstep', tags('drums')),
    product('Arturia', 'Vox V', tags('organ', 'analog')),
    product('Arturia', 'Wurlitzer V', tags('keys', 'analog')),
    product('Atom Hub', 'A day in the park', tags(
        'kontakt', 'drums', 'acoustic',
    )),
    product('Atom Hub', 'Old Mandolin v2', tags('kontakt', 'acoustic')),
    product('Atom Hub', 'Bell from Shelf v2', tags('kontakt', 'acoustic')),
    product('Atom Hub', 'Toolshed', tags('kontakt', 'drums', 'acoustic')),
    product('Audiothing', 'Organetta', tags('kontakt', 'acoustic')),
    product('FXpansion', 'Amber', tags('analog', 'string', 'ensemble')),
    product('FXpansion', 'Cypher', tags('analog', 'FM')),
    product('FXpansion', 'Strobe', tags(
        'analog', 'subtractive', 'mono', 'poly',
    )),
    product('FXpansion', 'Tremor', tags('drums', 'synth')),
    product('FXpansion', 'Geist', tags('drums', 'sampler')),
    product('iZotope', 'IRIS 2', tags('synth', 'spectral', 'sampler')),
    product('Korg', 'M1', tags('synth', 'digital')),
    product('Korg', 'MS-20', tags('analog', 'subtractive')),
    product('Korg', 'Polysix', tags('analog', 'subtractive')),
    product('Korg', 'Mono/poly', tags('analog', 'subtractive')),
    product('Korg', 'Wavestation', tags('digital', 'synth', 'wavetable')),
    product('Loops De La Creme', 'Cymbal Rolls', tags(
        'kontakt', 'acoustic', 'drums',
    )),
    product('Lux/Nox', 'PERC+', tags(
        'kontakt', 'acoustic', 'drums',
    )),
    product('Madrona Labs', 'AAlto', tags(
        'analog', 'mono', 'poly', 'subtractive',
    )),
    product('Madrona Labs', 'Kaivo', tags('granular', 'physmod')),
    product('Modartt', 'Pianoteq 5', tags('piano', 'acoustic')),
    product('Modartt', 'Electric Pianos', tags('keys')),
    product('Modartt', 'Celeste', tags('chromatic', 'acoustic')),
    product('Modartt', 'Xylo', tags('chromatic', 'acoustic')),
    product('Modartt', 'Vibes', tags('chromatic', 'acoustic')),
    product('Modwheel', 'The Lowdown', tags(
        'bass', 'string', 'bow', 'acoustic', 'kontakt',
    )),
    product('New Sonic Arts', 'Granite', tags('granular')),
    product('New Sonic Arts', 'Nuance', tags('sampler')),
    product('New Sonic Arts', 'Vice', tags('sampler', 'loop', 'rex')),
    product('Orange Tree', 'Angelic Harp', tags(
        'string', 'acoustic', 'kontakt',
    )),
    product('Pluginboutique', 'VirtualCZ', tags(
        'synth', 'phase modulation', 'digital',
    )),
    product('ReFX', 'QuadraSID', tags('synth', 'sid', 'digital', 'retro')),
    product('Roland', 'SH-2', tags('mono', 'analog', 'subtractive')),
    product('Sonic Charge', 'Microtonic', tags('drums', 'synth')),
    product('Sonokinetic', 'Hurdy Gurdy', tags(
        'kontakt', 'acoustic',
    )),
    product('Soundguru', 'The Mangle', tags('granular')),
    product('Soundsdivine', 'MM+', tags(
        'synth', 'subtractive', 'kontakt', 'analog',
    )),
    product('Soundsdivine', 'The2600', tags(
        'synth', 'subtractive', 'kontakt', 'analog',
    )),
    product('u-he', 'Diva', tags('analog', 'digital', 'subtractive')),
    product('u-he', 'Podolski', tags('digital', 'free')),
    product('u-he', 'Triple Cheese', tags('digital', 'free')),
    product('UVI', 'Acoustic Toy Museum', tags('acoustic', 'sampled')),
    product('UVI', 'Electric Toy Museum', tags('sampled')),
    product('UVI', 'Digital Synsations', tags('digital', 'synth', 'sampled')),
    product('UVI', 'Emulation One', tags('digital', 'retro', 'sampled')),
    product('UVI', 'Grand Piano Model D', tags('piano', 'sampled')),
    product('UVI', 'Mello', tags('retro', 'sampled')),
    product('UVI', 'Analogic Piano 09', tags('piano', 'sampled')),
    product('Xfer', 'Nerve', tags('drums', 'sampler')),
    product('Xfer', 'Serum', tags('synth', 'digital', 'wavetable')),
    product('XILS', 'PolyKB II', tags('synth', 'analog')),
    product('XILS', 'SynX', tags('synth', 'analog')),
    product('XILS', 'XILS 3', tags('synth', 'analog')),
    product('XILS', 'XILS 4', tags('synth', 'analog')),

}


FX = {
    product('Abbey Road', 'EMI RS 124 LE',
            tags('dynamics', 'character')),
    product('Abbey Road', 'EMI TG12412',
            tags('eq', 'character')),
    product('Abbey Road', 'EMI TG12414',
            tags('eq', 'character', 'filter')),
    product('Airwindows', 'Pressure 3', tags('dynamics', 'free')),
    product('Airwindows', 'Console 4', tags('character', 'free')),
    product('Apple', 'Delay Designer', tags(
        'logic', 'delay',
        'logic:delay',
    )),
    product('Apple', 'Bitcrusher', tags(
        'logic', 'bitcrusher', 'distortion', 'character',
        'logic:distortion',
    )),
    product('Apple', 'EVOC Filterbank', tags(
        'logic', 'vocoder', 'special', 'filter',
        'logic:filter',
    )),
    product('Apple', 'EVOC Track Oscillator', tags(
        'logic', 'vocoder', 'special', 'filter', 'sidechain',
        'logic:filter',
    )),
    product('Apple', 'Modulation Delay', tags(
        'logic', 'modulation', 'special', 'zipper-noise',
        'logic:modulation',
    )),
    product('Apple', 'Ringshifter', tags(
        'logic', 'modulation', 'special', 'ringmod', 'delay',
        'logic:modulation',
    )),
    product('Apple', 'Rotor Cabinet', tags(
        'logic', 'amp', 'cabinet', 'modulation', 'character',
        'logic:modulation',
    )),
    product('Apple', 'Scanner Vibrato', tags(
        'logic', 'modulation', 'vibrato', 'character',
        'logic:modulation',
    )),
    product('Apple', 'Spreader', tags(
        'logic', 'modulation', 'chorus', 'character', 'imaging',
        'logic:modulation',
    )),
    product('Apple', 'Vocal Transformer', tags(
        'logic', 'special', 'vocal', 'pitch',
        'logic:pitch',
    )),
    product('Apple', 'SubBass', tags(
        'logic', 'special', 'pitch', 'bass',
        'logic:specialized',
    )),
    product('Apple', 'Denoiser', tags(
        'logic', 'special', 'noise', 'spectral',
        'logic:specialized',
    )),
    product('Apple', 'Exciter', tags(
        'logic', 'special', 'zipper-noise',
        'logic:specialized',
    )),
    product('Apple', 'Phase Distortion', tags(
        'logic', 'distortion', 'monitor-option',
        'logic:distortion',
    )),
    product('Audio Ease', 'Altiverb 7', tags('reverb', 'delay', 'special')),
    product('Audio Ease', 'Speakerphone 2', tags(
        'special', 'character', 'eq',
    )),
    product('Brainworx', 'bx_solo', tags('imaging', 'free')),
    product('Brainworx', 'bx_cleansweep', tags('eq')),
    product('Eiosis', 'AirEQ', tags('eq', 'character')),
    product('Eventide', 'UltraReverb', tags('reverb', 'delay', 'special')),
    product('Eventide', 'Blackhole', tags('reverb', 'delay', 'special')),
    product('Eventide', 'H3000 Factory', tags('reverb', 'delay', 'special')),
    product('Eventide', 'Omnipressor', tags('dynamics', 'special')),
    product('Eventide', 'UltraChannel',
            tags('dynamics', 'delay', 'eq', 'character')),
    product('Exponential Audio', 'PhoenixVerb', tags('reverb')),
    product('Exponential Audio', 'R2', tags('reverb')),
    product('Flux', 'Alchemist', tags('dynamics', 'special')),
    product('Flux', 'Elixir', tags('dynamics', 'limiter')),
    product('Flux', 'Epure', tags('eq')),
    product('Flux', 'Pure Compressor', tags('dynamics')),
    product('Flux', 'Pure DCompressor', tags('dynamics')),
    product('Flux', 'Pure DExpander', tags('dynamics')),
    product('Flux', 'Pure Expander', tags('dynamics')),
    product('Flux', 'Pure Limiter', tags('dynamics', 'limiter')),
    product('Flux', 'Solera', tags('dynamics')),
    product('Flux', 'StereoToolV3', tags('imaging', 'free')),
    product('Flux', 'Syrah', tags('dynamics')),
    product('FXpansion', 'Bloom', tags('delay', 'reverb', 'special')),
    product('FXpansion', 'Maul', tags('distortion', 'special')),
    product('Goodhertz', 'Lossy', tags('special')),
    product('Illformed', 'Glitch2', tags('special', 'FSU')),
    product('Ina-GRM', 'Comb filters', tags('special', 'filter', 'grm')),
    product('Ina-GRM', 'Delays', tags('special', 'delay', 'grm')),
    product('Ina-GRM', 'Doppler', tags('special', 'delay', 'imaging', 'grm')),
    product('Ina-GRM', 'Band pass', tags('special', 'filter', 'grm')),
    product('Ina-GRM', 'Freeze', tags('special', 'granular', 'grm')),
    product('Ina-GRM', 'Shuffling', tags('special', 'delay', 'grm')),
    product('Ina-GRM', 'Pitch Accum', tags('special', 'grm')),
    product('Ina-GRM', 'Reson', tags('special', 'grm')),
    product('Ina-GRM', 'Evolution', tags('special', 'grm')),
    product('Ina-GRM', 'Grinder', tags('special', 'grm')),
    product('Ina-GRM', 'Fusion', tags('special', 'grm')),
    product('Ina-GRM', 'Contrast', tags('special', 'spectral', 'grm')),
    product('Ina-GRM', 'Equalize', tags('special', 'spectral', 'grm')),
    product('Ina-GRM', 'FreqWarp', tags('special', 'spectral', 'grm')),
    product('Ina-GRM', 'FreqShift', tags('special', 'spectral', 'grm')),
    product('Izotope', 'Vinyl', tags('special', 'character', 'free')),
    product('Kush Audio', 'Clariphonic', tags('eq', 'exciter')),
    product('Kush Audio', 'Pusher', tags('distortion', 'character')),
    product('Kush Audio', 'UBK-1', tags('dynamics', 'character', 'special')),
    product('Lexicon', 'Chamber PCM', tags('reverb')),
    product('Lexicon', 'Concert Hall PCM', tags('reverb')),
    product('Lexicon', 'Hall PCM', tags('reverb')),
    product('Lexicon', 'Plate PCM', tags('reverb')),
    product('Lexicon', 'RandomHall PCM', tags('reverb')),
    product('Lexicon', 'Room PCM', tags('reverb')),
    product('Lexicon', 'VintagePlate PCM', tags('reverb')),
    product('Lexicon', 'Chorus', tags('chorus', 'delay')),
    product('Lexicon', 'DualDelay', tags('delay')),
    product('Lexicon', 'MultivoiceShift', tags('pitch', 'special', 'delay')),
    product('Lexicon', 'Pitchshift', tags('pitch', 'special')),
    product('Lexicon', 'RandomDelay', tags('delay', 'special')),
    product('Lexicon', 'ResonantChords', tags('delay', 'pitch', 'special')),
    product('Lexicon', 'StringBox', tags('reverb', 'pitch', 'special')),
    product('Little Endian', 'SpectrumWorx', tags('spectral', 'special')),
    product('McDSP', 'Analog Channel', tags('distortion', 'character')),
    product('McDSP', 'FutzBox',
            tags('special', 'eq', 'distortion', 'character')),
    product('MeldaProduction', 'MMultibandGranular',
            tags('granular', 'special')),
    product('Metric Halo', 'Dirty Delay', tags('delay')),
    product('Plogue', 'Chipcrusher',
            tags('character', 'distortion', 'bitcrush')),
    product('Relab', 'LX480 Complete', tags('reverb', 'delay')),
    product('SampleSumo', 'SaltyGrain', tags('granular', 'delay', 'pitch')),
    product('Slate Digital', 'FG-116 (VMR)', tags('dynamics', 'character')),
    product('Slate Digital', 'FG-401 (VMR)', tags('dynamics', 'character')),
    product('Slate Digital', 'FG-N (VMR)', tags('eq', 'character')),
    product('Slate Digital', 'FG-S (VMR)', tags('eq', 'character')),
    product('Slate Digital', 'Revival (VMR)', tags(
        'exciter', 'character', 'free',
    )),

    product('Slate Digital', 'FG-MU (VBC)', tags('dynamics')),
    product('Slate Digital', 'FG-Grey (VBC)', tags('dynamics')),
    product('Slate Digital', 'FG-Red (VBC)', tags('dynamics')),
    product('Smartelectronix', 'Ambience (Magnus)', tags('reverb', 'free')),
    product('Smartelectronix', 'Geometer (DestroyFX)', tags(
        'special', 'character', 'free', 'distoration', 'waveshaper',
    )),
    product('Smartelectronix', 'Monomaker (DestroyFX)', tags(
        'imaging', 'character', 'free', 'zipper-noise',
    )),
    product('Smartelectronix', 'Polarizer (DestroyFX)', tags(
        'character', 'bitcrusher', 'free', 'distortion',
    )),
    product('Smartelectronix', 'Scrubby (DestroyFX)', tags(
        'special', 'free', 'pitch',
    )),
    product('Smartelectronix', 'Skidder (DestroyFX)', tags(
        'tremolo', 'special', 'free',
    )),
    product('Smartelectronix', 'Bouncy (Bram)', tags(
        'delay', 'special', 'free', 'zipper-noise',
    )),
    product('Smartelectronix', 'Buffer Override (DestroyFX)', tags(
        'special', 'free', 'FSU',
    )),
    product('Smartelectronix', 'Transverb (DestroyFX)', tags(
        'delay', 'special', 'pitch', 'free',
    )),
    product('Softube', 'Abbey Road RS137 Box',
            tags('eq', 'character', 'exciter')),
    product('Softube', 'Abbey Road RS137 Rack',
            tags('eq', 'character', 'exciter')),
    product('Softube', 'Abbey Road RS135', tags('eq', 'character', 'exciter')),
    product('Softube', 'Acoustic Feedback', tags('guitar', 'special')),
    product('Softube', 'Bass Amp Room',
            tags('amp', 'distortion', 'character')),
    product('Softube', 'Metal Amp Room',
            tags('amp', 'distortion', 'character')),
    product('Softube', 'Vintage Amp Room',
            tags('amp', 'distortion', 'character')),
    product('Softube', 'FET Compressor', tags('character', 'dynamocs')),
    product('Softube', 'Passive-Active Pack', tags('character', 'eq')),
    product('Softube', 'Spring Reverb', tags('reverb')),
    product('Softube', 'Tonelux Tilt', tags('eq')),
    product('Softube', 'Trident A-Range', tags('character', 'eq')),
    product('Softube', 'TSAR-1', tags('reverb')),
    product('Softube', 'Tube Delay', tags('delay', 'character')),
    product('Softube', 'Valley People Dyna-mite',
            tags('character', 'dynamics')),
    product('Softube', 'EQF-100', tags('character', 'eq')),
    product('Softube', 'TLA-100A', tags('character', 'dynamics')),
    product('Softube', 'Tube-Tech CL 1B', tags('character', 'dynamics')),
    product('Softube', 'Tube-Tech ME 1B', tags('character', 'eq')),
    product('Softube', 'Tube-Tech PE 1C', tags('character', 'eq')),
    product('Softube', 'Mutronics Mutator', tags('character', 'filter')),
    product('Sonic Charge', 'Bitspeek', tags('vocal', 'special')),
    product('Sonic Charge', 'Permut8', tags('FSU', 'special')),
    product('Sonnox', 'Oxford Dynamics', tags('dynamics', 'character')),
    product('Sonnox', 'Oxford Inflator',
            tags('dynamics', 'exciter', 'character')),
    product('Sonnox', 'Oxford TransMod',
            tags('character', 'dynamics', 'transient designer')),
    product('Sonnox', 'Oxford Limiter',
            tags('dynamics', 'character', 'limiter')),
    product('Soundhack', '+pitchsift (pvoc)',
            tags('vocoder', 'pitch', 'harmonics', 'special')),
    product('Soundhack', '+spiralstretch (pvoc)',
            tags('granular', 'special')),
    product('Soundhack', '+phasemash (pvoc)', tags('special')),
    product('Soundhack', '+morphfilter',
            tags('spectral', 'special', 'filter')),
    product('Soundhack', '+spectralcompand',
            tags('spectral', 'special', 'eq')),
    product('Soundhack', '+spectralgate',
            tags('spectral', 'special', 'dynamics')),
    product('Soundhack', '+chebyshev', tags('distortion', 'special')),
    product('Soundhack', '+decimate', tags('character', 'bitcrush')),
    product('Soundhack', '+pitchdelay', tags('delay', 'pitch', 'special')),
    product('Soundhack', '+bubbler', tags('granular', 'delay', 'special')),
    product('Soundtoys', 'Devil-loc', tags('dynamics', 'character')),
    product('Soundtoys', 'Devil-loc Deluxe', tags('dynamics', 'character')),
    product('Soundtoys', 'Little Primaltap', tags(
        'delay', 'special', 'character',
    )),
    product('Soundtoys', 'Microshift', tags('delay', 'pitch')),
    product('Soundtoys', 'Little Microshift', tags('delay', 'pitch')),
    product('Soundtoys', 'Radiator', tags('character', 'amp')),
    product('Soundtoys', 'Little Radiator', tags('character', 'amp')),
    product('Soundtoys', 'Crystallizer',
            tags('granular', 'delay', 'special')),
    product('Soundtoys', 'Decapitator', tags('character', 'distortion')),
    product('Soundtoys', 'Echoboy', tags('character', 'delay')),
    product('Soundtoys', 'Filterfreak',
            tags('character', 'filter', 'special')),
    product('Soundtoys', 'Panman', tags('imaging', 'character')),
    product('Soundtoys', 'Phase Mistress', tags('special', 'character')),
    product('Soundtoys', 'Tremolator', tags('special', 'character')),
    product('SPL', 'DeVerb', tags('dynamics')),
    product('Unfiltered Audio', 'G8 Gate', tags('dynamics', 'special')),
    product('Unfiltered Audio', 'Sandman', tags('delay', 'special')),
}

INST.update(MFX)
FX.update(MFX)

fx_by_tag = defaultdict(set)
inst_by_tag = defaultdict(set)

for f in FX:
    for tag in f.tags:
        fx_by_tag[tag].add(f)
for i in INST:
    for tag in i.tags:
        inst_by_tag[tag].add(f)


def find_info(p, key, sep=':'):
    return [t.split(sep) for t in p.tags if t.startswith(key + sep)]


def hp(p, cat=''):
    if 'logic' in p.tags:
        tag, menu = find_info(p, 'logic')[0]
        cat = '({0}:{1})'.format(tag, menu.capitalize())
    return '{0.brand} {0.name} {cat}'.format(p, cat=cat)


def get_random(bag, tag):
    return random.choice(list(bag[tag]))

random_fx_by_tag = partial(get_random, fx_by_tag)
random_inst_by_tag = partial(get_random, inst_by_tag)


def select():
    seen = set()

    def retry(fun, *args):
        while 1:
            r = fun(*args)
            if r not in seen:
                return r

    return FMT.format(
        inst=hp(random.choice(list(INST))),
        reverb=hp(retry(random_fx_by_tag, 'reverb')),
        delay=hp(retry(random_fx_by_tag, 'delay')),
        special=hp(retry(random_fx_by_tag, 'special')),
        character=hp(retry(random_fx_by_tag, 'character')),
        eq=hp(retry(random_fx_by_tag, 'eq')),
        dynamics=hp(retry(random_fx_by_tag, 'dynamics')),
    )

print(select())
