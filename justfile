# List possible actions, then exit
default:
    just --list

# Run tests using tox across multiple Python versions
test *ARGS:
    pytest {{ARGS}}

# Build the package with uv
build:
    uv build

# Remove build artifacts
clean:
    rm -rf build dist docs/_build
    rm -rf src/*.egg-info
    rm -rf docs/sphinx/build

# Build documentation with Sphinx
docs:
    sphinx-apidoc src/ -o docs/sphinx/source/api
    sphinx-build --color docs/sphinx/source/ docs/sphinx/build/html

# Open the local file for the documentation homepage
view-docs:
    open docs/sphinx/build/html/index.html
