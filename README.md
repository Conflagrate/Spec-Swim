# Spec Swim
A "Fantasy Football" interpretation of swimming written entirely by John Limberis under the alias "Conflagrate". This project was first started on March 28th, 2020 and doubles as the official submission for the 2020 AP Computer Science Principles Create Task as well as a local mobile/web game for the Lakeland Hills YMCA 2019-2020 Senior 4 and Senior 3 groups.

## Licensing
This repository and the included files are currently licensed under the MIT License. As a permissive license, it puts very limited restrictions on reuse and has, therefore, high license compatibility. For further information, please refer to LICENSE.md included in this repository.

## Usage and Permissions
The `main.py` file and its contents are used by an automated program and sources its input from Meet Mobile's API. Personal usage is considered unofficial and therefore not recorded in the live app. Only automated usage and identified contributors have access to the official output. For more information about being an input contributor, please contact us at our [official email](https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=GTvVlcRzCMpvXBQzsZpHdzVPQtcpvKLsWzcXQXmBwPkQPBJqJSmNCNPpMmcZPrKczZVMnjmzphTMP).

Besides input contributors, we would also love some coding contributions! If you see an opportunity to refactor the code to make it more efficient, you should [create a pull request](https://github.com/Conflagrate/Spec-Swim/pulls). To merge your branch into the master, shoot us an email and we'll check out your new code.

## Rules and Regulations
The official rule book has not yet been published, but here is a simple breakdown of the point structure:

### Individual Events
| Placement     | Points        |
| :------------:|:-------------:|
| 1st Place Overall      | 12 |
| Top 3 *(excluding 1st)*      | 8      |
| Top 5 *(excluding Top 3)* | 6      |
| Outside Top 5      | 0 |

| Placement     | Points        |
| :------------:|:-------------:|
| Top 10% *(including Top 75%, Top 50%, and Top 25%)*                | 3               |
| Top 25% *(including Top 75% and Top 50%)*          | 1.75      |
| Top 50% *(including Top 75%)*           | 1                    |
| Top 75%             | 0.5      |
| Last Place             | -5      |

| Net Time Differential | Points |
|:---------:|:---------:|
| -0.5 second(s) | 1 |
| +0.5 second(s) | -1 |

### Relay Events
| Placement     | Points        |
| :------------:|:-------------:|
| 1st Place Overall      | 6 |
| Top 3 *(excluding 1st)*      | 4      |
| Top 5 *(excluding Top 3)* | 3      |
| Outside Top 5      | 0 |

| Placement     | Points        |
| :------------:|:-------------:|
| Top 10% *(including Top 75%, Top 50%, and Top 25%)*                | 1.5               |
| Top 25% *(including Top 75% and Top 50%)*          | 0.875      |
| Top 50% *(including Top 75%)*           | 0.5                    |
| Top 75%             | 0.25      |
| Last Place             | -5      |

| Net Time Differential | Points |
|:---------:|:---------:|
| -0.5 second(s) | 1 |
| +0.5 second(s) | -1 |

**Some important things you should have noticed:**

Your placement percentage (calculated by your placement divided by the total, then multiplied by 100) compoundly increases whereas your overall placement does not.

The positive increment from relays are worth half of an individual event, or conversely, individual events give twice as many points as relays. However, getting last in an individual event or a relay with always net you **-5 points**.

For each half a second dropped, you will tally **1 point**.

For each half a second added, you will tally **-1 point**.

The maximum amount of points that can be achieved for an individual event (without factoring in time improvement, or the lack thereof) is **36.5 points**. 

The maximum amount of points that can be achieved for a relay event is (without factoring in time improvement, or the lack thereof) **18.25 points**.

*These rules are subject to change, but an official notice will be released to all users several days prior to any changes.*

**For each meet day, the participant may submit exactly one (1) event to have scored. This is to prevent swimmers who are competing in more events to have an unfair advantage. Swimmers who compete in relays will be scored against each other whereas strictly individual performers will be scored in a separate bracket. This is also meant to prevent unfair point inflation.**