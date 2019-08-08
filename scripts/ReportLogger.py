from EventDispatcher import event_props
from EventDispatcher import event_list
import rospy

class ReportLogger:
    """Class for formating and writing events to files"""

    def __init__(self, file_path):
        """ initialize log writer """
        self._file_path = file_path
        self._log_msg = ''

    def log_event(self, event):
        """ Dispatch all event's properties and store to a file 
            Args:
                event(logger.msg.*): Event with a base type of Event

        """
        if event is None:
            self._log ('Missed status report event')
        else:
            self._log_base_event(event.base)
            attrs = event_props[str(event.base.type)]
            for attr in attrs:
                log_method = getattr(self, '_log_' + attr)
                log_method(event)
        self._dump()

    def _log_base_event(self, msg):
        """ Put common information of an event to a file
            Args:
                msg(logger.msg.Event) Base class of an event

        """
        self._log('id: ' + str(msg.header.seq))
        self._log('type: ' + event_list[msg.type])
        self._log('name: ' + msg.name)
        self._log('severity: ' + str(msg.severity))
    
    def _log_gps_data(self, msg):
        """ Put GPS data to a file
            Args:
                msg(logger.msg.*) Base class of an event

        """
        msg = msg.gps_data
        self._log ('GPS: lat=%f, lon=%f, alt=%f' % (msg.latitude, msg.longitude, msg.altitude))

    def _log_battery(self, msg):
        """ Put battery data to a file
            Args:
                msg(logger.msg.*) Base class of an event

        """
        self._log ('battery: vol=%f, amp=%f' % (msg.battery.voltage, msg.battery.amperage)) 
        
    def _log_mision_id(self, msg):
        """ Put mistion id to a file
            Args:
                msg(logger.msg.*) Base class of an event

        """
        self._log ('mision_id: %d' % msg.mision_id)
    
    def _log(self, log_str):
        if self._log_msg:
            self._log_msg += '\n'
        self._log_msg += log_str

    def _dump(self):
        """ Put mistion id to a file
            Args:
                msg(logger.msg.*) Base class of an event

        """
        rospy.loginfo(self._log_msg + '\n')
        with open(self._file_path, 'a+') as f:
            f.write(self._log_msg)
        self._log_msg = ''
