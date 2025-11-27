# Vacances Scolaires FR

## Installation

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=lalexdotcom&repository=ha-vacances-fr&category=integration)

<details>
    <summary>Cliquez ici pour afficher les instructions détaillées</summary>
    <ol>
        <li>Installation</li>
        <ul>
            <li>
                <u>Avec HACS</u><br />
                Dans le panel HACS, aller sur les intégrations et cliquer sur le gros bouton '+' orange.
                Chercher 'Vacances Scolaires FR' and cliquer sur 'Install this repository in HACS'.
            </li>
            <li>
                <u>Manuellement</u><br />
                Télécharger la <a href="https://github.com/lalexdotcom/ha-vacances-fr/releases">dernière release</a> au format ZIP l'extraire dans le répertoire <code>custom_components</code> de votre installation HA.
            </li>
        </ul>
        <li>Redémarrer HA pour qu'il charge l'intégration.</li>
        <li>Aller dans 'Paramètres > Appareils et services' and cliquer sur le bouton bleu '+ Ajouter une intégration'. Chercher 'Vacances Scolaires FR' et le sélectionner pour ajouter une zone.</li>
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

L'intégration se met à jour tous les 120 jours: vu que l'éducation nationale fournit les plannings jusqu'à 2027, ca devrait pas évoluer trop souvent 😇

## Mise à jour

<details>
    <summary>Cliquez pour afficher les instructions de mise à jour</summary>
    <ol>
        <li>Mettre à jour les fichiers</li>
        <ul>
            <li>
                <u>Avec HACS</u><br>
                Dans le panneau HACS, une noitification devrait apparaître quand une nouvelle version est disponible. Suivre les instruction de HACS pour mettre à jour.
            </li>
            <li>
                <u>Manuellement</u><br>
                Télécharger la <a href="https://github.com/lalexdotcom/ha-vacances-fr/releases">dernière release</a> au format ZIP l'extraire dans le répertoire <code>custom_components</code> de votre installation HA pour écraser l'ancienne version.
            </li>
        </ul>
        <li>Redémarrer HA pour charger les modifications</li>
    </ol>
</details>

## Désinstaller

<details>
    <summary>Cliquez pour afficher les instruction de désinstallation</summary>
    <ol>
        <li>
            <u>Supprimer Vacances Scolaires FR de HA:</u><br>
            Aller dans 'Paramètres > Appareils et services'. Dans la section Vacances Scolaires FR, cliquer sur le bouton '...', et selectionner 'Supprimer'.
        </li>
        <li>Supprimer les fichiers</li>
        <ul>
            <li>
                <u>Avec HACS</u><br />
                Dans le panneau HACS panel aller sur les intégrations et chercher 'Vacances Scolaires FR'.
                Cliquer sur le bouton '...' et sélectionner 'Uninstall'.
            </li>
            <li>
                <u>Manuellement</u><br />
                Dans le répertoire <code>custom_components</code>, supprimer le répertoire <code>vacances_fr</code>.
            </li>
        </ul>
        <li>Redémarrer HA pour supprimer toutes les traces de l'intégration.</li>
    </ol>
</details>

## Bugs

Avant de créer un nouveau ticket de bug:

1. Verifiez le nombre de devices sur la page [System Health page](https://my.home-assistant.io/redirect/system_health)
2. Vérifiez les warning et errors sur la page [Logs page](https://my.home-assistant.io/redirect/logs/)
3. Vérifier les **debug logs** sur la page [Debug page](#debug-page) (doit être activé dans les réglages de l'intégration)
4. Vérifier les [tickets **ouverts et fermés**](https://github.com/lalexdotcom/ha-vacances-fr/issues?q=is%3Aissue)
5. Partager les [diagnostics de l'integration](https://www.home-assistant.io/integrations/diagnostics/) (à partir de la v2022.2):

- Tous les appareils: Paramètres > Appareils et services > [Intégrations](https://my.home-assistant.io/redirect/integrations/) > **Vacances Scolaires FR** > [[...]] > Télécharger les diagnostics
- Un appareil: Paramètres > Appareils et services > [Appareils](https://my.home-assistant.io/redirect/devices/) > (votre appareil) > Télécharger les diagnostics

*Aucune donnée privée n'est transmise, mais vous pouvez supprimer tout ce que vous considererez comme sensible.*