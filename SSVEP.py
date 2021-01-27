

from psychopy import visual, core, event
#import csv_collector
from numpy import pi, sin, repeat
from random import shuffle

class SSVEP(object):
    #init sets the window(mywin), and the frequency of the flashing(frame_on, frame_off)
    #Frame duration in seconds = 1/monitorframerate(in Hz)
    #Thus the fastest frame rate could be 1 frame on 1 frame off
    #which equals 2/60 == 30Hz
    #Flash frequency = refreshrate/(frame_on+frame_off)
    
    def __init__(self, mywin=visual.Window([900, 700], fullscr=False, monitor='testMonitor', units='deg'),
                freq=[8], trialdur = 2.0, port='/dev/tty.usbserial-DM00D5SD',
                fname='SSVEP.csv', numtrials=1, waitdur=2):
        self.mywin = mywin
        self.trialdur = trialdur
        self.fname = fname
        self.numtrials = numtrials
        self.waitdur = waitdur
        self.port = port
        self.freq = freq

        if len(freq) == 1:  # TO DO: upon initialization, prepare the positions for each target (determined by number of freq)
            self.targets = [visual.GratingStim(win=self.mywin, name='pattern1', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[0, 0], size=10, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True)]
        elif len(freq) == 2:
            self.targets = [visual.GratingStim(win=self.mywin, name='pattern1', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[-5, 0], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True),
                             visual.GratingStim(win=self.mywin, name='pattern2', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[5, 0], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0)]
        elif len(freq) == 3:
            self.targets = [visual.GratingStim(win=self.mywin, name='pattern1', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[-10, 0], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern2', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[0, 0], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern3', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[10, 0], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0)]
        elif len(freq) == 4:
            self.targets = [visual.GratingStim(win=self.mywin, name='pattern1', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[0, 7], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern2', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[-10, 0], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern3', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[10, 0], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern4', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[0, -7], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0)]
        elif len(freq) == 5:
            self.targets = [visual.GratingStim(win=self.mywin, name='pattern1', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[0, 7], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern2', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[-10, 0], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern3', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[0, 0], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern4', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[10, 0], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern5', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[0, -7], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0)]
        elif len(freq) == 6:
            self.targets = [visual.GratingStim(win=self.mywin, name='pattern1', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[-5, 7], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern2', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[5, 7], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern3', units='cm',
                                                tex=None, mask=None,
                                                ori=0, pos=[-10, 0], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern4', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[10, 0], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern5', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[-5, -7], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern6', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[5, -7], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0)]
        elif len(freq) == 7:
            self.targets = [visual.GratingStim(win=self.mywin, name='pattern1', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[-5, 7], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern2', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[5, 7], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern3', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[-10, 0], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern4', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[0, 0], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern5', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[10, 0], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern6', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[-5, -7], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern7', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[5, -7], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0)]
        elif len(freq) == 8:
            self.targets = [visual.GratingStim(win=self.mywin, name='pattern1', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[-10, 7], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern2', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[0, 7], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern3', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[10, 7], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern4', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[-10, 0], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern5', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[10, 0], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern6', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[-10, -7], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern7', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[0, -7], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern8', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[10, -7], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0)]
        else:
            self.targets = [visual.GratingStim(win=self.mywin, name='pattern1', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[-10, 7], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern2', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[0, 7], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern3', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[10, 7], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern4', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[-10, 0], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern5', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[0, 0], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern6', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[10, 0], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern7', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[-10, -7], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern8', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[0, -7], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0),
                             visual.GratingStim(win=self.mywin, name='pattern9', units='cm',
                                                tex=None, mask='circle',
                                                ori=0, pos=[10, -7], size=5, sf=1, phase=0.0,
                                                color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                                texRes=256, interpolate=True, depth=-1.0)]

    def collecting(self):
        print('sp: initializing collector')
        self.collector = csv_collector.CSVCollector(fname=self.fname, port=self.port)
        self.collector.start()

    def epoch(self, mark):
        self.collector.tag(mark)

    def stop(self):
        self.mywin.close()
        core.quit()
        
   
    def start(self):

        # TO DO: have this object be managed by threading because it's clogging up BLE communication

        print('Generating drawing thread for stimuli presentation...')
        #self.bg_thread = threading.Thread(group=None, target=self.collector.start,
        #                                  args=(self.receive_sample,))
        print('sp: starting SSVEP session...')
        # possibly convert trialdur into frames given refresh rate (normally set at 60Hz)
        self.framerate = self.mywin.getActualFrameRate()
        # divison here makes it tricky
        self.trialframes = self.trialdur / 60
        self.count = 0

        omega = []
        for element in self.freq:
            omega.append(2 * pi * element)  # generate horizontal transformations for sin wave sampling

        order = repeat(range(0, len(omega)), self.numtrials)
        shuffle(order)  # create a list of classes to test at

        ###Testing framerate grabber###
        print(self.mywin.getActualFrameRate())
        self.Trialclock = core.Clock()
        #self.collecting()  # start saving data from EEG device

        while self.count < self.numtrials*len(self.freq):  # within each trial...

            #self.epoch(0)  # reset tagging
            # to do: randomly select class to watch and highlight that class
            classid = order[self.count]
            for i in range(0, len(omega)):
                self.targets[i].color = [-1, -1, -1]
                self.targets[i].setAutoDraw(True)
            self.targets[classid].color = [1, 0, -1]
            self.mywin.flip()
            core.wait(2)  # wait 2s for next trial begin (prepare period)
            self.Trialclock.reset()  # reset clock for next trial



            # also set fixate object on top of class so user knows which one to look at
            ''' Block executed during trial '''
            while self.Trialclock.getTime() < self.trialdur:

                # manages target flashing rates and epoch tagging during trial
                for i in range(0, len(omega)):
                    value = sin(omega[i]*self.Trialclock.getTime())  # sample the sin wave at the current time
                    if value >= 0:
                        self.targets[i].color = [1, 1, 1]
                    else:
                        self.targets[i].color = [-1, -1, -1]
                    self.targets[i].setAutoDraw(True)
                self.mywin.flip()
                #self.epoch(self.freq[classid])

            ''' Block executed at end of trial'''
            #self.epoch(0)

            for target in self.targets:
                # target.color = [-1, -1, -1]  # reset all targets to black
                target.setAutoDraw(False)
            self.mywin.flip()

            core.wait(self.waitdur)  # wait certain time for next trial (rest period)
            self.count += 1  # count number of trials


        #self.collector.disconnect()
        self.stop()


  
"""
Here are some test cases 
Just run this program by itself if you don't want to use run.py

"""

if __name__ == '__main__':
    stimulitest = SSVEP(freq=[8, 11, 13, 10], numtrials=2)
    stimulitest.start()

   



