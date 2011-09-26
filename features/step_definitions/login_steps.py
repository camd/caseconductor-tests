from lettuce import step, world

@step(u'Given user "([^"]*)" is not logged in')
def given_user_group1_is_not_logged_in(step, user_name):
    assert False, 'This step must be implemented'


@step(u'When user "([^"]*)" logs in')
def when_user_group1_logs_in(step, user_name):
    assert False, 'This step must be implemented'


@step(u'Then user "([^"]*)" is logged in')
def then_user_group1_is_logged_in(step, group1):
    assert False, 'This step must be implemented'