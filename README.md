![Mycroft Pierre Tombale](https://raw.githubusercontent.com/stevechretien111/Not-a-project/main/mycroft-pierre_tombale.png)


[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE.md) 
[![CLA](https://img.shields.io/badge/CLA%3F-Required-blue.svg)](https://mycroft.ai/cla) 
[![Team](https://img.shields.io/badge/Team-Mycroft_Core-violetblue.svg)](https://github.com/MycroftAI/contributors/blob/master/team/Mycroft%20Core.md) 
![Status](https://img.shields.io/badge/-Production_ready-green.svg)

- [What about this project](#what-about-this-project)
- [A propos de ce projet](#a-propos-de-ce-projet)

![Unit Tests](https://github.com/mycroftai/mycroft-core/workflows/Unit%20Tests/badge.svg)
[![codecov](https://codecov.io/gh/MycroftAI/mycroft-core/branch/dev/graph/badge.svg?token=zQzRlkXxAr)](https://codecov.io/gh/MycroftAI/mycroft-core)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![Join chat](https://img.shields.io/badge/Mattermost-join_chat-brightgreen.svg)](https://chat.mycroft.ai)

# Mycroft

Mycroft is a hackable open source voice assistant.

## Table of Contents

- [Getting Started](#getting-started)
- [Running Mycroft](#running-mycroft)
- [Using Mycroft](#using-mycroft)
  * [*Home* Device and Account Manager](#home-device-and-account-manager)
  * [Skills](#skills)
- [Behind the scenes](#behind-the-scenes)
  * [Pairing Information](#pairing-information)
  * [Configuration](#configuration)
  * [Using Mycroft Without Home](#using-mycroft-without-home)
  * [API Key Services](#api-key-services)
  * [Using Mycroft behind a proxy](#using-mycroft-behind-a-proxy)
    + [Using Mycroft behind a proxy without authentication](#using-mycroft-behind-a-proxy-without-authentication)
    + [Using Mycroft behind an authenticated proxy](#using-mycroft-behind-an-authenticated-proxy)
- [Getting Involved](#getting-involved)
- [Links](#links)


## What about this project

"I'm currently working on Mycroft to address the lack of online services that no longer exist. My main goal is to enable Mycroft users to continue using it, especially for those who prefer not to turn to alternatives. Additionally, I aim to port Mycroft to Windows, knowing that the majority of users have a computer running this operating system, and since Mycroft is primarily developed in Python, this should be achievable and significantly extend its accessibility.Next, I want to translate Mycroft skills into as many languages as possible and ideally create new skills to expand its functionality. I firmly believe that making Mycroft available on Windows will significantly increase its user base. Similarly, translating skills into different languages ​​is crucial because although English is widely spoken, some users prefer to interact with software in their native language for a more natural and immersive experience.I also think it's important to develop a user-friendly graphical interface for skill installation and general system configuration. Not everyone is comfortable with command lines or editing configuration files, and a web interface would be a perfect addition to make Mycroft even more accessible.Although I have no programming background, I rely on tools like Sourcegraph's Cody and ChatGPT to generate code and help me understand how it works. If anyone is interested in this project, whether they're a programmer or not, any contribution is welcome. Mycroft is an open source and community-driven project, and I'm confident that we can create something useful, efficient, and truly awesome with everyone's knowledge and talents."

## A propos de ce projet

Actuellement, je travaille sur Mycroft pour pallier le manque des services en ligne qui n'existent plus. Mon objectif principal est de permettre aux utilisateurs de Mycroft de continuer à l'utiliser, en particulier pour ceux qui préfèrent ne pas se tourner vers des alternatives. De plus, je vise à porter Mycroft sur Windows, sachant que la majorité des utilisateurs disposent d'un ordinateur sous ce système d'exploitation, et étant donné que Mycroft est principalement développé en Python, cela devrait être réalisable et étendre considérablement son accessibilité.Ensuite, je souhaite traduire les compétences de Mycroft dans un maximum de langues possible et idéalement créer de nouvelles compétences pour étendre ses fonctionnalités. Je crois fermement que rendre Mycroft disponible sur Windows augmentera significativement sa base d'utilisateurs. De même, la traduction des compétences dans différentes langues est cruciale, car bien que l'anglais soit largement parlé, certains utilisateurs préfèrent interagir avec des logiciels dans leur langue maternelle pour une expérience plus naturelle et immersive.Je pense également qu'il est important de développer une interface graphique conviviale pour l'installation de compétences et la configuration générale du système. Tout le monde n'est pas à l'aise avec les lignes de commande ou la modification de fichiers de configuration, et une interface web serait un ajout parfait pour rendre Mycroft encore plus accessible.Bien que je n'aie aucune formation en programmation, je m'appuie sur des outils comme Cody de Sourcegraph et ChatGPT pour générer du code et m'aider à comprendre son fonctionnement. Si quelqu'un est intéressé par ce projet, qu'il soit programmeur ou non, toute contribution est la bienvenue. Mycroft étant un projet open source et communautaire, je suis convaincu que nous pouvons créer quelque chose d'utile, performant et vraiment génial grâce aux connaissances et talents de chacun.


## Getting Started

First, get the code on your system!  The simplest method is via git ([git installation instructions](https://gist.github.com/derhuerst/1b15ff4652a867391f03)):
- `cd ~/`
- `git clone
 this repo
https://github.com/stevechretien111/mycroft-core.git
  or the original Mycroft repos
- https://github.com/MycroftAI/mycroft-core.git`
- `cd mycroft-core`
- `bash dev_setup.sh`


This script sets up dependencies and a [virtualenv][about-virtualenv].  If running in an environment besides Ubuntu/Debian, Arch or Fedora you may need to manually install packages as instructed by dev_setup.sh.

[about-virtualenv]:https://virtualenv.pypa.io/en/stable/

NOTE: The default branch for this repository is 'dev', which should be considered a work-in-progress. If you want to clone a more stable version, switch over to the 'master' branch.

## Running Mycroft

Mycroft provides `start-mycroft.sh` to perform common tasks. This script uses a virtualenv created by `dev_setup.sh`.  Assuming you installed mycroft-core in your home directory run:
- `cd ~/mycroft-core`
- `./start-mycroft.sh debug`

The "debug" command will start the background services (microphone listener, skill, messagebus, and audio subsystems) as well as bringing up a text-based Command Line Interface (CLI) you can use to interact with Mycroft and see the contents of the various logs. Alternatively you can run `./start-mycroft.sh all` to begin the services without the command line interface.  Later you can bring up the CLI using `./start-mycroft.sh cli`.

The background services can be stopped as a group with:
- `./stop-mycroft.sh`

## Using Mycroft, note that Mycroft.ai is no more.

### *Home* Device and Account Manager
Mycroft AI, Inc. maintains a device and account management system known as Mycroft Home. Developers may sign up at: https://home.mycroft.ai

By default, mycroft-core  is configured to use Home. By saying "Hey Mycroft, pair my device" (or any other request verbal request) you will be informed that your device needs to be paired. Mycroft will speak a 6-digit code which you can enter into the pairing page within the [Mycroft Home site](https://home.mycroft.ai).

Once paired, your unit will use Mycroft API keys for services such as Speech-to-Text (STT), weather and various other skills.

### Skills

Mycroft is nothing without skills.  There are a handful of default skills that are downloaded automatically to your `/opt/mycroft/skills` directory, but most need to be installed explicitly.  See the [Skill Repo](https://github.com/MycroftAI/mycroft-skills#welcome) to discover skills made by others.  Please share your own interesting work!

## Behind the scenes

### Pairing Information
Pairing information generated by registering with Home is stored in:
`~/.config/mycroft/identity/identity2.json` <b><-- DO NOT SHARE THIS WITH OTHERS!</b>

### Configuration
Mycroft's configuration consists of 4 possible locations:
- `mycroft-core/mycroft/configuration/mycroft.conf`(Defaults)
- [Mycroft Home](https://home.mycroft.ai) (Remote)
- `/etc/mycroft/mycroft.conf` (Machine)
- `$XDG_CONFIG_DIR/mycroft/mycroft.conf` (which is by default `$HOME/.config/mycroft/mycroft.conf`) (USER)

When the configuration loader starts, it looks in these locations in this order, and loads ALL configurations. Keys that exist in multiple configuration files will be overridden by the last file to contain the value. This process results in a minimal amount being written for a specific device and user, without modifying default distribution files.

### Using Mycroft Without Home

If you do not wish to use the Mycroft Home service, before starting Mycroft for the first time, create `$HOME/.config/mycroft/mycroft.conf` with the following contents:

```
{
  "skills": {
    "blacklisted_skills": [
      "mycroft-configuration.mycroftai",
      "mycroft-pairing.mycroftai"
    ]
  }
}
```

### API Key Services

The Mycroft backend provides access to a range of API keys for specific services. Without pairing with the Mycroft backend, you will need to add your own API keys, install a different Skill or Plugin to perform that function, or not have access to that functionality.

These are the keys currently used in Mycroft Core through the Mycroft backend:

- [STT API, Google STT, Google Cloud Speech](http://www.chromium.org/developers/how-tos/api-keys)
  - [A range of STT services](https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/customizations/stt-engine) are available for use with Mycroft.
- [Weather Skill API, OpenWeatherMap](http://openweathermap.org/api)
- [Wolfram-Alpha Skill](http://products.wolframalpha.com/api/)


### Using Mycroft behind a proxy

Many schools, universities and workplaces run a `proxy` on their network. If you need to type in a username and password to access the external internet, then you are likely behind a `proxy`.

If you plan to use Mycroft behind a proxy, then you will need to do an additional configuration step.

_NOTE: In order to complete this step, you will need to know the `hostname` and `port` for the proxy server. Your network administrator will be able to provide these details. Your network administrator may want information on what type of traffic Mycroft will be using. We use `https` traffic on port `443`, primarily for accessing ReST-based APIs._

#### Using Mycroft behind a proxy without authentication

If you are using Mycroft behind a proxy without authentication, add the following environment variables, changing the `proxy_hostname.com` and `proxy_port` for the values for your network. These commands are executed from the Linux command line interface (CLI).

```bash
$ export http_proxy=http://proxy_hostname.com:proxy_port
$ export https_port=http://proxy_hostname.com:proxy_port
$ export no_proxy="localhost,127.0.0.1,localaddress,.localdomain.com,0.0.0.0,::1"
```

#### Using Mycroft behind an authenticated proxy

If  you are behind a proxy which requires authentication, add the following environment variables, changing the `proxy_hostname.com` and `proxy_port` for the values for your network. These commands are executed from the Linux command line interface (CLI).

```bash
$ export http_proxy=http://user:password@proxy_hostname.com:proxy_port
$ export https_port=http://user:password@proxy_hostname.com:proxy_port
$ export no_proxy="localhost,127.0.0.1,localaddress,.localdomain.com,0.0.0.0,::1"
```

## Getting Involved

This is an open source project. We would love your help. We have prepared a [contributing](.github/CONTRIBUTING.md) guide to help you get started.



## Links
* [Creating a Skill](https://mycroft-ai.gitbook.io/docs/skill-development/your-first-skill)
* [Documentation](https://docs.mycroft.ai)
* [Skill Writer API Docs](https://mycroft-core.readthedocs.io/en/master/)
* [Release Notes](https://github.com/MycroftAI/mycroft-core/releases)
* [Community open conversational ai](https://community.openconversational.ai/)
