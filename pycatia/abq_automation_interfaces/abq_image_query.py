#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.analysis_interfaces.analysis_entity import AnalysisEntity
from pycatia.analysis_interfaces.analysis_images import AnalysisImages
from pycatia.system_interfaces.any_object import AnyObject


class ABQImageQuery(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQImageQuery
                | 
                | Provides an image query object.
                | 
                | Role: Use to query result images for values on nodes / elements / groups. Image query can be done simultaneously for multiple images. User can call methods such as ExportImageData or ExportGroupImageData. Use following method to get an object of ABQImageQuery Dim abqCase As ABQAnalysisCase Dim ImageQuery As ABQImageQuery Set ImageQuery = abqCase.GetItem ("ABQVBImageQuery")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_image_query = com_object

    def export_group_image_data(
            self,
            i_images_list: AnalysisImages,
            i_group: AnalysisEntity,
            i_type: int,
            i_file: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ExportGroupImageData(AnalysisImages iImagesList,
                | AnalysisEntity iGroup,
                | ABQEntityType iType,
                | CATBSTR iFile)
                | 
                |     Method to export image data in text or excel format for a
                |     group.
                |     The data in a row will be in following order: Node / element id, X
                |     coordinate, Y coordinate, Z coordinate, value for image 1, value for image 2,
                |     ...
                | 
                |     File type will be identified using file extension. If file extension is
                |     'xls' then it will be exported in excel otherwise the file type will be
                |     considered as text
                | 
                |     Parameters:
                | 
                |         iImagesList
                |             List of images to export 
                |         iGroup
                |             CATIA group or display group to query image data 
                |         iType
                |             Entity type to query.
                |             Legal values
                | 
                |             ABQ_NODE
                |             ABQ_ELEMENT
                | 
                |         iFile
                |             File path to export data. 
                |         Example:
                |             The following example exports image query data to specified
                |             file
                | 
                |              Dim ImageQuery As ABQImageQuery
                |              Dim File As FileSystem
                |              Dim MyGroup As AnalysisEntity
                |              Dim imageList As AnalysisImages
                |              ImageQuery.ExportImageData imageList, MyGroup, ABQ_NODE,
                |              File

        :param AnalysisImages i_images_list:
        :param AnalysisEntity i_group:
        :param int i_type:
        :param str i_file:
        :return: None
        :rtype: None
        """
        return self.abq_image_query.ExportGroupImageData(i_images_list.com_object, i_group.com_object, i_type, i_file)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'export_group_image_data'
        # # vba_code = """
        # # Public Function export_group_image_data(abq_image_query)
        # #     Dim iImagesList (2)
        # #     abq_image_query.ExportGroupImageData iImagesList
        # #     export_group_image_data = iImagesList
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def export_image_data(self, i_images_list: AnalysisImages, i_list_numbers: tuple, i_type: int, i_file: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ExportImageData(AnalysisImages iImagesList,
                | CATSafeArrayVariant iListNumbers,
                | ABQEntityType iType,
                | CATBSTR iFile)
                | 
                |     Method to export image data in text or excel format.
                |     The data in a row will be in following order: Node / element id, X
                |     coordinate, Y coordinate, Z coordinate, value for image 1, value for image 2,
                |     ...
                | 
                |     File type will be identified using file extension. If file extension is
                |     'xls' then it will be exported in excel otherwise the file type will be
                |     considered as text
                | 
                |     Parameters:
                | 
                |         iImagesList
                |             List of images to export 
                |         iListNumbers
                |             List of entity indices to export (node numbers or element numbers)
                |             
                |         iType
                |             Entity type to query.
                |             Legal values
                | 
                |             ABQ_NODE
                |             ABQ_ELEMENT
                | 
                |         iFile
                |             File path to export data 
                |         Example:
                |             The following example exports image query data to specified
                |             file
                | 
                |              Dim ImageQuery As ABQImageQuery
                |              Dim File As FileSystem
                |              Dim EntityList As CATSafeArrayVariant
                |              Dim imageList As AnalysisImages
                |              ImageQuery.ExportImageData imageList, EntityList, ABQ_NODE,
                |              File

        :param AnalysisImages i_images_list:
        :param tuple i_list_numbers:
        :param int i_type:
        :param str i_file:
        :return: None
        :rtype: None
        """
        return self.abq_image_query.ExportImageData(i_images_list.com_object, i_list_numbers, i_type, i_file)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'export_image_data'
        # # vba_code = """
        # # Public Function export_image_data(abq_image_query)
        # #     Dim iImagesList (2)
        # #     abq_image_query.ExportImageData iImagesList
        # #     export_image_data = iImagesList
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQImageQuery(name="{self.name}")'
