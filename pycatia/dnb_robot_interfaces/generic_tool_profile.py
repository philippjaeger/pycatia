#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_robot_interfaces.rob_generic_controller import RobGenericController
from pycatia.system_interfaces.any_object import AnyObject


class GenericToolProfile(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     GenericToolProfile
                | 
                | Interface to manage Generic Tool Profile of Robot controller.
                | 
                | Role: This interface provides methods to get/set data related to Tool
                | Profile.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.generic_tool_profile = com_object

    def get_centroid(self, cx: float, cy: float, cz: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetCentroid(double cx,
                | double cy,
                | double cz)
                | 
                |     Retrieve the underlying x,y,z of the Tool centroid.
                | 
                |     Parameters:
                | 
                |         cx,
                |             The out parameter contains X Coordinate of the Tool centroid.
                |             
                |         cy,
                |             The out parameter contains Y Coordinate of the Tool centroid.
                |             
                |         cz,
                |             The out parameter contains Z Coordinate of the Tool centroid.
                |             
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float cx:
        :param float cy:
        :param float cz:
        :return: None
        :rtype: None
        """
        return self.generic_tool_profile.GetCentroid(cx, cy, cz)

    def get_controller(self, o_controller: RobGenericController) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetController(RobGenericController oController)
                | 
                |     Retrieves controller owning the profile.
                | 
                |     Parameters:
                | 
                |         oController
                |             This parameter contains pointer to controller. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param RobGenericController o_controller:
        :return: None
        :rtype: None
        """
        return self.generic_tool_profile.GetController(o_controller.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_controller'
        # # vba_code = """
        # # Public Function get_controller(generic_tool_profile)
        # #     Dim oController (2)
        # #     generic_tool_profile.GetController oController
        # #     get_controller = oController
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_inertia(self, ixx: float, iyy: float, izz: float, ixy: float, iyz: float, izx: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetInertia(double Ixx,
                | double Iyy,
                | double Izz,
                | double Ixy,
                | double Iyz,
                | double Izx)
                | 
                |     Get the underlying coefficient of the tool inertia.
                | 
                |     Parameters:
                | 
                |         Ixx,
                |             The Ixx coefficient. 
                |         Iyy,
                |             The Ixx coefficient. 
                |         Izz,
                |             The Ixx coefficient. 
                |         Ixy,
                |             The Ixx coefficient. 
                |         Iyz,
                |             The Ixx coefficient. 
                |         Izx,
                |             The Ixx coefficient. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float ixx:
        :param float iyy:
        :param float izz:
        :param float ixy:
        :param float iyz:
        :param float izx:
        :return: None
        :rtype: None
        """
        return self.generic_tool_profile.GetInertia(ixx, iyy, izz, ixy, iyz, izx)

    def get_mass(self, mass: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetMass(double mass)
                | 
                |     Retrieves the mass of the tool.
                | 
                |     Parameters:
                | 
                |         mass
                |             This out parameter contains mass of the tool. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float mass:
        :return: None
        :rtype: None
        """
        return self.generic_tool_profile.GetMass(mass)

    def get_name(self, o_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetName(CATBSTR oName)
                | 
                |     Gets name of the Tool Profile.
                | 
                |     Parameters:
                | 
                |         oName
                |             Name of the required Tool Profile. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param str o_name:
        :return: None
        :rtype: None
        """
        return self.generic_tool_profile.GetName(o_name)

    def get_tcp_offset(self, x: float, y: float, z: float, roll: float, pitch: float, yaw: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetTCPOffset(double x,
                | double y,
                | double z,
                | double roll,
                | double pitch,
                | double yaw)
                | 
                |     Retrieve the underlying x,y,z, roll, pitch, yaw of the Tool TCP
                |     offset.
                | 
                |     Parameters:
                | 
                |         x,
                |             The out parameter contains X Coordinate. 
                |         y,
                |             The out parameter contains Y Coordinate. 
                |         z,
                |             The out parameter contains Z Coordinate. 
                |         roll,
                |             The out parameter contains roll Coordinate. 
                |         pitch,
                |             The out parameter contains pitch Coordinate. 
                |         yaw,
                |             The out parameter contains yaw Coordinate. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float x:
        :param float y:
        :param float z:
        :param float roll:
        :param float pitch:
        :param float yaw:
        :return: None
        :rtype: None
        """
        return self.generic_tool_profile.GetTCPOffset(x, y, z, roll, pitch, yaw)

    def get_tool_mobility(self, o_mobile: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetToolMobility(boolean oMobile)
                | 
                |     Retrieves tool mobility.
                | 
                |     Parameters:
                | 
                |         oMobile
                |             This out parameter contains whether tool is mobiled.
                |             
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise
                |             .

        :param bool o_mobile:
        :return: None
        :rtype: None
        """
        return self.generic_tool_profile.GetToolMobility(o_mobile)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_tool_mobility'
        # # vba_code = """
        # # Public Function get_tool_mobility(generic_tool_profile)
        # #     Dim oMobile (2)
        # #     generic_tool_profile.GetToolMobility oMobile
        # #     get_tool_mobility = oMobile
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_centroid(self, cx: float, cy: float, cz: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetCentroid(double cx,
                | double cy,
                | double cz)
                | 
                |     Set the tool centroid of Profile.
                | 
                |     Parameters:
                | 
                |         cx,
                |             The X Coordinate of tool centroid. 
                |         cy,
                |             The Y Coordinate of tool centroid. 
                |         cz,
                |             The Z Coordinate of tool centroid. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float cx:
        :param float cy:
        :param float cz:
        :return: None
        :rtype: None
        """
        return self.generic_tool_profile.SetCentroid(cx, cy, cz)

    def set_inertia(self, ixx: float, iyy: float, izz: float, ixy: float, iyz: float, izx: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetInertia(double Ixx,
                | double Iyy,
                | double Izz,
                | double Ixy,
                | double Iyz,
                | double Izx)
                | 
                |     Set the underlying coefficient of the tool inertia.
                | 
                |     Parameters:
                | 
                |         Ixx,
                |             The Ixx coefficient. 
                |         Iyy,
                |             The Ixx coefficient. 
                |         Izz,
                |             The Ixx coefficient. 
                |         Ixy,
                |             The Ixx coefficient. 
                |         Iyz,
                |             The Ixx coefficient. 
                |         Izx,
                |             The Ixx coefficient. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float ixx:
        :param float iyy:
        :param float izz:
        :param float ixy:
        :param float iyz:
        :param float izx:
        :return: None
        :rtype: None
        """
        return self.generic_tool_profile.SetInertia(ixx, iyy, izz, ixy, iyz, izx)

    def set_mass(self, mass: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetMass(double mass)
                | 
                |     Set tool mass.
                | 
                |     Parameters:
                | 
                |         mass
                |             set mass of tool . 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float mass:
        :return: None
        :rtype: None
        """
        return self.generic_tool_profile.SetMass(mass)

    def set_name(self, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetName(CATBSTR iName)
                | 
                |     Set name of the Tool Profile.
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the Tool Profile to be set. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param str i_name:
        :return: None
        :rtype: None
        """
        return self.generic_tool_profile.SetName(i_name)

    def set_tcp_offset(self, x: float, y: float, z: float, roll: float, pitch: float, yaw: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTCPOffset(double x,
                | double y,
                | double z,
                | double roll,
                | double pitch,
                | double yaw)
                | 
                |     Set the underlying x,y,z, roll, pitch, yaw of the tool TCP
                |     offset.
                | 
                |     Parameters:
                | 
                |         x,
                |             The X Coordinate. 
                |         y,
                |             The Y Coordinate. 
                |         z,
                |             The Z Coordinate. 
                |         roll,
                |             The roll Coordinate. 
                |         pitch,
                |             The pitch Coordinate. 
                |         yaw,
                |             The yaw Coordinate. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float x:
        :param float y:
        :param float z:
        :param float roll:
        :param float pitch:
        :param float yaw:
        :return: None
        :rtype: None
        """
        return self.generic_tool_profile.SetTCPOffset(x, y, z, roll, pitch, yaw)

    def set_tool_mobility(self, i_mobile: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetToolMobility(boolean iMobile)
                | 
                |     Set tool mobility.
                | 
                |     Parameters:
                | 
                |         iMobile
                |             set whether tool is mobile or not. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param bool i_mobile:
        :return: None
        :rtype: None
        """
        return self.generic_tool_profile.SetToolMobility(i_mobile)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_tool_mobility'
        # # vba_code = """
        # # Public Function set_tool_mobility(generic_tool_profile)
        # #     Dim iMobile (2)
        # #     generic_tool_profile.SetToolMobility iMobile
        # #     set_tool_mobility = iMobile
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'GenericToolProfile(name="{self.name}")'
