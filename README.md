
# hska-mail-forward

Simple Python script to forward your HsKA mails to any e-mail account.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine or any server, where it could run automatically.

### Prerequisites
You need to have a working Python 3 environment. If you haven't take a look at the [Python Website](https://www.python.org/).

### Installing
There will be two methods to get hska-mail-forward to run on your machine, which will be referred as Method #1 and Method #2 in the following instructions.

#### Method #1
For Linux (64bit) there is a single script release, built with [pyinstaller](https://www.pyinstaller.org/). You can find the download in the [releases](releases) tab.
Download the script and place it anywhere. The directory should be in your path variable.

#### Method #2
Get the sources from github by downloading the source code archive from [releases](releases) or cloning this repo with git.

First open a teminal in the unpacked or cloned source directory. In the following I assume you using linux. Otherwise the syntax, file extensions, directories … may differ, but that should not be to complicated to find out.
 
After that we create a [venvl](https://docs.python.org/3/library/venv.html) there.
```console
foo@bar:~/hska-mail-forward$ python3 -m venv ./venv
```
Now we are going to install the requirements.
```console
foo@bar:~/hska-mail-forward$ ./venv/bin/pip install -r requirements.txt
```
## First run
To run the program you have just execute the script for Method #1 or for Method #2:
```console
foo@bar:~/hska-mail-forward$ ./venv/bin/python hska-mail-forward.py
```
The first run will create the config file config.yaml in the systems config directory and will print out the path to this file (that's why you at least firstly run it from terminal).
Your default text editor should pop up to edit this empty file. Maybe you have to choose which program you like to use to open yaml files. Use any text editor here.

Paste the following config there. Don't forget to replace the variables.
```yaml
iz:
  username: muma1011 # your iz username
  password: myizpassword # your iz password
fwd:
  body: HsKA FWD # not necessary, body of all forwarded mails
  to: # at least one email adress to send the mails to
  - foo.bar@maildomain.test
skip: # you can skip folders and messages
  folder: # you should skip the Sent folder
  - VERYVERYLONGIDOFYOURFOLDER
#  message: # you could also skip specific mails, also all fwd mail ids go here to not send them again
#  - VERYVERYLONGIDOFYOURMESSAGE
```
**Important:** Because all forwarded messages will be saved also in the Sent folder, you should exclude it in general. Otherwise all fwd messages will be send every time you run it again which results in a full message box really quick. You can find your id to the Sent folder by going to [https://www.iwi.hs-karlsruhe.de/iwii/REST/exchange/mailfolders](https://www.iwi.hs-karlsruhe.de/iwii/REST/exchange/mailfolders). Sign in there with your iz credentials.

## Contributing
This project is just a quick helper for the unpleasant mailing situation in the HsKA.
There are some points that really could be improved. So if you willing to help to get this better, feel free to improve it.
### List of improvements
This is my list of improvements. If you want to contribute you could start here.
 - shell script options in general (also a help)
 - option to exclude Sent folder
 - option to delete the forwarded message
 - option to delete the saved FWD message
 - don't open the config file, rather ask for the config options in the script and save them after that
 - pyinstaller releases for other OSs and platforms (ios, windows, maybe also 32bit?)

## Authors

* **Jan Otto** - *Initial work* - [derOtto](https://github.com/derOtto/)

See also the list of [contributors](contributors) who participated in this project.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.