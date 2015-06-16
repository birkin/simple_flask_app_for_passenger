### Purpose

Demo flask app serving via [passenger](https://www.phusionpassenger.com).

### Notes

- This app assumes a project structure like:

        some_enclosing_directory
            flask_test
                config  # directory
                the_app.py
            env_flasktest


- This app assumes an entry in our existing apache passenger.conf file like:

        <Location /flasktest>
            PassengerBaseURI /flasktest
            PassengerAppType wsgi
            PassengerAppRoot /path/to/some_enclosing_directory/flask_test/config
            PassengerPython /path/to/some_enclosing_directory/env_flasktest/bin/python
        </Location>

    Note the use of the env's python -- that's what's cool about passenger: different projects can use different versions of python.

- Hit with url `http://127.0.0.1/flasktest/hello`

---
