# Welcome to Phoenix Spark at Travis Air Force Base

 As the inaugural Phoenix Spark Cell, Travis AFB is the role model for future Spark programs. By continuously learning as an organization, inspiring a culture of innovation, and empowering Airmen to lead at every level, Phoenix Spark is delivering tomorrow’s innovative capabilities to the warfighter today. Learn more at [travisspark.org](https://travisspark.org)

## About Spark-Database

This database allows Phoenix Spark to consistently, reliably, and easily document and manage the contact information of personnel who are interested in collaborating with the organization. It captures each person's contact information, skills, interests, contributions, and training. It also allows administrators to limit the access that personnel have to Phoenix Spark assets.

## Using Spark-Database

1. Follow the instructions in [Contributing.md](https://github.com/TravisSpark/spark-database/blob/master/.github/contributing.md) to setup the program
2. Run main.py from the Command Line:
   * ```(sudo) python3 spark_database/main.py```
3. The program will prompt the user with three options.
   * '''<function add_user at 0x7f6f41928c80>'''
   * '''<function show_all_users at 0x7f6f41928d08>'''
   * '''<function search_for_user at 0x7f6f41928d90>'''
4. *add_user* will lead to a prompts to input user information. There is an opportunity to change incorrect information.
   * **BUG ALERT** [Issue #4 Unable to leave Email + RFID Null](https://github.com/TravisSpark/spark-database/issues/4)
5. *show_all_users* prints to the console the contact information for every user
6. *search_for_user* searches by first and last name. It supports entering only a portion of the first and last names. It is case-sensitive.
7. After executing the selected function, users can choose whether to select another function or exit the program.

## Contributing to Phoenix Spark

There are several opportunitities to contribute to projects at Phoenix Spark:

1. Contribute to Spark-Database by reviewing its [Contributing.md](https://github.com/TravisSpark/spark-database/blob/master/.github/contributing.md) file.
2. Explore the [TravisSpark](https://github.com/TravisSpark) GitHub Organization to collaborate on an existing project or create a new project
3. Contact us at [travisspark.org](https://travisspark.org/contact/) to find interesting projects in topics that include, [3-D Printing](https://3dprint.com/218699/air-force-3d-printing-cups/), Drones, Additive Manufacturing, Virtual Reality, Machine Learning, and Operational Management Theory

## Open Sourcing in the DoD

On June 2, 2016, the U.S Chief Information and Acquisition Officers released Memorandum [M-16-21](https://code.gov/#/policy-guide/policy/introduction), creating a Federal Source Code Policy. The goal is to improve the the cost efficiency, mission effectiveness, and consumer experience of government programs by maximizing the amount of federal software that is reused by other agencies or made available to the general public to improve. To help implement this policy, the websites [code.gov](https://code.gov) and [code.mil](https://www.code.mil/#/) were created to address the needs of general federal agencies and the DoD, respectively. These websites provide great resources on navigating the complexities of sharing code developed by and for federal agencies. 