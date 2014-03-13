# training.py
# This is the training script which will be presented to the participant before they sleep
# or remain awake
#
# TODO

# Libraries - these seem fine and should not need altering.
from psychopy import visual, event, core, misc, data, gui, sound

# Participant needs to press y to continue.
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

# Metronome function - This plays the metronome; the timing can also be altered here.
# The timing required needs to be passed to metronome function.
#music = pyglet.resource.media('klack.ogg', streaming=False)
music = sound.Sound(900,secs=0.01) # Just temporary
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
  metronome(cvc_slow_rate)
  metronome(cvc_faster_rate)
  metronome(cvc_faster_rate)
  metronome(cvc_faster_rate)

# Variables
welcome_message = """Welcome to the training session! You will see four syllables in a row. Please read the entire row out loud 4 times in time to the metronome and try to say one syllable per beat. The first time will be slow, and the next 3 repetitions will be a little faster. Try to read as fluently as possible. Do not worry if you make mistakes, just keep in time with the beat.
Press y now to hear the speed of the metronome."""
sample_welcome = """The following will be a practice session to familiarize you with the sequences (press y to continue)"""
sample_goodbye = """The sample has ended, please press y if you are ready for the real session"""
thank_you = """The training session is complete,
Please inform a researcher you have finished.
Thank you."""
metronome_alone_message = """Playing the metronome..."""

# cvc rates
cvc_slow_rate = 1.0
# A cvc every 395ms with Warker e al (2008)
cvc_faster_rate = 0.395
# interval between each sequence
stim_interval = 1.0
between_tests_interval = 2.0

# Stimuli variables - These are the non counterbalanced stimuli.
sample_stim = ['haf gak mang san',
'kis mig hing fin',
'sak haf nam gang']

real_stim = ['kag hang saf man',
'fis hig ming kin',
'kam saf nag hang',
'fing gis kim hin',
'ham naf kang sag',
'kis fin gim hing',
'gaf nak ham sang',
'gim fik his ning',
'gan ham kang saf',
'gim fin king his',
'nag mang haf sak',
'fis him kig ning',
'gang haf san kam',
'gin king fis him',
'saf nag hang mak',
'fis nik mig hing',
'haf sang nam kag',
'kig fim his ning',
'han kang sag maf',
'mis hin kig fing',
'sang haf gam kan',
'him kig ning fis',
'mang saf hag kan',
'his kin fim ging',
'mang nag saf hak',
'fin kis him ging',
'saf hang gam kan',
'fim nis king hig',
'mak gang han saf',
'mig kin hing fis',
'saf nang mak hag',
'hing gis mik fin',
'haf nang kam sag',
'fin ging kim his',
'gak saf han mang',
'fing mis hin kig',
'sag nam haf kang',
'mis hin king fig',
'sag kam naf hang',
'fik his nim ging',
'gang mak saf han',
'fig mik ning his',
'maf sag hak nang',
'kin hing gim fis',
'ham sak nang gaf',
'king nis fig him',
'gak mang haf san',
'min hing kis fig']

# Setting up the screen.
stim_win = visual.Window(monitor = "testMonitor", units ='norm', fullscr=True)
message = visual.TextStim(stim_win, text = welcome_message, font = "Arial")
message.setAutoDraw(True)
ready_cont()
stim_win.flip()

# The metronome so participant's know what it's like.
# Hmm allow participant to repeat? - Not really fair if
# some participants' run it more than others and pronounce
# cvc's better due to familiarity with the beat.
message.setText(metronome_alone_message)
metronome_alone()
core.wait(stim_interval)
stim_win.flip()

# Welcome the participant.
message.setText(sample_welcome)
ready_cont()

# The sample loop
stim_win.flip()
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

# The real stimuli loop
stim_win.flip()
for i in range(len(real_stim)):
  message.setText(real_stim[i])
  stim_win.flip()
  core.wait(stim_interval)
  metronome(cvc_slow_rate)
  metronome(cvc_faster_rate)
  metronome(cvc_faster_rate)
  metronome(cvc_faster_rate)
  core.wait(stim_interval)

# Saying goodbye
stim_win.flip()
message.setText(thank_you)
ready_cont()
core.wait(stim_interval)

#cleanup
stim_win.close()
core.quit()
