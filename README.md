# Test task


How to launch

1. Migrations

   ```bash
    $ python manage.py makemigrations && python manage.py migrate
    ```

2. Get correct data from files .csv and .xml 

   ```bash
    $ python correct_data.py
    ```

3. Load fixtures

   ```bash
    $ python manage.py loaddata db_data.json
    ```

4. Unit tests

   ```bash
    $ python manage.py test
    ```

5. Run server

   ```bash
    $ python manage.py runserver
    ```
