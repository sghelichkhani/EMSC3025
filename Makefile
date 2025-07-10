# Main Makefile for groundwater project
# Runs mkdocs in test directory and then builds slides

# Default target
all: mkdocs slides

# Run mkdocs in test directory
mkdocs:
	@echo "Building documentation with mkdocs..."
	mkdir -p test && mkdocs build -d ./test/
	@echo "Documentation built successfully"

# Run the Makefile in slides directory
slides:
	@echo "Building slides..."
	cd slides && $(MAKE) && cd ..
	@echo "Slides built successfully"

# Clean all build artifacts
clean:
	@echo "Cleaning documentation..."
	cd test && mkdocs build --clean
	@echo "Cleaning slides..."
	cd slides && $(MAKE) clean
	@echo "All cleaned"

# Serve mkdocs for development
serve:
	@echo "Starting mkdocs server..."
	cd test && mkdocs serve

# Help target
help:
	@echo "Available targets:"
	@echo "  all     - Build documentation and slides (default)"
	@echo "  mkdocs  - Build documentation with mkdocs"
	@echo "  slides  - Build slides using slides/Makefile"
	@echo "  clean   - Clean all build artifacts"
	@echo "  serve   - Start mkdocs development server"
	@echo "  help    - Show this help message"

# Phony targets
.PHONY: all mkdocs slides clean serve help