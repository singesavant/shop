from django.http import HttpRequest
from django.contrib.auth.models import AnonymousUser

from oscar.apps.order import processing
from oscar.apps.checkout import mixins


class EventHandler(processing.EventHandler, mixins.OrderPlacementMixin):
    def handle_order_status_change(self, order, new_status, note_msg=None):
        super(EventHandler, self).handle_order_status_change(order, new_status, note_msg)

        self.request = HttpRequest()
        self.request.user = order.user or AnonymousUser()


        self.send_confirmation_message(order, "ORDER_STATUS_CHANGE_{0}".format(new_status))


