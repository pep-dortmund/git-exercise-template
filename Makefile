all: plot1.pdf plot2.pdf

plot1.pdf: plot1.py
	python plot1.py

plot2.pdf: plot2.py
	python plot2.py

clean:
	rm -f plot{1,2}.pdf

.PHONY: all clean
