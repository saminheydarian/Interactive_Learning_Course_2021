class Message:
    def __init__(self, sender_id, receiver_id, content):
        if sender_id is None or receiver_id is None or content is None:
            raise('Some arguments of message constructor are not provided.')
        if type(sender_id) != str or type(receiver_id) != str:
            raise('sender_id and receiver_id must be strings')
            
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.content = content

    def __str__(self):
        return 'from: {},\tto: {},\tcontent: {}'.format(self.sender_id, self.receiver_id, self.content)