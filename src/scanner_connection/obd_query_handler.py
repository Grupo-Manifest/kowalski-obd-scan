import obd
from obd import OBDStatus

from .obd_connection import OBDConnection

class OBDQueryHandler():
    """Handles the queries to the OBD scanner and parses its responses"""
    # TODO proper error handling on connection or response failure
    
    def __init__(self):
        """Instantiates the OBD connection handler"""
        self._connection = OBDConnection().connection


    def get_engine_rpm(self):
        """
        Retrieves the current engine revolutions per minute from the scanner.
        Returns:
            float: Current vehicle engine rpm, or None if the query is unsuccessful.
        """
        command = obd.commands.RPM
        response = self._query_obd_property(command)

        return response


    def get_speed(self) -> float:
        """
        Retrieves the current vehicle speed from the scanner.
        Returns:
            float: Current vehicle speed in km/h, or None if the query is unsuccessful.
        """
        command = obd.commands.SPEED
        response = self._query_obd_property(command)

        return response

    
    def get_accelerator_position(self) -> float:
        """
        Retrieves the relative accelerator pedal position from the scanner.
        Returns:
            float: Relative accelerator pedal position percentage, or None if the query is unsuccessful.
        """
        command = obd.commands.RELATIVE_ACCEL_POS
        response = self._query_obd_property(command)

        return response


    def get_coolant_temperature(self):
        """
        Retrieves the current vehicle coolant temperature from the scanner.
        Returns:
            float: Current vehicle coolant temperature in ºC, or None if the query is unsuccessful.
        """
        command = obd.commands.COOLANT_TEMP
        response = self._query_obd_property(command)

        return response


    def get_fuel_level(self):
        """
        Retrieves the current vehicle fuel level from the scanner.
        Returns:
            float: Current vehicle fuel level percentage, or None if the query is unsuccessful.
        """
        command = obd.commands.FUEL_LEVEL
        response = self._query_obd_property(command)

        return response


    def get_fuel_pressure(self):
        """
        Retrieves the current vehicle fuel pressure from the scanner.
        Returns:
            float: Current vehicle fuel pressure in kPa, or None if the query is unsuccessful.
        """
        command = obd.commands.FUEL_PRESSURE
        response = self._query_obd_property(command)

        return response


    def get_engine_load(self):
        """
        Retrieves the current vehicle engine load from the scanner.
        Returns:
            float: Current vehicle engine load percentage, or None if the query is unsuccessful.
        """
        command = obd.commands.ENGINE_LOAD
        response = self._query_obd_property(command)

        return response


    def _query_obd_property(self, command):
        """
        Helper method to query an OBD property and return the response value if successful.
        Args:
            command (obd.commands.ObdCommand): OBD command to query.

        Returns:
            Any: Response value if successful, otherwise None.
        """
        if self._connection.is_connected():
            response = self._connection.query(command)

            if response.is_successful():
                return response.value

            return None # TODO
        return None # TODO
