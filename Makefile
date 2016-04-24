MR=mroulette


cleans:
	rm -rf Effects/*
	rm -rf AMixing/*
	rm -rf BCreative/*
	rm -rf Instruments/*
	rm -rf fxbytag/*
	rm -rf insbytag/*


AMixing:
	$(MR) genfavmixfx $@

AMixing_clean:
	rm -rf AMixing/

BCreative:
	$(MR) genfavcreative $@

BCreative_clean:
	rm -rf BCreative/

Effects:
	$(MR) genfavfx $@

Effects_clean:
	-rm -rf Effects/

fxbytag:
	$(MR) genfx $@

fxbytag_clean:
	-rm -rf fxbytag/

Instruments:
	$(MR) genfavinst $@

Instruments_clean:
	-rm -rf Instruments/

insbytag:
	$(MR) geninst $@

insbytag_clean:
	-rm -rf insbytag/

fxclean: AMixing_clean BCreative_clean Effects_clean fxbytag_clean
instclean: Instruments_clean insbytag_clean

distclean: fxclean instclean

all: cleans AMixing BCreative Effects fxbytag Instruments insbytag

