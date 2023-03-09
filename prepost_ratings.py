#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on June 03, 2021, at 09:43
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'prepost_ratings'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\xf82\\Desktop\\OEA & HFD\\2 Baseline\\fMRI\\1 prescan ratings\\prepost_ratings.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='AliceBlue', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "internal_state"
internal_stateClock = core.Clock()
IS_slider = visual.Slider(win=win, name='IS_slider',
    size=(1000, 30), pos=(0,0), units=None,
    labels=None, ticks=[0,1000],
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)
ISlabel1 = visual.TextStim(win=win, name='ISlabel1',
    text='default text',
    font='Arial',
    pos=(-500, -43), height=25, wrapWidth=400, ori=0, 
    color='MidnightBlue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ISlabel2 = visual.TextStim(win=win, name='ISlabel2',
    text='default text',
    font='Arial',
    pos=(500, -43), height=25, wrapWidth=400, ori=0, 
    color='MidnightBlue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
IS_text = visual.TextStim(win=win, name='IS_text',
    text='default text',
    font='Arial',
    pos=(0, 100), height=40, wrapWidth=1200, ori=0, 
    color='MidnightBlue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "taste_presentation"
taste_presentationClock = core.Clock()
taste_pres = visual.TextStim(win=win, name='taste_pres',
    text='default text',
    font='Arial',
    pos=(0, 0), height=60, wrapWidth=None, ori=0, 
    color='lightgrey', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text = visual.TextStim(win=win, name='text',
    text='Experimenter: Send taste',
    font='Arial',
    pos=(0, 100), height=40, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
trigger = keyboard.Keyboard()

# Initialize components for Routine "intense"
intenseClock = core.Clock()
intense_slider = visual.Slider(win=win, name='intense_slider',
    size=(20,800), pos=(500,0), units=None,
    labels=['No sensation','Barely detectable', 'Weak', 'Moderate', 'Strong', 'Very strong', 'Strongest imaginable sensation of any kind'], ticks=[0, 1.4,6,17,35,51,100],
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)
intense_instructions = visual.TextStim(win=win, name='intense_instructions',
    text='How intense is this taste?',
    font='Arial',
    pos=(-300,0), height=40, wrapWidth=1000, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "liking"
likingClock = core.Clock()
like_slider = visual.Slider(win=win, name='like_slider',
    size=(20,800), pos=(500,0), units=None,
    labels=['Most disliked sensation imaginable','Dislike extremely','Dislike very much','Dislike moderately','Dislike slightly','Neutral','Like slightly','Like moderately','Like very much','Like extremely','Most liked sensation imaginable'], ticks=[-100, -62.89, -41.58, -17.59, -5.92, 0, 6.25, 17.82, 44.43, 65.72, 100],
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)
like_instructions = visual.TextStim(win=win, name='like_instructions',
    text='How much do you like or dislike this taste?',
    font='Arial',
    pos=(-300, 0), height=40, wrapWidth=1000, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "familiar"
familiarClock = core.Clock()
familiar_slider = visual.Slider(win=win, name='familiar_slider',
    size=(1000,30), pos=(0,0), units=None,
    labels=['Not familiar at all','More familiar than anything'], ticks=(0,1000),
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)
familiar_question = visual.TextStim(win=win, name='familiar_question',
    text='How familiar is this taste?',
    font='Arial',
    pos=(0, 100), height=40, wrapWidth=1200, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "want"
wantClock = core.Clock()
want_slider = visual.Slider(win=win, name='want_slider',
    size=(1000,30), pos=(0,0), units=None,
    labels=['Do not want at all','Want more than anything'], ticks=(0,1000),
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)
want_question = visual.TextStim(win=win, name='want_question',
    text='How much do you want to eat this taste?',
    font='Arial',
    pos=(0, 100), height=40, wrapWidth=1200, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "end"
endClock = core.Clock()
done = visual.TextStim(win=win, name='done',
    text='You have completed the ratings :)',
    font='Arial',
    pos=(0, 0), height=30, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
IS = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('internal_states.xlsx'),
    seed=None, name='IS')
thisExp.addLoop(IS)  # add the loop to the experiment
thisIS = IS.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisIS.rgb)
if thisIS != None:
    for paramName in thisIS:
        exec('{} = thisIS[paramName]'.format(paramName))

for thisIS in IS:
    currentLoop = IS
    # abbreviate parameter names if possible (e.g. rgb = thisIS.rgb)
    if thisIS != None:
        for paramName in thisIS:
            exec('{} = thisIS[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "internal_state"-------
    # update component parameters for each repeat
    IS_slider.reset()
    ISlabel1.setText(LabelL)
    ISlabel2.setText(LabelR)
    IS_text.setText(Question)
    ##start and hide mouse
    mouse = event.Mouse(visible=False)
    
    ##start timer - uncomment if you want RTs
    #timer = core.Clock()
    
    ##marker display options
    IS_slider.marker.size=(.1,2)
    IS_slider.marker.color='Red'
    
    ##set initial mouse and marker positions
    mouse.setPos((-500,0))
    IS_slider.markerPos=0
    # keep track of which components have finished
    internal_stateComponents = [IS_slider, ISlabel1, ISlabel2, IS_text]
    for thisComponent in internal_stateComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    internal_stateClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "internal_state"-------
    while continueRoutine:
        # get current time
        t = internal_stateClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=internal_stateClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *IS_slider* updates
        if IS_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IS_slider.frameNStart = frameN  # exact frame index
            IS_slider.tStart = t  # local t and not account for scr refresh
            IS_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IS_slider, 'tStartRefresh')  # time at next scr refresh
            IS_slider.setAutoDraw(True)
        
        # *ISlabel1* updates
        if ISlabel1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISlabel1.frameNStart = frameN  # exact frame index
            ISlabel1.tStart = t  # local t and not account for scr refresh
            ISlabel1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISlabel1, 'tStartRefresh')  # time at next scr refresh
            ISlabel1.setAutoDraw(True)
        
        # *ISlabel2* updates
        if ISlabel2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISlabel2.frameNStart = frameN  # exact frame index
            ISlabel2.tStart = t  # local t and not account for scr refresh
            ISlabel2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISlabel2, 'tStartRefresh')  # time at next scr refresh
            ISlabel2.setAutoDraw(True)
        
        # *IS_text* updates
        if IS_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IS_text.frameNStart = frameN  # exact frame index
            IS_text.tStart = t  # local t and not account for scr refresh
            IS_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IS_text, 'tStartRefresh')  # time at next scr refresh
            IS_text.setAutoDraw(True)
        ##tie marker to mouse position
        x = mouse.getPos()[0]
        IS_slider.markerPos=500 + (x)
        
        ##write marker position and/or RT on click and end routine
        if mouse.getPressed()[0]:
            IS.addData('ISval', (IS_slider.markerPos / 10))
            #IS.adddata('ISval_RT', timer.getTime=())
            continueRoutine = False
            
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in internal_stateComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "internal_state"-------
    for thisComponent in internal_stateComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ##take a nap to help prevent accidental double-clicks
    core.wait(0.5)
    # the Routine "internal_state" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'IS'


# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('tastes.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "taste_presentation"-------
    # update component parameters for each repeat
    taste_pres.setText(Taste)
    trigger.keys = []
    trigger.rt = []
    # keep track of which components have finished
    taste_presentationComponents = [taste_pres, text, trigger]
    for thisComponent in taste_presentationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    taste_presentationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "taste_presentation"-------
    while continueRoutine:
        # get current time
        t = taste_presentationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=taste_presentationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *taste_pres* updates
        if taste_pres.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            taste_pres.frameNStart = frameN  # exact frame index
            taste_pres.tStart = t  # local t and not account for scr refresh
            taste_pres.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(taste_pres, 'tStartRefresh')  # time at next scr refresh
            taste_pres.setAutoDraw(True)
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *trigger* updates
        waitOnFlip = False
        if trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trigger.frameNStart = frameN  # exact frame index
            trigger.tStart = t  # local t and not account for scr refresh
            trigger.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trigger, 'tStartRefresh')  # time at next scr refresh
            trigger.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(trigger.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trigger.status == STARTED and not waitOnFlip:
            theseKeys = trigger.getKeys(keyList=['return'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in taste_presentationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "taste_presentation"-------
    for thisComponent in taste_presentationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "taste_presentation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "intense"-------
    # update component parameters for each repeat
    intense_slider.reset()
    ###start and hide mouse
    mouse = event.Mouse(visible=False)
    
    ###start timer - uncomment if you want RTs
    #timer = core.Clock()
    
    ###marker display options
    intense_slider.marker.size=(2,.1);
    intense_slider.marker.color='Red';
    
    ###set initial mouse and marker positions
    mouse.setPos((0,0))
    intense_slider.markerPos=0
    # keep track of which components have finished
    intenseComponents = [intense_slider, intense_instructions]
    for thisComponent in intenseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    intenseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "intense"-------
    while continueRoutine:
        # get current time
        t = intenseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=intenseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *intense_slider* updates
        if intense_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intense_slider.frameNStart = frameN  # exact frame index
            intense_slider.tStart = t  # local t and not account for scr refresh
            intense_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intense_slider, 'tStartRefresh')  # time at next scr refresh
            intense_slider.setAutoDraw(True)
        
        # *intense_instructions* updates
        if intense_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intense_instructions.frameNStart = frameN  # exact frame index
            intense_instructions.tStart = t  # local t and not account for scr refresh
            intense_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intense_instructions, 'tStartRefresh')  # time at next scr refresh
            intense_instructions.setAutoDraw(True)
        ##tie marker to mouse position
        x = mouse.getPos()[1]
        intense_slider.markerPos=(x // 5)
        
        ##write marker position and/or RT on click and end routine
        if mouse.getPressed()[0]:
            trials.addData('Intense', intense_slider.markerPos)
            #trials.addData('Intense_RT', timer.getTime=())
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intenseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "intense"-------
    for thisComponent in intenseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ##take a nap to help prevent accidental double-clicks
    core.wait(0.5)
    # the Routine "intense" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "liking"-------
    # update component parameters for each repeat
    like_slider.reset()
    ##start and hide mouse
    mouse = event.Mouse(visible = False)
    
    ##start timer - uncomment if you want RTs
    #timer = core.Clock()
    
    ##marker display options
    like_slider.marker.size=(2,.1);
    like_slider.marker.color='Red';
    
    ##set initial mouse and marker positions
    mouse.setPos((0,0))
    like_slider.markerPos=0
    # keep track of which components have finished
    likingComponents = [like_slider, like_instructions]
    for thisComponent in likingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    likingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "liking"-------
    while continueRoutine:
        # get current time
        t = likingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=likingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *like_slider* updates
        if like_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            like_slider.frameNStart = frameN  # exact frame index
            like_slider.tStart = t  # local t and not account for scr refresh
            like_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(like_slider, 'tStartRefresh')  # time at next scr refresh
            like_slider.setAutoDraw(True)
        
        # *like_instructions* updates
        if like_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            like_instructions.frameNStart = frameN  # exact frame index
            like_instructions.tStart = t  # local t and not account for scr refresh
            like_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(like_instructions, 'tStartRefresh')  # time at next scr refresh
            like_instructions.setAutoDraw(True)
        ##tie marker to mouse position
        x = mouse.getPos()[1]
        like_slider.markerPos=(x // 5)
        
        ##write marker position and/or RT on click and end routine
        if mouse.getPressed()[0]:
            trials.addData('Like', like_slider.markerPos)
            #trials.addData('Like_RT', timer.getTime=())
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in likingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "liking"-------
    for thisComponent in likingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ##take a nap to help prevent accidental couble-clicks
    core.wait(0.5)
    # the Routine "liking" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "familiar"-------
    # update component parameters for each repeat
    familiar_slider.reset()
    ##start and hide mouse
    mouse = event.Mouse(visible=False)
    
    ##start timer - uncomment if you want RTs
    #timer = core.Clock()
    
    ##marker display options
    familiar_slider.marker.size=(.1,2)
    familiar_slider.marker.color='Red'
    
    ##set initial mouse and marker positions
    mouse.setPos((-500,0))
    familiar_slider.markerPos=0
    # keep track of which components have finished
    familiarComponents = [familiar_slider, familiar_question]
    for thisComponent in familiarComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    familiarClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "familiar"-------
    while continueRoutine:
        # get current time
        t = familiarClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=familiarClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *familiar_slider* updates
        if familiar_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            familiar_slider.frameNStart = frameN  # exact frame index
            familiar_slider.tStart = t  # local t and not account for scr refresh
            familiar_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(familiar_slider, 'tStartRefresh')  # time at next scr refresh
            familiar_slider.setAutoDraw(True)
        
        # *familiar_question* updates
        if familiar_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            familiar_question.frameNStart = frameN  # exact frame index
            familiar_question.tStart = t  # local t and not account for scr refresh
            familiar_question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(familiar_question, 'tStartRefresh')  # time at next scr refresh
            familiar_question.setAutoDraw(True)
        ##tie marker to mouse position
        x = mouse.getPos()[0]
        familiar_slider.markerPos= 500 + (x)
        
        ##write marker position and/or RT on click and end routine
        if mouse.getPressed()[0]:
            trials.addData('Familiar', (familiar_slider.markerPos / 10))
            #trials.addData('Familiar_RT', timer.getTime=())
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in familiarComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "familiar"-------
    for thisComponent in familiarComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ##take a nap to help prevent accidental double-clicks
    core.wait(0.5)
    # the Routine "familiar" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "want"-------
    # update component parameters for each repeat
    want_slider.reset()
    ##start and hide mouse
    mouse = event.Mouse(visible=False)
    
    ##start timer - uncomment if you want RTs
    #timer = core.Clock()
    
    ##marker display options
    want_slider.marker.size=(.1,2)
    want_slider.marker.color='Red'
    
    ##set initial mouse and marker positions
    mouse.setPos((-500,0))
    want_slider.markerPos=0
    # keep track of which components have finished
    wantComponents = [want_slider, want_question]
    for thisComponent in wantComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    wantClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "want"-------
    while continueRoutine:
        # get current time
        t = wantClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=wantClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *want_slider* updates
        if want_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            want_slider.frameNStart = frameN  # exact frame index
            want_slider.tStart = t  # local t and not account for scr refresh
            want_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(want_slider, 'tStartRefresh')  # time at next scr refresh
            want_slider.setAutoDraw(True)
        
        # *want_question* updates
        if want_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            want_question.frameNStart = frameN  # exact frame index
            want_question.tStart = t  # local t and not account for scr refresh
            want_question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(want_question, 'tStartRefresh')  # time at next scr refresh
            want_question.setAutoDraw(True)
        ##tie marker to mouse position
        x = mouse.getPos()[0]
        want_slider.markerPos= 500 + (x)
        
        ##write marker position and/or RT on click and end routine
        if mouse.getPressed()[0]:
            trials.addData('Want', (want_slider.markerPos / 10))
            #trials.addData('Want_RT', timer.getTime=())
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wantComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "want"-------
    for thisComponent in wantComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ##take a nap to help prevent accidental double-clicks
    core.wait(0.5)
    # the Routine "want" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "end"-------
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [done]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *done* updates
    if done.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        done.frameNStart = frameN  # exact frame index
        done.tStart = t  # local t and not account for scr refresh
        done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(done, 'tStartRefresh')  # time at next scr refresh
        done.setAutoDraw(True)
    if done.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > done.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            done.tStop = t  # not accounting for scr refresh
            done.frameNStop = frameN  # exact frame index
            win.timeOnFlip(done, 'tStopRefresh')  # time at next scr refresh
            done.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
