MR=mroulette


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

clean: Effects_clean fxbytag_clean Instruments_clean insbytag_clean

all: clean Effects fxbytag Instruments insbytag

