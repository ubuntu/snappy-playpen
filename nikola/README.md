# nikola

Nikola - Static Site Generator. In goes content, out comes a website, ready to 
deploy.

  * https://getnikola.com/getting-started.html

## Current state

`nikola` nearly works, running `/snap/bin/nikola --version` spits out lots of 
errors like this:

    Error message to be added soon...

Although depending on where your nikola sites are located, some symlinking 
maybe required.

## Install

The Snap `home` plug doesn't expose the user home directory, just an isolsated 
data directory within your home directory. Therefore any existing Nikola sites 
need to be symlinked into the `nikola` snap data directory.

Run the following, which will create the data directory.

    /snap/bin/nikola --version

Now symlink your existing sites.

    ln -s ~/Websites ~/snap/nikola/x{*}/

## Usage

Full a complete Getting Started guide see the official documentation.

  * https://getnikola.com/getting-started.html

### Creating a new site

    cd ~/snap/nikola/x1/Websites/
    /snap/bin/nikola init example.org

### Building and deploying an existing site

    cd ~/snap/nikola/x1/Websites/example.org
    /snap/bin/nikola build
    /snap/bin/nikola deploy
