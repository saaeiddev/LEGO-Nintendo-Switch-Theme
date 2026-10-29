# LEGO Nintendo Switch Theme

> **Work in progress — experimental HOME package only.** This is not the complete multi-screen theme and has not been tested on a Nintendo Switch. Do not treat it as a final release.

![Original HOME artwork](artwork/lego-home.jpg)

An unofficial fan-made theme concept for the original Nintendo Switch family. The original AI-generated art and its 1280 × 720 baseline JPEG export are included. The current HOME package uses the stock system layout; the image is not an actual console screenshot. No Nintendo system files are distributed.

## Status

- HOME background: experimental NXThemes 3 ZIP-format package in `themes/`.
- Lock, all applications, profile, settings, news and player select: **not yet designed or packaged**.
- NxThemeTool validation: pending. Console installation, compatibility, contrast and usability: **not tested**.
- Release and complete package: not available.

## Compatibility and installation

Requires a compatible original Switch, Switch Lite or Switch OLED with Atmosphère and NXThemes Installer. Switch 2 is not supported or tested. Firmware and layout compatibility cannot be guaranteed without testing. Check the [installer release notes](https://github.com/exelix11/SwitchThemeInjector/releases) for current firmware and patch requirements. Back up your SD card and remove themes before updating firmware. The upstream project documents installation and recovery: https://github.com/exelix11/SwitchThemeInjector

## Rebuild

Run `python3 scripts/build_home.py` with Pillow installed. Verify with `NxThemeTool validate themes/LEGO-HOME-EXPERIMENTAL.nxtheme`. This project does not bundle NxThemeTool. `artwork/lego-home-original.png` is the generated source image and `artwork/lego-home.jpg` is the installer-sized image. The original has no editable 3D scene or layered source.

LEGO and Nintendo are trademarks of their respective owners. This unofficial fan project is not affiliated with or endorsed by either company. Artwork is AI-generated. Tooling credit: [SwitchThemeInjector / NXThemes Installer](https://github.com/exelix11/SwitchThemeInjector).

[فارسی](README_FA.md)
