# Vacances Scolaires FR

## Installation

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=lalexdotcom&repository=ha-vacances-fr&category=integration)

<details>
    <summary>Click to show installation instructions</summary>
    <ol>
        <li>Install files:</li>
        <ul>
            <li>
                <u>Using HACS:</u><br />
                In the HACS panel, go to integrations and click the big orange '+' button.
                Search for 'Vacances Scolaires FR' and click 'Install this repository in HACS'.
            </li>
            <li>
                <u>Manually:</u><br />
                Download the <a href="https://github.com/lalexdotcom/ha-vacances-fr/releases">latest release</a> as a zip file and extract it into the `custom_components` folder in your HA installation.
            </li>
        </ul>
        <li>Restart HA to load the integration into HA.</li>
        <li>Go to Configuration -> Integrations and click the big orange '+' button. Look for Vacances Scolaires FR and click to add it.</li>
    </ol>
</details>

## Configuration
- on choisit une zone dans la liste déroulante
- ... et c'est tout! 😋

## Fonctionnalités
- un `calendar` avec toutes les vacances à venir pour la zone. Il sert aussi pour vérifier si on est en vacances, parce que le calendrier a un state `ON` si un évènement est en cours et un state `OFF` sinon.
- un `binary_sensor` qui dit si la zone sera en vacances demain
- un `sensor` "Vacances en cours" avec le nom de la période de vacances, et des attributs supplémentaire. Sa valeur est "Unknown" si pas de vacances en cours
- un `sensor` "Vacances à venir" comme le précédent mais pour les prochaines vacances, n'incluant pas les vacances en cours si c'est le cas (en gros, si vous êtes en pleines vacances de Noel, ca indiquera Vacances d'hiver)

L'intégration se met à jour tous les 120 jours: vu que l'éducation nationale fournit les plannings jusqu'à 2027, ca devrait pas évoluer trop souvent 😇## Updating

## Mise à jour

<details>
    <summary>Click to show updating instructions</summary>
    <ol>
        <li>Update the files:
            <ul>
                <li>
                    <u>Using HACS:</u><br>
                    In the HACS panel, there should be an notification when a new version is available. Follow the instructions within HACS to update the installation files.
                </li>
                <li>
                    <u>Manually:</u><br>
                    Download the <a href="https://github.com/lalexdotcom/ha-vacances-fr/releases">latest release</a> as a zip file and extract it into the <code>custom_components</code> folder in your HA installation, overwriting the previous installation.
                </li>
            </ul>
        </li>
        <li>Restart HA to load the changes.</li>
    </ol>
</details>

## Uninstalling

<details>
    <summary>Click to show uninstall instructions</summary>
    <ol>
        <li>
            <u>Remove Vacances Scolaires FR from HA:</u><br>
            In HA go to Configuration -> Integrations. In the Vacances Scolaires FR card, click the button with the 3 dots, and click 'Delete'.
        </li>
        <li>Remove the files:
            <ul>
                <li>
                    <u>When installed with HACS:</u><br />
                    In the HACS panel go to integrations and look for Vacances Scolaires FR.
                    Click the button with the 3 dots and click 'Uninstall'.
                </li>
                <li>
                    <u>When installed manually:</u><br />
                    In the <code>custom_components</code> directory, remove the 'vacances_fr' folder.
                </li>
            </ul>
        </li>
        <li>Restart HA to make all traces of the component dissapear.</li>
    </ol>
</details>

## Issues

Before posting new issue:

1. Check the number of online devices on the [System Health page](https://my.home-assistant.io/redirect/system_health)
2. Check warning and errors on the [Logs page](https://my.home-assistant.io/redirect/logs/)
3. Check **debug logs** on the [Debug page](#debug-page) (must be enabled in integration options)
4. Check **open and closed** [issues](https://github.com/lalexdotcom/ha-vacances-fr/issues?q=is%3Aissue)
5. Share integration [diagnostics](https://www.home-assistant.io/integrations/diagnostics/) (supported from Hass v2022.2):

- All devices: Configuration > [Integrations](https://my.home-assistant.io/redirect/integrations/) > **Vacances Scolaires FR** > 3 dots > Download diagnostics
- One device: Configuration > [Devices](https://my.home-assistant.io/redirect/devices/) > Device > Download diagnostics

*There is no private data, but you can delete anything you think is private.*