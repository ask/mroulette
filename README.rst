Musical roulette
================

Installation
------------

To install use::

    $ sudo python setup.py develop

or use a virtualenv (Python-persons will know what to do)

Usage
-----

Stupid personal project that maintains a database over instruments,
effects and sample libraries and enables you to:

- Generate a random instrument, along with a selection of effects to apply to
  that track

    Have way too much gear? Use ``mr`` to tell you what should be on each new
    track::

        $ mr
        ============================
        Ships Piano MK2 (SoundDUST)
        ============================

        reverb:    Toraverb (D16)
        delay:     LX480 Complete (Relab)
        special:   Crossfade Loop Synth (Expert Sleepers)
        character: RC 48 (Native Instruments)
        dynamics:  Oxford Dynamics (Sonnox)
        eq:        RED 2 EQ (Focusrite)

- Generate Ableton Live presets by category (OSX/Audiounit only)

    Use make to make all sections::

        $ make -B all

    The sections are generated into separate directories that you can add
    to your Ableton Live sidebar:

        - Effects/

            All effects by category (first tag in list of product tags).

        - AMixing/

            All mixing related effects by category (tagged with ``MIX``).

        - BCreative/

            All creative effects by category (tagged with ``CREATIVE``).

        - Instruments

            All instruments by brand.

        - fxbytag/

            Directory of tags, containing effect presets.

        - insbytag/

            Directory of tags, containing instrument presets.




Even though after years of loving audio I have nearly all
audio software ever released in my collection.  But only nearly, your
collection may be bigger (help add them) or smaller (eh, I guess you have to
fork and tag them as ``SOLD``).

I started working on a web view (in ``mrview``) late one Saturday, but never
finished it.


Contributing
------------

Database of effects is in ``mroulette/db/effects.py``, instruments is in
``mroulette/db/instruments.py``.

If you want to add a new audio unit, you need to find the AU id for that
plugin, e.g::

    product('Cytomic', 'The Drop', aumf('Cyto', 'Drp1'), tags(
        t.FILT, t.SPECIAL, 'mfx', t.CHARACTER, t.SC,
    )),

Here the autype is ``aumf``, the publisher is ``Cyto`` and the product is ``Drp1``.

The easiest way I have found to get this is by opening Logic Pro ->
Preferences -> Plugin Manager, select the plugin you want and rescan the
effect.  A window will open, scroll it to the top once the scan completes to
find the AU id (note the order is reversed here, it's type, product, publisher).

Possibly there's an easier way to do this using the auval command, but that
shit is a mystery.  Possibly the most unintuitive command ever.
