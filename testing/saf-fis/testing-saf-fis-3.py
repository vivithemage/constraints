#!/usr/bin/env python
# testing.py
#
# TODO
# have buttons for cvc selection rather than the scale.
#   Will do when rest is OK.

# Libraries needed.
from psychopy import visual, event, core, misc, data, gui, sound, log
import datetime, string, sys, os, time

# Participant needs to press y to continue or q to go. Can easily add other letters this
# way for other things.
def ready_cont():
  stim_win.flip()
  user_response=None
  while user_response==None:
    allKeys=event.waitKeys()
    for thisKey in allKeys:
      if thisKey=='y':
        user_response=1
      if thisKey=='q':
        core.quit()

# cvc rates
cvc_slow_rate = 1.0
# A cvc every 395ms with Warker and others (2008)
cvc_faster_rate = 0.395
# interval between each sequence
stim_interval = 1.0
between_tests_interval = 2.0

# Metronome function - This plays the metronome; the timing can also be altered here.
# The timing required needs to be passed to metronome function.
#  music.play()
music = sound.Sound(900,secs=0.01)
def metronome(met_time):
  music.play()
  core.wait(met_time)
  music.play()
  core.wait(met_time)
  music.play()
  core.wait(met_time)
  music.play()
  core.wait(met_time)

# The metronome alone so the participant can become familiar with
# the speed (no stimuli).
def metronome_alone():
  stim_win.flip()
  core.wait(stim_interval)
  metronome(cvc_slow_rate)
  metronome(cvc_faster_rate)
  metronome(cvc_faster_rate)
  metronome(cvc_faster_rate)

# Instruction variables
welcome_message = """Welcome to the testing session.This will be the same as before, but this time there will be twice as many trials.

Please read the entire row four times out loud in time to the metronome, and try to say one syllable per beat. Try and read the items as fluently as possible.  Do not worry if you make mistakes, just keep in time with the beat.

Press y now to hear the speed of the metronome."""
metronome_alone_message = """Playing the metronome..."""
sample_welcome = """The following will be a practice session to familiarize you with the sequences (press y to continue)"""
sample_goodbye = """The practice has ended, please press y when you are ready for the main session """
firstHalf_message = """You are half way through, please say "Half way" and press y when you are ready to continue."""
choose_and_rate = """You will now be presented with some pairs of items. You will have already seen one of these items before, and the other one will be new. From each pair please choose which one you think you have seen before.
 Then use the mouse to indicate how confident you are you have seen the item before, using a scale of 1 to 5, with one being not at all confident (guess) and 5 being certain.  Click on the item to select your answer, then click accept
Press y key to start."""

generalization_message = """You will now be presented with pairs of items, neither of which you have seen before. Please choose which one out of the pair you find most similar to items from the sequences you have seen before.

Press y key to start."""
welcome_recog = """Please indicate how confident you are that you have seen the item before using a scale of 1 to 5, 1 meaning not at all  (just a guess) and 5 meaning certain"""

thank_you = """The testing session is complete.

Please inform a researcher you have finished.

Thank you."""


# Stimuli variables
sample_stim = ['gin fim hing kis',
'kis hing mig fin',
'hang san maf kag']

# First set of 48
real_stim_1 =['kan hang mag saf',
'fim ning his kig',
'hang nag kaf sam',
'fig hing kis min',
'kang hag man saf',
'him fin king gis',
'saf han gam kang',
'kim nis fing hig',
'mang san haf kag',
'gin fis mik hing',
'kag hang san maf',
'fim king nis hig',
'haf nam kag sang',
'king gin him fis',
'hang san kaf mag',
'mik his ning fig',
'gang sak nam haf',
'fin him gis king',
'haf gam kang san',
'kim hin fing gis',
'nang sak ham gaf',
'mig his king fin',
'gang haf mak san',
'his gim fing kin',
'kam naf hag sang',
'his fing gik nim',
'san haf kang gam',
'nik hing gim fis',
'saf hang gan mak',
'ning hik fim gis',
'naf sak gang ham',
'fing his gin kim',
'hang gan saf mak',
'nis fim gik hing',
'hang mag nak saf',
'ging him nis fik',
'kang hag man saf',
'nis fing gik him',
'nag sam kang haf',
'ming fik nis hig',
'nag mang saf hak',
'him kis fin ging',
'sag nang kam haf',
'mis king hin fig',
'gang man sak haf',
'him king gis fin',
'hang sak naf gam',
'fis gim hing kin']

