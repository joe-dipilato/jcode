.PHONY:%
default:
%:
	@exit
*: %
	@echo "============================================================"
	@echo "WARNING: you should call 'just' directly"
	@echo "============================================================"
	just $(MAKECMDGOALS)
	@echo "============================================================"
	@echo "Next time just call: just $(MAKECMDGOALS)"
	@echo "============================================================"
	@exit 101