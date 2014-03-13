# training.py fas-sif set 1
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
sample_stim = ['gas fak man hang',
'has kag mang fan',
'gak nas ham fang']

real_stim = ['has fak nang mag',
'ning sif him kig',
'kam gas fan hang',
'sik nif ging him',
'fang hag mas kan',
'sif hik gim ning',
'fam hag kas nang',
'hin kif ging sim',
'nam hak fas gang',
'hing kin sim gif',
'nas gam hak fang',
'ning sik mif hig',
'nam kag has fang',
'king gin sif him',
'fam nak gas hang',
'sin ming hik gif',
'fang nak has mag',
'sig nif hik ming',
'fas man hak gang',
'him kif sing gin',
'nam hak gang fas',
'gin kif sing him',
'kan fang gam has',
'kim hif gin sing',
'fas man hag kang',
'hig kin ming sif',
'man fang kag has',
'hif ming nik sig',
'fak nag mas hang',
'nik him sif ging',
'kang fan mag has',
'hin kig sing mif',
'nak fam gang has',
'gim hing sik nif',
'has fan kang gam',
'sik mig hif ning',
'fas kam hag nang',
'mif hin sig king',
'nag kam hang fas',
'hing mig kif sin',
'gak hang mas fan',
'kim hig nif sing',
'fan kam has gang',
'hing mik sig nif',
'mag hang fas nak',
'mif hing sig nik',
'gam has fang kan',
'kin sing gif him']

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