# For the second set of 48
real_stim_2 = ['naf kag ham sang',
'fis hig kim ning',
'nak gang haf sam',
'nis hing kig fim',
'kan haf sang mag',
'hik nim fing gis',
'gak sang naf ham',
'ning mig hik fis',
'haf kag mang san',
'ming fik gin his',
'saf nag ham kang',
'mig nis fik hing',
'hang sam kag naf',
'hin ming fis gik',
'sang kan haf mag',
'mig kin fis hing',
'hang kam san gaf',
'him kig fing nis',
'saf kang hag nam',
'fim hik nis ging',
'han saf mag kang',
'min hing kis fig',
'hag sak mang naf',
'min hik fis ging',
'san gang haf kam',
'his fing nim kig',
'kang naf sam hag',
'nik ming fis hig',
'sang gam haf kan',
'hing nis mik fig',
'naf sam hang kag',
'hig kim fis ning',
'hang kag sam naf',
'fing gik him nis',
'kaf mang sag han',
'nis ming fik hig',
'mag nang sak haf',
'fim hing gin kis',
'kang ham san gaf',
'hig fis kin ming',
'man haf kang sag',
'gin his ming fik',
'gaf han sang kam',
'kig fing mis hin',
'haf gang mak san',
'fik gim his ning',
'saf kang nag ham',
'fing gis hik min']

# recognition variables.
# These are two arrays with both foils and legal cvc's. So recog_mix_left will appear on the left
# and recog_mix_right will appear on the right.
recog_mix_left = ['naf',
'kif',
'kaf',
'fik',
'fang',
'fam',
'sang',
'hif',
'sak',
'sig',
'maf',
'mis',
'san',
'sing',
'nif',
'sam',
'fin',
'nas',
'nis',
'fim']

recog_mix_right = ['sik',
'fig',
'gas',
'fan',
'gis',
'gaf',
'has',
'haf',
'mas',
'fing',
'mif',
'fas',
'fak',
'kis',
'saf',
'sim',
'kas',
'his',
'gif',
'sin']

recog_correct = ['haf',
'gis',
'fik',
'his',
'sak',
'sam',
'sang',
'gaf',
'kis',
'maf',
'san',
'saf',
'mis',
'fing',
'fig',
'fim',
'fin',
'nis',
'naf',
'kaf']

# Generalization variables
gen_left = ['sil',
'fiz',
'sit',
'fit',
'fid',
'tif',
'zif',
'mis',
'sat',
'fam',
'maf',
'das',
'sam',
'dis',
'zas',
'dif',
'lif',
'laf',
'faz',
'lis']

gen_right = ['sad',
'fad',
'daf',
'sim',
'mif',
'tis',
'fim',
'fal',
'sid',
'zis',
'fat',
'fil',
'siz',
'tas',
'saz',
'zaf',
'sal',
'las',
'taf',
'mas']

gen_correct = ['tis',
'fit',
'fim',
'sad',
'fil',
'mis',
'daf',
'sat',
'fid',
'sam',
'zaf',
'maf',
'zis',
'fiz',
'taf',
'saz',
'sal',
'lis',
'laf',
'dis']

# Compare answer to correct (legal) cvc's and report whether the cvc they
# chose was legal.
def check_answer(cvc_response, correct_array):
  if cvc_response in correct_array:
    return 'correct'
  else:
    return 'incorrect'

# User data - Experimenter should write in the participant's identification code so
# results can be distinguished.
myDlg = gui.Dlg(title="Participant details")
myDlg.addField('Numeric ID:')
myDlg.show() #you have to call show() for a Dlg (it gets done implicitly by a DlgFromDict)
if myDlg.OK:
  sub_id = myDlg.data #this will be a list of data returned from each field added in order
