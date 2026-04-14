#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on maj 04, 2024, at 22:08
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

import random
#definicja losowania
def wybieranieLiczb(maksLiczba,iloscWybranych):
    wszystkieLiczby = []
    wszystkieLiczby = [str(x) for x in range(maksLiczba+1)]
    wybraneLiczby = random.sample(wszystkieLiczby,iloscWybranych)
    liczbyString = ",".join (wybraneLiczby)
    return(liczbyString)
WL1 = 432 #144 ilość wszyskich liczbowych
WL2 = 33 #33 # liczbowe na próbę
Wi1 = 308 #154 ilość wszystkich literowych
Wi2 = 34 #34 # literowe na próbę
WK1 = 88 # ilość wszystkich prób krztałtowych
WK2 = 33 #33 # krztałtowe na próbę

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'lixnia'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\abc\\Desktop\\Kwatera Główna\\Studia\\Statystyki\\test\\lixnia.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1536, 864], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "blabla" ---
    blaBlaInst = visual.TextStim(win=win, name='blaBlaInst',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    KoniecInst = keyboard.Keyboard()
    
    # --- Initialize components for Routine "licztera" ---
    BokTarget = visual.TextStim(win=win, name='BokTarget',
        text='+',
        font='Open Sans',
        pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    CentrumTarget = visual.TextStim(win=win, name='CentrumTarget',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    CentrumTest = visual.TextStim(win=win, name='CentrumTest',
        text='',
        font='Open Sans',
        pos=(0,0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    BokTest = visual.TextStim(win=win, name='BokTest',
        text='',
        font='Open Sans',
        pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    KlawiszOdp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "blabla" ---
    blaBlaInst = visual.TextStim(win=win, name='blaBlaInst',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    KoniecInst = keyboard.Keyboard()
    
    # --- Initialize components for Routine "ksztalt" ---
    CentrumTestK = visual.Rect(
        win=win, name='CentrumTestK',units='cm', 
        width=[1.0, 1.0][0], height=[1.0, 1.0][1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor=[0.7000, 0.7000, 0.7000],
        opacity=None, depth=0.0, interpolate=True)
    BokTestK = visual.Rect(
        win=win, name='BokTestK',units='cm', 
        width=[1.0, 1.0][0], height=[1.0, 1.0][1],
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor=[0.7000, 0.7000, 0.7000],
        opacity=None, depth=-1.0, interpolate=True)
    KlawiszOdpK = keyboard.Keyboard()
    CentrumTargetK = visual.TextStim(win=win, name='CentrumTargetK',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    BokTargetK = visual.ShapeStim(
        win=win, name='BokTargetK', vertices='cross',units='cm', 
        size=(1.4, 1.4),
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
        opacity=1.0, depth=-4.0, interpolate=True)
    
    # --- Initialize components for Routine "blabla" ---
    blaBlaInst = visual.TextStim(win=win, name='blaBlaInst',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    KoniecInst = keyboard.Keyboard()
    
    # --- Initialize components for Routine "licztera" ---
    BokTarget = visual.TextStim(win=win, name='BokTarget',
        text='+',
        font='Open Sans',
        pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    CentrumTarget = visual.TextStim(win=win, name='CentrumTarget',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    CentrumTest = visual.TextStim(win=win, name='CentrumTest',
        text='',
        font='Open Sans',
        pos=(0,0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    BokTest = visual.TextStim(win=win, name='BokTest',
        text='',
        font='Open Sans',
        pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    KlawiszOdp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "blabla" ---
    blaBlaInst = visual.TextStim(win=win, name='blaBlaInst',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    KoniecInst = keyboard.Keyboard()
    
    # --- Initialize components for Routine "licztera" ---
    BokTarget = visual.TextStim(win=win, name='BokTarget',
        text='+',
        font='Open Sans',
        pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    CentrumTarget = visual.TextStim(win=win, name='CentrumTarget',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    CentrumTest = visual.TextStim(win=win, name='CentrumTest',
        text='',
        font='Open Sans',
        pos=(0,0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    BokTest = visual.TextStim(win=win, name='BokTest',
        text='',
        font='Open Sans',
        pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    KlawiszOdp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "blabla" ---
    blaBlaInst = visual.TextStim(win=win, name='blaBlaInst',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    KoniecInst = keyboard.Keyboard()
    
    # --- Initialize components for Routine "licztera" ---
    BokTarget = visual.TextStim(win=win, name='BokTarget',
        text='+',
        font='Open Sans',
        pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    CentrumTarget = visual.TextStim(win=win, name='CentrumTarget',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    CentrumTest = visual.TextStim(win=win, name='CentrumTest',
        text='',
        font='Open Sans',
        pos=(0,0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    BokTest = visual.TextStim(win=win, name='BokTest',
        text='',
        font='Open Sans',
        pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    KlawiszOdp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "blabla" ---
    blaBlaInst = visual.TextStim(win=win, name='blaBlaInst',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    KoniecInst = keyboard.Keyboard()
    
    # --- Initialize components for Routine "licztera" ---
    BokTarget = visual.TextStim(win=win, name='BokTarget',
        text='+',
        font='Open Sans',
        pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    CentrumTarget = visual.TextStim(win=win, name='CentrumTarget',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    CentrumTest = visual.TextStim(win=win, name='CentrumTest',
        text='',
        font='Open Sans',
        pos=(0,0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    BokTest = visual.TextStim(win=win, name='BokTest',
        text='',
        font='Open Sans',
        pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    KlawiszOdp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "koniec" ---
    TekstKoncowy = visual.TextStim(win=win, name='TekstKoncowy',
        text='Dzięki wykonanie za eksperymentu ^^',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    KlawiszKoniec = keyboard.Keyboard()
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # set up handler to look after randomisation of conditions etc
    t0 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TestNaX/Teksty.xlsx', selection='0'),
        seed=None, name='t0')
    thisExp.addLoop(t0)  # add the loop to the experiment
    thisT0 = t0.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisT0.rgb)
    if thisT0 != None:
        for paramName in thisT0:
            globals()[paramName] = thisT0[paramName]
    
    for thisT0 in t0:
        currentLoop = t0
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisT0.rgb)
        if thisT0 != None:
            for paramName in thisT0:
                globals()[paramName] = thisT0[paramName]
        
        # --- Prepare to start Routine "blabla" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('blabla.started', globalClock.getTime())
        blaBlaInst.setText(eee)
        KoniecInst.keys = []
        KoniecInst.rt = []
        _KoniecInst_allKeys = []
        # keep track of which components have finished
        blablaComponents = [blaBlaInst, KoniecInst]
        for thisComponent in blablaComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blabla" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blaBlaInst* updates
            
            # if blaBlaInst is starting this frame...
            if blaBlaInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blaBlaInst.frameNStart = frameN  # exact frame index
                blaBlaInst.tStart = t  # local t and not account for scr refresh
                blaBlaInst.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blaBlaInst, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blaBlaInst.started')
                # update status
                blaBlaInst.status = STARTED
                blaBlaInst.setAutoDraw(True)
            
            # if blaBlaInst is active this frame...
            if blaBlaInst.status == STARTED:
                # update params
                pass
            
            # *KoniecInst* updates
            waitOnFlip = False
            
            # if KoniecInst is starting this frame...
            if KoniecInst.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                KoniecInst.frameNStart = frameN  # exact frame index
                KoniecInst.tStart = t  # local t and not account for scr refresh
                KoniecInst.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(KoniecInst, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KoniecInst.started')
                # update status
                KoniecInst.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(KoniecInst.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(KoniecInst.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if KoniecInst.status == STARTED and not waitOnFlip:
                theseKeys = KoniecInst.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
                _KoniecInst_allKeys.extend(theseKeys)
                if len(_KoniecInst_allKeys):
                    KoniecInst.keys = _KoniecInst_allKeys[-1].name  # just the last key pressed
                    KoniecInst.rt = _KoniecInst_allKeys[-1].rt
                    KoniecInst.duration = _KoniecInst_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blablaComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blabla" ---
        for thisComponent in blablaComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('blabla.stopped', globalClock.getTime())
        # check responses
        if KoniecInst.keys in ['', [], None]:  # No response was made
            KoniecInst.keys = None
        t0.addData('KoniecInst.keys',KoniecInst.keys)
        if KoniecInst.keys != None:  # we had a response
            t0.addData('KoniecInst.rt', KoniecInst.rt)
            t0.addData('KoniecInst.duration', KoniecInst.duration)
        # the Routine "blabla" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 't0'
    
    
    # set up handler to look after randomisation of conditions etc
    TNA = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TestNaX/TestNaA.xlsx', selection=wybieranieLiczb(WL1,WL2)),
        seed=None, name='TNA')
    thisExp.addLoop(TNA)  # add the loop to the experiment
    thisTNA = TNA.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTNA.rgb)
    if thisTNA != None:
        for paramName in thisTNA:
            globals()[paramName] = thisTNA[paramName]
    
    for thisTNA in TNA:
        currentLoop = TNA
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTNA.rgb)
        if thisTNA != None:
            for paramName in thisTNA:
                globals()[paramName] = thisTNA[paramName]
        
        # --- Prepare to start Routine "licztera" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('licztera.started', globalClock.getTime())
        BokTarget.setPos([xtrona,0])
        CentrumTest.setText(Centrum)
        BokTest.setPos([xtrona,0])
        BokTest.setText(Bok)
        KlawiszOdp.keys = []
        KlawiszOdp.rt = []
        _KlawiszOdp_allKeys = []
        # keep track of which components have finished
        liczteraComponents = [BokTarget, CentrumTarget, CentrumTest, BokTest, KlawiszOdp]
        for thisComponent in liczteraComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "licztera" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *BokTarget* updates
            
            # if BokTarget is starting this frame...
            if BokTarget.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                BokTarget.frameNStart = frameN  # exact frame index
                BokTarget.tStart = t  # local t and not account for scr refresh
                BokTarget.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BokTarget, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'BokTarget.started')
                # update status
                BokTarget.status = STARTED
                BokTarget.setAutoDraw(True)
            
            # if BokTarget is active this frame...
            if BokTarget.status == STARTED:
                # update params
                pass
            
            # if BokTarget is stopping this frame...
            if BokTarget.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > BokTarget.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    BokTarget.tStop = t  # not accounting for scr refresh
                    BokTarget.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'BokTarget.stopped')
                    # update status
                    BokTarget.status = FINISHED
                    BokTarget.setAutoDraw(False)
            
            # *CentrumTarget* updates
            
            # if CentrumTarget is starting this frame...
            if CentrumTarget.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                CentrumTarget.frameNStart = frameN  # exact frame index
                CentrumTarget.tStart = t  # local t and not account for scr refresh
                CentrumTarget.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CentrumTarget, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CentrumTarget.started')
                # update status
                CentrumTarget.status = STARTED
                CentrumTarget.setAutoDraw(True)
            
            # if CentrumTarget is active this frame...
            if CentrumTarget.status == STARTED:
                # update params
                pass
            
            # if CentrumTarget is stopping this frame...
            if CentrumTarget.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > CentrumTarget.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    CentrumTarget.tStop = t  # not accounting for scr refresh
                    CentrumTarget.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'CentrumTarget.stopped')
                    # update status
                    CentrumTarget.status = FINISHED
                    CentrumTarget.setAutoDraw(False)
            
            # *CentrumTest* updates
            
            # if CentrumTest is starting this frame...
            if CentrumTest.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                CentrumTest.frameNStart = frameN  # exact frame index
                CentrumTest.tStart = t  # local t and not account for scr refresh
                CentrumTest.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CentrumTest, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CentrumTest.started')
                # update status
                CentrumTest.status = STARTED
                CentrumTest.setAutoDraw(True)
            
            # if CentrumTest is active this frame...
            if CentrumTest.status == STARTED:
                # update params
                pass
            
            # *BokTest* updates
            
            # if BokTest is starting this frame...
            if BokTest.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                BokTest.frameNStart = frameN  # exact frame index
                BokTest.tStart = t  # local t and not account for scr refresh
                BokTest.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BokTest, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'BokTest.started')
                # update status
                BokTest.status = STARTED
                BokTest.setAutoDraw(True)
            
            # if BokTest is active this frame...
            if BokTest.status == STARTED:
                # update params
                pass
            
            # *KlawiszOdp* updates
            waitOnFlip = False
            
            # if KlawiszOdp is starting this frame...
            if KlawiszOdp.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                KlawiszOdp.frameNStart = frameN  # exact frame index
                KlawiszOdp.tStart = t  # local t and not account for scr refresh
                KlawiszOdp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(KlawiszOdp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KlawiszOdp.started')
                # update status
                KlawiszOdp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(KlawiszOdp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(KlawiszOdp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if KlawiszOdp.status == STARTED and not waitOnFlip:
                theseKeys = KlawiszOdp.getKeys(keyList=['w','s','up','down'], ignoreKeys=["escape"], waitRelease=False)
                _KlawiszOdp_allKeys.extend(theseKeys)
                if len(_KlawiszOdp_allKeys):
                    KlawiszOdp.keys = _KlawiszOdp_allKeys[-1].name  # just the last key pressed
                    KlawiszOdp.rt = _KlawiszOdp_allKeys[-1].rt
                    KlawiszOdp.duration = _KlawiszOdp_allKeys[-1].duration
                    # was this correct?
                    if (KlawiszOdp.keys == str(poprawna)) or (KlawiszOdp.keys == poprawna):
                        KlawiszOdp.corr = 1
                    else:
                        KlawiszOdp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in liczteraComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "licztera" ---
        for thisComponent in liczteraComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('licztera.stopped', globalClock.getTime())
        # check responses
        if KlawiszOdp.keys in ['', [], None]:  # No response was made
            KlawiszOdp.keys = None
            # was no response the correct answer?!
            if str(poprawna).lower() == 'none':
               KlawiszOdp.corr = 1;  # correct non-response
            else:
               KlawiszOdp.corr = 0;  # failed to respond (incorrectly)
        # store data for TNA (TrialHandler)
        TNA.addData('KlawiszOdp.keys',KlawiszOdp.keys)
        TNA.addData('KlawiszOdp.corr', KlawiszOdp.corr)
        if KlawiszOdp.keys != None:  # we had a response
            TNA.addData('KlawiszOdp.rt', KlawiszOdp.rt)
            TNA.addData('KlawiszOdp.duration', KlawiszOdp.duration)
        # the Routine "licztera" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'TNA'
    
    
    # set up handler to look after randomisation of conditions etc
    t2 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TestNaX/Teksty.xlsx', selection='2'),
        seed=None, name='t2')
    thisExp.addLoop(t2)  # add the loop to the experiment
    thisT2 = t2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisT2.rgb)
    if thisT2 != None:
        for paramName in thisT2:
            globals()[paramName] = thisT2[paramName]
    
    for thisT2 in t2:
        currentLoop = t2
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisT2.rgb)
        if thisT2 != None:
            for paramName in thisT2:
                globals()[paramName] = thisT2[paramName]
        
        # --- Prepare to start Routine "blabla" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('blabla.started', globalClock.getTime())
        blaBlaInst.setText(eee)
        KoniecInst.keys = []
        KoniecInst.rt = []
        _KoniecInst_allKeys = []
        # keep track of which components have finished
        blablaComponents = [blaBlaInst, KoniecInst]
        for thisComponent in blablaComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blabla" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blaBlaInst* updates
            
            # if blaBlaInst is starting this frame...
            if blaBlaInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blaBlaInst.frameNStart = frameN  # exact frame index
                blaBlaInst.tStart = t  # local t and not account for scr refresh
                blaBlaInst.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blaBlaInst, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blaBlaInst.started')
                # update status
                blaBlaInst.status = STARTED
                blaBlaInst.setAutoDraw(True)
            
            # if blaBlaInst is active this frame...
            if blaBlaInst.status == STARTED:
                # update params
                pass
            
            # *KoniecInst* updates
            waitOnFlip = False
            
            # if KoniecInst is starting this frame...
            if KoniecInst.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                KoniecInst.frameNStart = frameN  # exact frame index
                KoniecInst.tStart = t  # local t and not account for scr refresh
                KoniecInst.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(KoniecInst, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KoniecInst.started')
                # update status
                KoniecInst.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(KoniecInst.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(KoniecInst.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if KoniecInst.status == STARTED and not waitOnFlip:
                theseKeys = KoniecInst.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
                _KoniecInst_allKeys.extend(theseKeys)
                if len(_KoniecInst_allKeys):
                    KoniecInst.keys = _KoniecInst_allKeys[-1].name  # just the last key pressed
                    KoniecInst.rt = _KoniecInst_allKeys[-1].rt
                    KoniecInst.duration = _KoniecInst_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blablaComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blabla" ---
        for thisComponent in blablaComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('blabla.stopped', globalClock.getTime())
        # check responses
        if KoniecInst.keys in ['', [], None]:  # No response was made
            KoniecInst.keys = None
        t2.addData('KoniecInst.keys',KoniecInst.keys)
        if KoniecInst.keys != None:  # we had a response
            t2.addData('KoniecInst.rt', KoniecInst.rt)
            t2.addData('KoniecInst.duration', KoniecInst.duration)
        # the Routine "blabla" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 't2'
    
    
    # set up handler to look after randomisation of conditions etc
    TNK = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TestNaX/TestNaKwadraty.xlsx', selection=wybieranieLiczb(WK1,WK2)),
        seed=None, name='TNK')
    thisExp.addLoop(TNK)  # add the loop to the experiment
    thisTNK = TNK.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTNK.rgb)
    if thisTNK != None:
        for paramName in thisTNK:
            globals()[paramName] = thisTNK[paramName]
    
    for thisTNK in TNK:
        currentLoop = TNK
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTNK.rgb)
        if thisTNK != None:
            for paramName in thisTNK:
                globals()[paramName] = thisTNK[paramName]
        
        # --- Prepare to start Routine "ksztalt" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('ksztalt.started', globalClock.getTime())
        CentrumTestK.setSize([Centrum, Centrum])
        BokTestK.setPos([xtrona, 0])
        BokTestK.setSize([Bok, Bok])
        KlawiszOdpK.keys = []
        KlawiszOdpK.rt = []
        _KlawiszOdpK_allKeys = []
        BokTargetK.setPos((xtrona, 0))
        # keep track of which components have finished
        ksztaltComponents = [CentrumTestK, BokTestK, KlawiszOdpK, CentrumTargetK, BokTargetK]
        for thisComponent in ksztaltComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ksztalt" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *CentrumTestK* updates
            
            # if CentrumTestK is starting this frame...
            if CentrumTestK.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                CentrumTestK.frameNStart = frameN  # exact frame index
                CentrumTestK.tStart = t  # local t and not account for scr refresh
                CentrumTestK.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CentrumTestK, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CentrumTestK.started')
                # update status
                CentrumTestK.status = STARTED
                CentrumTestK.setAutoDraw(True)
            
            # if CentrumTestK is active this frame...
            if CentrumTestK.status == STARTED:
                # update params
                pass
            
            # *BokTestK* updates
            
            # if BokTestK is starting this frame...
            if BokTestK.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                BokTestK.frameNStart = frameN  # exact frame index
                BokTestK.tStart = t  # local t and not account for scr refresh
                BokTestK.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BokTestK, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'BokTestK.started')
                # update status
                BokTestK.status = STARTED
                BokTestK.setAutoDraw(True)
            
            # if BokTestK is active this frame...
            if BokTestK.status == STARTED:
                # update params
                pass
            
            # *KlawiszOdpK* updates
            waitOnFlip = False
            
            # if KlawiszOdpK is starting this frame...
            if KlawiszOdpK.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                KlawiszOdpK.frameNStart = frameN  # exact frame index
                KlawiszOdpK.tStart = t  # local t and not account for scr refresh
                KlawiszOdpK.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(KlawiszOdpK, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KlawiszOdpK.started')
                # update status
                KlawiszOdpK.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(KlawiszOdpK.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(KlawiszOdpK.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if KlawiszOdpK.status == STARTED and not waitOnFlip:
                theseKeys = KlawiszOdpK.getKeys(keyList=['down','up'], ignoreKeys=["escape"], waitRelease=False)
                _KlawiszOdpK_allKeys.extend(theseKeys)
                if len(_KlawiszOdpK_allKeys):
                    KlawiszOdpK.keys = _KlawiszOdpK_allKeys[-1].name  # just the last key pressed
                    KlawiszOdpK.rt = _KlawiszOdpK_allKeys[-1].rt
                    KlawiszOdpK.duration = _KlawiszOdpK_allKeys[-1].duration
                    # was this correct?
                    if (KlawiszOdpK.keys == str('')) or (KlawiszOdpK.keys == ''):
                        KlawiszOdpK.corr = 1
                    else:
                        KlawiszOdpK.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *CentrumTargetK* updates
            
            # if CentrumTargetK is starting this frame...
            if CentrumTargetK.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                CentrumTargetK.frameNStart = frameN  # exact frame index
                CentrumTargetK.tStart = t  # local t and not account for scr refresh
                CentrumTargetK.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CentrumTargetK, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CentrumTargetK.started')
                # update status
                CentrumTargetK.status = STARTED
                CentrumTargetK.setAutoDraw(True)
            
            # if CentrumTargetK is active this frame...
            if CentrumTargetK.status == STARTED:
                # update params
                pass
            
            # if CentrumTargetK is stopping this frame...
            if CentrumTargetK.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > CentrumTargetK.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    CentrumTargetK.tStop = t  # not accounting for scr refresh
                    CentrumTargetK.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'CentrumTargetK.stopped')
                    # update status
                    CentrumTargetK.status = FINISHED
                    CentrumTargetK.setAutoDraw(False)
            
            # *BokTargetK* updates
            
            # if BokTargetK is starting this frame...
            if BokTargetK.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BokTargetK.frameNStart = frameN  # exact frame index
                BokTargetK.tStart = t  # local t and not account for scr refresh
                BokTargetK.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BokTargetK, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'BokTargetK.started')
                # update status
                BokTargetK.status = STARTED
                BokTargetK.setAutoDraw(True)
            
            # if BokTargetK is active this frame...
            if BokTargetK.status == STARTED:
                # update params
                pass
            
            # if BokTargetK is stopping this frame...
            if BokTargetK.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > BokTargetK.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    BokTargetK.tStop = t  # not accounting for scr refresh
                    BokTargetK.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'BokTargetK.stopped')
                    # update status
                    BokTargetK.status = FINISHED
                    BokTargetK.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ksztaltComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ksztalt" ---
        for thisComponent in ksztaltComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('ksztalt.stopped', globalClock.getTime())
        # check responses
        if KlawiszOdpK.keys in ['', [], None]:  # No response was made
            KlawiszOdpK.keys = None
            # was no response the correct answer?!
            if str('').lower() == 'none':
               KlawiszOdpK.corr = 1;  # correct non-response
            else:
               KlawiszOdpK.corr = 0;  # failed to respond (incorrectly)
        # store data for TNK (TrialHandler)
        TNK.addData('KlawiszOdpK.keys',KlawiszOdpK.keys)
        TNK.addData('KlawiszOdpK.corr', KlawiszOdpK.corr)
        if KlawiszOdpK.keys != None:  # we had a response
            TNK.addData('KlawiszOdpK.rt', KlawiszOdpK.rt)
            TNK.addData('KlawiszOdpK.duration', KlawiszOdpK.duration)
        # the Routine "ksztalt" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'TNK'
    
    
    # set up handler to look after randomisation of conditions etc
    t3a = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TestNaX/Teksty.xlsx', selection='3'),
        seed=None, name='t3a')
    thisExp.addLoop(t3a)  # add the loop to the experiment
    thisT3a = t3a.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisT3a.rgb)
    if thisT3a != None:
        for paramName in thisT3a:
            globals()[paramName] = thisT3a[paramName]
    
    for thisT3a in t3a:
        currentLoop = t3a
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisT3a.rgb)
        if thisT3a != None:
            for paramName in thisT3a:
                globals()[paramName] = thisT3a[paramName]
        
        # --- Prepare to start Routine "blabla" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('blabla.started', globalClock.getTime())
        blaBlaInst.setText(eee)
        KoniecInst.keys = []
        KoniecInst.rt = []
        _KoniecInst_allKeys = []
        # keep track of which components have finished
        blablaComponents = [blaBlaInst, KoniecInst]
        for thisComponent in blablaComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blabla" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blaBlaInst* updates
            
            # if blaBlaInst is starting this frame...
            if blaBlaInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blaBlaInst.frameNStart = frameN  # exact frame index
                blaBlaInst.tStart = t  # local t and not account for scr refresh
                blaBlaInst.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blaBlaInst, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blaBlaInst.started')
                # update status
                blaBlaInst.status = STARTED
                blaBlaInst.setAutoDraw(True)
            
            # if blaBlaInst is active this frame...
            if blaBlaInst.status == STARTED:
                # update params
                pass
            
            # *KoniecInst* updates
            waitOnFlip = False
            
            # if KoniecInst is starting this frame...
            if KoniecInst.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                KoniecInst.frameNStart = frameN  # exact frame index
                KoniecInst.tStart = t  # local t and not account for scr refresh
                KoniecInst.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(KoniecInst, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KoniecInst.started')
                # update status
                KoniecInst.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(KoniecInst.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(KoniecInst.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if KoniecInst.status == STARTED and not waitOnFlip:
                theseKeys = KoniecInst.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
                _KoniecInst_allKeys.extend(theseKeys)
                if len(_KoniecInst_allKeys):
                    KoniecInst.keys = _KoniecInst_allKeys[-1].name  # just the last key pressed
                    KoniecInst.rt = _KoniecInst_allKeys[-1].rt
                    KoniecInst.duration = _KoniecInst_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blablaComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blabla" ---
        for thisComponent in blablaComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('blabla.stopped', globalClock.getTime())
        # check responses
        if KoniecInst.keys in ['', [], None]:  # No response was made
            KoniecInst.keys = None
        t3a.addData('KoniecInst.keys',KoniecInst.keys)
        if KoniecInst.keys != None:  # we had a response
            t3a.addData('KoniecInst.rt', KoniecInst.rt)
            t3a.addData('KoniecInst.duration', KoniecInst.duration)
        # the Routine "blabla" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 't3a'
    
    
    # set up handler to look after randomisation of conditions etc
    TNB = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TestNaX/TestNaB.xlsx', selection=wybieranieLiczb(WL1,WL2)),
        seed=None, name='TNB')
    thisExp.addLoop(TNB)  # add the loop to the experiment
    thisTNB = TNB.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTNB.rgb)
    if thisTNB != None:
        for paramName in thisTNB:
            globals()[paramName] = thisTNB[paramName]
    
    for thisTNB in TNB:
        currentLoop = TNB
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTNB.rgb)
        if thisTNB != None:
            for paramName in thisTNB:
                globals()[paramName] = thisTNB[paramName]
        
        # --- Prepare to start Routine "licztera" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('licztera.started', globalClock.getTime())
        BokTarget.setPos([xtrona,0])
        CentrumTest.setText(Centrum)
        BokTest.setPos([xtrona,0])
        BokTest.setText(Bok)
        KlawiszOdp.keys = []
        KlawiszOdp.rt = []
        _KlawiszOdp_allKeys = []
        # keep track of which components have finished
        liczteraComponents = [BokTarget, CentrumTarget, CentrumTest, BokTest, KlawiszOdp]
        for thisComponent in liczteraComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "licztera" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *BokTarget* updates
            
            # if BokTarget is starting this frame...
            if BokTarget.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                BokTarget.frameNStart = frameN  # exact frame index
                BokTarget.tStart = t  # local t and not account for scr refresh
                BokTarget.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BokTarget, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'BokTarget.started')
                # update status
                BokTarget.status = STARTED
                BokTarget.setAutoDraw(True)
            
            # if BokTarget is active this frame...
            if BokTarget.status == STARTED:
                # update params
                pass
            
            # if BokTarget is stopping this frame...
            if BokTarget.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > BokTarget.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    BokTarget.tStop = t  # not accounting for scr refresh
                    BokTarget.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'BokTarget.stopped')
                    # update status
                    BokTarget.status = FINISHED
                    BokTarget.setAutoDraw(False)
            
            # *CentrumTarget* updates
            
            # if CentrumTarget is starting this frame...
            if CentrumTarget.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                CentrumTarget.frameNStart = frameN  # exact frame index
                CentrumTarget.tStart = t  # local t and not account for scr refresh
                CentrumTarget.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CentrumTarget, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CentrumTarget.started')
                # update status
                CentrumTarget.status = STARTED
                CentrumTarget.setAutoDraw(True)
            
            # if CentrumTarget is active this frame...
            if CentrumTarget.status == STARTED:
                # update params
                pass
            
            # if CentrumTarget is stopping this frame...
            if CentrumTarget.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > CentrumTarget.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    CentrumTarget.tStop = t  # not accounting for scr refresh
                    CentrumTarget.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'CentrumTarget.stopped')
                    # update status
                    CentrumTarget.status = FINISHED
                    CentrumTarget.setAutoDraw(False)
            
            # *CentrumTest* updates
            
            # if CentrumTest is starting this frame...
            if CentrumTest.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                CentrumTest.frameNStart = frameN  # exact frame index
                CentrumTest.tStart = t  # local t and not account for scr refresh
                CentrumTest.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CentrumTest, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CentrumTest.started')
                # update status
                CentrumTest.status = STARTED
                CentrumTest.setAutoDraw(True)
            
            # if CentrumTest is active this frame...
            if CentrumTest.status == STARTED:
                # update params
                pass
            
            # *BokTest* updates
            
            # if BokTest is starting this frame...
            if BokTest.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                BokTest.frameNStart = frameN  # exact frame index
                BokTest.tStart = t  # local t and not account for scr refresh
                BokTest.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BokTest, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'BokTest.started')
                # update status
                BokTest.status = STARTED
                BokTest.setAutoDraw(True)
            
            # if BokTest is active this frame...
            if BokTest.status == STARTED:
                # update params
                pass
            
            # *KlawiszOdp* updates
            waitOnFlip = False
            
            # if KlawiszOdp is starting this frame...
            if KlawiszOdp.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                KlawiszOdp.frameNStart = frameN  # exact frame index
                KlawiszOdp.tStart = t  # local t and not account for scr refresh
                KlawiszOdp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(KlawiszOdp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KlawiszOdp.started')
                # update status
                KlawiszOdp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(KlawiszOdp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(KlawiszOdp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if KlawiszOdp.status == STARTED and not waitOnFlip:
                theseKeys = KlawiszOdp.getKeys(keyList=['w','s','up','down'], ignoreKeys=["escape"], waitRelease=False)
                _KlawiszOdp_allKeys.extend(theseKeys)
                if len(_KlawiszOdp_allKeys):
                    KlawiszOdp.keys = _KlawiszOdp_allKeys[-1].name  # just the last key pressed
                    KlawiszOdp.rt = _KlawiszOdp_allKeys[-1].rt
                    KlawiszOdp.duration = _KlawiszOdp_allKeys[-1].duration
                    # was this correct?
                    if (KlawiszOdp.keys == str(poprawna)) or (KlawiszOdp.keys == poprawna):
                        KlawiszOdp.corr = 1
                    else:
                        KlawiszOdp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in liczteraComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "licztera" ---
        for thisComponent in liczteraComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('licztera.stopped', globalClock.getTime())
        # check responses
        if KlawiszOdp.keys in ['', [], None]:  # No response was made
            KlawiszOdp.keys = None
            # was no response the correct answer?!
            if str(poprawna).lower() == 'none':
               KlawiszOdp.corr = 1;  # correct non-response
            else:
               KlawiszOdp.corr = 0;  # failed to respond (incorrectly)
        # store data for TNB (TrialHandler)
        TNB.addData('KlawiszOdp.keys',KlawiszOdp.keys)
        TNB.addData('KlawiszOdp.corr', KlawiszOdp.corr)
        if KlawiszOdp.keys != None:  # we had a response
            TNB.addData('KlawiszOdp.rt', KlawiszOdp.rt)
            TNB.addData('KlawiszOdp.duration', KlawiszOdp.duration)
        # the Routine "licztera" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'TNB'
    
    
    # set up handler to look after randomisation of conditions etc
    t4a = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TestNaX/Teksty.xlsx', selection='1'),
        seed=None, name='t4a')
    thisExp.addLoop(t4a)  # add the loop to the experiment
    thisT4a = t4a.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisT4a.rgb)
    if thisT4a != None:
        for paramName in thisT4a:
            globals()[paramName] = thisT4a[paramName]
    
    for thisT4a in t4a:
        currentLoop = t4a
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisT4a.rgb)
        if thisT4a != None:
            for paramName in thisT4a:
                globals()[paramName] = thisT4a[paramName]
        
        # --- Prepare to start Routine "blabla" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('blabla.started', globalClock.getTime())
        blaBlaInst.setText(eee)
        KoniecInst.keys = []
        KoniecInst.rt = []
        _KoniecInst_allKeys = []
        # keep track of which components have finished
        blablaComponents = [blaBlaInst, KoniecInst]
        for thisComponent in blablaComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blabla" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blaBlaInst* updates
            
            # if blaBlaInst is starting this frame...
            if blaBlaInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blaBlaInst.frameNStart = frameN  # exact frame index
                blaBlaInst.tStart = t  # local t and not account for scr refresh
                blaBlaInst.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blaBlaInst, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blaBlaInst.started')
                # update status
                blaBlaInst.status = STARTED
                blaBlaInst.setAutoDraw(True)
            
            # if blaBlaInst is active this frame...
            if blaBlaInst.status == STARTED:
                # update params
                pass
            
            # *KoniecInst* updates
            waitOnFlip = False
            
            # if KoniecInst is starting this frame...
            if KoniecInst.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                KoniecInst.frameNStart = frameN  # exact frame index
                KoniecInst.tStart = t  # local t and not account for scr refresh
                KoniecInst.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(KoniecInst, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KoniecInst.started')
                # update status
                KoniecInst.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(KoniecInst.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(KoniecInst.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if KoniecInst.status == STARTED and not waitOnFlip:
                theseKeys = KoniecInst.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
                _KoniecInst_allKeys.extend(theseKeys)
                if len(_KoniecInst_allKeys):
                    KoniecInst.keys = _KoniecInst_allKeys[-1].name  # just the last key pressed
                    KoniecInst.rt = _KoniecInst_allKeys[-1].rt
                    KoniecInst.duration = _KoniecInst_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blablaComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blabla" ---
        for thisComponent in blablaComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('blabla.stopped', globalClock.getTime())
        # check responses
        if KoniecInst.keys in ['', [], None]:  # No response was made
            KoniecInst.keys = None
        t4a.addData('KoniecInst.keys',KoniecInst.keys)
        if KoniecInst.keys != None:  # we had a response
            t4a.addData('KoniecInst.rt', KoniecInst.rt)
            t4a.addData('KoniecInst.duration', KoniecInst.duration)
        # the Routine "blabla" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 't4a'
    
    
    # set up handler to look after randomisation of conditions etc
    TNLA = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TestNaX/TestNaLiteryA.xlsx', selection=wybieranieLiczb(Wi1,Wi2)),
        seed=None, name='TNLA')
    thisExp.addLoop(TNLA)  # add the loop to the experiment
    thisTNLA = TNLA.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTNLA.rgb)
    if thisTNLA != None:
        for paramName in thisTNLA:
            globals()[paramName] = thisTNLA[paramName]
    
    for thisTNLA in TNLA:
        currentLoop = TNLA
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTNLA.rgb)
        if thisTNLA != None:
            for paramName in thisTNLA:
                globals()[paramName] = thisTNLA[paramName]
        
        # --- Prepare to start Routine "licztera" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('licztera.started', globalClock.getTime())
        BokTarget.setPos([xtrona,0])
        CentrumTest.setText(Centrum)
        BokTest.setPos([xtrona,0])
        BokTest.setText(Bok)
        KlawiszOdp.keys = []
        KlawiszOdp.rt = []
        _KlawiszOdp_allKeys = []
        # keep track of which components have finished
        liczteraComponents = [BokTarget, CentrumTarget, CentrumTest, BokTest, KlawiszOdp]
        for thisComponent in liczteraComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "licztera" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *BokTarget* updates
            
            # if BokTarget is starting this frame...
            if BokTarget.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                BokTarget.frameNStart = frameN  # exact frame index
                BokTarget.tStart = t  # local t and not account for scr refresh
                BokTarget.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BokTarget, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'BokTarget.started')
                # update status
                BokTarget.status = STARTED
                BokTarget.setAutoDraw(True)
            
            # if BokTarget is active this frame...
            if BokTarget.status == STARTED:
                # update params
                pass
            
            # if BokTarget is stopping this frame...
            if BokTarget.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > BokTarget.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    BokTarget.tStop = t  # not accounting for scr refresh
                    BokTarget.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'BokTarget.stopped')
                    # update status
                    BokTarget.status = FINISHED
                    BokTarget.setAutoDraw(False)
            
            # *CentrumTarget* updates
            
            # if CentrumTarget is starting this frame...
            if CentrumTarget.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                CentrumTarget.frameNStart = frameN  # exact frame index
                CentrumTarget.tStart = t  # local t and not account for scr refresh
                CentrumTarget.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CentrumTarget, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CentrumTarget.started')
                # update status
                CentrumTarget.status = STARTED
                CentrumTarget.setAutoDraw(True)
            
            # if CentrumTarget is active this frame...
            if CentrumTarget.status == STARTED:
                # update params
                pass
            
            # if CentrumTarget is stopping this frame...
            if CentrumTarget.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > CentrumTarget.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    CentrumTarget.tStop = t  # not accounting for scr refresh
                    CentrumTarget.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'CentrumTarget.stopped')
                    # update status
                    CentrumTarget.status = FINISHED
                    CentrumTarget.setAutoDraw(False)
            
            # *CentrumTest* updates
            
            # if CentrumTest is starting this frame...
            if CentrumTest.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                CentrumTest.frameNStart = frameN  # exact frame index
                CentrumTest.tStart = t  # local t and not account for scr refresh
                CentrumTest.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CentrumTest, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CentrumTest.started')
                # update status
                CentrumTest.status = STARTED
                CentrumTest.setAutoDraw(True)
            
            # if CentrumTest is active this frame...
            if CentrumTest.status == STARTED:
                # update params
                pass
            
            # *BokTest* updates
            
            # if BokTest is starting this frame...
            if BokTest.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                BokTest.frameNStart = frameN  # exact frame index
                BokTest.tStart = t  # local t and not account for scr refresh
                BokTest.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BokTest, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'BokTest.started')
                # update status
                BokTest.status = STARTED
                BokTest.setAutoDraw(True)
            
            # if BokTest is active this frame...
            if BokTest.status == STARTED:
                # update params
                pass
            
            # *KlawiszOdp* updates
            waitOnFlip = False
            
            # if KlawiszOdp is starting this frame...
            if KlawiszOdp.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                KlawiszOdp.frameNStart = frameN  # exact frame index
                KlawiszOdp.tStart = t  # local t and not account for scr refresh
                KlawiszOdp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(KlawiszOdp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KlawiszOdp.started')
                # update status
                KlawiszOdp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(KlawiszOdp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(KlawiszOdp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if KlawiszOdp.status == STARTED and not waitOnFlip:
                theseKeys = KlawiszOdp.getKeys(keyList=['w','s','up','down'], ignoreKeys=["escape"], waitRelease=False)
                _KlawiszOdp_allKeys.extend(theseKeys)
                if len(_KlawiszOdp_allKeys):
                    KlawiszOdp.keys = _KlawiszOdp_allKeys[-1].name  # just the last key pressed
                    KlawiszOdp.rt = _KlawiszOdp_allKeys[-1].rt
                    KlawiszOdp.duration = _KlawiszOdp_allKeys[-1].duration
                    # was this correct?
                    if (KlawiszOdp.keys == str(poprawna)) or (KlawiszOdp.keys == poprawna):
                        KlawiszOdp.corr = 1
                    else:
                        KlawiszOdp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in liczteraComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "licztera" ---
        for thisComponent in liczteraComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('licztera.stopped', globalClock.getTime())
        # check responses
        if KlawiszOdp.keys in ['', [], None]:  # No response was made
            KlawiszOdp.keys = None
            # was no response the correct answer?!
            if str(poprawna).lower() == 'none':
               KlawiszOdp.corr = 1;  # correct non-response
            else:
               KlawiszOdp.corr = 0;  # failed to respond (incorrectly)
        # store data for TNLA (TrialHandler)
        TNLA.addData('KlawiszOdp.keys',KlawiszOdp.keys)
        TNLA.addData('KlawiszOdp.corr', KlawiszOdp.corr)
        if KlawiszOdp.keys != None:  # we had a response
            TNLA.addData('KlawiszOdp.rt', KlawiszOdp.rt)
            TNLA.addData('KlawiszOdp.duration', KlawiszOdp.duration)
        # the Routine "licztera" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'TNLA'
    
    
    # set up handler to look after randomisation of conditions etc
    t3c = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TestNaX/Teksty.xlsx', selection='3'),
        seed=None, name='t3c')
    thisExp.addLoop(t3c)  # add the loop to the experiment
    thisT3c = t3c.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisT3c.rgb)
    if thisT3c != None:
        for paramName in thisT3c:
            globals()[paramName] = thisT3c[paramName]
    
    for thisT3c in t3c:
        currentLoop = t3c
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisT3c.rgb)
        if thisT3c != None:
            for paramName in thisT3c:
                globals()[paramName] = thisT3c[paramName]
        
        # --- Prepare to start Routine "blabla" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('blabla.started', globalClock.getTime())
        blaBlaInst.setText(eee)
        KoniecInst.keys = []
        KoniecInst.rt = []
        _KoniecInst_allKeys = []
        # keep track of which components have finished
        blablaComponents = [blaBlaInst, KoniecInst]
        for thisComponent in blablaComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blabla" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blaBlaInst* updates
            
            # if blaBlaInst is starting this frame...
            if blaBlaInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blaBlaInst.frameNStart = frameN  # exact frame index
                blaBlaInst.tStart = t  # local t and not account for scr refresh
                blaBlaInst.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blaBlaInst, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blaBlaInst.started')
                # update status
                blaBlaInst.status = STARTED
                blaBlaInst.setAutoDraw(True)
            
            # if blaBlaInst is active this frame...
            if blaBlaInst.status == STARTED:
                # update params
                pass
            
            # *KoniecInst* updates
            waitOnFlip = False
            
            # if KoniecInst is starting this frame...
            if KoniecInst.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                KoniecInst.frameNStart = frameN  # exact frame index
                KoniecInst.tStart = t  # local t and not account for scr refresh
                KoniecInst.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(KoniecInst, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KoniecInst.started')
                # update status
                KoniecInst.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(KoniecInst.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(KoniecInst.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if KoniecInst.status == STARTED and not waitOnFlip:
                theseKeys = KoniecInst.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
                _KoniecInst_allKeys.extend(theseKeys)
                if len(_KoniecInst_allKeys):
                    KoniecInst.keys = _KoniecInst_allKeys[-1].name  # just the last key pressed
                    KoniecInst.rt = _KoniecInst_allKeys[-1].rt
                    KoniecInst.duration = _KoniecInst_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blablaComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blabla" ---
        for thisComponent in blablaComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('blabla.stopped', globalClock.getTime())
        # check responses
        if KoniecInst.keys in ['', [], None]:  # No response was made
            KoniecInst.keys = None
        t3c.addData('KoniecInst.keys',KoniecInst.keys)
        if KoniecInst.keys != None:  # we had a response
            t3c.addData('KoniecInst.rt', KoniecInst.rt)
            t3c.addData('KoniecInst.duration', KoniecInst.duration)
        # the Routine "blabla" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 't3c'
    
    
    # set up handler to look after randomisation of conditions etc
    TNC = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TestNaX/TestNaC.xlsx', selection=wybieranieLiczb(WL1,WL2)),
        seed=None, name='TNC')
    thisExp.addLoop(TNC)  # add the loop to the experiment
    thisTNC = TNC.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTNC.rgb)
    if thisTNC != None:
        for paramName in thisTNC:
            globals()[paramName] = thisTNC[paramName]
    
    for thisTNC in TNC:
        currentLoop = TNC
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTNC.rgb)
        if thisTNC != None:
            for paramName in thisTNC:
                globals()[paramName] = thisTNC[paramName]
        
        # --- Prepare to start Routine "licztera" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('licztera.started', globalClock.getTime())
        BokTarget.setPos([xtrona,0])
        CentrumTest.setText(Centrum)
        BokTest.setPos([xtrona,0])
        BokTest.setText(Bok)
        KlawiszOdp.keys = []
        KlawiszOdp.rt = []
        _KlawiszOdp_allKeys = []
        # keep track of which components have finished
        liczteraComponents = [BokTarget, CentrumTarget, CentrumTest, BokTest, KlawiszOdp]
        for thisComponent in liczteraComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "licztera" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *BokTarget* updates
            
            # if BokTarget is starting this frame...
            if BokTarget.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                BokTarget.frameNStart = frameN  # exact frame index
                BokTarget.tStart = t  # local t and not account for scr refresh
                BokTarget.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BokTarget, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'BokTarget.started')
                # update status
                BokTarget.status = STARTED
                BokTarget.setAutoDraw(True)
            
            # if BokTarget is active this frame...
            if BokTarget.status == STARTED:
                # update params
                pass
            
            # if BokTarget is stopping this frame...
            if BokTarget.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > BokTarget.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    BokTarget.tStop = t  # not accounting for scr refresh
                    BokTarget.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'BokTarget.stopped')
                    # update status
                    BokTarget.status = FINISHED
                    BokTarget.setAutoDraw(False)
            
            # *CentrumTarget* updates
            
            # if CentrumTarget is starting this frame...
            if CentrumTarget.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                CentrumTarget.frameNStart = frameN  # exact frame index
                CentrumTarget.tStart = t  # local t and not account for scr refresh
                CentrumTarget.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CentrumTarget, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CentrumTarget.started')
                # update status
                CentrumTarget.status = STARTED
                CentrumTarget.setAutoDraw(True)
            
            # if CentrumTarget is active this frame...
            if CentrumTarget.status == STARTED:
                # update params
                pass
            
            # if CentrumTarget is stopping this frame...
            if CentrumTarget.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > CentrumTarget.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    CentrumTarget.tStop = t  # not accounting for scr refresh
                    CentrumTarget.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'CentrumTarget.stopped')
                    # update status
                    CentrumTarget.status = FINISHED
                    CentrumTarget.setAutoDraw(False)
            
            # *CentrumTest* updates
            
            # if CentrumTest is starting this frame...
            if CentrumTest.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                CentrumTest.frameNStart = frameN  # exact frame index
                CentrumTest.tStart = t  # local t and not account for scr refresh
                CentrumTest.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CentrumTest, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CentrumTest.started')
                # update status
                CentrumTest.status = STARTED
                CentrumTest.setAutoDraw(True)
            
            # if CentrumTest is active this frame...
            if CentrumTest.status == STARTED:
                # update params
                pass
            
            # *BokTest* updates
            
            # if BokTest is starting this frame...
            if BokTest.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                BokTest.frameNStart = frameN  # exact frame index
                BokTest.tStart = t  # local t and not account for scr refresh
                BokTest.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BokTest, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'BokTest.started')
                # update status
                BokTest.status = STARTED
                BokTest.setAutoDraw(True)
            
            # if BokTest is active this frame...
            if BokTest.status == STARTED:
                # update params
                pass
            
            # *KlawiszOdp* updates
            waitOnFlip = False
            
            # if KlawiszOdp is starting this frame...
            if KlawiszOdp.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                KlawiszOdp.frameNStart = frameN  # exact frame index
                KlawiszOdp.tStart = t  # local t and not account for scr refresh
                KlawiszOdp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(KlawiszOdp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KlawiszOdp.started')
                # update status
                KlawiszOdp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(KlawiszOdp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(KlawiszOdp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if KlawiszOdp.status == STARTED and not waitOnFlip:
                theseKeys = KlawiszOdp.getKeys(keyList=['w','s','up','down'], ignoreKeys=["escape"], waitRelease=False)
                _KlawiszOdp_allKeys.extend(theseKeys)
                if len(_KlawiszOdp_allKeys):
                    KlawiszOdp.keys = _KlawiszOdp_allKeys[-1].name  # just the last key pressed
                    KlawiszOdp.rt = _KlawiszOdp_allKeys[-1].rt
                    KlawiszOdp.duration = _KlawiszOdp_allKeys[-1].duration
                    # was this correct?
                    if (KlawiszOdp.keys == str(poprawna)) or (KlawiszOdp.keys == poprawna):
                        KlawiszOdp.corr = 1
                    else:
                        KlawiszOdp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in liczteraComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "licztera" ---
        for thisComponent in liczteraComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('licztera.stopped', globalClock.getTime())
        # check responses
        if KlawiszOdp.keys in ['', [], None]:  # No response was made
            KlawiszOdp.keys = None
            # was no response the correct answer?!
            if str(poprawna).lower() == 'none':
               KlawiszOdp.corr = 1;  # correct non-response
            else:
               KlawiszOdp.corr = 0;  # failed to respond (incorrectly)
        # store data for TNC (TrialHandler)
        TNC.addData('KlawiszOdp.keys',KlawiszOdp.keys)
        TNC.addData('KlawiszOdp.corr', KlawiszOdp.corr)
        if KlawiszOdp.keys != None:  # we had a response
            TNC.addData('KlawiszOdp.rt', KlawiszOdp.rt)
            TNC.addData('KlawiszOdp.duration', KlawiszOdp.duration)
        # the Routine "licztera" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'TNC'
    
    
    # set up handler to look after randomisation of conditions etc
    t4b = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TestNaX/Teksty.xlsx', selection='4'),
        seed=None, name='t4b')
    thisExp.addLoop(t4b)  # add the loop to the experiment
    thisT4b = t4b.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisT4b.rgb)
    if thisT4b != None:
        for paramName in thisT4b:
            globals()[paramName] = thisT4b[paramName]
    
    for thisT4b in t4b:
        currentLoop = t4b
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisT4b.rgb)
        if thisT4b != None:
            for paramName in thisT4b:
                globals()[paramName] = thisT4b[paramName]
        
        # --- Prepare to start Routine "blabla" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('blabla.started', globalClock.getTime())
        blaBlaInst.setText(eee)
        KoniecInst.keys = []
        KoniecInst.rt = []
        _KoniecInst_allKeys = []
        # keep track of which components have finished
        blablaComponents = [blaBlaInst, KoniecInst]
        for thisComponent in blablaComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blabla" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blaBlaInst* updates
            
            # if blaBlaInst is starting this frame...
            if blaBlaInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blaBlaInst.frameNStart = frameN  # exact frame index
                blaBlaInst.tStart = t  # local t and not account for scr refresh
                blaBlaInst.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blaBlaInst, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blaBlaInst.started')
                # update status
                blaBlaInst.status = STARTED
                blaBlaInst.setAutoDraw(True)
            
            # if blaBlaInst is active this frame...
            if blaBlaInst.status == STARTED:
                # update params
                pass
            
            # *KoniecInst* updates
            waitOnFlip = False
            
            # if KoniecInst is starting this frame...
            if KoniecInst.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                KoniecInst.frameNStart = frameN  # exact frame index
                KoniecInst.tStart = t  # local t and not account for scr refresh
                KoniecInst.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(KoniecInst, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KoniecInst.started')
                # update status
                KoniecInst.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(KoniecInst.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(KoniecInst.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if KoniecInst.status == STARTED and not waitOnFlip:
                theseKeys = KoniecInst.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
                _KoniecInst_allKeys.extend(theseKeys)
                if len(_KoniecInst_allKeys):
                    KoniecInst.keys = _KoniecInst_allKeys[-1].name  # just the last key pressed
                    KoniecInst.rt = _KoniecInst_allKeys[-1].rt
                    KoniecInst.duration = _KoniecInst_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blablaComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blabla" ---
        for thisComponent in blablaComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('blabla.stopped', globalClock.getTime())
        # check responses
        if KoniecInst.keys in ['', [], None]:  # No response was made
            KoniecInst.keys = None
        t4b.addData('KoniecInst.keys',KoniecInst.keys)
        if KoniecInst.keys != None:  # we had a response
            t4b.addData('KoniecInst.rt', KoniecInst.rt)
            t4b.addData('KoniecInst.duration', KoniecInst.duration)
        # the Routine "blabla" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 't4b'
    
    
    # set up handler to look after randomisation of conditions etc
    TNLB = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TestNaX/TestNaLiteryB.xlsx',selection=wybieranieLiczb(Wi1,Wi2)),
        seed=None, name='TNLB')
    thisExp.addLoop(TNLB)  # add the loop to the experiment
    thisTNLB = TNLB.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTNLB.rgb)
    if thisTNLB != None:
        for paramName in thisTNLB:
            globals()[paramName] = thisTNLB[paramName]
    
    for thisTNLB in TNLB:
        currentLoop = TNLB
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTNLB.rgb)
        if thisTNLB != None:
            for paramName in thisTNLB:
                globals()[paramName] = thisTNLB[paramName]
        
        # --- Prepare to start Routine "licztera" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('licztera.started', globalClock.getTime())
        BokTarget.setPos([xtrona,0])
        CentrumTest.setText(Centrum)
        BokTest.setPos([xtrona,0])
        BokTest.setText(Bok)
        KlawiszOdp.keys = []
        KlawiszOdp.rt = []
        _KlawiszOdp_allKeys = []
        # keep track of which components have finished
        liczteraComponents = [BokTarget, CentrumTarget, CentrumTest, BokTest, KlawiszOdp]
        for thisComponent in liczteraComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "licztera" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *BokTarget* updates
            
            # if BokTarget is starting this frame...
            if BokTarget.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                BokTarget.frameNStart = frameN  # exact frame index
                BokTarget.tStart = t  # local t and not account for scr refresh
                BokTarget.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BokTarget, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'BokTarget.started')
                # update status
                BokTarget.status = STARTED
                BokTarget.setAutoDraw(True)
            
            # if BokTarget is active this frame...
            if BokTarget.status == STARTED:
                # update params
                pass
            
            # if BokTarget is stopping this frame...
            if BokTarget.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > BokTarget.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    BokTarget.tStop = t  # not accounting for scr refresh
                    BokTarget.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'BokTarget.stopped')
                    # update status
                    BokTarget.status = FINISHED
                    BokTarget.setAutoDraw(False)
            
            # *CentrumTarget* updates
            
            # if CentrumTarget is starting this frame...
            if CentrumTarget.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                CentrumTarget.frameNStart = frameN  # exact frame index
                CentrumTarget.tStart = t  # local t and not account for scr refresh
                CentrumTarget.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CentrumTarget, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CentrumTarget.started')
                # update status
                CentrumTarget.status = STARTED
                CentrumTarget.setAutoDraw(True)
            
            # if CentrumTarget is active this frame...
            if CentrumTarget.status == STARTED:
                # update params
                pass
            
            # if CentrumTarget is stopping this frame...
            if CentrumTarget.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > CentrumTarget.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    CentrumTarget.tStop = t  # not accounting for scr refresh
                    CentrumTarget.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'CentrumTarget.stopped')
                    # update status
                    CentrumTarget.status = FINISHED
                    CentrumTarget.setAutoDraw(False)
            
            # *CentrumTest* updates
            
            # if CentrumTest is starting this frame...
            if CentrumTest.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                CentrumTest.frameNStart = frameN  # exact frame index
                CentrumTest.tStart = t  # local t and not account for scr refresh
                CentrumTest.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CentrumTest, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CentrumTest.started')
                # update status
                CentrumTest.status = STARTED
                CentrumTest.setAutoDraw(True)
            
            # if CentrumTest is active this frame...
            if CentrumTest.status == STARTED:
                # update params
                pass
            
            # *BokTest* updates
            
            # if BokTest is starting this frame...
            if BokTest.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                BokTest.frameNStart = frameN  # exact frame index
                BokTest.tStart = t  # local t and not account for scr refresh
                BokTest.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BokTest, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'BokTest.started')
                # update status
                BokTest.status = STARTED
                BokTest.setAutoDraw(True)
            
            # if BokTest is active this frame...
            if BokTest.status == STARTED:
                # update params
                pass
            
            # *KlawiszOdp* updates
            waitOnFlip = False
            
            # if KlawiszOdp is starting this frame...
            if KlawiszOdp.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                KlawiszOdp.frameNStart = frameN  # exact frame index
                KlawiszOdp.tStart = t  # local t and not account for scr refresh
                KlawiszOdp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(KlawiszOdp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KlawiszOdp.started')
                # update status
                KlawiszOdp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(KlawiszOdp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(KlawiszOdp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if KlawiszOdp.status == STARTED and not waitOnFlip:
                theseKeys = KlawiszOdp.getKeys(keyList=['w','s','up','down'], ignoreKeys=["escape"], waitRelease=False)
                _KlawiszOdp_allKeys.extend(theseKeys)
                if len(_KlawiszOdp_allKeys):
                    KlawiszOdp.keys = _KlawiszOdp_allKeys[-1].name  # just the last key pressed
                    KlawiszOdp.rt = _KlawiszOdp_allKeys[-1].rt
                    KlawiszOdp.duration = _KlawiszOdp_allKeys[-1].duration
                    # was this correct?
                    if (KlawiszOdp.keys == str(poprawna)) or (KlawiszOdp.keys == poprawna):
                        KlawiszOdp.corr = 1
                    else:
                        KlawiszOdp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in liczteraComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "licztera" ---
        for thisComponent in liczteraComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('licztera.stopped', globalClock.getTime())
        # check responses
        if KlawiszOdp.keys in ['', [], None]:  # No response was made
            KlawiszOdp.keys = None
            # was no response the correct answer?!
            if str(poprawna).lower() == 'none':
               KlawiszOdp.corr = 1;  # correct non-response
            else:
               KlawiszOdp.corr = 0;  # failed to respond (incorrectly)
        # store data for TNLB (TrialHandler)
        TNLB.addData('KlawiszOdp.keys',KlawiszOdp.keys)
        TNLB.addData('KlawiszOdp.corr', KlawiszOdp.corr)
        if KlawiszOdp.keys != None:  # we had a response
            TNLB.addData('KlawiszOdp.rt', KlawiszOdp.rt)
            TNLB.addData('KlawiszOdp.duration', KlawiszOdp.duration)
        # the Routine "licztera" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'TNLB'
    
    
    # --- Prepare to start Routine "koniec" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('koniec.started', globalClock.getTime())
    KlawiszKoniec.keys = []
    KlawiszKoniec.rt = []
    _KlawiszKoniec_allKeys = []
    # keep track of which components have finished
    koniecComponents = [TekstKoncowy, KlawiszKoniec]
    for thisComponent in koniecComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "koniec" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TekstKoncowy* updates
        
        # if TekstKoncowy is starting this frame...
        if TekstKoncowy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TekstKoncowy.frameNStart = frameN  # exact frame index
            TekstKoncowy.tStart = t  # local t and not account for scr refresh
            TekstKoncowy.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TekstKoncowy, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TekstKoncowy.started')
            # update status
            TekstKoncowy.status = STARTED
            TekstKoncowy.setAutoDraw(True)
        
        # if TekstKoncowy is active this frame...
        if TekstKoncowy.status == STARTED:
            # update params
            pass
        
        # *KlawiszKoniec* updates
        waitOnFlip = False
        
        # if KlawiszKoniec is starting this frame...
        if KlawiszKoniec.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            KlawiszKoniec.frameNStart = frameN  # exact frame index
            KlawiszKoniec.tStart = t  # local t and not account for scr refresh
            KlawiszKoniec.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(KlawiszKoniec, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'KlawiszKoniec.started')
            # update status
            KlawiszKoniec.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(KlawiszKoniec.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(KlawiszKoniec.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if KlawiszKoniec.status == STARTED and not waitOnFlip:
            theseKeys = KlawiszKoniec.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
            _KlawiszKoniec_allKeys.extend(theseKeys)
            if len(_KlawiszKoniec_allKeys):
                KlawiszKoniec.keys = _KlawiszKoniec_allKeys[-1].name  # just the last key pressed
                KlawiszKoniec.rt = _KlawiszKoniec_allKeys[-1].rt
                KlawiszKoniec.duration = _KlawiszKoniec_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in koniecComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "koniec" ---
    for thisComponent in koniecComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('koniec.stopped', globalClock.getTime())
    # check responses
    if KlawiszKoniec.keys in ['', [], None]:  # No response was made
        KlawiszKoniec.keys = None
    thisExp.addData('KlawiszKoniec.keys',KlawiszKoniec.keys)
    if KlawiszKoniec.keys != None:  # we had a response
        thisExp.addData('KlawiszKoniec.rt', KlawiszKoniec.rt)
        thisExp.addData('KlawiszKoniec.duration', KlawiszKoniec.duration)
    thisExp.nextEntry()
    # the Routine "koniec" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
