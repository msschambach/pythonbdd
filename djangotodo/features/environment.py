import os
import django
from django.test import runner
# This is necessary for all installed apps to be recognized, for some reason.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configuration.settings.test')


def before_all(context):
    # Even though DJANGO_SETTINGS_MODULE is set, this may still be
    # necessary. Or it may be simple CYA insurance.
    django.setup()

    # Take a TestRunner hostage.
    # We'll use thise later to frog-march Django through the motions
    # of setting up and tearing down the test environment, including
    # test databases.
    context.runner = runner.DiscoverRunner()


def before_scenario(context, scenario):
    pass
    # Set up the scenario test environment
    # context.runner.setup_test_environment()
    # We must set up and tear down the entire database between
    # scenarios. We can't just use db transactions, as Django's
    # TestClient does, if we're doing full-stack tests with Mechanize,
    # because Django closes the db connection after finishing the HTTP
    # response.
    # context.old_db_config = context.runner.setup_databases()


def after_scenario(context, scenario):
    pass
    # Tear down the scenario test environment.
    # context.runner.teardown_databases(context.old_db_config)
    # context.runner.teardown_test_environment()
