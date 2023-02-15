#############################################################################
##
## Copyright (C) 2021 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of Qt for Python.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 3 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL3 included in the
## packaging of this file. Please review the following information to
## ensure the GNU Lesser General Public License version 3 requirements
## will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 2.0 or (at your option) the GNU General
## Public license version 3 or any later version approved by the KDE Free
## Qt Foundation. The licenses are as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-2.0.html and
## https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################
from __future__ import annotations

"""
This file contains the exact signatures for all functions in module
PySide6.Qt3DCore, except for defaults which are replaced by "...".
"""

# Module `PySide6.Qt3DCore`

import PySide6.Qt3DCore
import PySide6.QtCore
import PySide6.QtGui

from enum import Enum
from typing import Optional, Union, Sequence, List, overload
from shiboken6 import Shiboken


class QIntList(object): ...


class Qt3DCore(Shiboken.Object):

    class QAbstractAspect(PySide6.QtCore.QObject):

        def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

        def dependencies(self) -> List[str]: ...
        def rootEntityId(self) -> PySide6.Qt3DCore.Qt3DCore.QNodeId: ...
        def unregisterBackendType(self, arg__1: PySide6.QtCore.QMetaObject) -> None: ...

    class QAbstractFunctor(Shiboken.Object):

        def __init__(self) -> None: ...

        def id(self) -> int: ...

    class QAbstractSkeleton(PySide6.Qt3DCore.Qt3DCore.QNode):
        def jointCount(self) -> int: ...

    class QArmature(PySide6.Qt3DCore.Qt3DCore.QComponent):

        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def setSkeleton(self, skeleton: PySide6.Qt3DCore.Qt3DCore.QAbstractSkeleton) -> None: ...
        def skeleton(self) -> PySide6.Qt3DCore.Qt3DCore.QAbstractSkeleton: ...

    class QAspectEngine(PySide6.QtCore.QObject):

        Manual                   : Qt3DCore.QAspectEngine.RunMode = ... # 0x0
        Automatic                : Qt3DCore.QAspectEngine.RunMode = ... # 0x1

        class RunMode(Enum):

            Manual                   : Qt3DCore.QAspectEngine.RunMode = ... # 0x0
            Automatic                : Qt3DCore.QAspectEngine.RunMode = ... # 0x1


        def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

        def aspect(self, name: str) -> PySide6.Qt3DCore.Qt3DCore.QAbstractAspect: ...
        def aspects(self) -> List[PySide6.Qt3DCore.Qt3DCore.QAbstractAspect]: ...
        def executeCommand(self, command: str) -> Any: ...
        def lookupNode(self, id: PySide6.Qt3DCore.Qt3DCore.QNodeId) -> PySide6.Qt3DCore.Qt3DCore.QNode: ...
        def lookupNodes(self, ids: Sequence[PySide6.Qt3DCore.Qt3DCore.QNodeId]) -> List[PySide6.Qt3DCore.Qt3DCore.QNode]: ...
        def processFrame(self) -> None: ...
        @overload
        def registerAspect(self, aspect: PySide6.Qt3DCore.Qt3DCore.QAbstractAspect) -> None: ...
        @overload
        def registerAspect(self, name: str) -> None: ...
        def runMode(self) -> PySide6.Qt3DCore.Qt3DCore.QAspectEngine.RunMode: ...
        def setRunMode(self, mode: PySide6.Qt3DCore.Qt3DCore.QAspectEngine.RunMode) -> None: ...
        @overload
        def unregisterAspect(self, aspect: PySide6.Qt3DCore.Qt3DCore.QAbstractAspect) -> None: ...
        @overload
        def unregisterAspect(self, name: str) -> None: ...

    class QAspectJob(Shiboken.Object):

        def __init__(self) -> None: ...

        def isRequired(self) -> bool: ...
        def postFrame(self, aspectEngine: PySide6.Qt3DCore.Qt3DCore.QAspectEngine) -> None: ...
        def run(self) -> None: ...

    class QAttribute(PySide6.Qt3DCore.Qt3DCore.QNode):

        VertexAttribute          : Qt3DCore.QAttribute.AttributeType = ... # 0x0
        IndexAttribute           : Qt3DCore.QAttribute.AttributeType = ... # 0x1
        DrawIndirectAttribute    : Qt3DCore.QAttribute.AttributeType = ... # 0x2
        Byte                     : Qt3DCore.QAttribute.VertexBaseType = ... # 0x0
        UnsignedByte             : Qt3DCore.QAttribute.VertexBaseType = ... # 0x1
        Short                    : Qt3DCore.QAttribute.VertexBaseType = ... # 0x2
        UnsignedShort            : Qt3DCore.QAttribute.VertexBaseType = ... # 0x3
        Int                      : Qt3DCore.QAttribute.VertexBaseType = ... # 0x4
        UnsignedInt              : Qt3DCore.QAttribute.VertexBaseType = ... # 0x5
        HalfFloat                : Qt3DCore.QAttribute.VertexBaseType = ... # 0x6
        Float                    : Qt3DCore.QAttribute.VertexBaseType = ... # 0x7
        Double                   : Qt3DCore.QAttribute.VertexBaseType = ... # 0x8

        class AttributeType(Enum):

            VertexAttribute          : Qt3DCore.QAttribute.AttributeType = ... # 0x0
            IndexAttribute           : Qt3DCore.QAttribute.AttributeType = ... # 0x1
            DrawIndirectAttribute    : Qt3DCore.QAttribute.AttributeType = ... # 0x2

        class VertexBaseType(Enum):

            Byte                     : Qt3DCore.QAttribute.VertexBaseType = ... # 0x0
            UnsignedByte             : Qt3DCore.QAttribute.VertexBaseType = ... # 0x1
            Short                    : Qt3DCore.QAttribute.VertexBaseType = ... # 0x2
            UnsignedShort            : Qt3DCore.QAttribute.VertexBaseType = ... # 0x3
            Int                      : Qt3DCore.QAttribute.VertexBaseType = ... # 0x4
            UnsignedInt              : Qt3DCore.QAttribute.VertexBaseType = ... # 0x5
            HalfFloat                : Qt3DCore.QAttribute.VertexBaseType = ... # 0x6
            Float                    : Qt3DCore.QAttribute.VertexBaseType = ... # 0x7
            Double                   : Qt3DCore.QAttribute.VertexBaseType = ... # 0x8


        @overload
        def __init__(self, buf: PySide6.Qt3DCore.Qt3DCore.QBuffer, name: str, vertexBaseType: PySide6.Qt3DCore.Qt3DCore.QAttribute.VertexBaseType, vertexSize: int, count: int, offset: int = ..., stride: int = ..., parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...
        @overload
        def __init__(self, buf: PySide6.Qt3DCore.Qt3DCore.QBuffer, vertexBaseType: PySide6.Qt3DCore.Qt3DCore.QAttribute.VertexBaseType, vertexSize: int, count: int, offset: int = ..., stride: int = ..., parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...
        @overload
        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def attributeType(self) -> PySide6.Qt3DCore.Qt3DCore.QAttribute.AttributeType: ...
        def buffer(self) -> PySide6.Qt3DCore.Qt3DCore.QBuffer: ...
        def byteOffset(self) -> int: ...
        def byteStride(self) -> int: ...
        def count(self) -> int: ...
        @staticmethod
        def defaultColorAttributeName() -> str: ...
        @staticmethod
        def defaultJointIndicesAttributeName() -> str: ...
        @staticmethod
        def defaultJointWeightsAttributeName() -> str: ...
        @staticmethod
        def defaultNormalAttributeName() -> str: ...
        @staticmethod
        def defaultPositionAttributeName() -> str: ...
        @staticmethod
        def defaultTangentAttributeName() -> str: ...
        @staticmethod
        def defaultTextureCoordinate1AttributeName() -> str: ...
        @staticmethod
        def defaultTextureCoordinate2AttributeName() -> str: ...
        @staticmethod
        def defaultTextureCoordinateAttributeName() -> str: ...
        def divisor(self) -> int: ...
        def name(self) -> str: ...
        def setAttributeType(self, attributeType: PySide6.Qt3DCore.Qt3DCore.QAttribute.AttributeType) -> None: ...
        def setBuffer(self, buffer: PySide6.Qt3DCore.Qt3DCore.QBuffer) -> None: ...
        def setByteOffset(self, byteOffset: int) -> None: ...
        def setByteStride(self, byteStride: int) -> None: ...
        def setCount(self, count: int) -> None: ...
        def setDivisor(self, divisor: int) -> None: ...
        def setName(self, name: str) -> None: ...
        def setVertexBaseType(self, type: PySide6.Qt3DCore.Qt3DCore.QAttribute.VertexBaseType) -> None: ...
        def setVertexSize(self, size: int) -> None: ...
        def vertexBaseType(self) -> PySide6.Qt3DCore.Qt3DCore.QAttribute.VertexBaseType: ...
        def vertexSize(self) -> int: ...

    class QBackendNode(Shiboken.Object):

        ReadOnly                 : Qt3DCore.QBackendNode.Mode = ... # 0x0
        ReadWrite                : Qt3DCore.QBackendNode.Mode = ... # 0x1

        class Mode(Enum):

            ReadOnly                 : Qt3DCore.QBackendNode.Mode = ... # 0x0
            ReadWrite                : Qt3DCore.QBackendNode.Mode = ... # 0x1


        def __init__(self, mode: PySide6.Qt3DCore.Qt3DCore.QBackendNode.Mode = ...) -> None: ...

        def isEnabled(self) -> bool: ...
        def mode(self) -> PySide6.Qt3DCore.Qt3DCore.QBackendNode.Mode: ...
        def peerId(self) -> PySide6.Qt3DCore.Qt3DCore.QNodeId: ...
        def setEnabled(self, enabled: bool) -> None: ...
        def syncFromFrontEnd(self, frontEnd: PySide6.Qt3DCore.Qt3DCore.QNode, firstTime: bool) -> None: ...

    class QBackendNodeMapper(Shiboken.Object):

        def __init__(self) -> None: ...

        def create(self, id: PySide6.Qt3DCore.Qt3DCore.QNodeId) -> PySide6.Qt3DCore.Qt3DCore.QBackendNode: ...
        def destroy(self, id: PySide6.Qt3DCore.Qt3DCore.QNodeId) -> None: ...
        def get(self, id: PySide6.Qt3DCore.Qt3DCore.QNodeId) -> PySide6.Qt3DCore.Qt3DCore.QBackendNode: ...

    class QBoundingVolume(PySide6.Qt3DCore.Qt3DCore.QComponent):

        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def areImplicitPointsValid(self) -> bool: ...
        def implicitMaxPoint(self) -> PySide6.QtGui.QVector3D: ...
        def implicitMinPoint(self) -> PySide6.QtGui.QVector3D: ...
        def maxPoint(self) -> PySide6.QtGui.QVector3D: ...
        def minPoint(self) -> PySide6.QtGui.QVector3D: ...
        def setMaxPoint(self, maxPoint: PySide6.QtGui.QVector3D) -> None: ...
        def setMinPoint(self, minPoint: PySide6.QtGui.QVector3D) -> None: ...
        def setView(self, view: PySide6.Qt3DCore.Qt3DCore.QGeometryView) -> None: ...
        def updateImplicitBounds(self) -> bool: ...
        def view(self) -> PySide6.Qt3DCore.Qt3DCore.QGeometryView: ...

    class QBuffer(PySide6.Qt3DCore.Qt3DCore.QNode):

        Write                    : Qt3DCore.QBuffer.AccessType = ... # 0x1
        Read                     : Qt3DCore.QBuffer.AccessType = ... # 0x2
        ReadWrite                : Qt3DCore.QBuffer.AccessType = ... # 0x3
        StreamDraw               : Qt3DCore.QBuffer.UsageType = ... # 0x88e0
        StreamRead               : Qt3DCore.QBuffer.UsageType = ... # 0x88e1
        StreamCopy               : Qt3DCore.QBuffer.UsageType = ... # 0x88e2
        StaticDraw               : Qt3DCore.QBuffer.UsageType = ... # 0x88e4
        StaticRead               : Qt3DCore.QBuffer.UsageType = ... # 0x88e5
        StaticCopy               : Qt3DCore.QBuffer.UsageType = ... # 0x88e6
        DynamicDraw              : Qt3DCore.QBuffer.UsageType = ... # 0x88e8
        DynamicRead              : Qt3DCore.QBuffer.UsageType = ... # 0x88e9
        DynamicCopy              : Qt3DCore.QBuffer.UsageType = ... # 0x88ea

        class AccessType(Enum):

            Write                    : Qt3DCore.QBuffer.AccessType = ... # 0x1
            Read                     : Qt3DCore.QBuffer.AccessType = ... # 0x2
            ReadWrite                : Qt3DCore.QBuffer.AccessType = ... # 0x3

        class UsageType(Enum):

            StreamDraw               : Qt3DCore.QBuffer.UsageType = ... # 0x88e0
            StreamRead               : Qt3DCore.QBuffer.UsageType = ... # 0x88e1
            StreamCopy               : Qt3DCore.QBuffer.UsageType = ... # 0x88e2
            StaticDraw               : Qt3DCore.QBuffer.UsageType = ... # 0x88e4
            StaticRead               : Qt3DCore.QBuffer.UsageType = ... # 0x88e5
            StaticCopy               : Qt3DCore.QBuffer.UsageType = ... # 0x88e6
            DynamicDraw              : Qt3DCore.QBuffer.UsageType = ... # 0x88e8
            DynamicRead              : Qt3DCore.QBuffer.UsageType = ... # 0x88e9
            DynamicCopy              : Qt3DCore.QBuffer.UsageType = ... # 0x88ea


        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def accessType(self) -> PySide6.Qt3DCore.Qt3DCore.QBuffer.AccessType: ...
        def data(self) -> PySide6.QtCore.QByteArray: ...
        def setAccessType(self, access: PySide6.Qt3DCore.Qt3DCore.QBuffer.AccessType) -> None: ...
        def setData(self, bytes: Union[PySide6.QtCore.QByteArray, bytes]) -> None: ...
        def setUsage(self, usage: PySide6.Qt3DCore.Qt3DCore.QBuffer.UsageType) -> None: ...
        def updateData(self, offset: int, bytes: Union[PySide6.QtCore.QByteArray, bytes]) -> None: ...
        def usage(self) -> PySide6.Qt3DCore.Qt3DCore.QBuffer.UsageType: ...

    class QComponent(PySide6.Qt3DCore.Qt3DCore.QNode):

        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def entities(self) -> List[PySide6.Qt3DCore.Qt3DCore.QEntity]: ...
        def isShareable(self) -> bool: ...
        def setShareable(self, isShareable: bool) -> None: ...

    class QCoreSettings(PySide6.Qt3DCore.Qt3DCore.QComponent):

        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def boundingVolumesEnabled(self) -> bool: ...
        def setBoundingVolumesEnabled(self, boundingVolumesEnabled: bool) -> None: ...

    class QEntity(PySide6.Qt3DCore.Qt3DCore.QNode):

        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def addComponent(self, comp: PySide6.Qt3DCore.Qt3DCore.QComponent) -> None: ...
        def components(self) -> List[PySide6.Qt3DCore.Qt3DCore.QComponent]: ...
        def parentEntity(self) -> PySide6.Qt3DCore.Qt3DCore.QEntity: ...
        def removeComponent(self, comp: PySide6.Qt3DCore.Qt3DCore.QComponent) -> None: ...

    class QGeometry(PySide6.Qt3DCore.Qt3DCore.QNode):

        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def addAttribute(self, attribute: PySide6.Qt3DCore.Qt3DCore.QAttribute) -> None: ...
        def attributes(self) -> List[PySide6.Qt3DCore.Qt3DCore.QAttribute]: ...
        def boundingVolumePositionAttribute(self) -> PySide6.Qt3DCore.Qt3DCore.QAttribute: ...
        def maxExtent(self) -> PySide6.QtGui.QVector3D: ...
        def minExtent(self) -> PySide6.QtGui.QVector3D: ...
        def removeAttribute(self, attribute: PySide6.Qt3DCore.Qt3DCore.QAttribute) -> None: ...
        def setBoundingVolumePositionAttribute(self, boundingVolumePositionAttribute: PySide6.Qt3DCore.Qt3DCore.QAttribute) -> None: ...

    class QGeometryView(PySide6.Qt3DCore.Qt3DCore.QNode):

        Points                   : Qt3DCore.QGeometryView.PrimitiveType = ... # 0x0
        Lines                    : Qt3DCore.QGeometryView.PrimitiveType = ... # 0x1
        LineLoop                 : Qt3DCore.QGeometryView.PrimitiveType = ... # 0x2
        LineStrip                : Qt3DCore.QGeometryView.PrimitiveType = ... # 0x3
        Triangles                : Qt3DCore.QGeometryView.PrimitiveType = ... # 0x4
        TriangleStrip            : Qt3DCore.QGeometryView.PrimitiveType = ... # 0x5
        TriangleFan              : Qt3DCore.QGeometryView.PrimitiveType = ... # 0x6
        LinesAdjacency           : Qt3DCore.QGeometryView.PrimitiveType = ... # 0xa
        LineStripAdjacency       : Qt3DCore.QGeometryView.PrimitiveType = ... # 0xb
        TrianglesAdjacency       : Qt3DCore.QGeometryView.PrimitiveType = ... # 0xc
        TriangleStripAdjacency   : Qt3DCore.QGeometryView.PrimitiveType = ... # 0xd
        Patches                  : Qt3DCore.QGeometryView.PrimitiveType = ... # 0xe

        class PrimitiveType(Enum):

            Points                   : Qt3DCore.QGeometryView.PrimitiveType = ... # 0x0
            Lines                    : Qt3DCore.QGeometryView.PrimitiveType = ... # 0x1
            LineLoop                 : Qt3DCore.QGeometryView.PrimitiveType = ... # 0x2
            LineStrip                : Qt3DCore.QGeometryView.PrimitiveType = ... # 0x3
            Triangles                : Qt3DCore.QGeometryView.PrimitiveType = ... # 0x4
            TriangleStrip            : Qt3DCore.QGeometryView.PrimitiveType = ... # 0x5
            TriangleFan              : Qt3DCore.QGeometryView.PrimitiveType = ... # 0x6
            LinesAdjacency           : Qt3DCore.QGeometryView.PrimitiveType = ... # 0xa
            LineStripAdjacency       : Qt3DCore.QGeometryView.PrimitiveType = ... # 0xb
            TrianglesAdjacency       : Qt3DCore.QGeometryView.PrimitiveType = ... # 0xc
            TriangleStripAdjacency   : Qt3DCore.QGeometryView.PrimitiveType = ... # 0xd
            Patches                  : Qt3DCore.QGeometryView.PrimitiveType = ... # 0xe


        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def firstInstance(self) -> int: ...
        def firstVertex(self) -> int: ...
        def geometry(self) -> PySide6.Qt3DCore.Qt3DCore.QGeometry: ...
        def indexBufferByteOffset(self) -> int: ...
        def indexOffset(self) -> int: ...
        def instanceCount(self) -> int: ...
        def primitiveRestartEnabled(self) -> bool: ...
        def primitiveType(self) -> PySide6.Qt3DCore.Qt3DCore.QGeometryView.PrimitiveType: ...
        def restartIndexValue(self) -> int: ...
        def setFirstInstance(self, firstInstance: int) -> None: ...
        def setFirstVertex(self, firstVertex: int) -> None: ...
        def setGeometry(self, geometry: PySide6.Qt3DCore.Qt3DCore.QGeometry) -> None: ...
        def setIndexBufferByteOffset(self, offset: int) -> None: ...
        def setIndexOffset(self, indexOffset: int) -> None: ...
        def setInstanceCount(self, instanceCount: int) -> None: ...
        def setPrimitiveRestartEnabled(self, enabled: bool) -> None: ...
        def setPrimitiveType(self, primitiveType: PySide6.Qt3DCore.Qt3DCore.QGeometryView.PrimitiveType) -> None: ...
        def setRestartIndexValue(self, index: int) -> None: ...
        def setVertexCount(self, vertexCount: int) -> None: ...
        def setVerticesPerPatch(self, verticesPerPatch: int) -> None: ...
        def vertexCount(self) -> int: ...
        def verticesPerPatch(self) -> int: ...

    class QJoint(PySide6.Qt3DCore.Qt3DCore.QNode):

        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def addChildJoint(self, joint: PySide6.Qt3DCore.Qt3DCore.QJoint) -> None: ...
        def childJoints(self) -> List[PySide6.Qt3DCore.Qt3DCore.QJoint]: ...
        def inverseBindMatrix(self) -> PySide6.QtGui.QMatrix4x4: ...
        def name(self) -> str: ...
        def removeChildJoint(self, joint: PySide6.Qt3DCore.Qt3DCore.QJoint) -> None: ...
        def rotation(self) -> PySide6.QtGui.QQuaternion: ...
        def rotationX(self) -> float: ...
        def rotationY(self) -> float: ...
        def rotationZ(self) -> float: ...
        def scale(self) -> PySide6.QtGui.QVector3D: ...
        def setInverseBindMatrix(self, inverseBindMatrix: Union[PySide6.QtGui.QMatrix4x4, PySide6.QtGui.QTransform]) -> None: ...
        def setName(self, name: str) -> None: ...
        def setRotation(self, rotation: PySide6.QtGui.QQuaternion) -> None: ...
        def setRotationX(self, rotationX: float) -> None: ...
        def setRotationY(self, rotationY: float) -> None: ...
        def setRotationZ(self, rotationZ: float) -> None: ...
        def setScale(self, scale: PySide6.QtGui.QVector3D) -> None: ...
        def setToIdentity(self) -> None: ...
        def setTranslation(self, translation: PySide6.QtGui.QVector3D) -> None: ...
        def translation(self) -> PySide6.QtGui.QVector3D: ...

    class QNode(PySide6.QtCore.QObject):

        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def blockNotifications(self, block: bool) -> bool: ...
        def childNodes(self) -> List[PySide6.Qt3DCore.Qt3DCore.QNode]: ...
        def id(self) -> PySide6.Qt3DCore.Qt3DCore.QNodeId: ...
        def isEnabled(self) -> bool: ...
        def notificationsBlocked(self) -> bool: ...
        def parentNode(self) -> PySide6.Qt3DCore.Qt3DCore.QNode: ...
        def setEnabled(self, isEnabled: bool) -> None: ...
        def setParent(self, parent: PySide6.Qt3DCore.Qt3DCore.QNode) -> None: ...

    class QNodeId(Shiboken.Object):

        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, QNodeId: PySide6.Qt3DCore.Qt3DCore.QNodeId) -> None: ...

        @staticmethod
        def __copy__() -> None: ...
        @staticmethod
        def createId() -> PySide6.Qt3DCore.Qt3DCore.QNodeId: ...
        def id(self) -> int: ...
        def isNull(self) -> bool: ...

    class QNodeIdTypePair(Shiboken.Object):

        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, QNodeIdTypePair: PySide6.Qt3DCore.Qt3DCore.QNodeIdTypePair) -> None: ...
        @overload
        def __init__(self, _id: PySide6.Qt3DCore.Qt3DCore.QNodeId, _type: PySide6.QtCore.QMetaObject) -> None: ...

        @staticmethod
        def __copy__() -> None: ...

    class QSkeleton(PySide6.Qt3DCore.Qt3DCore.QAbstractSkeleton):

        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def rootJoint(self) -> PySide6.Qt3DCore.Qt3DCore.QJoint: ...
        def setRootJoint(self, rootJoint: PySide6.Qt3DCore.Qt3DCore.QJoint) -> None: ...

    class QSkeletonLoader(PySide6.Qt3DCore.Qt3DCore.QAbstractSkeleton):

        NotReady                 : Qt3DCore.QSkeletonLoader.Status = ... # 0x0
        Ready                    : Qt3DCore.QSkeletonLoader.Status = ... # 0x1
        Error                    : Qt3DCore.QSkeletonLoader.Status = ... # 0x2

        class Status(Enum):

            NotReady                 : Qt3DCore.QSkeletonLoader.Status = ... # 0x0
            Ready                    : Qt3DCore.QSkeletonLoader.Status = ... # 0x1
            Error                    : Qt3DCore.QSkeletonLoader.Status = ... # 0x2


        @overload
        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...
        @overload
        def __init__(self, source: Union[PySide6.QtCore.QUrl, str], parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def isCreateJointsEnabled(self) -> bool: ...
        def rootJoint(self) -> PySide6.Qt3DCore.Qt3DCore.QJoint: ...
        def setCreateJointsEnabled(self, enabled: bool) -> None: ...
        def setSource(self, source: Union[PySide6.QtCore.QUrl, str]) -> None: ...
        def source(self) -> PySide6.QtCore.QUrl: ...
        def status(self) -> PySide6.Qt3DCore.Qt3DCore.QSkeletonLoader.Status: ...

    class QTransform(PySide6.Qt3DCore.Qt3DCore.QComponent):

        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        @staticmethod
        def fromAxes(xAxis: PySide6.QtGui.QVector3D, yAxis: PySide6.QtGui.QVector3D, zAxis: PySide6.QtGui.QVector3D) -> PySide6.QtGui.QQuaternion: ...
        @overload
        @staticmethod
        def fromAxesAndAngles(axis1: PySide6.QtGui.QVector3D, angle1: float, axis2: PySide6.QtGui.QVector3D, angle2: float) -> PySide6.QtGui.QQuaternion: ...
        @overload
        @staticmethod
        def fromAxesAndAngles(axis1: PySide6.QtGui.QVector3D, angle1: float, axis2: PySide6.QtGui.QVector3D, angle2: float, axis3: PySide6.QtGui.QVector3D, angle3: float) -> PySide6.QtGui.QQuaternion: ...
        @overload
        @staticmethod
        def fromAxisAndAngle(axis: PySide6.QtGui.QVector3D, angle: float) -> PySide6.QtGui.QQuaternion: ...
        @overload
        @staticmethod
        def fromAxisAndAngle(x: float, y: float, z: float, angle: float) -> PySide6.QtGui.QQuaternion: ...
        @overload
        @staticmethod
        def fromEulerAngles(eulerAngles: PySide6.QtGui.QVector3D) -> PySide6.QtGui.QQuaternion: ...
        @overload
        @staticmethod
        def fromEulerAngles(pitch: float, yaw: float, roll: float) -> PySide6.QtGui.QQuaternion: ...
        def matrix(self) -> PySide6.QtGui.QMatrix4x4: ...
        @staticmethod
        def rotateAround(point: PySide6.QtGui.QVector3D, angle: float, axis: PySide6.QtGui.QVector3D) -> PySide6.QtGui.QMatrix4x4: ...
        @staticmethod
        def rotateFromAxes(xAxis: PySide6.QtGui.QVector3D, yAxis: PySide6.QtGui.QVector3D, zAxis: PySide6.QtGui.QVector3D) -> PySide6.QtGui.QMatrix4x4: ...
        def rotation(self) -> PySide6.QtGui.QQuaternion: ...
        def rotationX(self) -> float: ...
        def rotationY(self) -> float: ...
        def rotationZ(self) -> float: ...
        def scale(self) -> float: ...
        def scale3D(self) -> PySide6.QtGui.QVector3D: ...
        def setMatrix(self, matrix: Union[PySide6.QtGui.QMatrix4x4, PySide6.QtGui.QTransform]) -> None: ...
        def setRotation(self, rotation: PySide6.QtGui.QQuaternion) -> None: ...
        def setRotationX(self, rotationX: float) -> None: ...
        def setRotationY(self, rotationY: float) -> None: ...
        def setRotationZ(self, rotationZ: float) -> None: ...
        def setScale(self, scale: float) -> None: ...
        def setScale3D(self, scale: PySide6.QtGui.QVector3D) -> None: ...
        def setTranslation(self, translation: PySide6.QtGui.QVector3D) -> None: ...
        def translation(self) -> PySide6.QtGui.QVector3D: ...
        def worldMatrix(self) -> PySide6.QtGui.QMatrix4x4: ...


    @staticmethod
    def qHash(id: PySide6.Qt3DCore.Qt3DCore.QNodeId, seed: int = ...) -> int: ...
    @staticmethod
    def qIdForNode(node: PySide6.Qt3DCore.Qt3DCore.QNode) -> PySide6.Qt3DCore.Qt3DCore.QNodeId: ...


# eof
