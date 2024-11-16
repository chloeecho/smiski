# ![Logo](/assets/game/32x32_cursor.png) Curse of the Smiski

For an optimal experience, make sure all of the extensions in `.vscode/extensions.json` are installed.

## Setup

This project uses [rye](https://github.com/mitsuhiko/rye) for dependency management. After [installing it](https://rye-up.com/guide/installation/), use the following instructions:

On first usage:

```bash
rye sync # Create the virtual environment and install dependencies
```

Run the game:

```bash
rye run python3 src/main.py
# or
sudo chmod +x run.sh # only needs to be run the first time
./run.sh
```

## Dependencies

Adding dependencies:

```bash
rye add <package> # For regular dependencies
rye add --dev <package> # For development dependencies
```

Removing dependencies:

```bash
rye remove <package>
```

Applying changes:

```bash
rye sync # Run after adding or removing dependencies
```

For more information, see the [usage instructions](https://rye-up.com/guide/basics/).
