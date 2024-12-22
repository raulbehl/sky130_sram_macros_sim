
TOPLEVE_LANG = "verilog"
TOPLVEL = "sky130_sram_1kbyte_1rw1r_32x256_8_top"
MODULE = "sky130_sram_1kbyte_1rw1r_32x256_8_tb"
VERILOG_SOURCES = sky130_sram_1kbyte_1rw1r_32x256_8.v \
                  sky130_sram_1kbyte_1rw1r_32x256_8_top.v

include $(shell cocotb-config --makefiles)/Makefile.sim