else:
  print 'user cancelled, exit.'
  core.quit()

# Create output file name. This also gets the response timings.
current_time = datetime.datetime.now() # Retrieve the current time
formatted_time = current_time.strftime("%d-%m-%y_%H-%M-%S") # Format it nicely
sub_id=''.join(sub_id) # converting list to string :/
output_filename = "%s_%s" % (sub_id, formatted_time) # Add participant name and datetime together

# Creating output file.
print "Creating output file"
textfile = open(output_filename +".csv", "w")

# Setting up the monitor and presenting the welcome message.
stim_win = visual.Window(monitor = "testMonitor", units ='norm', fullscr=True)
message = visual.TextStim(stim_win, text = welcome_message, font = "Arial")
message.setAutoDraw(True)
ready_cont()
stim_win.flip()
core.wait(stim_interval)

# The metronome so participant's know what it's like.
# Hmm allow participant to repeat? - Not really fair if
# some participants' run it more than others and pronounce
# cvc's better due to familiarity with the beat.
stim_win.flip()
message.setText(metronome_alone_message)
metronome_alone()
stim_win.flip()
core.wait(between_tests_interval)

# Welcome the participant.
message.setText(sample_welcome)
ready_cont()
stim_win.flip()
core.wait(between_tests_interval)

# The sample loop
for i in range(len(sample_stim)):
  message.setText(sample_stim[i])
  stim_win.flip()
  core.wait(stim_interval)
  metronome(cvc_slow_rate)
  metronome(cvc_faster_rate)
  metronome(cvc_faster_rate)
  metronome(cvc_faster_rate)
  core.wait(stim_interval)

# Ask participant if they are ready to continue
message.setText(sample_goodbye)
ready_cont()
stim_win.flip()
core.wait(stim_interval)

# The first (48) real stimuli loop
for i in range(len(real_stim_1)):
  message.setText(real_stim_1[i])
  stim_win.flip()
  core.wait(stim_interval)
  metronome(cvc_slow_rate)
  metronome(cvc_faster_rate)
  metronome(cvc_faster_rate)
  metronome(cvc_faster_rate)
  core.wait(stim_interval)

# Ask participant if they want a break at this point?
# Break needed to compare the two and so we can discern between the
# first 48 and last 48 easily.
message.setText(firstHalf_message)
ready_cont()
stim_win.flip()
core.wait(between_tests_interval)

# The second (48) real stimuli loop
for i in range(len(real_stim_2)):
  message.setText(real_stim_2[i])
  stim_win.flip()
  core.wait(stim_interval)
  metronome(cvc_slow_rate)
  metronome(cvc_faster_rate)
  metronome(cvc_faster_rate)
  metronome(cvc_faster_rate)
  core.wait(stim_interval)

# The generalisation function - Which have already been seen before TODO Pass the idtime variable here.
def recognition(cvc1, cvc2):
  stim_win.clearBuffer()
  stim_win.flip()
  # create a window before creating your rating scale.
  RatingScale = visual.RatingScale(stim_win, choices=[cvc1, cvc2], acceptText='accept?', markerStyle='circle', markerColor='DarkGreen')

  # cvc to be rated
  question = "Which item do you find most recognisable?"
  myItem = visual.TextStim(stim_win, text=question, units='norm')
  event.clearEvents()
  # Start participant response timing.
  start_cvc = time.time()
  while RatingScale.noResponse: # show & update until a response has been made
    myItem.draw()
    RatingScale.draw()
    stim_win.flip()

  # End response timing
  elapsed_cvc = (time.time() - start_cvc)
  rating = RatingScale.getRating() # get the value indicated
  chosen_cvc = rating

  # mark the response
  answer = check_answer(rating, recog_correct)

  ## Now the confidence
  RatingScale = visual.RatingScale(stim_win, choices=['1', '2', '3', '4', '5'], acceptText='accept?', markerStyle='circle', markerColor='DarkGreen')
  RatingScale.scaleDescription.setText("""1 = not at all (guess), 5 = Certain.""")
  question = """How confident are you that you have seen """ + rating + " before.\n"
  myItem = visual.TextStim(stim_win, text=question, units='norm')
  event.clearEvents()
  # Response timing for rating.
  start_rating = time.time()
  while RatingScale.noResponse: # show & update until a response has been made
    myItem.draw()
    RatingScale.draw()
    stim_win.flip()
  elapsed_rating = (time.time() - start_rating)
  rating = RatingScale.getRating() # get the value indicated by the subject, 'None' if skipped
  complete_answer = output_filename + " " + chosen_cvc + " " + rating + " " + answer + " " + str(elapsed_cvc) + " " + str(elapsed_rating) + "\n"
  print complete_answer
  textfile.write(complete_answer)

