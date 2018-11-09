# Voiceminder Server
Repository the Voiceminder database and REST API

### Environment Setup
Install python3:
```
> brew upgrade python3
```

Install and configure virtualenv:
```
> pip install virtualenv
> mkdir ~/Python_envs
> cd ~/Python_envs
> virtualenv -p /usr/local/Cellar/python3/3.6.2/bin/python3 voicenotes
```

# Using and Updating the Environment:
To activate this environment, run the following command in the command line:
```
> source ~/Python_envs/voicenotes/bin/activate
```

If the environment is activated, your command line prompt will show the following:
```
(voicenotes) >
```

The required python packages are defined in the
requirements.txt file. Use the `pip` command to install or
upgrade. REMEMBER: you need to do this every time someone adds a required
package to the project.
```
(voicenotes) > pip3 install -r requirements.txt
```

To add a required package to the project, use the `pip freeze` command:
```
(voicenotes) > pip3 freeze > requirements.txt
```

##### Run instructions:
Install mysql

Make database named voicenotes

To export env variables, copy and paste voicenotes.env from wiki into repo and change python path export environment variables:
```
(voicenotes) > source voicenotes.env

```
Then, install mysql and create a database called voicenotes

```
brew install mysql
mysql -u root -p
mysql -u username -p
CREATE DATABASE voicenotes;
```
Once the voicenotes database has been created, you can now go to the your virtual environment
Navigate to src/ folder
Apply current migrations

```
(voicenotes) > alembic upgrade head
```

Create new migrations:
```
(voicenotes) > alembic revision -m "add comment here"
```
This creates a blank migration file under src/alembic/versions
Fill out the migration
Apply migration
```
(voicenotes) > alembic upgrade head

```

Run message seeding:
```
(voicenotes) > python3 src/seeds/seed.py

```

Execute voicenotes
```
(voicenotes) > python3 src/run.py
```

install localtunnel via localtunnel.me
launch in terminal
> lt -s voicenote -p 5000

This launches api as https://voicenote.localtunnel.me

### Usage

payload: String

{
  "sender": "df459b18-9563-836d-f343-75de6b8055de",
  "payload": {
    "speech": "Can you show me some cats",
    "endpoint": "https://zydkkkbc6k.execute-api.us-east-1.amazonaws.com/dev/ping",
    "state": {
      "directory":"home/catApp",
      "appState": {
        "status": "OK",
        "banned": false
      }
    }
  }
}
