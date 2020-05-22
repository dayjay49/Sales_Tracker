# Code Review

Dear candidate, thank you very much for you submission to the 
Backend Developer Co-op Position.

As a sign of respect and appreciation for the time you spent on this task,
I decided to give you a feedback about your code and I hope that this 
experience will be educational for you.

My feedback does should not imply your acceptance or rejection to the internship 
program. All candidates got a feedback like this.


## My comments

- bin and include directories should be excluded from git 

- I expected you to create initial data for the project,
  using Django's [data migration] scripts or [fixtures]. 

- app names should be in lowercase

- You have lots of empty files in your code and too many unjustified apps.
  The rule of thumb is to create a new app only if the can live by itself,
  (e.g. ported to another project etc.) or if the app encapsulates a large
  portion of the functionality that you do not want to include in the other apps.     
  For example: salesEntry, salesComReport and drinkOrder should have been a single app...


Additional comments can be found in the code with a comment that starts with `CR:` (i.e. CodeReview)


[data migration]: https://docs.djangoproject.com/en/3.0/topics/migrations/#data-migrations
[fixtures]: https://docs.djangoproject.com/en/3.0/howto/initial-data/
