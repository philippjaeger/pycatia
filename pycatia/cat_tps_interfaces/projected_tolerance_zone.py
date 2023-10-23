#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class ProjectedToleranceZone(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ProjectedToleranceZone
                | 
                | Interface for accessing projected tolerance zone informations of a
                | TPS.
                | ========| Position Length / |<----------->|<----------->| Toleranced | | |
                | Surface - - - +-------> +=============+ \ |\ \ \ \ | Origin Direction Projected
                | Tolerance Zone ========
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.projected_tolerance_zone = com_object

    @property
    def length(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Length() As double (Read Only)
                | 
                |     Retrieves length of the projected tolerance zone (in millimeters). The
                |     length defines the ending point of the tolerance zone. This point can be
                |     computed by using Origin and Direction of the axis.

        :rtype: float
        """

        return self.projected_tolerance_zone.Length

    @property
    def position(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Position() As double (Read Only)
                | 
                |     Retrieves position of the projected tolerance zone (in millimeters). The
                |     position defines the starting point of the tolerance zone. This point can be
                |     computed by using Origin and Direction of the axis.

        :rtype: float
        """

        return self.projected_tolerance_zone.Position

    def get_projected_tol_zone_reference(self, op_reference: tuple) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetProjectedTolZoneReference(CATSafeArrayVariant
                | opReference)
                | 
                |     Retrieves reference axis of the projected tolerance zone. The returned
                |     point and vector define a axis system that is used to defined the 3D position
                |     of the tolerance zone.
                | 
                |     Parameters:
                | 
                |         opReference
                |             The first 3 values of opReference correspond to the X,Y and Z
                |             values of the origin point respectively and the next 3 values correspond to the
                |             X,Y and Z values of the direction respectively. 
                | 
                |     Example:
                | 
                |           This example gets the Projected Tolerance Zone reference in a VB
                |           Script
                |          Dim oTab(6) As CATSafeArrayVariant
                |          Set projTol = annotation.ProjectedToleranceZone
                |           projTol.GetProjectedTolZoneReference(oTab)
                |           oStream.Write "Projected Tol Zone Reference Point : " & oTab(0) & " " & oTab(1) & " " & oTab(2) & sLF
                |           oStream.Write "Projected Tol Zone Reference Vector : " & oTab(3) & " " & oTab(4) & " " & oTab(5) & sLF

        :param tuple op_reference:
        :rtype: tuple
        """
        return self.projected_tolerance_zone.GetProjectedTolZoneReference(op_reference)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_projected_tol_zone_reference'
        # # vba_code = """
        # # Public Function get_projected_tol_zone_reference(projected_tolerance_zone)
        # #     Dim opReference (2)
        # #     projected_tolerance_zone.GetProjectedTolZoneReference opReference
        # #     get_projected_tol_zone_reference = opReference
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ProjectedToleranceZone(name="{ self.name }")'
