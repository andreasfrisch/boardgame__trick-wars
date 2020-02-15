All: moveassets clean

cards:
	python card_generation.py
	./latexdockercmd.sh pdflatex cards.tex
	./latexdockercmd.sh pdflatex territory_cards.tex

tiles:
	./latexdockercmd.sh pdflatex action_tiles.tex

moveassets: cards tiles
	mv cards.pdf ../
	mv territory_cards.pdf ../
	mv action_tiles.pdf ../


clean:
	rm *.log *.aux cards.tex
