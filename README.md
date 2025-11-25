# HA Custom Integration Devcontainer

[![Static Badge](https://img.shields.io/badge/HACS-default-orange?style=for-the-badge&logo=homeassistantcommunitystore&logoColor=white)](https://hacs.xyz/)
[![Static Badge](https://img.shields.io/badge/template-1.0.2--beta-blue?style=for-the-badge&logo=github)](https://github.com/lalexdotcom/ha-custom-integration-template/releases/tag/1.0.0-beta.2)



Start your [Home Assistant Custom Integration](https://developers.home-assistant.io/docs/creating_component_index/) for [Home Assistant Community Store (HACS)](https://hacs.xyz/) from a brand new test-ready and publish-ready project structure

## About
This repository template is just a VSCode devcontainer which gonna deploy a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template based on the [integration_blueprint](https://github.com/ludeeus/integration_blueprint) bootstrap and inspired by [cookiecutter-homeassistant-custom-component](https://github.com/oncleben31/cookiecutter-homeassistant-custom-component).

## Prerequisites
This template is a devcontainer for VS Code. Be sure to know how those things work...

## Installation
1. At the top right of this repository page, select the green button "Use this template" to create your new own custom integration repository (see [Github repository template doc](https://docs.github.com/fr/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template))
2. Clone your newly created repository in VS Code (see the see the [VSCode docs](https://code.visualstudio.com/docs/devcontainers/containers))
3. Reopen it in provided devcontainer (a popup should show up)
4. Answer to prompts when asked
5. Let the magic happen! :sparkles: :sparkles: :sparkles:

> [!WARNING]
> All files outside of the .devcontainer might be overwritten by the template (including this README)
> The default licence ifrom the template is MIT, consider updating the LICENSE file if you want a different licence

## Features
Every integration_blueprint features are here (Github Workflows, default structure, python environment and test home assistant instance), some of [cookiecutter-homeassistant-custom-component](https://github.com/oncleben31/cookiecutter-homeassistant-custom-component) also, and a bit more...
- Start from a brand new test-ready and production-ready folder structure
- Auto retrieval of github repository URL, project name and owner
- VSCode tasks to Run Home Assistant instance and Lint code
- Pre-filled class names
- README draft with HACS button link to my.home-assistant.io

For more infos and roadmap, please check the [template repository](https://github.com/lalexdotcom/ha-custom-integration-template)

## Roadmap
- Add versionning and release scripts
- Add test suite

## Publishing
You juste need to keep the HACS button on the README file to allow users adding your custom integration repository to HACS.

Please refer to the [HACS publish page](https://www.hacs.xyz/docs/publish/integration/) to match the required specifications before publish (basically, you just have to handle the (https://github.com/home-assistant/brands) part)...