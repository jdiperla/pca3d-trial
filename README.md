# PCA 3D Adventure Studio — Trial

Browser-based Trial of PCA3D v0.76.8.

## Try it

The GitHub Pages deployment opens the Trial editor directly. Its first load downloads approximately 340 MB before browser compression, including the two demonstration templates. A stable connection and WebGL 2 support are required.

## Trial limits

- Start from the Clockmaker or Prototype template.
- No blank projects, opening existing projects, recents, saving, recovery, building or exporting.
- Per session: add 10 assets, 2 scenes, 2 GUIs and 1 cutscene.
- Five editor themes.
- Edits are temporary and are lost when the page is reloaded or closed.

This repository distributes the compiled Trial and its deployment scripts. It does not include the editable paid editor project. No open-source license is granted for the proprietary application or artwork; bundled third-party components retain their own notices.

## Complete download

Download **PCA3D-v0.76.8-Trial-WebGL.zip** from the [Trial release](https://github.com/jdiperla/pca3d-trial/releases/tag/v0.76.8-trial). GitHub's automatically generated “Source code” archives contain the hosting repository, not the complete WebGL application.

## Deployment

GitHub Pages uses GitHub Actions. The workflow downloads the complete release ZIP, checks its SHA-256 and ZIP integrity, extracts it, and deploys only the website files. `assemble.py` expects the release ZIP to be named `trial-webgl.zip`.

Release SHA-256: `179fbc09649da1c37b95adc14049dd3aba6a033538fbcb60392656be4d8cbbe6`.
