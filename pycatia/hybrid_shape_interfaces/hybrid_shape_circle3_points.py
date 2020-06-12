#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.hybrid_shape_circle import HybridShapeCircle
from pycatia.in_interfaces.reference import Reference


class HybridShapeCircle3Points(HybridShapeCircle):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.HybridShapeCircle
                |                             HybridShapeCircle3Points
                | 
                | Represents the hybrid shape circle object defined using three
                | points.
                | Role: To access the data of the hybrid shape circle object.
                | 
                | This data includes the circle three passing points.
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeCircle2PointsRad
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle3_points = com_object

    @property
    def element1(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Element1() As Reference
                | 
                |     Returns or sets the circle first passing point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves the first passing point of the HybShpCircle3Pt
                |         hybrid shape circle in HybShpCircle3PtFirstPassingPoint
                |         point.
                | 
                |          Dim HybShpCircle3PtFirstPassingPoint As Reference
                |          Set HybShpCircle3PtFirstPassingPoint=
                |          HybShpCircle3Pt.Element1

        :return: Reference
        """

        return Reference(self.hybrid_shape_circle3_points.Element1)

    @element1.setter
    def element1(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_circle3_points.Element1 = value

    @property
    def element2(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Element2() As Reference
                | 
                |     Returns or sets the circle second passing point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example sets the second passing point of the HybShpCircle3Pt
                |         hybrid shape circle as the Point2 point.
                | 
                |          HybShpCircle3Pt.Element2 Point2

        :return: Reference
        """

        return Reference(self.hybrid_shape_circle3_points.Element2)

    @element2.setter
    def element2(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_circle3_points.Element2 = value

    @property
    def element3(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Element3() As Reference
                | 
                |     Returns or sets the circle third passing point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves the third passing point of the HybShpCircle3Pt
                |         hybrid shape circle in HybShpCircle3PtThirdPassingPoint
                |         point.
                | 
                |          Dim HybShpCircle3PtThirdPassingPoint As Reference
                |          Set HybShpCircle3PtThirdPassingPoint=
                |          HybShpCircle3Pt.Element3

        :return: Reference
        """

        return Reference(self.hybrid_shape_circle3_points.Element3)

    @element3.setter
    def element3(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_circle3_points.Element3 = value

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Support() As Reference
                | 
                |     Returns or sets the circle support surface.
                |     Sub-element(s) supported (see Boundary object): Face.
                | 
                |     Example:
                |         This example retrieves in HybShpCircleSupportSurf the support surface
                |         of the HybShpCircle hybrid shape circle.
                | 
                |          Dim HybShpCircleSupportSurf As Reference 
                |          HybShpCircleSupportSurf = HybShpCircle.Support

        :return: Reference
        """

        return Reference(self.hybrid_shape_circle3_points.Support)

    @support.setter
    def support(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_circle3_points.Support = value

    def remove_support(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub RemoveSupport()
                | 
                |     Removes the support surface.

        :return: None
        """
        return self.hybrid_shape_circle3_points.RemoveSupport()

    def __repr__(self):
        return f'HybridShapeCircle3Points(name="{ self.name }")'