# Second generalization test - the sets with new consonants.
def generalize(cvc1, cvc2):
  stim_win.clearBuffer()
  stim_win.flip()
  # create a window before creating your rating scale.
  RatingScale = visual.RatingScale(stim_win, choices=[cvc1, cvc2], acceptText='accept?', markerStyle='circle', markerColor='DarkGreen')

  # cvc to be rated
  question = "Which one do you think is most similar to the items you have seen before?"
  myItem = visual.TextStim(stim_win, text=question, units='norm')
  event.clearEvents()
  start_cvc = time.time()
  while RatingScale.noResponse: # show & update until a response has been made
    myItem.draw()
    RatingScale.draw()
    stim_win.flip()
  # Getting response for cvc choice
  elapsed_cvc = (time.time() - start_cvc)
  rating = RatingScale.getRating() # get the value indicated
  chosen_cvc = rating

  # mark the response
  answer = check_answer(rating, gen_correct)

  ## Now the confidence
  RatingScale = visual.RatingScale(stim_win, choices=['1', '2', '3', '4', '5'], acceptText='accept?', showValue=False, markerStyle='circle', markerColor='DarkGreen')
  RatingScale.scaleDescription.setText("""1 = not at all (guess),  5 = Certain.""")
  question = "How confident are you that " + rating + " was more similar to the items you have seen before?\n"
  myItem = visual.TextStim(stim_win, text=question, units='norm')
  # start timing rating
  start_rating = time.time()
  event.clearEvents()
  while RatingScale.noResponse: # show & update until a response has been made
    myItem.draw()
    RatingScale.draw()
    stim_win.flip()
  # Get rating time
  elapsed_rating = (time.time() - start_rating)
  rating = RatingScale.getRating() # get the value indicated by the subject, 'None' if skipped
  complete_answer = output_filename + " " + chosen_cvc + " " + rating + " " + answer + " " + str(elapsed_cvc) + " " + str(elapsed_rating) + "\n"
  print complete_answer
  textfile.write(complete_answer)

# Printing out the table headers
header = "id cvc rating mark cvctime ratingtime\n"
textfile.write(header)
print header

# instructions for choosing and rating.
message.setText(choose_and_rate)
ready_cont()
stim_win.flip()
message.setAutoDraw(False)

# Recognition loop
for i in range(len(recog_mix_left)): # recog_mix_left is being relied on to go through the list, so make sure it's equal to the right.
  recognition(recog_mix_left[i], recog_mix_right[i])

# Have a clear row to seperate the two tests.
header = "\n"
textfile.write(header)
print header

stim_win.flip()
message.setText(generalization_message)
message.draw()
ready_cont()
stim_win.flip()

# Generalization loop
for i in range(len(gen_left)): # recog_mix_left is being relied on to go through the list, so make sure it's equal to the right.
  generalize(gen_left[i], gen_right[i])

# Saying goodby
core.wait(between_tests_interval)
message.setText(thank_you)
message.draw()
ready_cont()
stim_win.flip()

# Cleanup
closingtext = "closing " + output_filename + '.csv'
print closingtext
textfile.close
print 'Successful exit'

# Done!
stim_win.close()
core.quit()
