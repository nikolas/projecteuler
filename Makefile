execs = one.native two.native three.native four.native five.native six.native

all: $(execs)

$(execs): %.native: %.ml
	corebuild $@

.PHONY: clean
clean:
	rm -rf _build
	rm *.native
