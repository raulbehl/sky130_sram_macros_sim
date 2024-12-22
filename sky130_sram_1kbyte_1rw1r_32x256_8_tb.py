# Cocotb testbench for SRAM

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge, ReadWrite, FallingEdge

import random

@cocotb.coroutine
async def sram_test(dut):

  sram_rand_addr = []

  # Generate the clock
  clock = cocotb.start_soon(Clock(dut.clk, 10, 'us').start(start_high=False))

  # Initial values of input
  dut.sram_cs_i.value = 0x0
  dut.sram_we_i.value = 0x0

  # Wait for few clocks
  for _ in range(4):
    await RisingEdge(dut.clk)

  # Write into random address
  for i in range(256):
    sram_rand_addr.append(random.randrange(0, 256))
    dut.sram_cs_i.value = 0x1
    dut.sram_we_i.value = 0x1
    dut.sram_addr_i.value = sram_rand_addr[i]
    dut.sram_wmask_i.value = random.randrange(0, 4)
    dut.sram_wr_data_i.value = random.randrange(0, 0xFFFFFFFF)
    await RisingEdge(dut.clk)

  random.shuffle(sram_rand_addr)
  # Read from the random addresses
  for i in range(256):
    dut.sram_cs_i.value = 0x1
    dut.sram_we_i.value = 0x0
    dut.sram_addr_i.value = sram_rand_addr[i]
    await RisingEdge(dut.clk)

  # Wait for few clocks
  for _ in range(4):
    await RisingEdge(dut.clk)

  clock.kill()

@cocotb.test()
def sram_rand_test(dut):
  yield sram_test(dut)
