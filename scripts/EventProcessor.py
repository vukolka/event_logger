import rospy
import threading
from ReportLogger import *
from logger.msg import *
import logger as lg
from EventDispatcher import event_list

class EventProcessor():
    """ Event processing class. 
        Creates subscribers for the given topics and processes incoming events
    """

    def __init__(self, rate=10, file_name='ros_event_log.csv'):
        """ init logger application """

        #configurable rate
        self._rate = rate

        # used for logging recieved data
        self._logger = ReportLogger(file_name)
        
        # holds the last event we got from subscribers
        self._recent_event = None
        self._lock = threading.Lock()
        
        self._init_subs()

    def enable_std_output(self, flag):
        """ If set to True - logs both to console and to a file
            Args:
                flag(bool)
        """
        
        self._logger.std_output = flag

    def _init_subs(self):
        """ Registers subscribers for the given topics """
        for event_type in event_list:
            event_class = getattr(lg.msg, event_type)
            sub = rospy.Subscriber(event_type, event_class, self._call_back, queue_size=1)
        rospy.sleep(1)
    
    def _get_recent_event(self):
        """ takes the most recent event and clears the stack(in real world it would)
            Returns:
                data(logger.msg.*) Recieved event or None if empty
        """
        # a lock for self._recent_event
        with self._lock:
            data = self._recent_event
            self._recent_event = None
        return data


    def _call_back(self, data):
        """ Callback function for all the Subscribers. Puts recived event onto a stack """
        #store recent event
        with self._lock:
            self._recent_event = data

    def start(self):
        """ Main loop which with a given rate checks for a recent event and 
        asks logger to write gather data to a file

        """
        loop_rate = rospy.Rate(self._rate)

        while not rospy.is_shutdown():
            event = self._get_recent_event()
            self._logger.log_event(event)

            loop_rate.sleep()

