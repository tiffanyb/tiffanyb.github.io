WHO:=$(shell whoami)
USERNAME:=$(subst parno,bparno,$(WHO))
WARNING = Fill out http://www.andrew.cmu.edu/server/publish.html to push the changes!

all: build
	jekyll serve 

build:
	jekyll build
		
publish: build
	rsync -zva -e "ssh -l $(USERNAME)" _site/ unix.andrew.cmu.edu:/afs/andrew.cmu.edu/course/18/330/www/
	echo
	echo $(WARNING)
	open http://www.andrew.cmu.edu/server/publish.html

publishczarate: build
	rsync -zva -e "ssh -l czarate" _site/ unix.andrew.cmu.edu:/afs/andrew.cmu.edu/course/18/330/www
	echo
	echo $(WARNING)

clean:
	rm -rf _site/
