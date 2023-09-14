#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_app_connectable import SchAppConnectable
from pycatia.cat_sch_platform_interfaces.sch_component import SchComponent
from pycatia.cat_sch_platform_interfaces.sch_grr_comp import SchGRRComp
from pycatia.in_interfaces.document import Document
from pycatia.system_interfaces.any_object import AnyObject


class SchComponent2(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchComponent2
                | 
                | Manage a schematic component.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_component2 = com_object

    def place_in_space(
            self,
            i_grr: SchGRRComp,
            i_db6_axis: tuple,
            i_doc: Document,
            o_new_component: SchComponent
    ) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub PlaceInSpace(SchGRRComp iGRR,
                | CATSafeArrayVariant iDb6Axis,
                | Document iDoc,
                | SchComponent oNewComponent)
                | 
                |     Place a component in space, unconnected to other objects. It will create
                |     local reference (from a catalog referenced document) if
                |     necessary.
                | 
                |     Parameters:
                | 
                |         iGRR
                |             Pointer to the component graphical representation. if NULL the
                |             "Primary" graphical representation will be used. 
                |         iDb6Axis[6]
                |             X-axis of the local axis of the new instance Y-axis of the local
                |             axis of the new instance X-Y coordinates of the orgin of the new instance. This
                |             axis defines the orientation and location of the new instance in space.
                |             
                |         iDoc
                |             Pointer to a document to create the object in. If NULL, the
                |             document associated with the current Editor will be used.
                |             
                |         oNewComponent
                |             Interface pointer to the new component instance placed.
                |
                |     Example:
                |
                |          Dim objThisIntf As SchComponent2
                |          Dim objArg1 As SchGRRComp
                |          Dim dbVar2(6) As CATSafeArrayVariant
                |          Dim objArg3 As Document
                |          Dim objArg4 As SchComponent
                |           ...
                |         
                |         objThisIntf.PlaceInSpaceobjArg1,dbVar2,objArg3,objArg4

        :param SchGRRComp i_grr:
        :param tuple i_db6_axis:
        :param Document i_doc:
        :param SchComponent o_new_component:
        :return: tuple
        :rtype: tuple
        """
        return self.sch_component2.PlaceInSpace(
            i_grr.com_object,
            i_db6_axis,
            i_doc.com_object,
            o_new_component.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'place_in_space'
        # # vba_code = """
        # # Public Function place_in_space(sch_component2)
        # #     Dim iGRR (2)
        # #     sch_component2.PlaceInSpace iGRR
        # #     place_in_space = iGRR
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def place_on_object(
            self,
            i_grr: SchGRRComp,
            i_db6_axis: tuple,
            i_object_to_connect: SchAppConnectable,
            i_doc: Document,
            o_new_component: SchComponent
    ) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub PlaceOnObject(SchGRRComp iGRR,
                | CATSafeArrayVariant iDb6Axis,
                | SchAppConnectable iObjectToConnect,
                | Document iDoc,
                | SchComponent oNewComponent)
                | 
                |     Place a component connected to another component or insert into a
                |     route.
                | 
                |     Parameters:
                | 
                |         iGRR
                |             Pointer to the component graphical representation. if NULL the
                |             "Primary" graphical representation will be used. 
                |         iDb6Axis[6]
                |             X-axis of the local axis of the new instance Y-axis of the local
                |             axis of the new instance X-Y coordinates of the orgin of the new instance. This
                |             axis defines the orientation and location of the new instance in space.
                |             
                |         iObjectToConnect
                |             Pointer to a component to connect the new instance to or a route
                |             object to insert new component into. 
                |         iDoc
                |             Pointer to a document to create the object in. If NULL, the
                |             document associated with the current Editor will be used.
                |             
                |         oNewComponent
                |             Interface pointer to the new component instance placed.
                |
                |     Example:
                |
                |          Dim objThisIntf As SchComponent2
                |          Dim objArg1 As SchGRRComp
                |          Dim dbVar2(6) As CATSafeArrayVariant
                |          Dim objArg3 As SchAppConnectable
                |          Dim objArg4 As Document
                |          Dim objArg5 As SchComponent
                |           ...
                |          objThisIntf.PlaceOnObjectobjArg1,dbVar2,objArg3,objArg4,objArg5

        :param SchGRRComp i_grr:
        :param tuple i_db6_axis:
        :param SchAppConnectable i_object_to_connect:
        :param Document i_doc:
        :param SchComponent o_new_component:
        :return: tuple
        :rtype: tuple
        """
        return self.sch_component2.PlaceOnObject(
            i_grr.com_object,
            i_db6_axis,
            i_object_to_connect.com_object,
            i_doc.com_object,
            o_new_component.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'place_on_object'
        # # vba_code = """
        # # Public Function place_on_object(sch_component2)
        # #     Dim iGRR (2)
        # #     sch_component2.PlaceOnObject iGRR
        # #     place_on_object = iGRR
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SchComponent2(name="{self.name}")'
