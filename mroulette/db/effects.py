from __future__ import absolute_import, unicode_literals

from mroulette.types import (
    aumu, aumf, aufx, reaktorFX, logic, livefx, product,
)
from mroulette.tags import t, tags

FX = {
    # -2c Audio-
    product('2c Audio', 'Kaleidoscope', aufx('2cau', '2cks'), tags(
        t.CREATIVE, 'special', 'granular', 'spectral', 'resonator',
    )),

    # -Abbey Road-
    product('Abbey Road', 'EMI RS 124 LE', aufx('AbRd', 'R124'), tags(
        t.COMP, 'dynamics', 'character',
    )),
    product('Abbey Road', 'EMI TG12412', aufx('AbRd', 'TGeq'), tags(
        t.EQ, 'character',
    )),
    product('Abbey Road', 'EMI TG12414', aufx('AbRd', 'TGfi'), tags(
        t.EQ, 'character', 'filter',
    )),
    product('Abbey Road', 'EMI TG12413 1969', aufx('AbRd', 'TG69'), tags(
        t.DYN, 'compressor', 'limiter',
    )),
    product('Abbey Road', 'EMI TG12413 2005', aufx('AbRd', 'TG05'), tags(
        t.DYN, 'compressor', 'limiter',
    )),

    # -accSone-
    product('accSone', 'CrusherX', aumf('bsCX', 'cXs1'), tags(
        t.GRAIN, 'special', 'mfx',
    )),

    # -Aegean Music-
    product('Aegean Music', 'Spirit Reverb', aumf('Aegn', 'Amsr'), tags(
        t.VERB, 'spring', 'special', 'amp',
    )),

    # -Airwindows-
    # product('Airwindows', 'Pressure 3', aufx('Dthr', 'prs3'), tags(
    #    t.DYN, 'free', 'compressor',
    # )),
    # product('Airwindows', 'Channel 4', aufx('Dthr', 'cha4'), tags(
    #    t.DIST, 'character', 'free', 'analog',
    # )),
    # product('Airwindows', 'DeRez', aufx('Dthr', 'derz'), tags(
    #    t.DIST, 'character', 'bitcrusher', 'free',
    # )),
    # product('Airwindows', 'DustBunny', aufx('Dthr', 'dbny'), tags(
    #    t.DIST, 'character', 'vinyl', 'free',
    # )),
    # product('Airwindows', 'TapeFat', aufx('Dthr', 'tayp'), tags(
    #    t.DIST, 'character', 'filter', 'tape', 'free',
    # )),

    # -Amazing Noises-
    product('Amazing Noises', 'Compulsive Switcher', livefx, tags(
        t.CREATIVE, 'special', 'tremolo', 'Live', 'maxforlive', 'free',
    )),
    product('Amazing Noises', 'GliderVerb', livefx, tags(
        t.VERB, 'special', 'creative', 'Live', 'maxforlive', 'free',
    )),
    product('Amazing Noises', 'Grain Crusher', livefx, tags(
        t.GRAIN, 'special', 'creative', 'Live', 'maxforlive',
    )),
    product('Amazing Noises', 'Grain Reverser', livefx, tags(
        t.GRAIN, 'special', 'creative', 'Live', 'maxforlive', 'free',
    )),
    product('Amazing Noises', 'Granular Mirror Maze', livefx, tags(
        t.GRAIN, 'special', 'creative', 'Live', 'maxforlive', 'free',
    )),
    product('Amazing Noises', 'Grip', livefx, tags(
        t.GRAIN, 'spectral', 'creative', 'Live', 'maxforlive',
    )),
    product('Amazing Noises', 'Spectrum Runner', livefx, tags(
        t.CREATIVE, 'spectral', 'creative', 'Live', 'maxforlive',
    )),

    # -Antares-
    product('Antares', 'Harmony Engine EVO', aumf('VST ', 'VZr2'), tags(
        t.PITCH, 'vocal', 'special', 'mfx',
    )),

    # -Apple-
    product('Apple', 'AUDistortion', aufx('appl', 'dist'), tags(
        t.DIST, 'character', 'free', 'bitcrusher', 'special',
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

    # -Audio Damage-
    product('Audio Damage', 'Bitcom', aumf('AuDa', 'ADbc'), tags(
        t.FSU, 'special', 'sequencer', 'bitcrush', 'distortion',
    )),

    # -Audio Ease-
    product('Audio Ease', 'Altiverb 7', aufx('AEas', 'AVr5'), tags(
        t.VERB, 'delay', 'special',
    )),
    product('Audio Ease', 'Speakerphone 2', aufx('AEas', 'SpVl'), tags(
        t.DIST, 'special', 'character', 'eq',
    )),

    # -Audiothing-
    product('Audiothing', 'Frostbite', aufx('AdTg', 'FrsB'), tags(
        t.CREATIVE, 'reverb', 'character', 'ringmod',
    )),


    # -Celemony-
    product('Celemony', 'Melodyne Editor', aumf('CLMY', 'MPLG'), tags(
        t.PITCH, 'vocal', 'special', 'creative',
    )),

    # -Cytomic-
    product('Cytomic', 'The Drop', aumf('Cyto', 'Drp1'), tags(
        t.FILT, 'special', 'mfx', 'character', 'sidechain',
    )),

    # -DMG Audio-
    product('DMG Audio', 'Essence', aumf('DMGa', 'Esse'), tags(
        t.DYN, 'eq', 'desser', 'vocal',
    )),
    product('DMG Audio', 'PitchFunk', aumf('DMGa', 'PiFu'), tags(
        t.DELAY, 'granular', 'special',
    )),

    # -Eiosis-
    product('Eiosis', 'AirEQ', aufx('Eios', 'AEq5'), tags(
        t.EQ, 'character',
    )),

    # -Eventide-
    product('Eventide', '2016 Stereo Room', aufx('TIDE', '22SR'), tags(
        t.VERB,
    )),
    product('Eventide', 'Blackhole', aufx('TIDE', 'HOLE'), tags(
        t.CREATIVE, 'reverb', 'delay', 'special',
    )),
    product('Eventide', 'H3000 Factory', aufx('TIDE', 'Fact'), tags(
        t.DELAY, 'pitch', 'delay', 'special', 'sidechain',
    )),
    product('Eventide', 'Omnipressor', aufx('TIDE', 'Omni'), tags(
        t.COMP, 'dynamics', 'special', 'expander', 'character',
        'saturation', 'sidechain',
    )),
    product('Eventide', 'UltraChannel', aufx('Tide', 'UlCh'), tags(
        t.STRIP, 'dynamics', 'delay', 'eq', 'character',
        'saturation', 'pitch', 'compressor', 'sidechain',
    )),
    product('Eventide', 'UltraReverb', aufx('Tide', 'Revb'), tags(
        t.VERB, 'delay', 'special', 'compressor', 'character',
        'distortion', 'sidechain',
    )),

    # -Expert Sleepers-
    product(
        'Expert Sleepers', 'Crossfade Loop Synth',
        aumf('ExSl', 'XFls'),
        tags(t.CREATIVE, 'sampler', 'special', 'mfx'),
    ),

    # -Exponential Audio-
    product('Exponential Audio', 'Excalibur', aufx('EXPa', 'EXca'), tags(
        t.MOD, 'delay', 'chorus', 'flanger', 'pitch', 'amp', 'ringmod',
    )),
    product('Exponential Audio', 'PhoenixVerb', aufx('EXPa', 'MCsr'), tags(
        t.VERB,
    )),
    product('Exponential Audio', 'R2', aufx('EXPa', 'MCs2'), tags(
        t.VERB,
    )),

    # -Flux-
    product('Flux', 'Alchemist', aufx('Fspd', 'fxAl'), tags(
        t.FLUX, 'dynamics', 'special', 'multiband', 'compressor',
        'mix', 'mastering',
    )),
    product('Flux', 'Elixir', aufx('Fspd', 'Flxr'), tags(
        t.FLUX, 'dynamics', 'limiter', 'mix', 'mastering',
    )),
    product('Flux', 'Epure', aufx('Fspd', 'Ftst'), tags(
        t.FLUX, 'eq', 'mix', 'mastering',
    )),
    product('Flux', 'Pure Compressor', aufx('Fspd', 'fxPc'), tags(
        t.FLUX, 'dynamics', 'compressor', 'mix', 'sidechain',
    )),
    product('Flux', 'Pure DCompressor', aufx('Fspd', 'fxDc'), tags(
        t.FLUX, 'dynamics', 'decompressor', 'mix', 'sidechain',
    )),
    product('Flux', 'Pure DExpander', aufx('Fspd', 'fxDx'), tags(
        t.FLUX, 'dynamics', 'deexpander', 'mix', 'sidechain',
    )),
    product('Flux', 'Pure Expander', aufx('Fspd', 'fxEx'), tags(
        t.FLUX, 'dynamics', 'expander', 'mix', 'sidechain',
    )),
    product('Flux', 'Pure Limiter', aufx('Fspd', 'fxPl'), tags(
        t.FLUX, 'dynamics', 'limiter', 'mix',
    )),
    product('Flux', 'Solera', aufx('Fspd', 'fxSo'), tags(
        t.FLUX, 'dynamics', 'compressor', 'decompressor',
        'expander', 'deexpander', 'mix', 'mastering', 'sidechain',
    )),
    product('Flux', 'StereoToolV3', aufx('Fspd', 'fxSt'), tags(
        t.IMAGE, 'imaging', 'free',
    )),
    product('Flux', 'Syrah', aufx('Fspd', 'fxSy'), tags(
        t.FLUX, 'dynamics', 'mix', 'mastering', 'bus',
        'track', 'compression', 'special',
    )),

    # -Focusrite-
    #product('Focusrite', 'RED 2 EQ', aufx('FCUS', 'rd2E'), tags(
    #    t.EQ,
    #)),
    product('Focusrite', 'RED 3 Compressor', aufx('FCUS', 'rd3C'), tags(
        t.COMP, 'character', 'dynamics',
    )),

    # -FXpansion-
    product('FXpansion', 'Bloom', aumf('FXPN', 'FXBL'), tags(
        t.DELAY, 'special',
    )),
    product('FXpansion', 'Etch', aumf('FXPN', 'FXET'), tags(
        t.FILT, 'special',
    )),
    product('FXpansion', 'Maul', aumf('FXPN', 'FXMA'), tags(
        t.DIST, 'distortion', 'special', 'multiband',
    )),

    # -Goodhertz-
    product('Goodhertz', 'Faraday Limiter', aufx('GDHZ', 'FDLM'), tags(
        t.DYN, 'limiter', 'character',
    )),
    product('Goodhertz', 'Lossy', aufx('GDHZ', 'LSSY'), tags(
        t.DIST, 'special', 'character',
    )),
    product('Goodhertz', 'Panpot', aufx('GDHZ', 'PNPT'), tags(
        t.IMAGE,
    )),
    product('Goodhertz', 'Vulf Compressor', aufx('GDHZ', 'VCM1'), tags(
        t.COMP, 'dynamics', 'character', 'vinyl',
    )),

    # -Illformed-
    product('Illformed', 'Glitch2', aumu('DBlu', 'igl2'), tags(
        t.FSU, 'special', 'mfx',
    )),

    # -Ina-GRM-
    product('Ina-GRM', 'Band pass', aumf('Grm ', 'BaPS'), tags(
        t.GRM, 'special', 'filter', 'grm',
    )),
    product('Ina-GRM', 'Comb filters', aumf('Grm ', 'Comb'), tags(
        t.GRM, 'special', 'filter', 'grm',
    )),
    product('Ina-GRM', 'Contrast', aumf('Grm ', 'ctrG'), tags(
        t.GRM, 'special', 'spectral', 'grm',
    )),
    product('Ina-GRM', 'Delays', aumf('Grm ', 'Dely'), tags(
        t.GRM, 'special', 'delay', 'grm',
    )),
    product('Ina-GRM', 'Doppler', aumf('Grm ', 'DopS'), tags(
        t.GRM, 'special', 'delay', 'imaging', 'grm',
    )),
    product('Ina-GRM', 'Evolution', aumf('Grm ', 'GrEv'), tags(
        t.GRM, 'special', 'grm',
    )),
    product('Ina-GRM', 'Equalize', aumf('aGRM', 'EquS'), tags(
        t.GRM, 'special', 'spectral', 'grm',
    )),
    product('Ina-GRM', 'Freeze', aumf('Grm ', 'Free'), tags(
        t.GRM, 'special', 'granular', 'grm',
    )),
    product('Ina-GRM', 'Fusion', aumf('Grm ', 'GFus'), tags(
        t.GRM, 'special', 'grm',
    )),
    product('Ina-GRM', 'Grinder', aumf('Grm ', 'Cruh'), tags(
        t.GRM, 'special', 'grm', 'sidechain',
    )),
    product('Ina-GRM', 'Pitch Accum', aumf('Grm ', 'Pitc'), tags(
        t.GRM, 'special', 'grm',
    )),
    product('Ina-GRM', 'Reson', aumf('Grm ', 'Reso'), tags(
        t.GRM, 'special', 'grm',
    )),
    product('Ina-GRM', 'FreqShift', aumf('Grm ', 'FrsG'), tags(
        t.GRM, 'special', 'spectral', 'grm',
    )),
    product('Ina-GRM', 'Shuffling', aumf('Grm ', 'Shuf'), tags(
        t.GRM, 'special', 'delay', 'grm', 'sidechain',
    )),
    product('Ina-GRM', 'FreqWarp', aumf('Grm ', 'Fw G'), tags(
        t.GRM, 'special', 'spectral', 'grm',
    )),

    # -IRCAM-
    product('IRCAM', 'IM-FXSequencer', livefx, tags(
        t.FSU, 'special', 'Live', 'maxforlive',
    )),
    product('IRCAM', 'IM-MultibandDelay', livefx, tags(
        t.CREATIVE, 'special', 'spectral', 'delay', 'IRCAM',
        'Live', 'maxforlive',
    )),
    product('IRCAM', 'IM-SimpleTransp', livefx, tags(
        t.GRAIN, 'special', 'creative', 'stretch', 'IRCAM',
        'Live', 'maxforlive',
    )),
    product('IRCAM', 'IM-Scrub', livefx, tags(
        t.GRAIN, 'special', 'creative', 'pitch', 'stretch', 'IRCAM',
        'Live', 'maxforlive',
    )),
    product('IRCAM', 'IM-Mover', livefx, tags(
        t.GRAIN, 'special', 'creative', 'pitch', 'stretch', 'IRCAM',
        'Live', 'maxforlive',
    )),

    # -iZotope-
    product('iZotope', 'Nectar Elements', aufx('iZtp', 'ZnNE'), tags(
        t.STRIP, 'vocal',
    )),
    product('iZotope', 'Ozone 6', aufx('iZtp', 'ZnO6'), tags(
        t.STRIP, 'mastering', 'compression', 'dynamics', 'limiter', 'eq',
        'dyneq', 'matching', 'exciter', 'imaging',
    )),
    product('iZotope', 'RX 4 Declicker', aufx('iZtp', 'Zn4K'), tags(
        t.OTHER, 'special', 'creative', 'restoration',
    )),
    product('iZotope', 'RX 4 Declipper', aufx('iZtp', 'Zn4P'), tags(
        t.OTHER, 'special', 'creative', 'restoration',
    )),
    product('iZotope', 'RX 4 Decrackler', aufx('iZtp', 'Zn4C'), tags(
        t.OTHER, 'special', 'creative', 'restoration',
    )),
    product('iZotope', 'RX 4 Denoiser', aufx('iZtp', 'Zn4N'), tags(
        t.OTHER, 'special', 'creative', 'restoration',
    )),
    product('iZotope', 'RX 4 Dialogue Denoiser', aufx('iZtp', 'Zn4D'), tags(
        t.OTHER, 'special', 'creative', 'restoration',
    )),
    product('iZotope', 'RX 4 Hum Removal', aufx('iZtp', 'Zn4H'), tags(
        t.OTHER, 'special', 'creative', 'restoration',
    )),
    product('iZotope', 'Vinyl', aufx('iZtp', 'Vnyl'), tags(
        t.DIST, 'special', 'character', 'free',
    )),

    # -K-Devices-
    product('K-Devices', 'Holder', livefx, tags(
        t.CREATIVE, 'special', 'spectral', 'freeze', 'Live', 'maxforlive',
    )),
    product('K-Devices', 'Alter Echo', livefx, tags(
        t.DELAY, 'special', 'creative', 'Live', 'maxforlive',
    )),

    # -Klevgrand-
    product('Klevgrand', 'R0Verb', aufx('Klev', 'rvrb'), tags(
        t.VERB, 'special',
    )),
    product('Klevgrand', 'SquashIt', aufx('Klev', 'Sqit'), tags(
        t.DIST, 'character', 'multiband',
    )),
    product('Klevgrand', 'Svep', aufx('Klev', 'modl'), tags(
        t.MOD, 'phaser', 'flanger', 'chorus', 'free',
    )),
    product('Klevgrand', 'Vandelay', aufx('Klev', 'dely'), tags(
        t.DELAY, 'multiband', 'free',
    )),

    # -Kush Audio-
    product('Kush Audio', 'Clariphonic', aufx('Kush', 'clar'), tags(
        t.EQ, 'exciter'
    )),
    product('Kush Audio', 'Electra DSP', aufx('Kush', 'Elec'), tags(
        t.EQ, 'analog',
    )),
    product('Kush Audio', 'Pusher', aufx('Kush', 'Push'), tags(
        t.DIST, 'character', 'saturation',
    )),
    product('Kush Audio', 'UBK-1', aufx('KuSh', 'dcmp'), tags(
        t.COMP, 'dynamics', 'character', 'special', 'saturation',
    )),

    # -Lexicon-
    product('Lexicon', 'LexChamber PCM', aufx('Lexi', 'Lcm1'), tags(
        t.VERB,
    )),
    product('Lexicon', 'LexChorus', aufx('Lexi', 'Lcr1'), tags(
        t.MOD, 'chorus', 'delay',
    )),
    product('Lexicon', 'LexConcert Hall PCM', aufx('Lexi', 'Lch1'), tags(
        t.VERB,
    )),
    product('Lexicon', 'LexDualDelay', aufx('Lexi', 'Ldd1'), tags(
        t.DELAY,
    )),
    product('Lexicon', 'LexHall PCM', aufx('Lexi', 'Lhl1'), tags(
        t.VERB,
    )),
    product('Lexicon', 'LexMultivoiceShift', aufx('Lexi', 'Lmp1'), tags(
        t.PITCH, 'special', 'delay',
    )),
    product('Lexicon', 'LexPitchshift', aufx('Lexi', 'Lsp1'), tags(
        t.PITCH, 'special',
    )),
    product('Lexicon', 'LexPlate PCM', aufx('Lexi', 'Lpl1'), tags(
        t.VERB,
    )),
    product('Lexicon', 'LexRandomDelay', aufx('Lexi', 'Lrd1'), tags(
        t.DELAY, 'special',
    )),
    product('Lexicon', 'LexRandomHall PCM', aufx('Lexi', 'Lrh1'), tags(
        t.VERB,
    )),
    product('Lexicon', 'LexResonantChords', aufx('Lexi', 'Lrc1'), tags(
        t.CREATIVE, 'delay', 'pitch', 'special',
    )),
    product('Lexicon', 'LexRoom PCM', aufx('Lexi', 'Lrm1'), tags(
        t.VERB,
    )),
    product('Lexicon', 'LexStringBox', aufx('Lexi', 'Sbx1'), tags(
        t.CREATIVE, 'reverb', 'pitch', 'special',
    )),
    product('Lexicon', 'LexVintagePlate PCM', aufx('Lexi', 'Lpl0'), tags(
        t.VERB,
    )),

    # -Little Endian-
    product('Little Endian', 'SpectrumWorx', aufx('LE00', 'SW00'), tags(
        t.CREATIVE, 'spectral', 'special', 'sidechain',
    )),

    # -Max for Cats-
    product('Max for Cats', 'Skram Delay', livefx, tags(
        t.DELAY, 'special', 'Live', 'maxforlive',
    )),
    product('Max for Cats', 'Stochastic Delay', livefx, tags(
        t.DELAY, 'special', 'Live', 'maxforlive',
    )),

    # -McDSP-
    product('McDSP', 'Analog Channel AC101', aufx('McDP', 'AC01'), tags(
        t.DIST, 'character',
    )),
    product('McDSP', 'Analog Channel AC202', aufx('McDP', 'AC02'), tags(
        t.DIST, 'character', 'tape',
    )),
    product('McDSP', 'FutzBox', aufx('McDP', 'Futz'), tags(
        t.DIST, 'special', 'eq', 'character',
    )),

    # -MeldaProduction-
    product(
        'MeldaProduction', 'MMultibandGranular', aumf('Meld', 'MMGr'),
        tags(t.GRAIN, 'special', 'sidechain', 'multiband'),
    ),

    # -Metric Halo-
    product('Metric Halo', 'Dirty Delay', aufx('MHL ', 'DELY'), tags(
        t.DELAY,
    )),

    # -Native Instruments-
    product('Native Instruments', 'Driver', aufx('-NI-', 'Ni$='), tags(
        t.DIST, 'character', 'sidechain',
    )),
    product('Native Instruments', 'Reaktor 5 FX', reaktorFX, tags(
        t.STRIP, 'modular', 'sidechain',
    )),
    product('Native Instruments', 'Molekular', reaktorFX, tags(
        t.CREATIVE, 'special', 'delay', 'vocoder', 'pitch', 'sidechain',
    )),
    product('Native Instruments', 'Guitar Rig 5', aumf('-NI-', 'NiG5'), tags(
        t.AMP, 'guitar', 'strip', 'sidechain', 'amp',
    )),
    #product('Native Instruments', 'Solid Bus Comp', aufx('-NI-', 'Ni$6'), tags(
    #    t.COMP, 'dynamics',
    #)),
    #product('Native Instruments', 'Solid Dynamics', aufx('-NI-', 'Ni$7'), tags(
    #    t.DYN,
    #)),
    #product('Native Instruments', 'Solid EQ', aufx('-NI-', 'Ni$8'), tags(
    #    t.EQ,
    #)),
    product(
        'Native Instruments', 'Supercharger GT',
        aufx('-NI-', 'Ni$A'),
        tags(t.COMP, 'character',
             'distortion', 'dynamics', 'sidechain'),
    ),
    product(
        'Native Instruments', 'Transient Master',
        aufx('-NI-', 'Ni$5'), tags(t.DYN, 'transient shaper')
    ),
    product('Native Instruments', 'Replika', aufx('-NI-', 'Ni$B'), tags(
        t.DELAY, 'reverb'
    )),
    product('Native Instruments', 'Vari Comp', aufx('-NI-', 'Ni$;'), tags(
        t.COMP, 'dynamics', 'manley', 'vari-mu', 'sidechain',
    )),
    product('Native Instruments', 'VC 160', aufx('-NI-', 'Ni$2'), tags(
        t.COMP, 'dynamics', 'dbx',
    )),
    product('Native Instruments', 'VC 2A', aufx('-NI-', 'Ni$3'), tags(
        t.COMP, 'dynamics', 'la2a', 'teletronix', 'urei',
    )),

    # -Ohm Force-
    product('Ohm Force', 'Ohmicide', aumf('OmFo', 'Opd2'), tags(
        t.DIST, 'character', 'multiband',
    )),

    # -Plogue-
    product('Plogue', 'Chipcrusher', aufx('PLOG', 'PLGP'), tags(
        t.DIST, 'character', 'bitcrush', 'latency',
    )),

    # -Relab-
    product('Relab', 'LX480 Complete', aufx('RELB', 'LX4C'), tags(
        t.VERB, 'delay', 'retro',
    )),

    # -SampleSumo-
    product('SampleSumo', 'SaltyGrain', aumf('SaSu', 'StGr'), tags(
        t.GRAIN, 'delay', 'pitch', 'mfx',
    )),

    # -Sinevibes-
    product('Sinevibes', 'Zap', aufx('SNSH', 'zzap'), tags(
        t.MOD, 'free',
    )),

    # -Slate Digital-
    product('Slate Digital', 'FG-116 (VMR)', aufx('SlDg', 'VMXR'), tags(
        t.COMP, 'dynamics', 'character',
    )),
    product('Slate Digital', 'FG-401 (VMR)', aufx('SlDg', 'VMXR'), tags(
        t.COMP, 'dynamics', 'character',
    )),
    product('Slate Digital', 'FG-N (VMR)', aufx('SlDg', 'VMXR'), tags(
        t.EQ, 'character',
    )),
    product('Slate Digital', 'FG-S (VMR)', aufx('SlDg', 'VMXR'), tags(
        t.EQ, 'character',
    )),
    product('Slate Digital', 'Revival (VMR)', aufx('SlDg', 'VMXR'), tags(
        t.EQ, 'exciter', 'character', 'free',
    )),
    product('Slate Digital', 'FG-Grey (VBC)', aufx('SlDg', 'VBCg'), tags(
        t.COMP, 'dynamics', 'mix',
    )),
    product('Slate Digital', 'FG-MU (VBC)', aufx('SlDg', 'VBCm'), tags(
        t.COMP, 'dynamics', 'mix',
    )),
    product('Slate Digital', 'FG-Red (VBC)', aufx('SlDg', 'VBCr'), tags(
        t.COMP, 'dynamics', 'mix',
    )),
    product('Slate Digital', 'Virtual Mix Rack', aufx('SlDg', 'VMXR'), tags(
        t.STRIP,
    )),
    product(
        'Slate Digital', 'Virtual Tape Machines',
        aufx('SlDg', 'VTMs'),
        tags(t.STRIP),
    ),

    # -Smartelectronix-
    #product('Smartelectronix', 'Ambience', aufx('MagJ', '07C0BCD2'), tags(
    #    t.VERB, 'free',
    #)),
    product('Smartelectronix', 'Bouncy', aufx('BrDJ', 'BNCY'), tags(
        t.DELAY, 'special', 'free', 'zipper-noise',
    )),
    product('Smartelectronix', 'Buffer Override', aumf('DFX!', 'buff'), tags(
        t.CREATIVE, 'special', 'free', 'FSU',
    )),
    product('Smartelectronix', 'Geometer', aumf('DFX!', 'DFgr'), tags(
        t.CREATIVE, 'special', 'character', 'free', 'waveshaper',
    )),
    #product('Smartelectronix', 'Monomaker', aufx('DFX!', 'mono'), tags(
    #    t.IMAGE, 'character', 'free', 'zipper-noise',
    #)),
    product('Smartelectronix', 'Polarizer', aufx('DFX!', 'pola'), tags(
        t.DIST, 'character', 'bitcrusher', 'free',
    )),
    product('Smartelectronix', 'Scrubby', aumf('DFX!', 'scub'), tags(
        t.CREATIVE, 'special', 'free', 'pitch',
    )),
    product('Smartelectronix', 'Skidder', aumf('DFX!', 'skid'), tags(
        t.MOD, 'tremolo', 'special', 'free',
    )),
    product('Smartelectronix', 'Transverb', aumf('DFX!', 'DFtv'), tags(
        t.CREATIVE, 'delay', 'special', 'pitch', 'free',
    )),

    # -Softube-
    product('Softube', 'Abbey Road RS127 Box', aufx('AbRd', 'r127'), tags(
        t.EQ, 'character', 'exciter',
    )),
    product('Softube', 'Abbey Road RS127 Rack', aufx('AbRd', 'g127'), tags(
        t.EQ, 'character', 'exciter',
    )),
    product('Softube', 'Abbey Road RS135', aufx('AbRd', '8kbx'), tags(
        t.EQ, 'character', 'exciter',
    )),
    product('Softube', 'Acoustic Feedback', aufx('SfTb', 'FbAU'), tags(
        t.AMP, 'guitar', 'special',
    )),
    #product('Softube', 'Active Equalizer', aufx('SfTb', 'AcEQ'), tags(
    #    'eq', 'character',
    #)),
    product('Softube', 'Bass Amp Room', aufx('SfTb', 'BARn'), tags(
        t.AMP, 'distortion', 'character',
    )),
    product('Softube', 'FET Compressor', aufx('SfTb', 'Fcpn'), tags(
        t.COMP, 'character', 'dynamics', 'saturation', 'sidechain',
    )),
    product('Softube', 'Focusing Equalizer', aufx('SfTb', 'ChEq'), tags(
        t.EQ, 'character',
    )),
    product('Softube', 'Metal Amp Room', aufx('SfTb', 'Mtal'), tags(
        t.AMP, 'distortion', 'character',
    )),
    product('Softube', 'Mutronics Mutator', aufx('SfTb', 'z9x7'), tags(
        t.FILT, 'character', 'sidechain',
    )),
    #product('Softube', 'Passive Equalizer', aufx('SfTb', 'PvEQ'), tags(
    #    'character', 'eq',
    #)),
    product('Softube', 'Saturation Knob', aufx('SfTb', 'satn'), tags(
        t.DIST, 'character', 'saturation',
    )),
    product('Softube', 'Spring Reverb', aufx('SfTb', 'SpRn'), tags(
        t.VERB, 'spring',
    )),
    product('Softube', 'Summit Audio EQF-100', aufx('SfTb', 'e100'), tags(
        t.EQ, 'character',
    )),
    product(
        'Softube', 'Summit Audio Grand Channel', aufx('SfTb', 'SAGC'),
        tags(t.STRIP, 'character', 'eq', 'dynamics',
             'compressor', 'saturation', 'sidechain'),
    ),
    product('Softube', 'Summit Audio TLA-100A', aufx('SfTb', 't100'), tags(
        t.COMP, 'character', 'dynamics', 'saturation', 'sidechain',
    )),
    product('Softube', 'Tonelux Tilt', aufx('SfTb', 'Tilt'), tags(
        t.EQ,
    )),
    product('Softube', 'Transient Shaper', aufx('SfTb', 'Shpe'), tags(
        t.DYN, 'transient shaper', 'multiband',
    )),
    product('Softube', 'Trident A-Range', aufx('SfTb', 'Aran'), tags(
        t.EQ, 'character', 'saturation',
    )),
    product('Softube', 'TSAR-1', aufx('SfTb', 'tsar'), tags(
        t.VERB,
    )),
    #product('Softube', 'TSAR-1R', aufx('SfTb', 'ts1r'), tags(
    #    'reverb',
    #)),
    product('Softube', 'Tube Delay', aufx('SfTb', 'TbDe'), tags(
        t.DELAY, 'character', 'saturation',
    )),
    product('Softube', 'Tube-Tech CL 1B', aufx('SfTb', 'clST'), tags(
        t.COMP, 'character', 'dynamics', 'saturation', 'sidechain',
    )),
    product('Softube', 'Tube-Tech Classic Channel', aufx('SfTb', 'TTCC'), tags(
        t.STRIP, 'character', 'dynamics', 'eq', 'compressor',
        'saturation', 'sidechain',
    )),
    product('Softube', 'Tube-Tech ME 1B', aufx('SfTb', 'ME1B'), tags(
        t.EQ, 'character', 'saturation',
    )),
    product('Softube', 'Tube-Tech PE 1C', aufx('SfTb', 'PE1C'), tags(
        t.EQ, 'character', 'saturation',
    )),
    product('Softube', 'Valley People Dyna-mite', aufx('SfTb', 'DaMt'), tags(
        t.DYN, 'character', 'gate', 'expander', 'ducking', 'keying',
        'compression', 'saturation', 'sidechain',
    )),
    product('Softube', 'Vintage Amp Room', aufx('SfTb', 'ViAU'), tags(
        t.AMP, 'distortion', 'character',
    )),
    #product('Softube', 'White Amp', aufx('SfTb', 'WAmp'), tags(
    #    t.AMP, 'distortion', 'character',
    #)),

    # -Solid State Logic-
    product('Solid State Logic', 'SSL X-Saturator', aufx('SSL ', 'XSAT'), tags(
        t.DIST, 'saturation', 'analog', 'character',
    )),

    # -Sonic Charge-
    product('Sonic Charge', 'Bitspeek', aumf('NuEd', 'NuSq'), tags(
        t.PITCH, 'vocal', 'special',
    )),
    product('Sonic Charge', 'Permut8', aumf('NuEd', 'NuPr'), tags(
        t.FSU, 'special',
    )),

    # -Sonnox-
    product('Sonnox', 'Oxford Dynamics', aufx('Sony', 'OxDy'), tags(
        t.DYN, 'character', 'compression', 'gate', 'expander', 'limiter',
        'saturation', 'sidechain',
    )),
    product('Sonnox', 'Oxford Inflator', aufx('Sony', 'OxIn'), tags(
        t.DYN, 'exciter', 'character',
    )),
    product('Sonnox', 'Oxford Limiter', aufx('Sony', 'OxLm'), tags(
        t.DYN, 'character', 'limiter',
    )),
    product('Sonnox', 'Oxford TransMod', aufx('Sony', 'OxTM'), tags(
        t.DYN, 'character', 'transient shaper', 'distortion',
    )),

    # -Soundhack-
    product('Soundhack', '+bubbler', aumf('SDHK', '+bub'), tags(
        t.GRAIN, 'delay', 'special',
    )),
    product('Soundhack', '+chebyshev', aufx('SDHK', '+chb'), tags(
        t.CREATIVE, 'distortion', 'special',
    )),
    #product('Soundhack', '+compand', aufx('SDHK', 'ercm'), tags(
    #    t.DYN, 'dynamics', 'free',
    #)),
    product('Soundhack', '+decimate', aufx('SDHK', 'er10'), tags(
        t.DIST, 'character', 'bitcrush', 'free',
    )),
    #product('Soundhack', '+delay', aumf('SDHK', '+dla'), tags(
    #    t.DELAY, 'free',
    #)),
    #product('Soundhack', '+matrix', aufx('SDHK', '+mtx'), tags(
    #    'special', 'free',
    #)),
    product('Soundhack', '+morphfilter', aumf('SDHK', '+mrf'), tags(
        t.FILT, 'spectral', 'special',
    )),
    product('Soundhack', '+phasemash (pvoc)', aumf('SDHK', '+pvx'), tags(
        t.CREATIVE, 'special',
    )),
    #product('Soundhack', '+phasor', aumf('SDHK', '+phz'), tags(
    #    t.MOD, 'special', 'phaser', 'free',
    #)),
    product('Soundhack', '+pitchdelay', aumf('SDHK', '+pdl'), tags(
        t.DELAY, 'pitch', 'special',
    )),
    product('Soundhack', '+pitchsift (pvoc)', aumf('SDHK', '+pvp'), tags(
        t.CREATIVE, 'vocoder', 'pitch', 'harmonics', 'special',
    )),
    product('Soundhack', '+pvocloop (pvoc)', aumf('SDHK', '+pvt'), tags(
        t.CREATIVE, 'special', 'granular', 'mfx',
    )),
    product('Soundhack', '+spectralcompand', aumf('SDHK', '+spx'), tags(
        t.CREATIVE, 'spectral', 'special', 'eq',
    )),
    product('Soundhack', '+spectralgate', aumf('SDHK', '+spg'), tags(
        t.CREATIVE, 'spectral', 'special', 'dynamics', 'gate',
    )),
    product('Soundhack', '+spiralstretch (pvoc)', aumf('SDHK', '+pvm'), tags(
        t.GRAIN, 'special',
    )),

    # -Soundtoys-
    product('Soundtoys', 'Crystallizer', aufx('SToy', 'CR  '), tags(
        t.GRAIN, 'delay', 'special',
    )),
    product('Soundtoys', 'Decapitator', aufx('SToy', 'DEC '), tags(
        t.DIST, 'character', 'saturation',
    )),
    product('Soundtoys', 'DevilLoc', aufx('SToy', 'DVL '), tags(
        t.DYN, 'character', 'distortion', 'limiter', 'compressor',
    )),
    product('Soundtoys', 'DevilLoc Deluxe', aufx('SToy', 'DLD '), tags(
        t.DYN, 'character', 'distortion', 'limiter', 'compressor',
    )),
    product('Soundtoys', 'EchoBoy', aufx('SToy', 'EB  '), tags(
        t.DELAY, 'character', 'distortion',
    )),
    product('Soundtoys', 'Filterfreak1', aufx('SToy', 'FF1 '), tags(
        t.FILT, 'character', 'special',
    )),
    product('Soundtoys', 'Filterfreak2', aufx('SToy', 'FF2 '), tags(
        t.FILT, 'character', 'special',
    )),
    product('Soundtoys', 'Little AlterBoy', aumf('SToy', 'LAB '), tags(
        t.PITCH, 'vocal', 'character', 'distortion',
    )),
    product('Soundtoys', 'Little Microshift', aufx('SToy', 'LMS '), tags(
        t.MOD, 'delay', 'pitch',
    )),
    product('Soundtoys', 'Little Primaltap', aufx('SToy', 'LPT '), tags(
        t.DELAY, 'special', 'character', 'zipper-noise',
    )),
    product('Soundtoys', 'Little Radiator', aufx('SToy', 'LRD '), tags(
        t.AMP, 'character', 'amp',
    )),
    product('Soundtoys', 'Microshift', aufx('SToy', 'MCS '), tags(
        t.MOD, 'delay', 'pitch',
    )),
    product('Soundtoys', 'Panman', aufx('SToy', 'PMN '), tags(
        t.IMAGE, 'character',
    )),
    product('Soundtoys', 'Phase Mistress', aufx('SToy', 'PM  '), tags(
        t.MOD, 'special', 'character',
    )),
    product('Soundtoys', 'Radiator', aufx('SToy', 'RAD '), tags(
        t.AMP, 'character', 'amp',
    )),
    product('Soundtoys', 'Tremolator', aufx('SToy', 'TRM '), tags(
        t.MOD, 'special', 'character',
    )),

    # -SPL-
    # product('SPL', 'DeVerb', aufx('SPL1', 'SPDV'), tags(
    #     'dynamics', 'transient shaper',
    # )),

    # -Surreal Machines-
    product('Surreal Machines', 'Dub Machines', livefx, tags(
        t.DELAY, 'analog', 'creative', 'Live', 'maxforlive',
    )),

    # -Tokyo Dawn Labs-
    product('Tokyo Dawn Labs', 'TDR Kotelnikov GE', aufx('Tdrl', 'Td97'), tags(
        t.COMP, 'dynamics', 'sidechain',
    )),

    # -Twisted Tools-
    product('Twisted Tools', 'Buffeater', reaktorFX, tags(
        t.FSU, 'midi', 'creative', 'special',
    )),

    # -u-he-
    product('u-he', 'Filterscape', aumf('UHfX', 'AMEQ'), tags(
        t.FILT, 'special', 'delay',
    )),
    product('u-he', 'FilterscapeQ6', aumf('UHfX', 'FSQ6'), tags(
        t.EQ, 'dynamic',
    )),
    product('u-he', 'MFM2', aumf('UHfX', 'MFM2'), tags(
        t.DELAY, 'pitch', 'special',
    )),

    # -Unfiltered Audio-
    product('Unfiltered Audio', 'G8 Gate', aumf('UnAu', 'Gate'), tags(
        t.DYN, 'special', 'gate', 'granular',
    )),
    product('Unfiltered Audio', 'Sandman', aufx('UnAu', 'snDM'), tags(
        t.DELAY, 'special',
    )),

    # -Valhalla-
    product('Valhalla', 'Shimmer', aufx('oDin', 'shmr'), tags(
        t.VERB, 'special', 'pitch',
    )),

    # -Waldorf-
    product('Waldorf', 'D-Pole', aumf('3E00', 'DPol'), tags(
        t.FILT, 'special', 'distortion',
    )),

    # -Waves-
    product('Waves', 'Center', aufx('ksWV', 'CNTS'), tags(
        t.IMAGE, 'bass', 'exciter',
    )),
    product('Waves', 'MaxxBass', aufx('ksWV', 'MXBS'), tags(
        t.OTHER, 'bass', 'exciter',
    )),
    product('Waves', 'The Kings Microphones', aufx('ksWV', 'TKMS'), tags(
        t.AMP, 'character', 'special', 'vocal',
    )),

    # -XILS Labs-
    product('XILS Labs', 'XILS 5000', aumf('Xils', 'XiE5'), tags(
        t.PITCH, 'vocoder', 'special', 'mfx', 'sidechain',
    )),

    # -Zynaptiq-
    product('Zynaptiq', 'Morph 2', aumf('ZYNQ', 'MRPS'), tags(
        t.CREATIVE, 'special', 'morph', 'sidechain', 'vocoder',
    )),
}
