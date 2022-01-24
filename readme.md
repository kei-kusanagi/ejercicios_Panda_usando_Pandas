# Readme

Below we add configuration details to locally test your application

## To configure in windows:


## To configure in macOS:

For zsh
```zsh
# 1. Install homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. Install pyenv and it's plugin for virtualenv
brew install pyenv pyenv-virtualenv

# 3. Adds to ~/.zshrc the following lines:
echo '\n' >> ~/.zshrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/shims:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc

# 4. Activate the updated config for the current shell
exec $SHELL

# 4. Installs python 3.10.1, creates a virtualenv, 
# activates it and get dependencies.
pyenv install 3.10.1
pyenv virtualenv 3.10.1 venv_almacen
pyenv activate venv_almacen
pip install -r requirements.txt
```