# Makefile for compiling Quarkdown documents
# Uses quarkdown c command with -o ./dir/ --pretty --clean options

# Define the output directory
OUTPUT_DIR = ./dir/

# List of numbered .qmd files to compile
QMD_FILES = 00_introduction.qmd 01_IntroductionToWaterResources.qmd 02_precipitation.qmd 03_evapotranspiration.qmd 04_run_off.qmd 05_groundwater.qmd

# Define the quarkdown command with your preferred options
QUARKDOWN_CMD = quarkdown c

# Default target
all: $(QMD_FILES:.qmd=.html)

# Pattern rule to compile each .qmd file
%.html: %.qmd
	@echo "Compiling $< to $(OUTPUT_DIR)"
	$(QUARKDOWN_CMD) $< -o $(OUTPUT_DIR)
# Clean target to remove output files
clean:
	@echo "Cleaning output directory..."
	rm -rf $(OUTPUT_DIR)/*

# Help target
help:
	@echo "Available targets:"
	@echo "  all     - Compile all .qmd files (default)"
	@echo "  clean   - Remove all compiled files from output directory"
	@echo "  help    - Show this help message"
	@echo ""
	@echo "Individual files can be compiled with: make filename.html"
	@echo "Example: make 02_precipitation.html"

# Phony targets
.PHONY: all clean help