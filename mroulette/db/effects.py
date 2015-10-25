# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from mroulette.types import (
    aumu, aumf, aufx, reaktorFX, logic, livefx, product,
)
from mroulette.tags import t, tags

FX = {
    # -2c Audio-
    product('2c Audio', 'Kaleidoscope', aufx('2cau', '2cks'), tags(
        t.SPECTRAL, t.SPECIAL, t.GRAIN, t.CREATIVE, t.RESO,
    )),

    # -Abbey Road-
    product('Abbey Road', 'EMI RS 124 LE', aufx('AbRd', 'R124'), tags(
        t.COMP, t.DYN, t.CHARACTER, 'vari-mu', t.MASTER,
    )),
    product('Abbey Road', 'EMI TG12412', aufx('AbRd', 'TGeq'), tags(
        t.EQCR, t.EQ, t.CHARACTER,
    )),
    product('Abbey Road', 'EMI TG12414', aufx('AbRd', 'TGfi'), tags(
        t.EQCR, t.EQ, t.CHARACTER, t.FILT,
    )),
    product('Abbey Road', 'EMI TG12413 1969', aufx('AbRd', 'TG69'), tags(
        t.LIMIT, t.COMP, t.DYN,
    )),
    product('Abbey Road', 'EMI TG12413 2005', aufx('AbRd', 'TG05'), tags(
        t.LIMIT, t.COMP, t.DYN,
    )),

    # -accSone-
    product('accSone', 'CrusherX', aumf('bsCX', 'cXs1'), tags(
        t.GRAIN, t.SPECIAL, 'mfx',
    )),

    # -Acon Digital-
    product('Acon Digital', 'Verberate', aufx('ACON', 'ACVR'), tags(
        t.VERB, 'clean', t.DIGITAL,
    )),

    # -Aegean Music-
    product('Aegean Music', 'Spirit Reverb', aumf('Aegn', 'Amsr'), tags(
        t.VERB, 'spring', t.SPECIAL, t.AMP,
    )),

    # -Airwindows-
    # product('Airwindows', 'Pressure 3', aufx('Dthr', 'prs3'), tags(
    #    t.DYN, t.FREE, t.COMP,
    # )),
    # product('Airwindows', 'Channel 4', aufx('Dthr', 'cha4'), tags(
    #    t.DIST, t.CHARACTER, t.FREE, t.ANALOG,
    # )),
    # product('Airwindows', 'DeRez', aufx('Dthr', 'derz'), tags(
    #    t.DIST, t.CHARACTER, 'bitcrusher', t.FREE,
    # )),
    # product('Airwindows', 'DustBunny', aufx('Dthr', 'dbny'), tags(
    #    t.DIST, t.CHARACTER, 'vinyl', t.FREE,
    # )),
    # product('Airwindows', 'TapeFat', aufx('Dthr', 'tayp'), tags(
    #    t.DIST, t.CHARACTER, t.FILT, 'tape', t.FREE,
    # )),

    # -Amazing Noises-
    product('Amazing Noises', 'Compulsive Switcher', livefx, tags(
        t.CREATIVE, t.SPECIAL, t.TREMOLO, t.ABLETON, t.M4L, t.FREE,
    )),
    product('Amazing Noises', 'Dedalus Delay', livefx, tags(
        t.CREATIVE, t.SPECIAL, t.DELAY, t.ABLETON, t.M4L,
    )),
    product('Amazing Noises', 'Dedalus Delay', livefx, tags(
        t.CREATIVE, t.SPECIAL, t.DELAY, t.ABLETON, t.M4L,
    )),
    product('Amazing Noises', 'Stutter Switch', livefx, tags(
        t.FSU, t.SPECIAL, t.ABLETON, t.M4L,
    )),
    product('Amazing Noises', 'GliderVerb', livefx, tags(
        t.VERB, t.SPECIAL, t.CREATIVE, t.ABLETON, t.M4L, t.FREE,
    )),
    product('Amazing Noises', 'Grain Crusher', livefx, tags(
        t.GRAIN, t.SPECIAL, t.CREATIVE, t.ABLETON, t.M4L,
    )),
    product('Amazing Noises', 'Grain Reverser', livefx, tags(
        t.GRAIN, t.SPECIAL, t.CREATIVE, t.ABLETON, t.M4L, t.FREE,
    )),
    product('Amazing Noises', 'Granular Mirror Maze', livefx, tags(
        t.GRAIN, t.SPECIAL, t.CREATIVE, t.ABLETON, t.M4L, t.FREE,
    )),
    product('Amazing Noises', 'Grip', livefx, tags(
        t.SPECTRAL, t.GRAIN, t.CREATIVE, t.ABLETON, t.M4L,
    )),
    product('Amazing Noises', 'Spectrum Runner', livefx, tags(
        t.SPECTRAL, t.CREATIVE, t.ABLETON, t.M4L,
    )),

    # -Antares-
    product('Antares', 'Harmony Engine EVO', aumf('VST ', 'VZr2'), tags(
        t.PITCH, t.VOCAL, t.SPECIAL, 'mfx',
    )),

    # -Apple-
    product('Apple', 'AUDistortion', aufx('appl', 'dist'), tags(
        t.LOFI, t.DIST, t.CHARACTER, t.FREE, t.BITCRUSH, t.SPECIAL,
    )),

    # -Apple Logic Pro X-
    product('Apple', 'Delay Designer', logic, tags(
        t.LOGIC, t.DELAY,
        'logic:delay',
    )),
    product('Apple', 'Bitcrusher', logic, tags(
        t.LOGIC, t.BITCRUSH, t.DIST, t.CHARACTER,
        'logic:distortion',
    )),
    product('Apple', 'EVOC Filterbank', logic, tags(
        t.LOGIC, t.VOCODER, t.SPECIAL, t.FILT,
        'logic:filter',
    )),
    product('Apple', 'EVOC Track Oscillator', logic, tags(
        t.LOGIC, t.VOCODER, t.SPECIAL, t.FILT, t.SC,
        'logic:filter',
    )),
    product('Apple', 'Modulation Delay', logic, tags(
        t.LOGIC, t.MOD, t.SPECIAL, 'zipper-noise',
        'logic:modulation',
    )),
    product('Apple', 'Ringshifter', logic, tags(
        t.LOGIC, t.MOD, t.SPECIAL, t.RINGMOD, t.DELAY,
        'logic:modulation', t.SC,
    )),
    product('Apple', 'Rotor Cabinet', logic, tags(
        t.LOGIC, t.AMP, 'cabinet', t.MOD, t.CHARACTER,
        'logic:modulation',
    )),
    product('Apple', 'Scanner Vibrato', logic, tags(
        t.LOGIC, t.MOD, t.VIB, t.CHARACTER,
        'logic:modulation',
    )),
    product('Apple', 'Spreader', logic, tags(
        t.LOGIC, t.MOD, t.CHORUS, t.CHARACTER, t.IMAGE,
        'logic:modulation',
    )),
    product('Apple', 'Vocal Transformer', logic, tags(
        t.LOGIC, t.SPECIAL, t.VOCAL, t.PITCH,
        'logic:pitch',
    )),
    product('Apple', 'SubBass', logic, tags(
        t.LOGIC, t.SPECIAL, t.PITCH, t.BASS,
        'logic:specialized',
    )),
    product('Apple', 'Denoiser', logic, tags(
        t.LOGIC, t.SPECIAL, 'noise', t.SPECTRAL,
        'logic:specialized',
    )),
    product('Apple', 'Exciter', logic, tags(
        t.LOGIC, t.SPECIAL, 'zipper-noise',
        'logic:specialized',
    )),
    product('Apple', 'Phase Distortion', logic, tags(
        t.LOGIC, t.DIST, 'monitor-option',
        'logic:distortion',
    )),

    # -Audified-
    product('Audified', 'U73b Compressor', aufx('AdFd', 'U73b'), tags(
        t.COMP, t.CHARACTER,
    )),

    # -Audio Damage-
    product('Audio Damage', 'Bitcom', aumf('AuDa', 'ADbc'), tags(
        t.FSU, t.SPECIAL, t.SEQ, t.BITCRUSH, t.DIST,
    )),
    product('Audio Damage', 'Discord3', aumf('AuDa', 'ADd3'), tags(
        t.GRAIN, t.DELAY, t.SPECIAL, t.PITCH,
    )),
    product('Audio Damage', 'FuzzPlus3', aufx('AuDa', 'ADf3'), tags(
        t.DIST, t.CHARACTER,
    )),
    product('Audio Damage', 'Kombinat Dva', aufx('AuDa', 'ADkd'), tags(
        t.DIST, t.CHARACTER, t.SPECIAL, t.BITCRUSH, t.WAVESHAPE,
    )),

    # -Audio Ease-
    product('Audio Ease', 'Altiverb 7', aufx('AEas', 'AVr5'), tags(
        t.VERB, t.DELAY, t.SPECIAL,
    )),
    product('Audio Ease', 'Speakerphone 2', aumf('AEas', 'SpVl'), tags(
        t.LOFI, t.DIST, t.SPECIAL, t.CHARACTER, t.EQ,
    )),

    # -Audiothing-
    product('Audiothing', 'Frostbite', aufx('AdTg', 'FrsB'), tags(
        t.CREATIVE, t.VERB, t.CHARACTER, t.RINGMOD,
    )),

    # -Boz Digital Labs-
    #product('Boz Digital Labs', 'Bark of Dog', aufx('BDLa', 'BODg'), tags(
    #    t.EQEX, t.EQ, t.BASS, 'voice of god', t.FREE,
    #)),

    # -Brainworx-
    product('Brainworx', 'bx_saturator V2', aufx('Brwx', 'bxa2'), tags(
        t.SAT, t.CHARACTER, t.DIST,
    )),
    product('Brainworx', 'bx_tuner', aufx('Brwx', 'bxtn'), tags(
        t.PITCH, 'tuner', t.GUITAR,
    )),

    # -Celemony-
    product('Celemony', 'Melodyne Editor', aumf('CLMY', 'MPLG'), tags(
        t.PITCH, t.VOCAL, t.SPECIAL, t.CREATIVE, 'autotune',
    )),

    # -Cytomic-
    product('Cytomic', 'The Drop', aumf('Cyto', 'Drp1'), tags(
        t.FILT, t.SPECIAL, 'mfx', t.CHARACTER, t.SC,
    )),

    # -D16 Group-
    product('D16', 'Antresol', aumf('d16g', 'AnT3'), tags(
        t.MOD, t.FLANG, t.CHORUS, t.PHASER, 'bbd', t.ANALOG,
    )),
    product('D16', 'Decimort', aufx('d16g', 'DCm4'), tags(
        t.LOFI, t.CHARACTER, t.DIST,
    )),
    product('D16', 'Devastor 2', aumf('d16g', 'DV58'), tags(
        t.DIST, t.CHARACTER, t.MULTIBAND, t.CLIPPER,
    )),
    product('D16', 'Fazortan', aufx('d16g', 'F2R7'), tags(
        t.MOD, t.PHASER, t.FLANG, t.CHORUS,
    )),
    product('D16', 'Syntorus', aufx('d16g', 'Sn7R'), tags(
        t.MOD, t.CHORUS, t.PHASER,
    )),

    # -Dimitry Sches-
    product('Dimitry Sches', 'Tantra', aufx('DSCH', 'TntR'), tags(
        t.MOD, t.DELAY, t.DIST, t.FLANG, t.FSU, t.MULTIFX,
    )),

    # -DMG Audio-
    product('DMG Audio', 'Essence', aumf('DMGa', 'Esse'), tags(
        t.DYN, t.EQ, 'desser', t.VOCAL,
    )),
    product('DMG Audio', 'PitchFunk', aumf('DMGa', 'PiFu'), tags(
        t.GRAIN, t.DELAY, t.SPECIAL,
    )),

    # -Eiosis-
    product('Eiosis', 'AirEQ', aufx('Eios', 'AEq5'), tags(
        t.EQCL, t.EQ, t.CHARACTER,
    )),

    # -Eventide-
    product('Eventide', '2016 Stereo Room', aufx('TIDE', '22SR'), tags(
        t.VERB,
    )),
    product('Eventide', 'Blackhole', aufx('TIDE', 'HOLE'), tags(
        t.CREATIVE, t.VERB, t.DELAY, t.SPECIAL,
    )),
    product('Eventide', 'EChannel', aufx('Tide', 'EChn'), tags(
        t.STRIP,
    )),
    product('Eventide', 'EQ45', aufx('Tide', 'EQ45'), tags(
        t.EQCR,
    )),
    product('Eventide', 'EQ65', aufx('Tide', 'EQ65'), tags(
        t.EQCR,
    )),
    product('Eventide', 'H3000 Factory', aumf('TIDE', 'Fact'), tags(
        t.DELAY, t.PITCH, t.SPECIAL, t.SC,
    )),
    product('Eventide', 'H3000 Band Delays', aumf('Tide', 'BDls'), tags(
        t.MOD, t.SPECIAL, t.CREATIVE,
    )),
    product('Eventide', 'H910 Dual Harmonizer', aumf('Tide', 'H91d'), tags(
        t.DELAY, t.CHARACTER, t.SPECIAL, t.CREATIVE,
    )),
    product('Eventide', 'H910 Harmonizer', aumf('Tide', 'H910'), tags(
        t.DELAY, t.CHARACTER, t.SPECIAL, t.CREATIVE,
    )),
    product('Eventide', 'H949 Dual Harmonizer', aumf('Tide', 'H94d'), tags(
        t.DELAY, t.CHARACTER, t.SPECIAL, t.CREATIVE,
    )),
    product('Eventide', 'H949 Harmonizer', aumf('Tide', 'H949'), tags(
        t.DELAY, t.CHARACTER, t.SPECIAL, t.CREATIVE,
    )),
    product('Eventide', 'Instant Flanger', aumf('Tide', 'InFl'), tags(
        t.MOD, t.FLANG, t.CHARACTER, t.SPECIAL, t.CREATIVE,
    )),
    product('Eventide', 'Instant Phaser', aumf('Tide', 'InPh'), tags(
        t.MOD, t.PHASER, t.CHARACTER, t.SPECIAL, t.CREATIVE,
    )),
    product('Eventide', 'Octavox', aufx('Tide', 'OctW'), tags(
        t.PITCH, t.DELAY,
    )),
    product('Eventide', 'Omnipressor', aufx('TIDE', 'Omni'), tags(
        t.COMP, t.DYN, t.SPECIAL, 'expander', t.CHARACTER,
        t.SAT, t.SC,
    )),
    product('Eventide', 'Precision Time Align', aufx('Tide', 'PTAl'), tags(
        t.OTHER, t.DELAY,
    )),
    product('Eventide', 'Precision Time Delay', aufx('Tide', 'PTDl'), tags(
        t.OTHER, t.DELAY,
    )),
    product('Eventide', 'Quadravox', aufx('Tide', 'QudW'), tags(
        t.PITCH, t.DELAY,
    )),
    product('Eventide', 'UltraChannel', aufx('Tide', 'UlCh'), tags(
        t.STRIP, t.DYN, t.DELAY, t.EQ, t.CHARACTER,
        t.SAT, t.PITCH, t.COMP, t.SC,
    )),
    product('Eventide', 'UltraReverb', aufx('Tide', 'Revb'), tags(
        t.VERB, t.DELAY, t.SPECIAL, t.COMP, t.CHARACTER,
        t.DIST, t.SC,
    )),

    # -Expert Sleepers-
    product(
        'Expert Sleepers', 'Crossfade Loop Synth',
        aumf('ExSl', 'XFls'),
        tags(t.CREATIVE, t.SAMPLER, t.SPECIAL, 'mfx'),
    ),

    # -Exponential Audio-
    product('Exponential Audio', 'Excalibur', aufx('EXPa', 'EXca'), tags(
        t.MOD, t.DELAY, t.CHORUS, t.FLANG, t.PITCH, t.AMP, t.RINGMOD,
    )),
    product('Exponential Audio', 'PhoenixVerb', aufx('EXPa', 'MCsr'), tags(
        t.VERB,
    )),
    product('Exponential Audio', 'R2', aufx('EXPa', 'MCs2'), tags(
        t.VERB,
    )),

    # -Fabfilter-
    product('Fabfilter', 'Saturn', aumf('FabF', 'FSat'), tags(
        t.DIST, t.CREATIVE, t.CHARACTER,
    )),
    product('Fabfilter', 'Timeless 2', aumf('FabF', 'FTms'), tags(
        t.DELAY, t.CREATIVE, 'tape',
    )),
    product('Fabfilter', 'Volcano 2', aumf('FabF', 'FV2l'), tags(
        t.FILT, t.CREATIVE,
    )),

    # -Flux-
    product('Flux', 'Alchemist', aufx('Fspd', 'fxAl'), tags(
        t.FLUX, t.DYN, t.SPECIAL, t.MULTIBAND, t.COMP,
        t.MIX, t.MASTER,
    )),
    product('Flux', 'Elixir', aufx('Fspd', 'Flxr'), tags(
        t.FLUX, t.DYN, t.LIMIT, t.MIX, t.MASTER,
    )),
    product('Flux', 'Epure', aufx('Fspd', 'Ftst'), tags(
        t.EQCL, t.EQ, t.MIX, t.MASTER,
    )),
    product('Flux', 'Pure Compressor', aufx('Fspd', 'fxPc'), tags(
        t.FLUX, t.DYN, t.COMP, t.MIX, t.SC,
    )),
    product('Flux', 'Pure DCompressor', aufx('Fspd', 'fxDc'), tags(
        t.FLUX, t.DYN, t.COMP, t.MIX, t.SC,
    )),
    product('Flux', 'Pure DExpander', aufx('Fspd', 'fxDx'), tags(
        t.FLUX, t.DYN, 'deexpander', t.MIX, t.SC,
    )),
    product('Flux', 'Pure Expander', aufx('Fspd', 'fxEx'), tags(
        t.FLUX, t.DYN, 'expander', t.MIX, t.SC,
    )),
    product('Flux', 'Pure Limiter', aufx('Fspd', 'fxPl'), tags(
        t.FLUX, t.DYN, t.LIMIT, t.MIX,
    )),
    product('Flux', 'Solera', aufx('Fspd', 'fxSo'), tags(
        t.FLUX, t.DYN, t.COMP, 'decompressor',
        'expander', 'deexpander', 'mix', t.MASTER, t.SC,
    )),
    product('Flux', 'StereoToolV3', aufx('Fspd', 'fxSt'), tags(
        t.IMAGE, t.FREE,
    )),
    product('Flux', 'Syrah', aufx('Fspd', 'fxSy'), tags(
        t.FLUX, t.DYN, t.MIX, t.MASTER, 'bus',
        'track', t.COMP, t.SPECIAL,
    )),

    # -Focusrite-
    #product('Focusrite', 'RED 2 EQ', aufx('FCUS', 'rd2E'), tags(
    #    t.EQCL, t.EQ,
    #)),
    product('Focusrite', 'RED 3 Compressor', aufx('FCUS', 'rd3C'), tags(
        t.COMP, t.CHARACTER, t.DYN, 'VCA',
    )),

    # -FXpansion-
    product('FXpansion', 'Bloom', aumf('FXPN', 'FXBL'), tags(
        t.DELAY, t.SPECIAL,
    )),
    product('FXpansion', 'Etch', aumf('FXPN', 'FXET'), tags(
        t.FILT, t.SPECIAL,
    )),
    product('FXpansion', 'Maul', aumf('FXPN', 'FXMA'), tags(
        t.DIST, t.DIST, t.SPECIAL, t.MULTIBAND,
    )),

    # -Glitchmachines-
    product('Glitchmachines', 'Convex', aumf('GlMa', 'GmCo'), tags(
        t.FSU, t.CREATIVE,
    )),
    product('Glitchmachines', 'Cryogen', aumf('GlMa', 'GlCr'), tags(
        t.FSU, t.CREATIVE,
    )),
    product('Glitchmachines', 'Subvert', aumf('GlMa', 'GlSu'), tags(
        t.DIST, t.FSU,
    )),

    # -Goodhertz-
    product('Goodhertz', 'Faraday Limiter', aufx('GDHZ', 'FDLM'), tags(
        t.LIMIT, t.DYN, t.CHARACTER,
    )),
    product('Goodhertz', 'Lohi', aufx('GDHZ', 'LOHI'), tags(
        t.FILT, t.CHARACTER,
    )),
    product('Goodhertz', 'Lossy', aufx('GDHZ', 'LSSY'), tags(
        t.LOFI, t.SPECIAL, t.CHARACTER,
    )),
    product('Goodhertz', 'Panpot', aufx('GDHZ', 'PNPT'), tags(
        t.IMAGE,
    )),
    product('Goodhertz', 'Trem Control', aufx('GDHZ', 'TRM1'), tags(
        t.MOD, t.CHARACTER, t.SAT, t.TREMOLO,
    )),
    product('Goodhertz', 'Vulf Compressor', aufx('GDHZ', 'VCM1'), tags(
        t.COMP, t.DYN, t.CHARACTER, 'vinyl',
    )),

    # -Illformed-
    product('Illformed', 'Glitch2', aumu('DBlu', 'igl2'), tags(
        t.FSU, t.SPECIAL, 'mfx',
    )),

    # -Ina-GRM-
    product('Ina-GRM', 'Band pass', aumf('Grm ', 'BaPS'), tags(
        t.GRM, t.SPECIAL, t.FILT,
    )),
    product('Ina-GRM', 'Comb filters', aumf('Grm ', 'Comb'), tags(
        t.GRM, t.SPECIAL, t.FILT,
    )),
    product('Ina-GRM', 'Contrast', aumf('Grm ', 'ctrG'), tags(
        t.GRM, t.SPECIAL, t.SPECTRAL,
    )),
    product('Ina-GRM', 'Delays', aumf('Grm ', 'Dely'), tags(
        t.GRM, t.SPECIAL, t.DELAY,
    )),
    product('Ina-GRM', 'Doppler', aumf('Grm ', 'DopS'), tags(
        t.GRM, t.SPECIAL, t.DELAY, t.IMAGE,
    )),
    product('Ina-GRM', 'Evolution', aumf('Grm ', 'GrEv'), tags(
        t.GRM, t.SPECIAL,
    )),
    product('Ina-GRM', 'Equalize', aumf('aGRM', 'EquS'), tags(
        t.GRM, t.SPECIAL, t.SPECTRAL,
    )),
    product('Ina-GRM', 'Freeze', aumf('Grm ', 'Free'), tags(
        t.GRM, t.SPECIAL, t.GRAIN,
    )),
    product('Ina-GRM', 'FreqShift', aumf('Grm ', 'FrsG'), tags(
        t.GRM, t.SPECIAL, t.SPECTRAL,
    )),
    product('Ina-GRM', 'FreqWarp', aumf('Grm ', 'Fw G'), tags(
        t.GRM, t.SPECIAL, t.SPECTRAL,
    )),
    product('Ina-GRM', 'Fusion', aumf('Grm ', 'GFus'), tags(
        t.GRM, t.SPECIAL,
    )),
    product('Ina-GRM', 'Grinder', aumf('Grm ', 'Cruh'), tags(
        t.GRM, t.SPECIAL, t.SC,
    )),
    product('Ina-GRM', 'Pitch Accum', aumf('Grm ', 'Pitc'), tags(
        t.GRM, t.SPECIAL,
    )),
    product('Ina-GRM', 'Reson', aumf('Grm ', 'Reso'), tags(
        t.GRM, t.SPECIAL,
    )),
    product('Ina-GRM', 'Shuffling', aumf('Grm ', 'Shuf'), tags(
        t.GRM, t.SPECIAL, t.DELAY, t.SC,
    )),
    product('Ina-GRM', 'SpaceFilter', aumf('Grm ', 'GSFi'), tags(
        t.GRM, t.SPECIAL, t.FILT, t.IMAGE, t.SURROUND,
    )),
    product('Ina-GRM', 'SpaceGrain', aumf('Grm ', 'GSGa'), tags(
        t.GRM, t.SPECIAL, t.GRAIN, t.IMAGE, t.SURROUND,
    )),
    product('Ina-GRM', 'Spaces', aumf('Grm ', 'GrSp'), tags(
        t.GRM, t.SPECIAL, t.IMAGE, t.SURROUND,
    )),

    # -IRCAM-
    product('IRCAM', 'IM-FXSequencer', livefx, tags(
        t.FSU, t.SPECIAL, t.ABLETON, t.M4L,
    )),
    product('IRCAM', 'IM-MultibandDelay', livefx, tags(
        t.CREATIVE, t.SPECIAL, t.SPECTRAL, t.DELAY, 'IRCAM',
        t.ABLETON, t.M4L,
    )),
    product('IRCAM', 'IM-SimpleTransp', livefx, tags(
        t.GRAIN, t.SPECIAL, t.CREATIVE, 'stretch', 'IRCAM',
        t.ABLETON, t.M4L,
    )),
    product('IRCAM', 'IM-Scrub', livefx, tags(
        t.GRAIN, t.SPECIAL, t.CREATIVE, t.PITCH, 'stretch', 'IRCAM',
        t.ABLETON, t.M4L,
    )),
    product('IRCAM', 'IM-Mover', livefx, tags(
        t.GRAIN, t.SPECIAL, t.CREATIVE, t.PITCH, 'stretch', 'IRCAM',
        t.ABLETON, t.M4L,
    )),

    # -iZotope-
    product('iZotope', 'Alloy 2', aufx('iZtp', 'ZnA2'), tags(
        t.STRIP,
    )),
    product('iZotope', 'Insight', aufx('iZtp', 'ZnIS'), tags(
        t.METER,
    )),
    product('iZotope', 'Ozone 6 Advanced', aufx('iZtp', 'ZnO6'), tags(
        t.STRIP, t.MASTER, t.COMP, t.DYN, t.LIMIT, t.EQ,
        'dyneq', 'matching', t.EQEX, t.IMAGE,
    )),
    product('iZotope', 'Ozone 6 Dynamic EQ', aufx('iZtp', 'ZnY6'), tags(
        t.EQCL, t.EQ, 'dyneq', t.DYN, t.EQ,
    )),
    product('iZotope', 'Ozone 6 Dynamics', aufx('iZtp', 'ZnD6'), tags(
        t.DYN, t.DYN, t.COMP,
    )),
    product('iZotope', 'Ozone 6 Equalizer', aufx('iZtp', 'ZnE6'), tags(
        t.EQCL, t.EQ,
    )),
    product('iZotope', 'Ozone 6 Exciter', aufx('iZtp', 'ZO6X'), tags(
        t.EQEX, t.EQ,
    )),
    product('iZotope', 'Ozone 6 Imager', aufx('iZtp', 'ZnI6'), tags(
        t.IMAGE,
    )),
    product('iZotope', 'Ozone 6 Maximizer', aufx('iZtp', 'ZO6M'), tags(
        t.LIMIT,
    )),

    product('iZotope', 'Nectar 2', aumf('iZtp', 'ZnN2'), tags(
        t.STRIP, t.VOCAL,
    )),
    product('iZotope', 'Nectar 2 Breath Control', aufx('iZtp', 'ZnDB'), tags(
        t.PITCH, t.VOCAL, t.RESTORE,
    )),
    product('iZotope', 'Nectar 2 Pitch Editor', aufx('iZtp', 'ZnMP'), tags(
        t.PITCH, t.VOCAL, 'autotune',
    )),
    #product('iZotope', 'Nectar Elements', aufx('iZtp', 'ZnNE'), tags(
    #    t.STRIP, t.VOCAL,
    #)),

    product('iZotope', 'RX 5 De-click', aufx('iZtp', 'Zn5K'), tags(
        t.OTHER, t.SPECIAL, t.CREATIVE, t.RESTORE,
    )),
    product('iZotope', 'RX 5 De-clip', aufx('iZtp', 'Zn5P'), tags(
    )),
    product('iZotope', 'RX 5 De-crackle', aufx('iZtp', 'Zn5C'), tags(
        t.OTHER, t.SPECIAL, t.CREATIVE, t.RESTORE,
    )),
    product('iZotope', 'RX 5 De-hum', aufx('iZtp', 'Zn5H'), tags(
        t.OTHER, t.SPECIAL, t.CREATIVE, t.RESTORE,
    )),
    product('iZotope', 'RX 5 De-noise', aufx('iZtp', 'Zn5N'), tags(
        t.OTHER, t.SPECIAL, t.CREATIVE, t.RESTORE,
    )),
    product('iZotope', 'RX 5 De-reverb', aufx('iZtp', 'Zn5V'), tags(
        t.OTHER, t.SPECIAL, t.CREATIVE, t.RESTORE,
    )),
    product('iZotope', 'RX 5 Dialogue De-noise', aufx('iZtp', 'Zn5D'), tags(
        t.OTHER, t.SPECIAL, t.CREATIVE, t.RESTORE,
    )),

    #product('iZotope', 'RX 4 Declicker', aufx('iZtp', 'Zn4K'), tags(
    #    t.OTHER, t.SPECIAL, t.CREATIVE, t.RESTORE,
    #)),
    #product('iZotope', 'RX 4 Declipper', aufx('iZtp', 'Zn4P'), tags(
    #)),
    #product('iZotope', 'RX 4 Decrackler', aufx('iZtp', 'Zn4C'), tags(
    #    t.OTHER, t.SPECIAL, t.CREATIVE, t.RESTORE,
    #)),
    #product('iZotope', 'RX 4 Denoiser', aufx('iZtp', 'Zn4N'), tags(
    #    t.OTHER, t.SPECIAL, t.CREATIVE, t.RESTORE,
    #)),
    #product('iZotope', 'RX 4 Dialogue Denoiser', aufx('iZtp', 'Zn4D'), tags(
    #    t.OTHER, t.SPECIAL, t.CREATIVE, t.RESTORE,
    #)),
    #product('iZotope', 'RX 4 Hum Removal', aufx('iZtp', 'Zn4H'), tags(
    #    t.OTHER, t.SPECIAL, t.CREATIVE, t.RESTORE,
    #)),

    product('iZotope', 'Trash 2', aufx('iZtp', 'ZnT2'), tags(
        t.LOFI, t.SAT, t.SPECIAL, t.CREATIVE, t.CHARACTER,
    )),
    product('iZotope', 'Vinyl', aufx('iZtp', 'Vnyl'), tags(
        t.LOFI, t.SPECIAL, t.CHARACTER, t.FREE,
    )),

    # -Klanghelm-
    product('Klanghelm', 'MJUC', aufx('KlHm', 'MJUC'), tags(
        t.COMP, 'vari-mu',
    )),
    product('Klanghelm', 'SDRR', aufx('KlHm', 'SDRR'), tags(
        t.SAT, t.DIST, t.CHARACTER,
    )),
    product('Klanghelm', 'VUMTDuo', aufx('KlHm', 'VUTd'), tags(
        t.METER, 'VU', 'RMS', 'PPM', 'stereo',
    )),
    product('Klanghelm', 'VUMTSolo', aufx('KlHm', 'VUTs'), tags(
        t.METER, 'VU', 'RMS', 'PPM', 'mono',
    )),

    # -K-Devices-
    product('K-Devices', 'Holder', livefx, tags(
        t.CREATIVE, t.SPECIAL, t.SPECTRAL, 'freeze', t.ABLETON, t.M4L,
    )),
    product('K-Devices', 'Alter Echo', livefx, tags(
        t.DELAY, t.SPECIAL, t.CREATIVE, t.ABLETON, t.M4L,
    )),

    # -Klevgränd Produktion-
    product('Klevgrand Produktion', 'R0Verb', aufx('Klev', 'rvrb'), tags(
        t.VERB, t.SPECIAL,
    )),
    product('Klevgrand Produktion', 'SquashIt', aufx('Klev', 'Sqit'), tags(
        t.DIST, t.CHARACTER, t.MULTIBAND,
    )),
    product('Klevgrand Produktion', 'Svep', aufx('Klev', 'modl'), tags(
        t.MOD, t.PHASER, t.FLANG, t.CHORUS, t.FREE,
    )),
    product('Klevgrand Produktion', 'Vandelay', aufx('Klev', 'dely'), tags(
        t.DELAY, t.MULTIBAND, t.FREE,
    )),

    # -Kush Audio-
    product('Kush Audio', 'Clariphonic', aufx('Kush', 'clar'), tags(
        t.EQEX, t.EQ,
    )),
    product('Kush Audio', 'Clariphonic mkii', aufx('Kush', 'Clr2'), tags(
        t.EQEX, t.EQ, t.MS,
    )),
    product('Kush Audio', 'Electra DSP', aufx('Kush', 'Elec'), tags(
        t.EQCR, t.EQ, t.CHARACTER, t.ANALOG,
    )),
    product('Kush Audio', 'Pusher', aufx('Kush', 'Push'), tags(
        t.DIST, t.CHARACTER, t.SAT,
    )),
    product('Kush Audio', 'UBK-1', aufx('KuSh', 'dcmp'), tags(
        t.COMP, t.DYN, t.CHARACTER, t.SPECIAL, t.SAT,
    )),

    # -Lexicon-
    product('Lexicon', 'LexChamber PCM', aufx('Lexi', 'Lcm1'), tags(
        t.VERB,
    )),
    product('Lexicon', 'LexChorus', aufx('Lexi', 'Lcr1'), tags(
        t.MOD, t.CHORUS, t.DELAY,
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
        t.PITCH, t.SPECIAL, t.DELAY,
    )),
    product('Lexicon', 'LexPitchshift', aufx('Lexi', 'Lsp1'), tags(
        t.PITCH, t.SPECIAL,
    )),
    product('Lexicon', 'LexPlate PCM', aufx('Lexi', 'Lpl1'), tags(
        t.VERB,
    )),
    product('Lexicon', 'LexRandomDelay', aufx('Lexi', 'Lrd1'), tags(
        t.DELAY, t.SPECIAL,
    )),
    product('Lexicon', 'LexRandomHall PCM', aufx('Lexi', 'Lrh1'), tags(
        t.VERB,
    )),
    product('Lexicon', 'LexResonantChords', aufx('Lexi', 'Lrc1'), tags(
        t.CREATIVE, t.DELAY, t.PITCH, t.SPECIAL,
    )),
    product('Lexicon', 'LexRoom PCM', aufx('Lexi', 'Lrm1'), tags(
        t.VERB,
    )),
    product('Lexicon', 'LexStringBox', aufx('Lexi', 'Sbx1'), tags(
        t.CREATIVE, t.VERB, t.PITCH, t.SPECIAL,
    )),
    product('Lexicon', 'LexVintagePlate PCM', aufx('Lexi', 'Lpl0'), tags(
        t.VERB,
    )),

    # -Little Endian-
    product('Little Endian', 'SpectrumWorx', aufx('LE00', 'SW00'), tags(
        t.SPECTRAL, t.CREATIVE, t.SPECIAL, t.SC,
    )),

    # -Mathew Lane-
    product('Mathew Lane', 'DrMS v4', aufx('MaLa', 'DMS4'), tags(
        t.IMAGE, t.MS,
    )),

    # -Max for Cats-
    product('Max for Cats', 'Skram Delay', livefx, tags(
        t.DELAY, t.SPECIAL, t.ABLETON, t.M4L,
    )),
    product('Max for Cats', 'Stochastic Delay', livefx, tags(
        t.DELAY, t.SPECIAL, t.ABLETON, t.M4L,
    )),

    # -McDSP-
    product('McDSP', '4040 Retro Limiter', aufx('McDP', 'McDP'), tags(
        t.LIMIT, t.DYN, t.CHARACTER,
    )),
    product('MCDSP', 'AE400 Active EQ', aufx('McDP', 'McAE'), tags(
        t.EQCL, t.EQ, t.DYN, 'dyneq',
    )),
    product('McDSP', 'Analog Channel AC101', aufx('McDP', 'AC01'), tags(
        t.SAT, t.CHARACTER,
    )),
    product('McDSP', 'Analog Channel AC202', aufx('McDP', 'AC02'), tags(
        t.SAT, t.CHARACTER, 'tape',
    )),
    product('McDSP', 'FutzBox', aufx('McDP', 'Futz'), tags(
        t.LOFI, t.DIST, t.SPECIAL, t.EQ, t.CHARACTER,
    )),
    product('McDSP', 'MC2000 MC202', aufx('McDP', 'MC02'), tags(
        t.DYN, t.MULTIBAND, t.COMP,
    )),
    product('McDSP', 'MC2000 MC303', aufx('McDP', 'MC03'), tags(
        t.DYN, t.MULTIBAND, t.COMP,
    )),
    product('McDSP', 'MC2000 MC404', aufx('McDP', 'MC04'), tags(
        t.DYN, t.MULTIBAND, t.COMP,
    )),

    # -MeldaProduction-
    product(
        'MeldaProduction', 'MMultibandGranular', aumf('Meld', 'MMGr'),
        tags(t.GRAIN, t.SPECIAL, t.SC, t.MULTIBAND),
    ),
    product(
        'MeldaProduction', 'MTransformer', aumf('Meld', 'MFTr'),
        tags(t.CREATIVE, t.SPECTRAL, t.SPECIAL),
    ),

    # -Metric Halo-
    product('Metric Halo', 'MH Channel Strip', aufx('BJJk', 'Chns'), tags(
        t.STRIP, t.DYN, t.EQ,
    )),
    product('Metric Halo', 'MH Character', aufx('MHL ', 'CHAR'), tags(
        t.SAT, t.CHARACTER,
    )),
    product('Metric Halo', 'Dirty Delay', aufx('MHL ', 'DELY'), tags(
        t.DELAY,
    )),

    # -Native Instruments-
    product('Native Instruments', 'Driver', aufx('-NI-', 'Ni$='), tags(
        t.DIST, t.CHARACTER, t.SC,
    )),
    #product('Native Instruments', 'Enhanced EQ', aufx('-NI-', 'Ni$:'), tags(
    #    t.EQCL, t.EQ, t.CHARACTER,
    #)),
    product('Native Instruments', 'Guitar Rig 5', aumf('-NI-', 'NiG5'), tags(
        t.AMP, t.GUITAR, t.STRIP, t.SC,
    )),
    product('Native Instruments', 'Molekular', reaktorFX, tags(
        t.CREATIVE, t.SPECIAL, t.DELAY, t.VOCODER, t.PITCH, t.SC,
    )),
    #product('Native Instruments', 'Passive EQ', aufx('-NI-', 'Ni$9'), tags(
    #    t.EQCL, t.EQ, t.CHARACTER,
    #)),
    product('Native Instruments', 'Reaktor 6 FX', reaktorFX, tags(
        t.STRIP, 'modular', t.SC,
    )),
    #product('Native Instruments', 'RC 24', aufx('-NI-', 'Ni$>'), tags(
    #    t.VERB, t.CHARACTER,
    #)),
    #product('Native Instruments', 'RC 48', aufx('-NI-', 'Ni$?'), tags(
    #    t.VERB, t.CHARACTER,
    #)),
    product('Native Instruments', 'The Mouth', reaktorFX, tags(
        t.FSU, t.SPECIAL,
    )),
    #product('Native Instruments', 'Solid Bus Comp', aufx('-NI-', 'Ni$6'), tags(
    #    t.COMP, t.DYN,
    #)),
    #product('Native Instruments', 'Solid Dynamics', aufx('-NI-', 'Ni$7'), tags(
    #    t.DYN,
    #)),
    #product('Native Instruments', 'Solid EQ', aufx('-NI-', 'Ni$8'), tags(
    #    t.EQCL, t.EQ,
    #)),
    product(
        'Native Instruments', 'Supercharger GT',
        aufx('-NI-', 'Ni$A'),
        tags(t.COMP, t.CHARACTER,
             t.DIST, t.DYN, t.SC),
    ),
    #product(
    #    'Native Instruments', 'Transient Master',
    #    aufx('-NI-', 'Ni$5'), tags(t.TRANS, t.DYN)
    #),
    product('Native Instruments', 'Replika', aufx('-NI-', 'Ni$B'), tags(
        t.DELAY, t.VERB,
    )),
    product('Native Instruments', 'Vari Comp', aufx('-NI-', 'Ni$;'), tags(
        t.COMP, t.DYN, 'vari-mu', t.SC,
    )),
    product('Native Instruments', 'VC 160', aufx('-NI-', 'Ni$2'), tags(
        t.COMP, t.DYN, 'dbx', 'VCA',
    )),
    product('Native Instruments', 'VC 2A', aufx('-NI-', 'Ni$3'), tags(
        t.COMP, t.DYN, 'la2a', 'teletronix', 'urei', 'opto', 'tube',
    )),
    product('Native Instruments', 'VC 76', aufx('-NI-', 'Ni$4'), tags(
        t.COMP, t.DYN, 'FET', '1176',
    )),

    # -Noveltech-
    product('Noveltech', t.CHARACTER, aufx('Brwx', 'NTCH'), tags(
        t.EQEX, t.EQ,
    )),

    # -Ohm Force-
    product('Ohm Force', 'Hematohm', aumf('OmFo', 'OHmt'), tags(
        t.MOD, t.FREQSHIFT, t.RINGMOD,
    )),
    product('Ohm Force', 'Ohmicide', aumf('OmFo', 'Opd2'), tags(
        t.DIST, t.CHARACTER, t.MULTIBAND,
    )),

    # -Plogue-
    product('Plogue', 'Chipcrusher', aufx('PLOG', 'PLGP'), tags(
        t.LOFI, t.DIST, t.CHARACTER, t.BITCRUSH, t.LATENCY,
    )),

    # -PSPaudioware-
    product('PSP', 'TripleMeter', aufx('PSPa', 'PPm3'), tags(
        t.METER, 'stereo', 'VU', 'RMS', 'PPM',
    )),

    # -Relab-
    product('Relab', 'LX480 Complete', aufx('RELB', 'LX4C'), tags(
        t.VERB, t.DELAY, 'retro',
    )),

    # -Rob Chokehold-
    product('Rob Chokehold', 'Clipmax', aufx('RaCH', 'RcCm'), tags(
        t.DIST, t.CLIPPER, t.FREE,
    )),

    # -SampleSumo-
    product('SampleSumo', 'SaltyGrain', aumf('SaSu', 'StGr'), tags(
        t.GRAIN, t.DELAY, t.PITCH, 'mfx',
    )),

    # -Sinevibes-
    #product('Sinevibes', 'Atom', aufx('SNSH', 'atom'), tags(
    #    t.FILT, t.FREE,
    #)),
    #product('Sinevibes', 'Zap', aufx('SNSH', 'zzap'), tags(
    #    t.MOD, t.FREE,
    #)),

    # -Sknote-
    product('Sknote', 'Disto', aufx('SKno', 4477780), tags(
        t.COMP, t.DYN, t.CHARACTER, t.SAT, 'distressor',
    )),

    # -Slate Digital-
    #product('Slate Digital', 'FG-116 (VMR)', aufx('SlDg', 'VMXR'), tags(
    #    t.COMP, t.DYN, t.CHARACTER, 'FET', '1176',
    #)),
    #product('Slate Digital', 'FG-401 (VMR)', aufx('SlDg', 'VMXR'), tags(
    #    t.COMP, t.DYN, t.CHARACTER, 'SSL 4000', 'bus',
    #)),
    #product('Slate Digital', 'FG-N (VMR)', aufx('SlDg', 'VMXR'), tags(
    #    t.EQCR, t.EQ, t.CHARACTER,
    #)),
    #product('Slate Digital', 'FG-S (VMR)', aufx('SlDg', 'VMXR'), tags(
    #    t.EQCR, t.EQ, t.CHARACTER,
    #)),
    #product('Slate Digital', 'Revival (VMR)', aufx('SlDg', 'VMXR'), tags(
    #    t.EQEX, t.EQ, t.CHARACTER, t.FREE,
    #)),
    #product('Slate Digital', 'FG-Grey (VBC)', aufx('SlDg', 'VBCg'), tags(
    #    t.COMP, t.DYN, t.MIX, 'SSL 4000',
    #)),
    #product('Slate Digital', 'FG-MU (VBC)', aufx('SlDg', 'VBCm'), tags(
    #    t.COMP, t.DYN, t.MIX, 'vari-mu',
    #)),
    #product('Slate Digital', 'FG-Red (VBC)', aufx('SlDg', 'VBCr'), tags(
    #    t.COMP, t.DYN, t.MIX, 'VCA',
    #)),
    #product('Slate Digital', 'Virtual Mix Rack', aufx('SlDg', 'VMXR'), tags(
    #    t.STRIP,
    #)),
    product(
        'Slate Digital', 'Virtual Tape Machines',
        aufx('SlDg', 'VTMs'),
        tags(t.STRIP),
    ),

    # -Sly-fy-
    product('Sly-fy', 'Axis EQ', aufx('SlyF', 'KPI1'), tags(
        t.EQCR, t.EQ, 'api 550a', 'api 550b', t.CHARACTER, t.SAT,
    )),
    product('Sly-Fy', 'Deflector', aufx('SlyF', 'Defl'), tags(
        t.COMP, 'distressor', t.CHARACTER, t.DYN, t.SAT,
    )),
    product('Sly-Fy', 'Kaya', aufx('SlyF', 'KPA1'), tags(
        t.SAT, 'tube', 'tape', t.AMP, t.CHARACTER,
    )),


    # -Smartelectronix-
    #product('Smartelectronix', 'Ambience', aufx('MagJ', '07C0BCD2'), tags(
    #    t.VERB, t.FREE,
    #)),
    #product('Smartelectronix', 'Bouncy', aufx('BrDJ', 'BNCY'), tags(
    #    t.DELAY, t.SPECIAL, t.FREE, 'zipper-noise',
    #)),
    product('Smartelectronix', 'Buffer Override', aumf('DFX!', 'buff'), tags(
        t.CREATIVE, t.SPECIAL, t.FREE, t.FSU,
    )),
    #product('Smartelectronix', 'Geometer', aumf('DFX!', 'DFgr'), tags(
    #    t.CREATIVE, t.SPECIAL, t.CHARACTER, t.FREE, t.WAVESHAPE,
    #)),
    #product('Smartelectronix', 'Monomaker', aufx('DFX!', 'mono'), tags(
    #    t.IMAGE, t.CHARACTER, t.FREE, 'zipper-noise',
    #)),
    product('Smartelectronix', 'Polarizer', aufx('DFX!', 'pola'), tags(
        t.LOFI, t.DIST, t.CHARACTER, t.BITCRUSH, t.FREE,
    )),
    #product('Smartelectronix', 'Scrubby', aumf('DFX!', 'scub'), tags(
    #    t.CREATIVE, t.SPECIAL, t.FREE, t.PITCH,
    #)),
    #product('Smartelectronix', 'Skidder', aumf('DFX!', 'skid'), tags(
    #    t.MOD, t.TREMOLO, t.SPECIAL, t.FREE,
    #)),
    product('Smartelectronix', 'Transverb', aumf('DFX!', 'DFtv'), tags(
        t.CREATIVE, t.DELAY, t.SPECIAL, t.PITCH, t.FREE,
    )),

    # -Softube-
    product('Softube', 'Abbey Road RS127 Box', aufx('AbRd', 'r127'), tags(
        t.EQEX, t.EQ, t.CHARACTER,
    )),
    product('Softube', 'Abbey Road RS127 Rack', aufx('AbRd', 'g127'), tags(
        t.EQEX, t.EQ, t.CHARACTER,
    )),
    product('Softube', 'Abbey Road RS135', aufx('AbRd', '8kbx'), tags(
        t.EQEX, t.EQ, t.CHARACTER,
    )),
    product('Softube', 'Acoustic Feedback', aufx('SfTb', 'FbAU'), tags(
        t.AMP, t.GUITAR, t.SPECIAL,
    )),
    #product('Softube', 'Active Equalizer', aufx('SfTb', 'AcEQ'), tags(
    #    t.EQ, t.CHARACTER,
    #)),
    product('Softube', 'Bass Amp Room', aufx('SfTb', 'BARn'), tags(
        t.AMP, t.DIST, t.CHARACTER,
    )),
    product('Softube', 'Console 1', aufx('SfTb', 'ScPi'), tags(
        t.STRIP, 'ssl 4000', 'ssl 9000', t.CHARACTER, t.EQ, t.DYN,
    )),
    product('Softube', 'FET Compressor', aufx('SfTb', 'Fcpn'), tags(
        t.COMP, t.CHARACTER, t.DYN, t.SAT, t.SC,
        '1176', 'FET',
    )),
    product('Softube', 'Focusing Equalizer', aufx('SfTb', 'ChEq'), tags(
        t.EQCR, t.EQ, t.CHARACTER,
    )),
    product('Softube', 'Metal Amp Room', aufx('SfTb', 'Mtal'), tags(
        t.AMP, t.DIST, t.CHARACTER,
    )),
    product('Softube', 'Mutronics Mutator', aufx('SfTb', 'z9x7'), tags(
        t.FILT, t.CHARACTER, t.SC,
    )),
    #product('Softube', 'Passive Equalizer', aufx('SfTb', 'PvEQ'), tags(
    #    t.CHARACTER, t.EQ,
    #)),
    #product('Softube', 'Saturation Knob', aufx('SfTb', 'satn'), tags(
    #    t.SAT, t.CHARACTER,
    #)),
    product('Softube', 'Spring Reverb', aufx('SfTb', 'SpRn'), tags(
        t.VERB, 'spring',
    )),
    product('Softube', 'Summit Audio EQF-100', aufx('SfTb', 'e100'), tags(
        t.EQCR, t.EQ, t.CHARACTER,
    )),
    product(
        'Softube', 'Summit Audio Grand Channel', aufx('SfTb', 'SAGC'),
        tags(t.STRIP, t.CHARACTER, t.EQ, t.DYN,
             t.COMP, t.SAT, t.SC),
    ),
    product('Softube', 'Summit Audio TLA-100A', aufx('SfTb', 't100'), tags(
        t.COMP, t.CHARACTER, t.DYN, t.SAT, t.SC,
        'opto',
    )),
    product('Softube', 'Tonelux Tilt', aufx('SfTb', 'Tilt'), tags(
        t.EQCL, t.EQ,
    )),
    product('Softube', 'Transient Shaper', aufx('SfTb', 'Shpe'), tags(
        t.TRANS, t.DYN, t.MULTIBAND,
    )),
    product('Softube', 'Trident A-Range', aufx('SfTb', 'Aran'), tags(
        t.EQCR, t.EQ, t.CHARACTER, t.SAT,
    )),
    product('Softube', 'TSAR-1', aufx('SfTb', 'tsar'), tags(
        t.VERB,
    )),
    #product('Softube', 'TSAR-1R', aufx('SfTb', 'ts1r'), tags(
    #    t.VERB,
    #)),
    product('Softube', 'Tube Delay', aufx('SfTb', 'TbDe'), tags(
        t.DELAY, t.CHARACTER, t.SAT,
    )),
    product('Softube', 'Tube-Tech CL 1B', aufx('SfTb', 'clST'), tags(
        t.COMP, t.CHARACTER, t.DYN, t.SAT, t.SC,
        'vari-mu',
    )),
    product('Softube', 'Tube-Tech Classic Channel', aufx('SfTb', 'TTCC'), tags(
        t.STRIP, t.CHARACTER, t.DYN, t.EQ, t.COMP,
        t.SAT, t.SC,
    )),
    product('Softube', 'Tube-Tech ME 1B', aufx('SfTb', 'ME1B'), tags(
        t.EQCR, t.EQ, t.CHARACTER, t.SAT,
    )),
    product('Softube', 'Tube-Tech PE 1C', aufx('SfTb', 'PE1C'), tags(
        t.EQCR, t.EQ, t.CHARACTER, t.SAT,
    )),
    product('Softube', 'Valley People Dyna-mite', aufx('SfTb', 'DaMt'), tags(
        t.DYN, t.CHARACTER, t.GATE, 'expander', 'ducking', 'keying',
        t.COMP, t.SAT, t.SC,
    )),
    product('Softube', 'Vintage Amp Room', aufx('SfTb', 'ViAU'), tags(
        t.AMP, t.DIST, t.CHARACTER,
    )),
    #product('Softube', 'White Amp', aufx('SfTb', 'WAmp'), tags(
    #    t.AMP, t.DIST, t.CHARACTER,
    #)),

    # -Solid State Logic-
    product('Solid State Logic', 'SSL X-Saturator', aufx('SSL ', 'XSAT'), tags(
        t.SAT, t.ANALOG, t.CHARACTER,
    )),
    product('Solid State Logic', 'SSL X-Verb', aufx('_SSL', 'XVRB'), tags(
        t.VERB,
    )),

    # -Sonic Charge-
    product('Sonic Charge', 'Bitspeek', aumf('NuEd', 'NuSq'), tags(
        t.PITCH, t.VOCAL, t.SPECIAL,
    )),
    product('Sonic Charge', 'Echobode', aumf('NuEd', 'NuEB'), tags(
        t.MOD, t.SPECIAL,
    )),
    product('Sonic Charge', 'Permut8', aumf('NuEd', 'NuPr'), tags(
        t.FSU, t.SPECIAL,
    )),

    # -Sonnox-
    product('Sonnox', 'Oxford Dynamics', aufx('Sony', 'OxDy'), tags(
        t.DYN, t.CHARACTER, t.COMP, t.GATE, 'expander', t.LIMIT,
        t.SAT, t.SC,
    )),
    product('Sonnox', 'Oxford Inflator', aufx('Sony', 'OxIn'), tags(
        t.DYN, t.EQEX, t.CHARACTER,
    )),
    product('Sonnox', 'Oxford Limiter', aufx('Sony', 'OxLm'), tags(
        t.LIMIT, t.CHARACTER,
    )),
    product('Sonnox', 'Oxford TransMod', aufx('Sony', 'OxTM'), tags(
        t.TRANS, t.CHARACTER, t.DYN, t.DIST,
    )),

    # -Soundhack-
    product('Soundhack', '+bubbler', aumf('SDHK', '+bub'), tags(
        t.GRAIN, t.DELAY, t.SPECIAL,
    )),
    product('Soundhack', '++chebyshev', aufx('SDHK', '+2ch'), tags(
        t.CREATIVE, t.DIST, t.SPECIAL,
    )),
    #product('Soundhack', '++compand', aufx('SDHK', '+2cm'), tags(
    #    t.DYN, t.DYN, t.FREE,
    #)),
    product('Soundhack', '++decimate', aufx('SDHK', '+210'), tags(
        t.LOFI, t.CHARACTER, t.BITCRUSH, t.FREE,
    )),
    #product('Soundhack', '+delay', aumf('SDHK', '+dla'), tags(
    #    t.DELAY, t.FREE,
    #)),
    #product('Soundhack', '+matrix', aufx('SDHK', '+mtx'), tags(
    #    t.SPECIAL, t.FREE,
    #)),
    product('Soundhack', '++morphfilter', aufx('SDHK', '+mrf'), tags(
        t.SPECTRAL, t.FILT, t.SPECIAL,
    )),
    product('Soundhack', '+phasemash (pvoc)', aumf('SDHK', '+pvx'), tags(
        t.CREATIVE, t.SPECIAL,
    )),
    #product('Soundhack', '++phasor', aumf('SDHK', '+2pz'), tags(
    #    t.MOD, t.SPECIAL, t.PHASER, t.FREE,
    #)),
    product('Soundhack', '+pitchdelay', aumf('SDHK', '+pdl'), tags(
        t.DELAY, t.PITCH, t.SPECIAL,
    )),
    product('Soundhack', '+pitchsift (pvoc)', aumf('SDHK', '+pvp'), tags(
        t.CREATIVE, t.VOCODER, t.PITCH, 'harmonics', t.SPECIAL,
    )),
    product('Soundhack', '+pvocloop (pvoc)', aumf('SDHK', '+pvt'), tags(
        t.CREATIVE, t.SPECIAL, t.GRAIN, 'mfx',
    )),
    product('Soundhack', '++spectralcompand', aufx('SDHK', '+2sc'), tags(
        t.SPECTRAL, t.CREATIVE, t.SPECIAL, t.EQ,
    )),
    product('Soundhack', '++spectralgate', aufx('SDHK', '+2sg'), tags(
        t.SPECTRAL, t.CREATIVE, t.SPECIAL, t.DYN, t.GATE,
    )),
    product('Soundhack', '+spiralstretch (pvoc)', aumf('SDHK', '+pvm'), tags(
        t.GRAIN, t.SPECIAL,
    )),

    # -Soundtoys-
    product('Soundtoys', 'Crystallizer', aufx('SToy', 'CR  '), tags(
        t.GRAIN, t.DELAY, t.SPECIAL,
    )),
    product('Soundtoys', 'Decapitator', aufx('SToy', 'DEC '), tags(
        t.SAT, t.CHARACTER,
    )),
    product('Soundtoys', 'DevilLoc', aufx('SToy', 'DVL '), tags(
        t.LIMIT, t.CHARACTER, t.DIST, t.COMP,
    )),
    product('Soundtoys', 'DevilLoc Deluxe', aufx('SToy', 'DLD '), tags(
        t.LIMIT, t.CHARACTER, t.DIST, t.COMP,
    )),
    product('Soundtoys', 'EchoBoy', aufx('SToy', 'EB  '), tags(
        t.DELAY, t.CHARACTER, t.DIST,
    )),
    product('Soundtoys', 'EffectRack', aumf('SToy', 'FXR '), tags(
        t.STRIP, t.MULTIFX,
    )),
    product('Soundtoys', 'Filterfreak1', aufx('SToy', 'FF1 '), tags(
        t.FILT, t.CHARACTER, t.SPECIAL,
    )),
    product('Soundtoys', 'Filterfreak2', aufx('SToy', 'FF2 '), tags(
        t.FILT, t.CHARACTER, t.SPECIAL,
    )),
    product('Soundtoys', 'Little AlterBoy', aumf('SToy', 'LAB '), tags(
        t.PITCH, t.VOCAL, t.CHARACTER, t.DIST,
    )),
    product('Soundtoys', 'Little Microshift', aufx('SToy', 'LMS '), tags(
        t.MOD, t.DELAY, t.PITCH,
    )),
    product('Soundtoys', 'Little Primaltap', aufx('SToy', 'LPT '), tags(
        t.DELAY, t.SPECIAL, t.CHARACTER, 'zipper-noise',
    )),
    product('Soundtoys', 'Little Radiator', aufx('SToy', 'LRD '), tags(
        t.AMP, t.CHARACTER,
    )),
    product('Soundtoys', 'Microshift', aufx('SToy', 'MCS '), tags(
        t.MOD, t.DELAY, t.PITCH,
    )),
    product('Soundtoys', 'Panman', aufx('SToy', 'PMN '), tags(
        t.IMAGE, t.CHARACTER,
    )),
    product('Soundtoys', 'Phase Mistress', aufx('SToy', 'PM  '), tags(
        t.MOD, t.SPECIAL, t.CHARACTER,
    )),
    product('Soundtoys', 'Primaltap', aumf('SToy', 'PT  '), tags(
        t.DELAY, t.SPECIAL, t.DIGITAL, 'lexicon', 'primetime',
    )),
    product('Soundtoys', 'Radiator', aufx('SToy', 'RAD '), tags(
        t.AMP, t.CHARACTER,
    )),
    product('Soundtoys', 'Tremolator', aufx('SToy', 'TRM '), tags(
        t.MOD, t.SPECIAL, t.CHARACTER,
    )),

    # -SPL-
    #product('SPL', 'DeVerb', aufx('SPL1', 'SPDV'), tags(
    #    t.TRANS, t.DYN,
    #)),

    # -Sugar Bytes-
    product('Sugar Bytes', 'Turnado', aumf('Sbar', 'sbtu'), tags(
        t.FSU,
    )),

    # -Surreal Machines-
    product('Surreal Machines', 'Dub Machines', livefx, tags(
        t.DELAY, t.ANALOG, t.CREATIVE, t.ABLETON, t.M4L,
    )),

    # -Tokyo Dawn Labs-
    product('Tokyo Dawn Labs', 'TDR Kotelnikov GE', aufx('Tdrl', 'Td97'), tags(
        t.COMP, t.DYN, t.SC,
    )),

    # -Tritik-
    product('Tritik', 'Moodal', aumf('TrTk', 'tkMd'), tags(
        t.SPECTRAL, t.SPECIAL, t.RESO, t.CREATIVE,
    )),


    # -Twisted Tools-
    product('Twisted Tools', 'Buffeater', reaktorFX, tags(
        t.FSU, 'midi', t.CREATIVE, t.SPECIAL,
    )),

    # -u-he-
    product('u-he', 'Filterscape', aumf('UHfX', 'AMEQ'), tags(
        t.FILT, t.SPECIAL, t.DELAY,
    )),
    product('u-he', 'FilterscapeQ6', aumf('UHfX', 'FSQ6'), tags(
        t.EQCL, t.EQ,
    )),
    product('u-he', 'MFM2', aumf('UHfX', 'MFM2'), tags(
        t.DELAY, t.PITCH, t.SPECIAL,
    )),
    product('u-he', 'Satin', aumf('UHfX', 'uhST'), tags(
        t.LOFI, t.SAT, t.DELAY, t.MOD, t.FLANG, 'tape', t.CHARACTER,
    )),

    # -Unfiltered Audio-
    product('Unfiltered Audio', 'G8 Gate', aumf('UnAu', 'Gate'), tags(
        t.DYN, t.SPECIAL, t.GATE, t.GRAIN,
    )),
    product('Unfiltered Audio', 'Sandman', aufx('UnAu', 'snDM'), tags(
        t.DELAY, t.SPECIAL,
    )),

    # -UVI-
    product('UVI', 'Relayer', aufx('UVI ', 'Rela'), tags(
        t.DELAY, t.SPECIAL, t.GRAIN, t.MOD, 'comb', 'time',
        'swing', t.LOFI, t.CHARACTER,
    )),

    # -Valhalla-
    #product('Valhalla', 'Shimmer', aufx('oDin', 'shmr'), tags(
    #    t.VERB, t.SPECIAL, t.PITCH,
    #)),

    # -Vertigo-
    product('Vertigo', 'VSC-2', aufx('Brwx', 'VSC2'), tags(
        t.COMP, t.CHARACTER, t.DYN, 'VCA',
    )),
    product('Vertigo', 'VSM-3', aufx('Brwx', 'VSM3'), tags(
        t.SAT, t.CHARACTER, t.DIST, t.MS, 'FET', 'valve',
    )),

    # -Waldorf-
    product('Waldorf', 'D-Pole', aumf('3E00', 'DPol'), tags(
        t.FILT, t.SPECIAL, t.DIST,
    )),

    # -Waves-
    #product('Waves', 'Center', aufx('ksWV', 'CNTS'), tags(
    #    t.IMAGE, t.MS,
    #)),
    product('Waves', 'MaxxBass', aufx('ksWV', 'MXBS'), tags(
        t.EQEX, t.EQ, t.BASS,
    )),
    product('Waves', 'The Kings Microphones', aufx('ksWV', 'TKMS'), tags(
        t.AMP, t.CHARACTER, t.SPECIAL, t.VOCAL,
    )),

    # -XILS Labs-
    product('XILS Labs', 'XILS 5000', aumf('Xils', 'XiE5'), tags(
        t.PITCH, t.VOCODER, t.SPECIAL, 'mfx', t.SC,
    )),

    # -Zynaptiq-
    product('Zynaptiq', 'Morph 2', aumf('ZYNQ', 'MRPS'), tags(
        t.CREATIVE, t.SPECIAL, 'morph', t.SC, t.VOCODER,
    )),
    product('Zynaptiq', 'Pitchmap', aumf('ZYNQ', 'PTMP'), tags(
        t.PITCH, 'autotune', t.CREATIVE, t.LATENCY,
    )),
}
