import math


class PositionInitializer:

    def __init__(self):

        # ==========================================
        # Reference Origin
        # ==========================================

        self.lat0 = None
        self.lon0 = None
        self.alt0 = None

        # ==========================================
        # Local NED Position
        # ==========================================

        self.pn = 0.0
        self.pe = 0.0
        self.pd = 0.0

        # ==========================================
        # Initialization Flag
        # ==========================================

        self.initialized = False

    # ==================================================
    # INITIALIZE FROM PX4 NAVIGATION
    # ==================================================

    def initialize_position(self, nav_gps):

        self.lat0 = nav_gps.lat

        self.lon0 = nav_gps.lon

        self.alt0 = nav_gps.alt

        # Initial NED position starts at origin

        self.pn = 0.0
        self.pe = 0.0
        self.pd = 0.0

        self.initialized = True

        print("\\n==============================")
        print("POSITION INITIALIZED")
        print("==============================")

        print(f"LAT0 : {self.lat0:.7f}")

        print(f"LON0 : {self.lon0:.7f}")

        print(f"ALT0 : {self.alt0:.2f} m")

    # ==================================================
    # NED → GEODETIC
    # ==================================================

    def ned_to_geodetic(self):

        if not self.initialized:

            return None, None, None

        earth_radius = 6378137.0

        lat = self.lat0 + math.degrees(
            self.pn / earth_radius
        )

        lon = self.lon0 + math.degrees(
            self.pe / (
                earth_radius *
                math.cos(math.radians(self.lat0))
            )
        )

        alt = self.alt0 - self.pd

        return lat, lon, alt