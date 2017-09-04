execs = one.native two.native three.native four.native five.native \
	six.native seven.native twentyone.native

all: $(execs)

$(execs): %.native: %.ml
	corebuild $@

.PHONY: clean
clean:
	rm -rf _build
	rm -f *.native
