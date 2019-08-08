import rospy
import random
import string
import logger as lg
from logger.msg import *
from EventDispatcher import event_list


class EventPublisher():
    """ Class creates a separate publisher for every Event type and when asked publishes a random message
    """
    def __init__(self):
        """ Initialize and register Publishers """
        self._seq_counter = 0
        self._pub_list = []
        for event_type in event_list:
            event_class = getattr(lg.msg, event_type)
            sub = rospy.Publisher(event_type, event_class, queue_size=1)
            self._pub_list.append(sub)

    def _generate_msg(self, event_id):
        """ Given the id of event - generates corresponding message from event_list
            Args:
                event_id(int) id of and event from event_list
            Returns:
                msg(logger.msg.*) an instance of Event from the given id

        """
        event_class = getattr(lg.msg, event_list[event_id])
        msg = event_class()
        msg.base.header.stamp = rospy.Time.now()
        msg.base.header.seq = self._seq_counter
        self._seq_counter += 1
        msg.base.type = event_id
        letters = string.ascii_lowercase
        msg.base.name = ''.join(random.choice(letters) for i in range(10))
        msg.base.severity = random.randint(0,5)
        return msg

    def publish_random_msg(self, timer):
        """ generates a random Event msg and publishes on corresponding topic
            Args:
                timer(rospy.Time.timer) timer obj

        """
        event_id = random.randint(0, len(event_list) - 1)
        msg = self._generate_msg(event_id) 
        self._pub_list[event_id].publish(msg)
        print event_list[event_id]
