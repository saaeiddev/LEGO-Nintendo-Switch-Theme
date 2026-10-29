# LEGO Nintendo Switch Theme

An unofficial fan-made LEGO-inspired background theme for the original Nintendo Switch family. Seven separate NXTheme packages retain the system's stock layout; icons and navigation are not replaced.

[فارسی](README_FA.md) · [Download complete ZIP](dist/LEGO-Nintendo-Switch-Theme.zip) · [Individual themes](themes/) · [Checksums](dist/SHA256SUMS.txt)

## Concept previews

These are **composited conceptual mockups**, not screenshots from a console. Icons, labels and placement are illustrative; actual firmware and system settings can look different.

![HOME concept](previews/home-concept.jpg)
![Lock concept](previews/lock-concept.jpg)
![Games concept](previews/apps-concept.jpg)
![Profile concept](previews/user-concept.jpg)
![Settings concept](previews/set-concept.jpg)

## Theme parts

| Screen | File | Artwork |
|---|---|---|
| HOME | [LEGO-Home](themes/LEGO-Home.nxtheme) | City |
| Lock | [LEGO-Lock](themes/LEGO-Lock.nxtheme) | Space station |
| All software | [LEGO-Games](themes/LEGO-Games.nxtheme) | Construction |
| Profile | [LEGO-Profile](themes/LEGO-Profile.nxtheme) | Explorer |
| Settings | [LEGO-Settings](themes/LEGO-Settings.nxtheme) | Gears |
| News | [LEGO-News](themes/LEGO-News.nxtheme) | Construction, reused |
| Player select | [LEGO-Player-Select](themes/LEGO-Player-Select.nxtheme) | Explorer, reused |

## Compatibility and validation

Targets Switch, Switch OLED and Switch Lite running compatible Atmosphère CFW and NXThemes Installer 3.0 or newer. Switch 2 is not targeted. Upstream 3.0.2 release notes state support for firmware 23.0 / 23.0.1 with Atmosphère 1.12.1 or newer; check [upstream releases](https://github.com/exelix11/SwitchThemeInjector/releases) for current firmware and patch requirements. This project has **not been installed on hardware**; readability, layout and compatibility with any particular firmware are unverified.

Built and validated with NxThemeTool from upstream commit `66ccc56c6370908cbc1b09059122004cbb6ee605` (ThemesCommon 4.9): pack and validate reported no warnings on all seven files. ZIP integrity, manifests and JPEG dimensions were also checked. No proprietary SZS files are included. Artwork is AI-generated raster imagery; editable 3D scenes are not available. No custom layout patches or modified application icons are included.

## Installation

1. Back up the SD card and ensure compatible CFW, installer and patches are installed. Remove themes before firmware updates.
2. Extract the ZIP and copy the `.nxtheme` files to `/themes/` on the SD card.
3. Open NXThemes Installer, install desired parts, and reboot. For system-data extraction and current steps consult the [upstream guide](https://github.com/exelix11/SwitchThemeInjector).
4. If the console fails to boot, follow upstream recovery instructions; uninstall normally from the installer.

## Build

Install Python 3 with Pillow, .NET 8 and [NxThemeTool](https://github.com/exelix11/SwitchThemeInjector). On Linux/macOS run `DOTNET=dotnet NXTHEME_TOOL=/path/to/NxThemeTool.dll python3 scripts/build.py`, substituting the correct DLL path. Alternatively set `NXTHEME_TOOL` to its executable and omit `DOTNET`. The script exports baseline JPEGs, invokes the official packer and validator, verifies archives, creates the ZIP and writes SHA-256 checksums. `python3 scripts/previews.py` regenerates the mockups and requires DejaVu Sans fonts.

`artwork/originals/` contains original generated images; `artwork/backgrounds/` contains the exports; `scripts/` contains build and preview code; `previews/` has conceptual mockups; `themes/` has individual files; `dist/` has the bundle and checksums. `INSTALL.txt` provides short instructions.

## Troubleshooting and credits

If installation fails, check installer and firmware compatibility and current patches. If text overlaps artwork, uninstall that part. When updating firmware remove themes first; see the upstream guide for recovery and the SD-card path. No Nintendo system data is distributed here.

Created for Amir Saeid Dehghan. AI-generated art; mockups are illustrative. Packer and installer: [exelix11 / SwitchThemeInjector](https://github.com/exelix11/SwitchThemeInjector). LEGO and Nintendo are trademarks of their respective owners. This unofficial fan project is not affiliated with or endorsed by either company.
