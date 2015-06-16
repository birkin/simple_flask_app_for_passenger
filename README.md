### Purpose

Demo flask app serving via passenger.

### Notes

- This app assumes a project structure like:

        some_enclosing_directory
            flask_test
                config  # directory
                the_app.py
            env_flasktest


- This app assumes an entry in our existing apache .conf file like:

        <Location /flasktest>
            PassengerBaseURI /flasktest
            PassengerAppType wsgi
            PassengerAppRoot /path/to/some_enclosing_directory/flask_test/config
            PassengerPython /path/to/some_enclosing_directory/env_flasktest/bin/python
        </Location>


---
