#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.funct_system_interfaces.funct_actions_group import FunctActionsGroup
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class FunctActionsGroups(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     FunctActionsGroups
                | 
                | The interface to access the groups of functional actions in a
                | system.
    
    """

    def __init__(self, com_object, child_object=FunctActionsGroup):
        super().__init__(com_object, child_object=FunctActionsGroup)
        self.funct_actions_groups = com_object
        self.child_object = child_object

    def create(self, i_name: str, i_input_x: float, i_input_y: float, i_output_x: float,
               i_output_y: float) -> FunctActionsGroup:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Create(CATBSTR iName,
                | double iInputX,
                | double iInputY,
                | double iOutputX,
                | double iOutputY) As FunctActionsGroup
                | 
                |     Create a Group of Actions.

        :param str i_name:
        :param float i_input_x:
        :param float i_input_y:
        :param float i_output_x:
        :param float i_output_y:
        :return: FunctActionsGroup
        :rtype: FunctActionsGroup
        """
        return FunctActionsGroup(self.funct_actions_groups.Create(i_name, i_input_x, i_input_y, i_output_x, i_output_y))

    def delete(self, i_act_grp: FunctActionsGroup) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Delete(FunctActionsGroup iActGrp)
                | 
                |     Delete a Group of Actions.

        :param FunctActionsGroup i_act_grp:
        :return: None
        :rtype: None
        """
        return self.funct_actions_groups.Delete(i_act_grp.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'delete'
        # # vba_code = """
        # # Public Function delete(funct_actions_groups)
        # #     Dim iActGrp (2)
        # #     funct_actions_groups.Delete iActGrp
        # #     delete = iActGrp
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def elem(self, i_index: cat_variant) -> FunctActionsGroup:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Elem(CATVariant iIndex) As FunctActionsGroup
                | 
                |     Returns an actions' group using its index or its name from the actions'
                |     groups collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the actions' group to retrieve from the
                |             collection of actions' groups. As a numerics, this index is the rank of the
                |             actions' group in the collection. The index of the first actions' group in the
                |             collection is 1, and the index of the last actions' group is Count. As a
                |             string, it is the name you assigned to the actions' group using the
                |             
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved action 
                |     Example:
                |         This example retrieves in AG1 the fifth actions' group in the
                |         collection and in AG2 the actions' group named
                |         Transmission.
                | 
                |          Dim AG1 As FunctActionsGroup
                |          Set AG1 = ActionsGroups.Elem(5)
                |          Dim AG2 As FunctActionsGroup
                |          Set AG2 = ActionsGroups.Elem("Transmission")

        :param CATVariant i_index:
        :return: FunctActionsGroup
        :rtype: FunctActionsGroup
        """
        return FunctActionsGroup(self.funct_actions_groups.Elem(i_index))

    def __repr__(self):
        return f'FunctActionsGroups(name="{self.name}")'
