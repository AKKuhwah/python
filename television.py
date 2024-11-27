class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self):
        """
        Start new Television object with default values
        - Status off(False)
        - Mute off(False)
        - Volume is at the minimum value of 0
        - Channel is set to the minimum value of 0
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        """
        Switches the power status of the Object on or off

        No parameters.
        No return value.
        """
        self.__status = not self.__status

    def mute(self):
        """
        Switches the mute status of the TV from unumute to mute and vice-versa

        No parameters.
        No return value.
        """
        if self.__status == True:
            self.__muted = not self.__muted

    def channel_up(self):
        """
        Increases channel by 1
        If channel is at maximum, it goes to the minimum channel of 0.

        No parameters.
        No return value.
        """
        if self.__status == True:
            if self.__channel < self.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self):
        """
        Decreases channel by 1
        If channel is at minimum, it goes to the maximum channel of 3.

        No parameters.
        No return value.
        """
        if self.__status == True:
            if self.__channel > self.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self):
        """
        Increases the volume by 1
        If volume at maximum, it no longers increase.
        Mute is turned off(False) when the volume increases.

        No parameters.
        No return value.
        """
        if self.__status == True:
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1
            self.__muted = False


    def volume_down(self):
        """
        Decreases the volume by 1
        If volume at minimum, it no longers decrease.
        Mute is turned off(False) when the volume decreases.

        No parameters.
        No return value.
        """
        if self.__status == True:
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1
            self.__muted = False

    def __str__(self):
        """
       Returns a string of the television status, channel, and volume

       Returns:
       str: A string showing the television current power status, channel, and volume (muted volume is shown as 0).
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {0 if self.__muted == True else self.__volume}'
