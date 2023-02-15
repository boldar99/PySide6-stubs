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
PySide6.QtBluetooth, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtBluetooth`

import PySide6.QtBluetooth
import PySide6.QtCore

from typing import Any, Optional, Protocol, Tuple, Union, Sequence, Dict, List, overload
from shiboken6 import Shiboken


class QBluetooth(Shiboken.Object):

    class AttAccessConstraint(Shiboken.Enum):

        AttAuthorizationRequired : QBluetooth.AttAccessConstraint = ... # 0x1
        AttAuthenticationRequired: QBluetooth.AttAccessConstraint = ... # 0x2
        AttEncryptionRequired    : QBluetooth.AttAccessConstraint = ... # 0x4

    class AttAccessConstraints(object): ...

    class Security(Shiboken.Enum):

        NoSecurity               : QBluetooth.Security = ... # 0x0
        Authorization            : QBluetooth.Security = ... # 0x1
        Authentication           : QBluetooth.Security = ... # 0x2
        Encryption               : QBluetooth.Security = ... # 0x4
        Secure                   : QBluetooth.Security = ... # 0x8

    class SecurityFlags(object): ...


class QBluetoothAddress(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, address: str) -> None: ...
    @overload
    def __init__(self, address: int) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtBluetooth.QBluetoothAddress) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def clear(self) -> None: ...
    def isNull(self) -> bool: ...
    def toString(self) -> str: ...
    def toUInt64(self) -> int: ...


class QBluetoothDeviceDiscoveryAgent(PySide6.QtCore.QObject):

    NoMethod                 : QBluetoothDeviceDiscoveryAgent.DiscoveryMethod = ... # 0x0
    ClassicMethod            : QBluetoothDeviceDiscoveryAgent.DiscoveryMethod = ... # 0x1
    LowEnergyMethod          : QBluetoothDeviceDiscoveryAgent.DiscoveryMethod = ... # 0x2
    NoError                  : QBluetoothDeviceDiscoveryAgent.Error = ... # 0x0
    InputOutputError         : QBluetoothDeviceDiscoveryAgent.Error = ... # 0x1
    PoweredOffError          : QBluetoothDeviceDiscoveryAgent.Error = ... # 0x2
    InvalidBluetoothAdapterError: QBluetoothDeviceDiscoveryAgent.Error = ... # 0x3
    UnsupportedPlatformError : QBluetoothDeviceDiscoveryAgent.Error = ... # 0x4
    UnsupportedDiscoveryMethod: QBluetoothDeviceDiscoveryAgent.Error = ... # 0x5
    LocationServiceTurnedOffError: QBluetoothDeviceDiscoveryAgent.Error = ... # 0x6
    UnknownError             : QBluetoothDeviceDiscoveryAgent.Error = ... # 0x64

    class DiscoveryMethod(Shiboken.Enum):

        NoMethod                 : QBluetoothDeviceDiscoveryAgent.DiscoveryMethod = ... # 0x0
        ClassicMethod            : QBluetoothDeviceDiscoveryAgent.DiscoveryMethod = ... # 0x1
        LowEnergyMethod          : QBluetoothDeviceDiscoveryAgent.DiscoveryMethod = ... # 0x2

    class Error(Shiboken.Enum):

        NoError                  : QBluetoothDeviceDiscoveryAgent.Error = ... # 0x0
        InputOutputError         : QBluetoothDeviceDiscoveryAgent.Error = ... # 0x1
        PoweredOffError          : QBluetoothDeviceDiscoveryAgent.Error = ... # 0x2
        InvalidBluetoothAdapterError: QBluetoothDeviceDiscoveryAgent.Error = ... # 0x3
        UnsupportedPlatformError : QBluetoothDeviceDiscoveryAgent.Error = ... # 0x4
        UnsupportedDiscoveryMethod: QBluetoothDeviceDiscoveryAgent.Error = ... # 0x5
        LocationServiceTurnedOffError: QBluetoothDeviceDiscoveryAgent.Error = ... # 0x6
        UnknownError             : QBluetoothDeviceDiscoveryAgent.Error = ... # 0x64


    @overload
    def __init__(self, deviceAdapter: PySide6.QtBluetooth.QBluetoothAddress, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...
    @overload
    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def discoveredDevices(self) -> List[PySide6.QtBluetooth.QBluetoothDeviceInfo]: ...
    def error(self) -> PySide6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.Error: ...
    def errorString(self) -> str: ...
    def isActive(self) -> bool: ...
    def lowEnergyDiscoveryTimeout(self) -> int: ...
    def setLowEnergyDiscoveryTimeout(self, msTimeout: int) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...


class QBluetoothDeviceInfo(Shiboken.Object):

    UnknownCoreConfiguration : QBluetoothDeviceInfo.CoreConfiguration = ... # 0x0
    LowEnergyCoreConfiguration: QBluetoothDeviceInfo.CoreConfiguration = ... # 0x1
    BaseRateCoreConfiguration: QBluetoothDeviceInfo.CoreConfiguration = ... # 0x2
    BaseRateAndLowEnergyCoreConfiguration: QBluetoothDeviceInfo.CoreConfiguration = ... # 0x3
    MiscellaneousDevice      : QBluetoothDeviceInfo.MajorDeviceClass = ... # 0x0
    ComputerDevice           : QBluetoothDeviceInfo.MajorDeviceClass = ... # 0x1
    PhoneDevice              : QBluetoothDeviceInfo.MajorDeviceClass = ... # 0x2
    NetworkDevice            : QBluetoothDeviceInfo.MajorDeviceClass = ... # 0x3
    AudioVideoDevice         : QBluetoothDeviceInfo.MajorDeviceClass = ... # 0x4
    PeripheralDevice         : QBluetoothDeviceInfo.MajorDeviceClass = ... # 0x5
    ImagingDevice            : QBluetoothDeviceInfo.MajorDeviceClass = ... # 0x6
    WearableDevice           : QBluetoothDeviceInfo.MajorDeviceClass = ... # 0x7
    ToyDevice                : QBluetoothDeviceInfo.MajorDeviceClass = ... # 0x8
    HealthDevice             : QBluetoothDeviceInfo.MajorDeviceClass = ... # 0x9
    UncategorizedDevice      : QBluetoothDeviceInfo.MajorDeviceClass = ... # 0x1f
    UncategorizedAudioVideoDevice: QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0x0
    WearableHeadsetDevice    : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0x1
    HandsFreeDevice          : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0x2
    Microphone               : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0x4
    Loudspeaker              : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0x5
    Headphones               : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0x6
    PortableAudioDevice      : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0x7
    CarAudio                 : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0x8
    SetTopBox                : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0x9
    HiFiAudioDevice          : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0xa
    Vcr                      : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0xb
    VideoCamera              : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0xc
    Camcorder                : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0xd
    VideoMonitor             : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0xe
    VideoDisplayAndLoudspeaker: QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0xf
    VideoConferencing        : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0x10
    GamingDevice             : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0x12
    UncategorizedComputer    : QBluetoothDeviceInfo.MinorComputerClass = ... # 0x0
    DesktopComputer          : QBluetoothDeviceInfo.MinorComputerClass = ... # 0x1
    ServerComputer           : QBluetoothDeviceInfo.MinorComputerClass = ... # 0x2
    LaptopComputer           : QBluetoothDeviceInfo.MinorComputerClass = ... # 0x3
    HandheldClamShellComputer: QBluetoothDeviceInfo.MinorComputerClass = ... # 0x4
    HandheldComputer         : QBluetoothDeviceInfo.MinorComputerClass = ... # 0x5
    WearableComputer         : QBluetoothDeviceInfo.MinorComputerClass = ... # 0x6
    UncategorizedHealthDevice: QBluetoothDeviceInfo.MinorHealthClass = ... # 0x0
    HealthBloodPressureMonitor: QBluetoothDeviceInfo.MinorHealthClass = ... # 0x1
    HealthThermometer        : QBluetoothDeviceInfo.MinorHealthClass = ... # 0x2
    HealthWeightScale        : QBluetoothDeviceInfo.MinorHealthClass = ... # 0x3
    HealthGlucoseMeter       : QBluetoothDeviceInfo.MinorHealthClass = ... # 0x4
    HealthPulseOximeter      : QBluetoothDeviceInfo.MinorHealthClass = ... # 0x5
    HealthDataDisplay        : QBluetoothDeviceInfo.MinorHealthClass = ... # 0x7
    HealthStepCounter        : QBluetoothDeviceInfo.MinorHealthClass = ... # 0x8
    UncategorizedImagingDevice: QBluetoothDeviceInfo.MinorImagingClass = ... # 0x0
    ImageDisplay             : QBluetoothDeviceInfo.MinorImagingClass = ... # 0x4
    ImageCamera              : QBluetoothDeviceInfo.MinorImagingClass = ... # 0x8
    ImageScanner             : QBluetoothDeviceInfo.MinorImagingClass = ... # 0x10
    ImagePrinter             : QBluetoothDeviceInfo.MinorImagingClass = ... # 0x20
    UncategorizedMiscellaneous: QBluetoothDeviceInfo.MinorMiscellaneousClass = ... # 0x0
    NetworkFullService       : QBluetoothDeviceInfo.MinorNetworkClass = ... # 0x0
    NetworkLoadFactorOne     : QBluetoothDeviceInfo.MinorNetworkClass = ... # 0x8
    NetworkLoadFactorTwo     : QBluetoothDeviceInfo.MinorNetworkClass = ... # 0x10
    NetworkLoadFactorThree   : QBluetoothDeviceInfo.MinorNetworkClass = ... # 0x18
    NetworkLoadFactorFour    : QBluetoothDeviceInfo.MinorNetworkClass = ... # 0x20
    NetworkLoadFactorFive    : QBluetoothDeviceInfo.MinorNetworkClass = ... # 0x28
    NetworkLoadFactorSix     : QBluetoothDeviceInfo.MinorNetworkClass = ... # 0x30
    NetworkNoService         : QBluetoothDeviceInfo.MinorNetworkClass = ... # 0x38
    UncategorizedPeripheral  : QBluetoothDeviceInfo.MinorPeripheralClass = ... # 0x0
    JoystickPeripheral       : QBluetoothDeviceInfo.MinorPeripheralClass = ... # 0x1
    GamepadPeripheral        : QBluetoothDeviceInfo.MinorPeripheralClass = ... # 0x2
    RemoteControlPeripheral  : QBluetoothDeviceInfo.MinorPeripheralClass = ... # 0x3
    SensingDevicePeripheral  : QBluetoothDeviceInfo.MinorPeripheralClass = ... # 0x4
    DigitizerTabletPeripheral: QBluetoothDeviceInfo.MinorPeripheralClass = ... # 0x5
    CardReaderPeripheral     : QBluetoothDeviceInfo.MinorPeripheralClass = ... # 0x6
    KeyboardPeripheral       : QBluetoothDeviceInfo.MinorPeripheralClass = ... # 0x10
    PointingDevicePeripheral : QBluetoothDeviceInfo.MinorPeripheralClass = ... # 0x20
    KeyboardWithPointingDevicePeripheral: QBluetoothDeviceInfo.MinorPeripheralClass = ... # 0x30
    UncategorizedPhone       : QBluetoothDeviceInfo.MinorPhoneClass = ... # 0x0
    CellularPhone            : QBluetoothDeviceInfo.MinorPhoneClass = ... # 0x1
    CordlessPhone            : QBluetoothDeviceInfo.MinorPhoneClass = ... # 0x2
    SmartPhone               : QBluetoothDeviceInfo.MinorPhoneClass = ... # 0x3
    WiredModemOrVoiceGatewayPhone: QBluetoothDeviceInfo.MinorPhoneClass = ... # 0x4
    CommonIsdnAccessPhone    : QBluetoothDeviceInfo.MinorPhoneClass = ... # 0x5
    UncategorizedToy         : QBluetoothDeviceInfo.MinorToyClass = ... # 0x0
    ToyRobot                 : QBluetoothDeviceInfo.MinorToyClass = ... # 0x1
    ToyVehicle               : QBluetoothDeviceInfo.MinorToyClass = ... # 0x2
    ToyDoll                  : QBluetoothDeviceInfo.MinorToyClass = ... # 0x3
    ToyController            : QBluetoothDeviceInfo.MinorToyClass = ... # 0x4
    ToyGame                  : QBluetoothDeviceInfo.MinorToyClass = ... # 0x5
    UncategorizedWearableDevice: QBluetoothDeviceInfo.MinorWearableClass = ... # 0x0
    WearableWristWatch       : QBluetoothDeviceInfo.MinorWearableClass = ... # 0x1
    WearablePager            : QBluetoothDeviceInfo.MinorWearableClass = ... # 0x2
    WearableJacket           : QBluetoothDeviceInfo.MinorWearableClass = ... # 0x3
    WearableHelmet           : QBluetoothDeviceInfo.MinorWearableClass = ... # 0x4
    WearableGlasses          : QBluetoothDeviceInfo.MinorWearableClass = ... # 0x5
    NoService                : QBluetoothDeviceInfo.ServiceClass = ... # 0x0
    PositioningService       : QBluetoothDeviceInfo.ServiceClass = ... # 0x1
    NetworkingService        : QBluetoothDeviceInfo.ServiceClass = ... # 0x2
    RenderingService         : QBluetoothDeviceInfo.ServiceClass = ... # 0x4
    CapturingService         : QBluetoothDeviceInfo.ServiceClass = ... # 0x8
    ObjectTransferService    : QBluetoothDeviceInfo.ServiceClass = ... # 0x10
    AudioService             : QBluetoothDeviceInfo.ServiceClass = ... # 0x20
    TelephonyService         : QBluetoothDeviceInfo.ServiceClass = ... # 0x40
    InformationService       : QBluetoothDeviceInfo.ServiceClass = ... # 0x80
    AllServices              : QBluetoothDeviceInfo.ServiceClass = ... # 0x7ff

    class CoreConfiguration(Shiboken.Enum):

        UnknownCoreConfiguration : QBluetoothDeviceInfo.CoreConfiguration = ... # 0x0
        LowEnergyCoreConfiguration: QBluetoothDeviceInfo.CoreConfiguration = ... # 0x1
        BaseRateCoreConfiguration: QBluetoothDeviceInfo.CoreConfiguration = ... # 0x2
        BaseRateAndLowEnergyCoreConfiguration: QBluetoothDeviceInfo.CoreConfiguration = ... # 0x3

    class CoreConfigurations(object): ...

    class Field(Shiboken.Enum):

        None_                    : QBluetoothDeviceInfo.Field = ... # 0x0
        RSSI                     : QBluetoothDeviceInfo.Field = ... # 0x1
        ManufacturerData         : QBluetoothDeviceInfo.Field = ... # 0x2
        ServiceData              : QBluetoothDeviceInfo.Field = ... # 0x4
        All                      : QBluetoothDeviceInfo.Field = ... # 0x7fff

    class Fields(object): ...

    class MajorDeviceClass(Shiboken.Enum):

        MiscellaneousDevice      : QBluetoothDeviceInfo.MajorDeviceClass = ... # 0x0
        ComputerDevice           : QBluetoothDeviceInfo.MajorDeviceClass = ... # 0x1
        PhoneDevice              : QBluetoothDeviceInfo.MajorDeviceClass = ... # 0x2
        NetworkDevice            : QBluetoothDeviceInfo.MajorDeviceClass = ... # 0x3
        AudioVideoDevice         : QBluetoothDeviceInfo.MajorDeviceClass = ... # 0x4
        PeripheralDevice         : QBluetoothDeviceInfo.MajorDeviceClass = ... # 0x5
        ImagingDevice            : QBluetoothDeviceInfo.MajorDeviceClass = ... # 0x6
        WearableDevice           : QBluetoothDeviceInfo.MajorDeviceClass = ... # 0x7
        ToyDevice                : QBluetoothDeviceInfo.MajorDeviceClass = ... # 0x8
        HealthDevice             : QBluetoothDeviceInfo.MajorDeviceClass = ... # 0x9
        UncategorizedDevice      : QBluetoothDeviceInfo.MajorDeviceClass = ... # 0x1f

    class MinorAudioVideoClass(Shiboken.Enum):

        UncategorizedAudioVideoDevice: QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0x0
        WearableHeadsetDevice    : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0x1
        HandsFreeDevice          : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0x2
        Microphone               : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0x4
        Loudspeaker              : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0x5
        Headphones               : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0x6
        PortableAudioDevice      : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0x7
        CarAudio                 : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0x8
        SetTopBox                : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0x9
        HiFiAudioDevice          : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0xa
        Vcr                      : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0xb
        VideoCamera              : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0xc
        Camcorder                : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0xd
        VideoMonitor             : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0xe
        VideoDisplayAndLoudspeaker: QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0xf
        VideoConferencing        : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0x10
        GamingDevice             : QBluetoothDeviceInfo.MinorAudioVideoClass = ... # 0x12

    class MinorComputerClass(Shiboken.Enum):

        UncategorizedComputer    : QBluetoothDeviceInfo.MinorComputerClass = ... # 0x0
        DesktopComputer          : QBluetoothDeviceInfo.MinorComputerClass = ... # 0x1
        ServerComputer           : QBluetoothDeviceInfo.MinorComputerClass = ... # 0x2
        LaptopComputer           : QBluetoothDeviceInfo.MinorComputerClass = ... # 0x3
        HandheldClamShellComputer: QBluetoothDeviceInfo.MinorComputerClass = ... # 0x4
        HandheldComputer         : QBluetoothDeviceInfo.MinorComputerClass = ... # 0x5
        WearableComputer         : QBluetoothDeviceInfo.MinorComputerClass = ... # 0x6

    class MinorHealthClass(Shiboken.Enum):

        UncategorizedHealthDevice: QBluetoothDeviceInfo.MinorHealthClass = ... # 0x0
        HealthBloodPressureMonitor: QBluetoothDeviceInfo.MinorHealthClass = ... # 0x1
        HealthThermometer        : QBluetoothDeviceInfo.MinorHealthClass = ... # 0x2
        HealthWeightScale        : QBluetoothDeviceInfo.MinorHealthClass = ... # 0x3
        HealthGlucoseMeter       : QBluetoothDeviceInfo.MinorHealthClass = ... # 0x4
        HealthPulseOximeter      : QBluetoothDeviceInfo.MinorHealthClass = ... # 0x5
        HealthDataDisplay        : QBluetoothDeviceInfo.MinorHealthClass = ... # 0x7
        HealthStepCounter        : QBluetoothDeviceInfo.MinorHealthClass = ... # 0x8

    class MinorImagingClass(Shiboken.Enum):

        UncategorizedImagingDevice: QBluetoothDeviceInfo.MinorImagingClass = ... # 0x0
        ImageDisplay             : QBluetoothDeviceInfo.MinorImagingClass = ... # 0x4
        ImageCamera              : QBluetoothDeviceInfo.MinorImagingClass = ... # 0x8
        ImageScanner             : QBluetoothDeviceInfo.MinorImagingClass = ... # 0x10
        ImagePrinter             : QBluetoothDeviceInfo.MinorImagingClass = ... # 0x20

    class MinorMiscellaneousClass(Shiboken.Enum):

        UncategorizedMiscellaneous: QBluetoothDeviceInfo.MinorMiscellaneousClass = ... # 0x0

    class MinorNetworkClass(Shiboken.Enum):

        NetworkFullService       : QBluetoothDeviceInfo.MinorNetworkClass = ... # 0x0
        NetworkLoadFactorOne     : QBluetoothDeviceInfo.MinorNetworkClass = ... # 0x8
        NetworkLoadFactorTwo     : QBluetoothDeviceInfo.MinorNetworkClass = ... # 0x10
        NetworkLoadFactorThree   : QBluetoothDeviceInfo.MinorNetworkClass = ... # 0x18
        NetworkLoadFactorFour    : QBluetoothDeviceInfo.MinorNetworkClass = ... # 0x20
        NetworkLoadFactorFive    : QBluetoothDeviceInfo.MinorNetworkClass = ... # 0x28
        NetworkLoadFactorSix     : QBluetoothDeviceInfo.MinorNetworkClass = ... # 0x30
        NetworkNoService         : QBluetoothDeviceInfo.MinorNetworkClass = ... # 0x38

    class MinorPeripheralClass(Shiboken.Enum):

        UncategorizedPeripheral  : QBluetoothDeviceInfo.MinorPeripheralClass = ... # 0x0
        JoystickPeripheral       : QBluetoothDeviceInfo.MinorPeripheralClass = ... # 0x1
        GamepadPeripheral        : QBluetoothDeviceInfo.MinorPeripheralClass = ... # 0x2
        RemoteControlPeripheral  : QBluetoothDeviceInfo.MinorPeripheralClass = ... # 0x3
        SensingDevicePeripheral  : QBluetoothDeviceInfo.MinorPeripheralClass = ... # 0x4
        DigitizerTabletPeripheral: QBluetoothDeviceInfo.MinorPeripheralClass = ... # 0x5
        CardReaderPeripheral     : QBluetoothDeviceInfo.MinorPeripheralClass = ... # 0x6
        KeyboardPeripheral       : QBluetoothDeviceInfo.MinorPeripheralClass = ... # 0x10
        PointingDevicePeripheral : QBluetoothDeviceInfo.MinorPeripheralClass = ... # 0x20
        KeyboardWithPointingDevicePeripheral: QBluetoothDeviceInfo.MinorPeripheralClass = ... # 0x30

    class MinorPhoneClass(Shiboken.Enum):

        UncategorizedPhone       : QBluetoothDeviceInfo.MinorPhoneClass = ... # 0x0
        CellularPhone            : QBluetoothDeviceInfo.MinorPhoneClass = ... # 0x1
        CordlessPhone            : QBluetoothDeviceInfo.MinorPhoneClass = ... # 0x2
        SmartPhone               : QBluetoothDeviceInfo.MinorPhoneClass = ... # 0x3
        WiredModemOrVoiceGatewayPhone: QBluetoothDeviceInfo.MinorPhoneClass = ... # 0x4
        CommonIsdnAccessPhone    : QBluetoothDeviceInfo.MinorPhoneClass = ... # 0x5

    class MinorToyClass(Shiboken.Enum):

        UncategorizedToy         : QBluetoothDeviceInfo.MinorToyClass = ... # 0x0
        ToyRobot                 : QBluetoothDeviceInfo.MinorToyClass = ... # 0x1
        ToyVehicle               : QBluetoothDeviceInfo.MinorToyClass = ... # 0x2
        ToyDoll                  : QBluetoothDeviceInfo.MinorToyClass = ... # 0x3
        ToyController            : QBluetoothDeviceInfo.MinorToyClass = ... # 0x4
        ToyGame                  : QBluetoothDeviceInfo.MinorToyClass = ... # 0x5

    class MinorWearableClass(Shiboken.Enum):

        UncategorizedWearableDevice: QBluetoothDeviceInfo.MinorWearableClass = ... # 0x0
        WearableWristWatch       : QBluetoothDeviceInfo.MinorWearableClass = ... # 0x1
        WearablePager            : QBluetoothDeviceInfo.MinorWearableClass = ... # 0x2
        WearableJacket           : QBluetoothDeviceInfo.MinorWearableClass = ... # 0x3
        WearableHelmet           : QBluetoothDeviceInfo.MinorWearableClass = ... # 0x4
        WearableGlasses          : QBluetoothDeviceInfo.MinorWearableClass = ... # 0x5

    class ServiceClass(Shiboken.Enum):

        NoService                : QBluetoothDeviceInfo.ServiceClass = ... # 0x0
        PositioningService       : QBluetoothDeviceInfo.ServiceClass = ... # 0x1
        NetworkingService        : QBluetoothDeviceInfo.ServiceClass = ... # 0x2
        RenderingService         : QBluetoothDeviceInfo.ServiceClass = ... # 0x4
        CapturingService         : QBluetoothDeviceInfo.ServiceClass = ... # 0x8
        ObjectTransferService    : QBluetoothDeviceInfo.ServiceClass = ... # 0x10
        AudioService             : QBluetoothDeviceInfo.ServiceClass = ... # 0x20
        TelephonyService         : QBluetoothDeviceInfo.ServiceClass = ... # 0x40
        InformationService       : QBluetoothDeviceInfo.ServiceClass = ... # 0x80
        AllServices              : QBluetoothDeviceInfo.ServiceClass = ... # 0x7ff

    class ServiceClasses(object): ...


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, address: PySide6.QtBluetooth.QBluetoothAddress, name: str, classOfDevice: int) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtBluetooth.QBluetoothDeviceInfo) -> None: ...
    @overload
    def __init__(self, uuid: Union[PySide6.QtBluetooth.QBluetoothUuid, PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType, PySide6.QtBluetooth.QBluetoothUuid.DescriptorType, PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid, PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid, PySide6.QtCore.QUuid], name: str, classOfDevice: int) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def address(self) -> PySide6.QtBluetooth.QBluetoothAddress: ...
    def coreConfigurations(self) -> PySide6.QtBluetooth.QBluetoothDeviceInfo.CoreConfigurations: ...
    def deviceUuid(self) -> PySide6.QtBluetooth.QBluetoothUuid: ...
    def isCached(self) -> bool: ...
    def isValid(self) -> bool: ...
    def majorDeviceClass(self) -> PySide6.QtBluetooth.QBluetoothDeviceInfo.MajorDeviceClass: ...
    @overload
    def manufacturerData(self) -> Dict[int, PySide6.QtCore.QByteArray]: ...
    @overload
    def manufacturerData(self, manufacturerId: int) -> PySide6.QtCore.QByteArray: ...
    def manufacturerIds(self) -> List[int]: ...
    def minorDeviceClass(self) -> int: ...
    def name(self) -> str: ...
    def rssi(self) -> int: ...
    def serviceClasses(self) -> PySide6.QtBluetooth.QBluetoothDeviceInfo.ServiceClasses: ...
    @overload
    def serviceData(self) -> Dict[PySide6.QtBluetooth.QBluetoothUuid, PySide6.QtCore.QByteArray]: ...
    @overload
    def serviceData(self, serviceId: Union[PySide6.QtBluetooth.QBluetoothUuid, PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType, PySide6.QtBluetooth.QBluetoothUuid.DescriptorType, PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid, PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid, PySide6.QtCore.QUuid]) -> PySide6.QtCore.QByteArray: ...
    def serviceIds(self) -> List[PySide6.QtBluetooth.QBluetoothUuid]: ...
    def serviceUuids(self) -> List[PySide6.QtBluetooth.QBluetoothUuid]: ...
    def setCached(self, cached: bool) -> None: ...
    def setCoreConfigurations(self, coreConfigs: PySide6.QtBluetooth.QBluetoothDeviceInfo.CoreConfigurations) -> None: ...
    def setDeviceUuid(self, uuid: Union[PySide6.QtBluetooth.QBluetoothUuid, PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType, PySide6.QtBluetooth.QBluetoothUuid.DescriptorType, PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid, PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid, PySide6.QtCore.QUuid]) -> None: ...
    def setManufacturerData(self, manufacturerId: int, data: Union[PySide6.QtCore.QByteArray, bytes]) -> bool: ...
    def setName(self, name: str) -> None: ...
    def setRssi(self, signal: int) -> None: ...
    def setServiceData(self, serviceId: Union[PySide6.QtBluetooth.QBluetoothUuid, PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType, PySide6.QtBluetooth.QBluetoothUuid.DescriptorType, PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid, PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid, PySide6.QtCore.QUuid], data: Union[PySide6.QtCore.QByteArray, bytes]) -> bool: ...
    def setServiceUuids(self, uuids: Sequence[PySide6.QtBluetooth.QBluetoothUuid]) -> None: ...


class QBluetoothHostInfo(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtBluetooth.QBluetoothHostInfo) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def address(self) -> PySide6.QtBluetooth.QBluetoothAddress: ...
    def name(self) -> str: ...
    def setAddress(self, address: PySide6.QtBluetooth.QBluetoothAddress) -> None: ...
    def setName(self, name: str) -> None: ...


class QBluetoothLocalDevice(PySide6.QtCore.QObject):

    NoError                  : QBluetoothLocalDevice.Error = ... # 0x0
    PairingError             : QBluetoothLocalDevice.Error = ... # 0x1
    UnknownError             : QBluetoothLocalDevice.Error = ... # 0x64
    HostPoweredOff           : QBluetoothLocalDevice.HostMode = ... # 0x0
    HostConnectable          : QBluetoothLocalDevice.HostMode = ... # 0x1
    HostDiscoverable         : QBluetoothLocalDevice.HostMode = ... # 0x2
    HostDiscoverableLimitedInquiry: QBluetoothLocalDevice.HostMode = ... # 0x3
    Unpaired                 : QBluetoothLocalDevice.Pairing = ... # 0x0
    Paired                   : QBluetoothLocalDevice.Pairing = ... # 0x1
    AuthorizedPaired         : QBluetoothLocalDevice.Pairing = ... # 0x2

    class Error(Shiboken.Enum):

        NoError                  : QBluetoothLocalDevice.Error = ... # 0x0
        PairingError             : QBluetoothLocalDevice.Error = ... # 0x1
        UnknownError             : QBluetoothLocalDevice.Error = ... # 0x64

    class HostMode(Shiboken.Enum):

        HostPoweredOff           : QBluetoothLocalDevice.HostMode = ... # 0x0
        HostConnectable          : QBluetoothLocalDevice.HostMode = ... # 0x1
        HostDiscoverable         : QBluetoothLocalDevice.HostMode = ... # 0x2
        HostDiscoverableLimitedInquiry: QBluetoothLocalDevice.HostMode = ... # 0x3

    class Pairing(Shiboken.Enum):

        Unpaired                 : QBluetoothLocalDevice.Pairing = ... # 0x0
        Paired                   : QBluetoothLocalDevice.Pairing = ... # 0x1
        AuthorizedPaired         : QBluetoothLocalDevice.Pairing = ... # 0x2


    @overload
    def __init__(self, address: PySide6.QtBluetooth.QBluetoothAddress, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...
    @overload
    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def address(self) -> PySide6.QtBluetooth.QBluetoothAddress: ...
    @staticmethod
    def allDevices() -> List[PySide6.QtBluetooth.QBluetoothHostInfo]: ...
    def connectedDevices(self) -> List[PySide6.QtBluetooth.QBluetoothAddress]: ...
    def hostMode(self) -> PySide6.QtBluetooth.QBluetoothLocalDevice.HostMode: ...
    def isValid(self) -> bool: ...
    def name(self) -> str: ...
    def pairingStatus(self, address: PySide6.QtBluetooth.QBluetoothAddress) -> PySide6.QtBluetooth.QBluetoothLocalDevice.Pairing: ...
    def powerOn(self) -> None: ...
    def requestPairing(self, address: PySide6.QtBluetooth.QBluetoothAddress, pairing: PySide6.QtBluetooth.QBluetoothLocalDevice.Pairing) -> None: ...
    def setHostMode(self, mode: PySide6.QtBluetooth.QBluetoothLocalDevice.HostMode) -> None: ...


class QBluetoothServer(PySide6.QtCore.QObject):

    NoError                  : QBluetoothServer.Error = ... # 0x0
    UnknownError             : QBluetoothServer.Error = ... # 0x1
    PoweredOffError          : QBluetoothServer.Error = ... # 0x2
    InputOutputError         : QBluetoothServer.Error = ... # 0x3
    ServiceAlreadyRegisteredError: QBluetoothServer.Error = ... # 0x4
    UnsupportedProtocolError : QBluetoothServer.Error = ... # 0x5

    class Error(Shiboken.Enum):

        NoError                  : QBluetoothServer.Error = ... # 0x0
        UnknownError             : QBluetoothServer.Error = ... # 0x1
        PoweredOffError          : QBluetoothServer.Error = ... # 0x2
        InputOutputError         : QBluetoothServer.Error = ... # 0x3
        ServiceAlreadyRegisteredError: QBluetoothServer.Error = ... # 0x4
        UnsupportedProtocolError : QBluetoothServer.Error = ... # 0x5


    def __init__(self, serverType: PySide6.QtBluetooth.QBluetoothServiceInfo.Protocol, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def close(self) -> None: ...
    def error(self) -> PySide6.QtBluetooth.QBluetoothServer.Error: ...
    def hasPendingConnections(self) -> bool: ...
    def isListening(self) -> bool: ...
    @overload
    def listen(self, address: PySide6.QtBluetooth.QBluetoothAddress = ..., port: int = ...) -> bool: ...
    @overload
    def listen(self, uuid: Union[PySide6.QtBluetooth.QBluetoothUuid, PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType, PySide6.QtBluetooth.QBluetoothUuid.DescriptorType, PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid, PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid, PySide6.QtCore.QUuid], serviceName: str = ...) -> PySide6.QtBluetooth.QBluetoothServiceInfo: ...
    def maxPendingConnections(self) -> int: ...
    def nextPendingConnection(self) -> PySide6.QtBluetooth.QBluetoothSocket: ...
    def securityFlags(self) -> PySide6.QtBluetooth.QBluetooth.SecurityFlags: ...
    def serverAddress(self) -> PySide6.QtBluetooth.QBluetoothAddress: ...
    def serverPort(self) -> int: ...
    def serverType(self) -> PySide6.QtBluetooth.QBluetoothServiceInfo.Protocol: ...
    def setMaxPendingConnections(self, numConnections: int) -> None: ...
    def setSecurityFlags(self, security: PySide6.QtBluetooth.QBluetooth.SecurityFlags) -> None: ...


class QBluetoothServiceDiscoveryAgent(PySide6.QtCore.QObject):

    MinimalDiscovery         : QBluetoothServiceDiscoveryAgent.DiscoveryMode = ... # 0x0
    FullDiscovery            : QBluetoothServiceDiscoveryAgent.DiscoveryMode = ... # 0x1
    NoError                  : QBluetoothServiceDiscoveryAgent.Error = ... # 0x0
    InputOutputError         : QBluetoothServiceDiscoveryAgent.Error = ... # 0x1
    PoweredOffError          : QBluetoothServiceDiscoveryAgent.Error = ... # 0x2
    InvalidBluetoothAdapterError: QBluetoothServiceDiscoveryAgent.Error = ... # 0x3
    UnknownError             : QBluetoothServiceDiscoveryAgent.Error = ... # 0x64

    class DiscoveryMode(Shiboken.Enum):

        MinimalDiscovery         : QBluetoothServiceDiscoveryAgent.DiscoveryMode = ... # 0x0
        FullDiscovery            : QBluetoothServiceDiscoveryAgent.DiscoveryMode = ... # 0x1

    class Error(Shiboken.Enum):

        NoError                  : QBluetoothServiceDiscoveryAgent.Error = ... # 0x0
        InputOutputError         : QBluetoothServiceDiscoveryAgent.Error = ... # 0x1
        PoweredOffError          : QBluetoothServiceDiscoveryAgent.Error = ... # 0x2
        InvalidBluetoothAdapterError: QBluetoothServiceDiscoveryAgent.Error = ... # 0x3
        UnknownError             : QBluetoothServiceDiscoveryAgent.Error = ... # 0x64


    @overload
    def __init__(self, deviceAdapter: PySide6.QtBluetooth.QBluetoothAddress, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...
    @overload
    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def clear(self) -> None: ...
    def discoveredServices(self) -> List[PySide6.QtBluetooth.QBluetoothServiceInfo]: ...
    def error(self) -> PySide6.QtBluetooth.QBluetoothServiceDiscoveryAgent.Error: ...
    def errorString(self) -> str: ...
    def isActive(self) -> bool: ...
    def remoteAddress(self) -> PySide6.QtBluetooth.QBluetoothAddress: ...
    def setRemoteAddress(self, address: PySide6.QtBluetooth.QBluetoothAddress) -> bool: ...
    @overload
    def setUuidFilter(self, uuid: Union[PySide6.QtBluetooth.QBluetoothUuid, PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType, PySide6.QtBluetooth.QBluetoothUuid.DescriptorType, PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid, PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid, PySide6.QtCore.QUuid]) -> None: ...
    @overload
    def setUuidFilter(self, uuids: Sequence[PySide6.QtBluetooth.QBluetoothUuid]) -> None: ...
    def start(self, mode: PySide6.QtBluetooth.QBluetoothServiceDiscoveryAgent.DiscoveryMode = ...) -> None: ...
    def stop(self) -> None: ...
    def uuidFilter(self) -> List[PySide6.QtBluetooth.QBluetoothUuid]: ...


class QBluetoothServiceInfo(Shiboken.Object):

    ServiceRecordHandle      : QBluetoothServiceInfo.AttributeId = ... # 0x0
    ServiceClassIds          : QBluetoothServiceInfo.AttributeId = ... # 0x1
    ServiceRecordState       : QBluetoothServiceInfo.AttributeId = ... # 0x2
    ServiceId                : QBluetoothServiceInfo.AttributeId = ... # 0x3
    ProtocolDescriptorList   : QBluetoothServiceInfo.AttributeId = ... # 0x4
    BrowseGroupList          : QBluetoothServiceInfo.AttributeId = ... # 0x5
    LanguageBaseAttributeIdList: QBluetoothServiceInfo.AttributeId = ... # 0x6
    ServiceInfoTimeToLive    : QBluetoothServiceInfo.AttributeId = ... # 0x7
    ServiceAvailability      : QBluetoothServiceInfo.AttributeId = ... # 0x8
    BluetoothProfileDescriptorList: QBluetoothServiceInfo.AttributeId = ... # 0x9
    DocumentationUrl         : QBluetoothServiceInfo.AttributeId = ... # 0xa
    ClientExecutableUrl      : QBluetoothServiceInfo.AttributeId = ... # 0xb
    IconUrl                  : QBluetoothServiceInfo.AttributeId = ... # 0xc
    AdditionalProtocolDescriptorList: QBluetoothServiceInfo.AttributeId = ... # 0xd
    PrimaryLanguageBase      : QBluetoothServiceInfo.AttributeId = ... # 0x100
    ServiceName              : QBluetoothServiceInfo.AttributeId = ... # 0x100
    ServiceDescription       : QBluetoothServiceInfo.AttributeId = ... # 0x101
    ServiceProvider          : QBluetoothServiceInfo.AttributeId = ... # 0x102
    UnknownProtocol          : QBluetoothServiceInfo.Protocol = ... # 0x0
    L2capProtocol            : QBluetoothServiceInfo.Protocol = ... # 0x1
    RfcommProtocol           : QBluetoothServiceInfo.Protocol = ... # 0x2

    class Alternative(Shiboken.Object):

        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, Alternative: Union[PySide6.QtBluetooth.QBluetoothServiceInfo.Alternative, Sequence[Any]]) -> None: ...
        @overload
        def __init__(self, list: Sequence[Any]) -> None: ...

        def __add__(self, l: Sequence[Any]) -> List[Any]: ...
        @staticmethod
        def __copy__() -> None: ...
        def __iadd__(self, l: Sequence[Any]) -> List[Any]: ...
        def __lshift__(self, l: Sequence[Any]) -> List[Any]: ...
        @overload
        def append(self, arg__1: Any) -> None: ...
        @overload
        def append(self, l: Sequence[Any]) -> None: ...
        def at(self, i: int) -> Any: ...
        def back(self) -> Any: ...
        def capacity(self) -> int: ...
        def clear(self) -> None: ...
        def constData(self) -> object: ...
        def constFirst(self) -> Any: ...
        def constLast(self) -> Any: ...
        def count(self) -> int: ...
        def data(self) -> object: ...
        def empty(self) -> bool: ...
        @overload
        def first(self) -> Any: ...
        @overload
        def first(self, n: int) -> List[Any]: ...
        @staticmethod
        def fromList(list: Sequence[Any]) -> List[Any]: ...
        @staticmethod
        def fromVector(vector: Sequence[Any]) -> List[Any]: ...
        def front(self) -> Any: ...
        def insert(self, arg__1: int, arg__2: Any) -> None: ...
        def isEmpty(self) -> bool: ...
        def isSharedWith(self, other: Sequence[Any]) -> bool: ...
        @overload
        def last(self) -> Any: ...
        @overload
        def last(self, n: int) -> List[Any]: ...
        def length(self) -> int: ...
        def mid(self, pos: int, len: int = ...) -> List[Any]: ...
        def move(self, from_: int, to: int) -> None: ...
        def pop_back(self) -> None: ...
        def pop_front(self) -> None: ...
        def prepend(self, arg__1: Any) -> None: ...
        def push_back(self, arg__1: Any) -> None: ...
        def push_front(self, arg__1: Any) -> None: ...
        def remove(self, i: int, n: int = ...) -> None: ...
        def removeAll(self, arg__1: Any) -> None: ...
        def removeAt(self, i: int) -> None: ...
        def removeFirst(self) -> None: ...
        def removeLast(self) -> None: ...
        def removeOne(self, arg__1: Any) -> None: ...
        def reserve(self, size: int) -> None: ...
        def resize(self, size: int) -> None: ...
        def shrink_to_fit(self) -> None: ...
        def size(self) -> int: ...
        @overload
        def sliced(self, pos: int) -> List[Any]: ...
        @overload
        def sliced(self, pos: int, n: int) -> List[Any]: ...
        def squeeze(self) -> None: ...
        def swap(self, other: Sequence[Any]) -> None: ...
        def swapItemsAt(self, i: int, j: int) -> None: ...
        def takeAt(self, i: int) -> Any: ...
        def toList(self) -> List[Any]: ...
        def toVector(self) -> List[Any]: ...
        def value(self, i: int) -> Any: ...

    class AttributeId(Shiboken.Enum):

        ServiceRecordHandle      : QBluetoothServiceInfo.AttributeId = ... # 0x0
        ServiceClassIds          : QBluetoothServiceInfo.AttributeId = ... # 0x1
        ServiceRecordState       : QBluetoothServiceInfo.AttributeId = ... # 0x2
        ServiceId                : QBluetoothServiceInfo.AttributeId = ... # 0x3
        ProtocolDescriptorList   : QBluetoothServiceInfo.AttributeId = ... # 0x4
        BrowseGroupList          : QBluetoothServiceInfo.AttributeId = ... # 0x5
        LanguageBaseAttributeIdList: QBluetoothServiceInfo.AttributeId = ... # 0x6
        ServiceInfoTimeToLive    : QBluetoothServiceInfo.AttributeId = ... # 0x7
        ServiceAvailability      : QBluetoothServiceInfo.AttributeId = ... # 0x8
        BluetoothProfileDescriptorList: QBluetoothServiceInfo.AttributeId = ... # 0x9
        DocumentationUrl         : QBluetoothServiceInfo.AttributeId = ... # 0xa
        ClientExecutableUrl      : QBluetoothServiceInfo.AttributeId = ... # 0xb
        IconUrl                  : QBluetoothServiceInfo.AttributeId = ... # 0xc
        AdditionalProtocolDescriptorList: QBluetoothServiceInfo.AttributeId = ... # 0xd
        PrimaryLanguageBase      : QBluetoothServiceInfo.AttributeId = ... # 0x100
        ServiceName              : QBluetoothServiceInfo.AttributeId = ... # 0x100
        ServiceDescription       : QBluetoothServiceInfo.AttributeId = ... # 0x101
        ServiceProvider          : QBluetoothServiceInfo.AttributeId = ... # 0x102

    class Protocol(Shiboken.Enum):

        UnknownProtocol          : QBluetoothServiceInfo.Protocol = ... # 0x0
        L2capProtocol            : QBluetoothServiceInfo.Protocol = ... # 0x1
        RfcommProtocol           : QBluetoothServiceInfo.Protocol = ... # 0x2

    class Sequence(Shiboken.Object):

        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, Sequence: Union[PySide6.QtBluetooth.QBluetoothServiceInfo.Sequence, Sequence[Any]]) -> None: ...
        @overload
        def __init__(self, list: Sequence[Any]) -> None: ...

        def __add__(self, l: Sequence[Any]) -> List[Any]: ...
        @staticmethod
        def __copy__() -> None: ...
        def __iadd__(self, l: Sequence[Any]) -> List[Any]: ...
        def __lshift__(self, l: Sequence[Any]) -> List[Any]: ...
        @overload
        def append(self, arg__1: Any) -> None: ...
        @overload
        def append(self, l: Sequence[Any]) -> None: ...
        def at(self, i: int) -> Any: ...
        def back(self) -> Any: ...
        def capacity(self) -> int: ...
        def clear(self) -> None: ...
        def constData(self) -> object: ...
        def constFirst(self) -> Any: ...
        def constLast(self) -> Any: ...
        def count(self) -> int: ...
        def data(self) -> object: ...
        def empty(self) -> bool: ...
        @overload
        def first(self) -> Any: ...
        @overload
        def first(self, n: int) -> List[Any]: ...
        @staticmethod
        def fromList(list: Sequence[Any]) -> List[Any]: ...
        @staticmethod
        def fromVector(vector: Sequence[Any]) -> List[Any]: ...
        def front(self) -> Any: ...
        def insert(self, arg__1: int, arg__2: Any) -> None: ...
        def isEmpty(self) -> bool: ...
        def isSharedWith(self, other: Sequence[Any]) -> bool: ...
        @overload
        def last(self) -> Any: ...
        @overload
        def last(self, n: int) -> List[Any]: ...
        def length(self) -> int: ...
        def mid(self, pos: int, len: int = ...) -> List[Any]: ...
        def move(self, from_: int, to: int) -> None: ...
        def pop_back(self) -> None: ...
        def pop_front(self) -> None: ...
        def prepend(self, arg__1: Any) -> None: ...
        def push_back(self, arg__1: Any) -> None: ...
        def push_front(self, arg__1: Any) -> None: ...
        def remove(self, i: int, n: int = ...) -> None: ...
        def removeAll(self, arg__1: Any) -> None: ...
        def removeAt(self, i: int) -> None: ...
        def removeFirst(self) -> None: ...
        def removeLast(self) -> None: ...
        def removeOne(self, arg__1: Any) -> None: ...
        def reserve(self, size: int) -> None: ...
        def resize(self, size: int) -> None: ...
        def shrink_to_fit(self) -> None: ...
        def size(self) -> int: ...
        @overload
        def sliced(self, pos: int) -> List[Any]: ...
        @overload
        def sliced(self, pos: int, n: int) -> List[Any]: ...
        def squeeze(self) -> None: ...
        def swap(self, other: Sequence[Any]) -> None: ...
        def swapItemsAt(self, i: int, j: int) -> None: ...
        def takeAt(self, i: int) -> Any: ...
        def toList(self) -> List[Any]: ...
        def toVector(self) -> List[Any]: ...
        def value(self, i: int) -> Any: ...


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtBluetooth.QBluetoothServiceInfo) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def attribute(self, attributeId: int) -> Any: ...
    def attributes(self) -> List[int]: ...
    def contains(self, attributeId: int) -> bool: ...
    def device(self) -> PySide6.QtBluetooth.QBluetoothDeviceInfo: ...
    def isComplete(self) -> bool: ...
    def isRegistered(self) -> bool: ...
    def isValid(self) -> bool: ...
    def protocolDescriptor(self, protocol: PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid) -> PySide6.QtBluetooth.QBluetoothServiceInfo.Sequence: ...
    def protocolServiceMultiplexer(self) -> int: ...
    def registerService(self, localAdapter: PySide6.QtBluetooth.QBluetoothAddress = ...) -> bool: ...
    def removeAttribute(self, attributeId: int) -> None: ...
    def serverChannel(self) -> int: ...
    def serviceAvailability(self) -> int: ...
    def serviceClassUuids(self) -> List[PySide6.QtBluetooth.QBluetoothUuid]: ...
    def serviceDescription(self) -> str: ...
    def serviceName(self) -> str: ...
    def serviceProvider(self) -> str: ...
    def serviceUuid(self) -> PySide6.QtBluetooth.QBluetoothUuid: ...
    @overload
    def setAttribute(self, attributeId: int, value: Any) -> None: ...
    @overload
    def setAttribute(self, attributeId: int, value: Union[PySide6.QtBluetooth.QBluetoothServiceInfo.Alternative, Sequence[Any]]) -> None: ...
    @overload
    def setAttribute(self, attributeId: int, value: Union[PySide6.QtBluetooth.QBluetoothServiceInfo.Sequence, Sequence[Any]]) -> None: ...
    @overload
    def setAttribute(self, attributeId: int, value: Union[PySide6.QtBluetooth.QBluetoothUuid, PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType, PySide6.QtBluetooth.QBluetoothUuid.DescriptorType, PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid, PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid, PySide6.QtCore.QUuid]) -> None: ...
    def setDevice(self, info: PySide6.QtBluetooth.QBluetoothDeviceInfo) -> None: ...
    def setServiceAvailability(self, availability: int) -> None: ...
    def setServiceDescription(self, description: str) -> None: ...
    def setServiceName(self, name: str) -> None: ...
    def setServiceProvider(self, provider: str) -> None: ...
    def setServiceUuid(self, uuid: Union[PySide6.QtBluetooth.QBluetoothUuid, PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType, PySide6.QtBluetooth.QBluetoothUuid.DescriptorType, PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid, PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid, PySide6.QtCore.QUuid]) -> None: ...
    def socketProtocol(self) -> PySide6.QtBluetooth.QBluetoothServiceInfo.Protocol: ...
    def unregisterService(self) -> bool: ...


class QBluetoothSocket(PySide6.QtCore.QIODevice):

    class SocketError(Shiboken.Enum):

        NoSocketError            : QBluetoothSocket.SocketError = ... # 0x0
        UnknownSocketError       : QBluetoothSocket.SocketError = ... # 0x1
        RemoteHostClosedError    : QBluetoothSocket.SocketError = ... # 0x2
        HostNotFoundError        : QBluetoothSocket.SocketError = ... # 0x3
        ServiceNotFoundError     : QBluetoothSocket.SocketError = ... # 0x4
        NetworkError             : QBluetoothSocket.SocketError = ... # 0x5
        UnsupportedProtocolError : QBluetoothSocket.SocketError = ... # 0x6
        OperationError           : QBluetoothSocket.SocketError = ... # 0x7

    class SocketState(Shiboken.Enum):

        UnconnectedState         : QBluetoothSocket.SocketState = ... # 0x0
        ServiceLookupState       : QBluetoothSocket.SocketState = ... # 0x1
        ConnectingState          : QBluetoothSocket.SocketState = ... # 0x2
        ConnectedState           : QBluetoothSocket.SocketState = ... # 0x3
        BoundState               : QBluetoothSocket.SocketState = ... # 0x4
        ClosingState             : QBluetoothSocket.SocketState = ... # 0x5
        ListeningState           : QBluetoothSocket.SocketState = ... # 0x6


    @overload
    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...
    @overload
    def __init__(self, socketType: PySide6.QtBluetooth.QBluetoothServiceInfo.Protocol, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def abort(self) -> None: ...
    def bytesAvailable(self) -> int: ...
    def bytesToWrite(self) -> int: ...
    def canReadLine(self) -> bool: ...
    def close(self) -> None: ...
    @overload
    def connectToService(self, address: PySide6.QtBluetooth.QBluetoothAddress, port: int, openMode: PySide6.QtCore.QIODeviceBase.OpenMode = ...) -> None: ...
    @overload
    def connectToService(self, address: PySide6.QtBluetooth.QBluetoothAddress, uuid: PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid, mode: PySide6.QtCore.QIODeviceBase.OpenMode = ...) -> None: ...
    @overload
    def connectToService(self, address: PySide6.QtBluetooth.QBluetoothAddress, uuid: Union[PySide6.QtBluetooth.QBluetoothUuid, PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType, PySide6.QtBluetooth.QBluetoothUuid.DescriptorType, PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid, PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid, PySide6.QtCore.QUuid], openMode: PySide6.QtCore.QIODeviceBase.OpenMode = ...) -> None: ...
    @overload
    def connectToService(self, service: PySide6.QtBluetooth.QBluetoothServiceInfo, openMode: PySide6.QtCore.QIODeviceBase.OpenMode = ...) -> None: ...
    def disconnectFromService(self) -> None: ...
    def doDeviceDiscovery(self, service: PySide6.QtBluetooth.QBluetoothServiceInfo, openMode: PySide6.QtCore.QIODeviceBase.OpenMode) -> None: ...
    def error(self) -> PySide6.QtBluetooth.QBluetoothSocket.SocketError: ...
    def errorString(self) -> str: ...
    def isSequential(self) -> bool: ...
    def localAddress(self) -> PySide6.QtBluetooth.QBluetoothAddress: ...
    def localName(self) -> str: ...
    def localPort(self) -> int: ...
    def peerAddress(self) -> PySide6.QtBluetooth.QBluetoothAddress: ...
    def peerName(self) -> str: ...
    def peerPort(self) -> int: ...
    def preferredSecurityFlags(self) -> PySide6.QtBluetooth.QBluetooth.SecurityFlags: ...
    def readData(self, data: bytes, maxSize: int) -> object: ...
    def setPreferredSecurityFlags(self, flags: PySide6.QtBluetooth.QBluetooth.SecurityFlags) -> None: ...
    def setSocketDescriptor(self, socketDescriptor: int, socketType: PySide6.QtBluetooth.QBluetoothServiceInfo.Protocol, socketState: PySide6.QtBluetooth.QBluetoothSocket.SocketState = ..., openMode: PySide6.QtCore.QIODeviceBase.OpenMode = ...) -> bool: ...
    def setSocketError(self, error: PySide6.QtBluetooth.QBluetoothSocket.SocketError) -> None: ...
    def setSocketState(self, state: PySide6.QtBluetooth.QBluetoothSocket.SocketState) -> None: ...
    def socketDescriptor(self) -> int: ...
    def socketType(self) -> PySide6.QtBluetooth.QBluetoothServiceInfo.Protocol: ...
    def state(self) -> PySide6.QtBluetooth.QBluetoothSocket.SocketState: ...
    def writeData(self, data: bytes, maxSize: int) -> int: ...


class QBluetoothUuid(PySide6.QtCore.QUuid):

    class CharacteristicType(Shiboken.Enum):

        DeviceName               : QBluetoothUuid.CharacteristicType = ... # 0x2a00
        Appearance               : QBluetoothUuid.CharacteristicType = ... # 0x2a01
        PeripheralPrivacyFlag    : QBluetoothUuid.CharacteristicType = ... # 0x2a02
        ReconnectionAddress      : QBluetoothUuid.CharacteristicType = ... # 0x2a03
        PeripheralPreferredConnectionParameters: QBluetoothUuid.CharacteristicType = ... # 0x2a04
        ServiceChanged           : QBluetoothUuid.CharacteristicType = ... # 0x2a05
        AlertLevel               : QBluetoothUuid.CharacteristicType = ... # 0x2a06
        TxPowerLevel             : QBluetoothUuid.CharacteristicType = ... # 0x2a07
        DateTime                 : QBluetoothUuid.CharacteristicType = ... # 0x2a08
        DayOfWeek                : QBluetoothUuid.CharacteristicType = ... # 0x2a09
        DayDateTime              : QBluetoothUuid.CharacteristicType = ... # 0x2a0a
        ExactTime256             : QBluetoothUuid.CharacteristicType = ... # 0x2a0c
        DSTOffset                : QBluetoothUuid.CharacteristicType = ... # 0x2a0d
        TimeZone                 : QBluetoothUuid.CharacteristicType = ... # 0x2a0e
        LocalTimeInformation     : QBluetoothUuid.CharacteristicType = ... # 0x2a0f
        TimeWithDST              : QBluetoothUuid.CharacteristicType = ... # 0x2a11
        TimeAccuracy             : QBluetoothUuid.CharacteristicType = ... # 0x2a12
        TimeSource               : QBluetoothUuid.CharacteristicType = ... # 0x2a13
        ReferenceTimeInformation : QBluetoothUuid.CharacteristicType = ... # 0x2a14
        TimeUpdateControlPoint   : QBluetoothUuid.CharacteristicType = ... # 0x2a16
        TimeUpdateState          : QBluetoothUuid.CharacteristicType = ... # 0x2a17
        GlucoseMeasurement       : QBluetoothUuid.CharacteristicType = ... # 0x2a18
        BatteryLevel             : QBluetoothUuid.CharacteristicType = ... # 0x2a19
        TemperatureMeasurement   : QBluetoothUuid.CharacteristicType = ... # 0x2a1c
        TemperatureType          : QBluetoothUuid.CharacteristicType = ... # 0x2a1d
        IntermediateTemperature  : QBluetoothUuid.CharacteristicType = ... # 0x2a1e
        MeasurementInterval      : QBluetoothUuid.CharacteristicType = ... # 0x2a21
        BootKeyboardInputReport  : QBluetoothUuid.CharacteristicType = ... # 0x2a22
        SystemID                 : QBluetoothUuid.CharacteristicType = ... # 0x2a23
        ModelNumberString        : QBluetoothUuid.CharacteristicType = ... # 0x2a24
        SerialNumberString       : QBluetoothUuid.CharacteristicType = ... # 0x2a25
        FirmwareRevisionString   : QBluetoothUuid.CharacteristicType = ... # 0x2a26
        HardwareRevisionString   : QBluetoothUuid.CharacteristicType = ... # 0x2a27
        SoftwareRevisionString   : QBluetoothUuid.CharacteristicType = ... # 0x2a28
        ManufacturerNameString   : QBluetoothUuid.CharacteristicType = ... # 0x2a29
        IEEE1107320601RegulatoryCertificationDataList: QBluetoothUuid.CharacteristicType = ... # 0x2a2a
        CurrentTime              : QBluetoothUuid.CharacteristicType = ... # 0x2a2b
        MagneticDeclination      : QBluetoothUuid.CharacteristicType = ... # 0x2a2c
        ScanRefresh              : QBluetoothUuid.CharacteristicType = ... # 0x2a31
        BootKeyboardOutputReport : QBluetoothUuid.CharacteristicType = ... # 0x2a32
        BootMouseInputReport     : QBluetoothUuid.CharacteristicType = ... # 0x2a33
        GlucoseMeasurementContext: QBluetoothUuid.CharacteristicType = ... # 0x2a34
        BloodPressureMeasurement : QBluetoothUuid.CharacteristicType = ... # 0x2a35
        IntermediateCuffPressure : QBluetoothUuid.CharacteristicType = ... # 0x2a36
        HeartRateMeasurement     : QBluetoothUuid.CharacteristicType = ... # 0x2a37
        BodySensorLocation       : QBluetoothUuid.CharacteristicType = ... # 0x2a38
        HeartRateControlPoint    : QBluetoothUuid.CharacteristicType = ... # 0x2a39
        AlertStatus              : QBluetoothUuid.CharacteristicType = ... # 0x2a3f
        RingerControlPoint       : QBluetoothUuid.CharacteristicType = ... # 0x2a40
        RingerSetting            : QBluetoothUuid.CharacteristicType = ... # 0x2a41
        AlertCategoryIDBitMask   : QBluetoothUuid.CharacteristicType = ... # 0x2a42
        AlertCategoryID          : QBluetoothUuid.CharacteristicType = ... # 0x2a43
        AlertNotificationControlPoint: QBluetoothUuid.CharacteristicType = ... # 0x2a44
        UnreadAlertStatus        : QBluetoothUuid.CharacteristicType = ... # 0x2a45
        NewAlert                 : QBluetoothUuid.CharacteristicType = ... # 0x2a46
        SupportedNewAlertCategory: QBluetoothUuid.CharacteristicType = ... # 0x2a47
        SupportedUnreadAlertCategory: QBluetoothUuid.CharacteristicType = ... # 0x2a48
        BloodPressureFeature     : QBluetoothUuid.CharacteristicType = ... # 0x2a49
        HIDInformation           : QBluetoothUuid.CharacteristicType = ... # 0x2a4a
        ReportMap                : QBluetoothUuid.CharacteristicType = ... # 0x2a4b
        HIDControlPoint          : QBluetoothUuid.CharacteristicType = ... # 0x2a4c
        Report                   : QBluetoothUuid.CharacteristicType = ... # 0x2a4d
        ProtocolMode             : QBluetoothUuid.CharacteristicType = ... # 0x2a4e
        ScanIntervalWindow       : QBluetoothUuid.CharacteristicType = ... # 0x2a4f
        PnPID                    : QBluetoothUuid.CharacteristicType = ... # 0x2a50
        GlucoseFeature           : QBluetoothUuid.CharacteristicType = ... # 0x2a51
        RecordAccessControlPoint : QBluetoothUuid.CharacteristicType = ... # 0x2a52
        RSCMeasurement           : QBluetoothUuid.CharacteristicType = ... # 0x2a53
        RSCFeature               : QBluetoothUuid.CharacteristicType = ... # 0x2a54
        SCControlPoint           : QBluetoothUuid.CharacteristicType = ... # 0x2a55
        CSCMeasurement           : QBluetoothUuid.CharacteristicType = ... # 0x2a5b
        CSCFeature               : QBluetoothUuid.CharacteristicType = ... # 0x2a5c
        SensorLocation           : QBluetoothUuid.CharacteristicType = ... # 0x2a5d
        CyclingPowerMeasurement  : QBluetoothUuid.CharacteristicType = ... # 0x2a63
        CyclingPowerVector       : QBluetoothUuid.CharacteristicType = ... # 0x2a64
        CyclingPowerFeature      : QBluetoothUuid.CharacteristicType = ... # 0x2a65
        CyclingPowerControlPoint : QBluetoothUuid.CharacteristicType = ... # 0x2a66
        LocationAndSpeed         : QBluetoothUuid.CharacteristicType = ... # 0x2a67
        Navigation               : QBluetoothUuid.CharacteristicType = ... # 0x2a68
        PositionQuality          : QBluetoothUuid.CharacteristicType = ... # 0x2a69
        LNFeature                : QBluetoothUuid.CharacteristicType = ... # 0x2a6a
        LNControlPoint           : QBluetoothUuid.CharacteristicType = ... # 0x2a6b
        Elevation                : QBluetoothUuid.CharacteristicType = ... # 0x2a6c
        Pressure                 : QBluetoothUuid.CharacteristicType = ... # 0x2a6d
        Temperature              : QBluetoothUuid.CharacteristicType = ... # 0x2a6e
        Humidity                 : QBluetoothUuid.CharacteristicType = ... # 0x2a6f
        TrueWindSpeed            : QBluetoothUuid.CharacteristicType = ... # 0x2a70
        TrueWindDirection        : QBluetoothUuid.CharacteristicType = ... # 0x2a71
        ApparentWindSpeed        : QBluetoothUuid.CharacteristicType = ... # 0x2a72
        ApparentWindDirection    : QBluetoothUuid.CharacteristicType = ... # 0x2a73
        GustFactor               : QBluetoothUuid.CharacteristicType = ... # 0x2a74
        PollenConcentration      : QBluetoothUuid.CharacteristicType = ... # 0x2a75
        UVIndex                  : QBluetoothUuid.CharacteristicType = ... # 0x2a76
        Irradiance               : QBluetoothUuid.CharacteristicType = ... # 0x2a77
        Rainfall                 : QBluetoothUuid.CharacteristicType = ... # 0x2a78
        WindChill                : QBluetoothUuid.CharacteristicType = ... # 0x2a79
        HeatIndex                : QBluetoothUuid.CharacteristicType = ... # 0x2a7a
        DewPoint                 : QBluetoothUuid.CharacteristicType = ... # 0x2a7b
        DescriptorValueChanged   : QBluetoothUuid.CharacteristicType = ... # 0x2a7d
        AerobicHeartRateLowerLimit: QBluetoothUuid.CharacteristicType = ... # 0x2a7e
        AerobicThreshold         : QBluetoothUuid.CharacteristicType = ... # 0x2a7f
        Age                      : QBluetoothUuid.CharacteristicType = ... # 0x2a80
        AnaerobicHeartRateLowerLimit: QBluetoothUuid.CharacteristicType = ... # 0x2a81
        AnaerobicHeartRateUpperLimit: QBluetoothUuid.CharacteristicType = ... # 0x2a82
        AnaerobicThreshold       : QBluetoothUuid.CharacteristicType = ... # 0x2a83
        AerobicHeartRateUpperLimit: QBluetoothUuid.CharacteristicType = ... # 0x2a84
        DateOfBirth              : QBluetoothUuid.CharacteristicType = ... # 0x2a85
        DateOfThresholdAssessment: QBluetoothUuid.CharacteristicType = ... # 0x2a86
        EmailAddress             : QBluetoothUuid.CharacteristicType = ... # 0x2a87
        FatBurnHeartRateLowerLimit: QBluetoothUuid.CharacteristicType = ... # 0x2a88
        FatBurnHeartRateUpperLimit: QBluetoothUuid.CharacteristicType = ... # 0x2a89
        FirstName                : QBluetoothUuid.CharacteristicType = ... # 0x2a8a
        FiveZoneHeartRateLimits  : QBluetoothUuid.CharacteristicType = ... # 0x2a8b
        Gender                   : QBluetoothUuid.CharacteristicType = ... # 0x2a8c
        HeartRateMax             : QBluetoothUuid.CharacteristicType = ... # 0x2a8d
        Height                   : QBluetoothUuid.CharacteristicType = ... # 0x2a8e
        HipCircumference         : QBluetoothUuid.CharacteristicType = ... # 0x2a8f
        LastName                 : QBluetoothUuid.CharacteristicType = ... # 0x2a90
        MaximumRecommendedHeartRate: QBluetoothUuid.CharacteristicType = ... # 0x2a91
        RestingHeartRate         : QBluetoothUuid.CharacteristicType = ... # 0x2a92
        SportTypeForAerobicAnaerobicThresholds: QBluetoothUuid.CharacteristicType = ... # 0x2a93
        ThreeZoneHeartRateLimits : QBluetoothUuid.CharacteristicType = ... # 0x2a94
        TwoZoneHeartRateLimits   : QBluetoothUuid.CharacteristicType = ... # 0x2a95
        VO2Max                   : QBluetoothUuid.CharacteristicType = ... # 0x2a96
        WaistCircumference       : QBluetoothUuid.CharacteristicType = ... # 0x2a97
        Weight                   : QBluetoothUuid.CharacteristicType = ... # 0x2a98
        DatabaseChangeIncrement  : QBluetoothUuid.CharacteristicType = ... # 0x2a99
        UserIndex                : QBluetoothUuid.CharacteristicType = ... # 0x2a9a
        BodyCompositionFeature   : QBluetoothUuid.CharacteristicType = ... # 0x2a9b
        BodyCompositionMeasurement: QBluetoothUuid.CharacteristicType = ... # 0x2a9c
        WeightMeasurement        : QBluetoothUuid.CharacteristicType = ... # 0x2a9d
        WeightScaleFeature       : QBluetoothUuid.CharacteristicType = ... # 0x2a9e
        UserControlPoint         : QBluetoothUuid.CharacteristicType = ... # 0x2a9f
        MagneticFluxDensity2D    : QBluetoothUuid.CharacteristicType = ... # 0x2aa0
        MagneticFluxDensity3D    : QBluetoothUuid.CharacteristicType = ... # 0x2aa1
        Language                 : QBluetoothUuid.CharacteristicType = ... # 0x2aa2
        BarometricPressureTrend  : QBluetoothUuid.CharacteristicType = ... # 0x2aa3

    class DescriptorType(Shiboken.Enum):

        UnknownDescriptorType    : QBluetoothUuid.DescriptorType = ... # 0x0
        CharacteristicExtendedProperties: QBluetoothUuid.DescriptorType = ... # 0x2900
        CharacteristicUserDescription: QBluetoothUuid.DescriptorType = ... # 0x2901
        ClientCharacteristicConfiguration: QBluetoothUuid.DescriptorType = ... # 0x2902
        ServerCharacteristicConfiguration: QBluetoothUuid.DescriptorType = ... # 0x2903
        CharacteristicPresentationFormat: QBluetoothUuid.DescriptorType = ... # 0x2904
        CharacteristicAggregateFormat: QBluetoothUuid.DescriptorType = ... # 0x2905
        ValidRange               : QBluetoothUuid.DescriptorType = ... # 0x2906
        ExternalReportReference  : QBluetoothUuid.DescriptorType = ... # 0x2907
        ReportReference          : QBluetoothUuid.DescriptorType = ... # 0x2908
        EnvironmentalSensingConfiguration: QBluetoothUuid.DescriptorType = ... # 0x290b
        EnvironmentalSensingMeasurement: QBluetoothUuid.DescriptorType = ... # 0x290c
        EnvironmentalSensingTriggerSetting: QBluetoothUuid.DescriptorType = ... # 0x290d

    class ProtocolUuid(Shiboken.Enum):

        Sdp                      : QBluetoothUuid.ProtocolUuid = ... # 0x1
        Udp                      : QBluetoothUuid.ProtocolUuid = ... # 0x2
        Rfcomm                   : QBluetoothUuid.ProtocolUuid = ... # 0x3
        Tcp                      : QBluetoothUuid.ProtocolUuid = ... # 0x4
        TcsBin                   : QBluetoothUuid.ProtocolUuid = ... # 0x5
        TcsAt                    : QBluetoothUuid.ProtocolUuid = ... # 0x6
        Att                      : QBluetoothUuid.ProtocolUuid = ... # 0x7
        Obex                     : QBluetoothUuid.ProtocolUuid = ... # 0x8
        Ip                       : QBluetoothUuid.ProtocolUuid = ... # 0x9
        Ftp                      : QBluetoothUuid.ProtocolUuid = ... # 0xa
        Http                     : QBluetoothUuid.ProtocolUuid = ... # 0xc
        Wsp                      : QBluetoothUuid.ProtocolUuid = ... # 0xe
        Bnep                     : QBluetoothUuid.ProtocolUuid = ... # 0xf
        Upnp                     : QBluetoothUuid.ProtocolUuid = ... # 0x10
        Hidp                     : QBluetoothUuid.ProtocolUuid = ... # 0x11
        HardcopyControlChannel   : QBluetoothUuid.ProtocolUuid = ... # 0x12
        HardcopyDataChannel      : QBluetoothUuid.ProtocolUuid = ... # 0x14
        HardcopyNotification     : QBluetoothUuid.ProtocolUuid = ... # 0x16
        Avctp                    : QBluetoothUuid.ProtocolUuid = ... # 0x17
        Avdtp                    : QBluetoothUuid.ProtocolUuid = ... # 0x19
        Cmtp                     : QBluetoothUuid.ProtocolUuid = ... # 0x1b
        UdiCPlain                : QBluetoothUuid.ProtocolUuid = ... # 0x1d
        McapControlChannel       : QBluetoothUuid.ProtocolUuid = ... # 0x1e
        McapDataChannel          : QBluetoothUuid.ProtocolUuid = ... # 0x1f
        L2cap                    : QBluetoothUuid.ProtocolUuid = ... # 0x100

    class ServiceClassUuid(Shiboken.Enum):

        ServiceDiscoveryServer   : QBluetoothUuid.ServiceClassUuid = ... # 0x1000
        BrowseGroupDescriptor    : QBluetoothUuid.ServiceClassUuid = ... # 0x1001
        PublicBrowseGroup        : QBluetoothUuid.ServiceClassUuid = ... # 0x1002
        SerialPort               : QBluetoothUuid.ServiceClassUuid = ... # 0x1101
        LANAccessUsingPPP        : QBluetoothUuid.ServiceClassUuid = ... # 0x1102
        DialupNetworking         : QBluetoothUuid.ServiceClassUuid = ... # 0x1103
        IrMCSync                 : QBluetoothUuid.ServiceClassUuid = ... # 0x1104
        ObexObjectPush           : QBluetoothUuid.ServiceClassUuid = ... # 0x1105
        OBEXFileTransfer         : QBluetoothUuid.ServiceClassUuid = ... # 0x1106
        IrMCSyncCommand          : QBluetoothUuid.ServiceClassUuid = ... # 0x1107
        Headset                  : QBluetoothUuid.ServiceClassUuid = ... # 0x1108
        AudioSource              : QBluetoothUuid.ServiceClassUuid = ... # 0x110a
        AudioSink                : QBluetoothUuid.ServiceClassUuid = ... # 0x110b
        AV_RemoteControlTarget   : QBluetoothUuid.ServiceClassUuid = ... # 0x110c
        AdvancedAudioDistribution: QBluetoothUuid.ServiceClassUuid = ... # 0x110d
        AV_RemoteControl         : QBluetoothUuid.ServiceClassUuid = ... # 0x110e
        AV_RemoteControlController: QBluetoothUuid.ServiceClassUuid = ... # 0x110f
        HeadsetAG                : QBluetoothUuid.ServiceClassUuid = ... # 0x1112
        PANU                     : QBluetoothUuid.ServiceClassUuid = ... # 0x1115
        NAP                      : QBluetoothUuid.ServiceClassUuid = ... # 0x1116
        GN                       : QBluetoothUuid.ServiceClassUuid = ... # 0x1117
        DirectPrinting           : QBluetoothUuid.ServiceClassUuid = ... # 0x1118
        ReferencePrinting        : QBluetoothUuid.ServiceClassUuid = ... # 0x1119
        BasicImage               : QBluetoothUuid.ServiceClassUuid = ... # 0x111a
        ImagingResponder         : QBluetoothUuid.ServiceClassUuid = ... # 0x111b
        ImagingAutomaticArchive  : QBluetoothUuid.ServiceClassUuid = ... # 0x111c
        ImagingReferenceObjects  : QBluetoothUuid.ServiceClassUuid = ... # 0x111d
        Handsfree                : QBluetoothUuid.ServiceClassUuid = ... # 0x111e
        HandsfreeAudioGateway    : QBluetoothUuid.ServiceClassUuid = ... # 0x111f
        DirectPrintingReferenceObjectsService: QBluetoothUuid.ServiceClassUuid = ... # 0x1120
        ReflectedUI              : QBluetoothUuid.ServiceClassUuid = ... # 0x1121
        BasicPrinting            : QBluetoothUuid.ServiceClassUuid = ... # 0x1122
        PrintingStatus           : QBluetoothUuid.ServiceClassUuid = ... # 0x1123
        HumanInterfaceDeviceService: QBluetoothUuid.ServiceClassUuid = ... # 0x1124
        HardcopyCableReplacement : QBluetoothUuid.ServiceClassUuid = ... # 0x1125
        HCRPrint                 : QBluetoothUuid.ServiceClassUuid = ... # 0x1126
        HCRScan                  : QBluetoothUuid.ServiceClassUuid = ... # 0x1127
        SIMAccess                : QBluetoothUuid.ServiceClassUuid = ... # 0x112d
        PhonebookAccessPCE       : QBluetoothUuid.ServiceClassUuid = ... # 0x112e
        PhonebookAccessPSE       : QBluetoothUuid.ServiceClassUuid = ... # 0x112f
        PhonebookAccess          : QBluetoothUuid.ServiceClassUuid = ... # 0x1130
        HeadsetHS                : QBluetoothUuid.ServiceClassUuid = ... # 0x1131
        MessageAccessServer      : QBluetoothUuid.ServiceClassUuid = ... # 0x1132
        MessageNotificationServer: QBluetoothUuid.ServiceClassUuid = ... # 0x1133
        MessageAccessProfile     : QBluetoothUuid.ServiceClassUuid = ... # 0x1134
        GNSS                     : QBluetoothUuid.ServiceClassUuid = ... # 0x1135
        GNSSServer               : QBluetoothUuid.ServiceClassUuid = ... # 0x1136
        Display3D                : QBluetoothUuid.ServiceClassUuid = ... # 0x1137
        Glasses3D                : QBluetoothUuid.ServiceClassUuid = ... # 0x1138
        Synchronization3D        : QBluetoothUuid.ServiceClassUuid = ... # 0x1139
        MPSProfile               : QBluetoothUuid.ServiceClassUuid = ... # 0x113a
        MPSService               : QBluetoothUuid.ServiceClassUuid = ... # 0x113b
        PnPInformation           : QBluetoothUuid.ServiceClassUuid = ... # 0x1200
        GenericNetworking        : QBluetoothUuid.ServiceClassUuid = ... # 0x1201
        GenericFileTransfer      : QBluetoothUuid.ServiceClassUuid = ... # 0x1202
        GenericAudio             : QBluetoothUuid.ServiceClassUuid = ... # 0x1203
        GenericTelephony         : QBluetoothUuid.ServiceClassUuid = ... # 0x1204
        VideoSource              : QBluetoothUuid.ServiceClassUuid = ... # 0x1303
        VideoSink                : QBluetoothUuid.ServiceClassUuid = ... # 0x1304
        VideoDistribution        : QBluetoothUuid.ServiceClassUuid = ... # 0x1305
        HDP                      : QBluetoothUuid.ServiceClassUuid = ... # 0x1400
        HDPSource                : QBluetoothUuid.ServiceClassUuid = ... # 0x1401
        HDPSink                  : QBluetoothUuid.ServiceClassUuid = ... # 0x1402
        GenericAccess            : QBluetoothUuid.ServiceClassUuid = ... # 0x1800
        GenericAttribute         : QBluetoothUuid.ServiceClassUuid = ... # 0x1801
        ImmediateAlert           : QBluetoothUuid.ServiceClassUuid = ... # 0x1802
        LinkLoss                 : QBluetoothUuid.ServiceClassUuid = ... # 0x1803
        TxPower                  : QBluetoothUuid.ServiceClassUuid = ... # 0x1804
        CurrentTimeService       : QBluetoothUuid.ServiceClassUuid = ... # 0x1805
        ReferenceTimeUpdateService: QBluetoothUuid.ServiceClassUuid = ... # 0x1806
        NextDSTChangeService     : QBluetoothUuid.ServiceClassUuid = ... # 0x1807
        Glucose                  : QBluetoothUuid.ServiceClassUuid = ... # 0x1808
        HealthThermometer        : QBluetoothUuid.ServiceClassUuid = ... # 0x1809
        DeviceInformation        : QBluetoothUuid.ServiceClassUuid = ... # 0x180a
        HeartRate                : QBluetoothUuid.ServiceClassUuid = ... # 0x180d
        PhoneAlertStatusService  : QBluetoothUuid.ServiceClassUuid = ... # 0x180e
        BatteryService           : QBluetoothUuid.ServiceClassUuid = ... # 0x180f
        BloodPressure            : QBluetoothUuid.ServiceClassUuid = ... # 0x1810
        AlertNotificationService : QBluetoothUuid.ServiceClassUuid = ... # 0x1811
        HumanInterfaceDevice     : QBluetoothUuid.ServiceClassUuid = ... # 0x1812
        ScanParameters           : QBluetoothUuid.ServiceClassUuid = ... # 0x1813
        RunningSpeedAndCadence   : QBluetoothUuid.ServiceClassUuid = ... # 0x1814
        CyclingSpeedAndCadence   : QBluetoothUuid.ServiceClassUuid = ... # 0x1816
        CyclingPower             : QBluetoothUuid.ServiceClassUuid = ... # 0x1818
        LocationAndNavigation    : QBluetoothUuid.ServiceClassUuid = ... # 0x1819
        EnvironmentalSensing     : QBluetoothUuid.ServiceClassUuid = ... # 0x181a
        BodyComposition          : QBluetoothUuid.ServiceClassUuid = ... # 0x181b
        UserData                 : QBluetoothUuid.ServiceClassUuid = ... # 0x181c
        WeightScale              : QBluetoothUuid.ServiceClassUuid = ... # 0x181d
        BondManagement           : QBluetoothUuid.ServiceClassUuid = ... # 0x181e
        ContinuousGlucoseMonitoring: QBluetoothUuid.ServiceClassUuid = ... # 0x181f


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, uuid: PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType) -> None: ...
    @overload
    def __init__(self, uuid: PySide6.QtBluetooth.QBluetoothUuid.DescriptorType) -> None: ...
    @overload
    def __init__(self, uuid: PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid) -> None: ...
    @overload
    def __init__(self, uuid: PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid) -> None: ...
    @overload
    def __init__(self, uuid: PySide6.QtCore.QUuid) -> None: ...
    @overload
    def __init__(self, uuid: str) -> None: ...
    @overload
    def __init__(self, uuid: int) -> None: ...
    @overload
    def __init__(self, uuid: int) -> None: ...
    @overload
    def __init__(self, uuid: Union[PySide6.QtBluetooth.QBluetoothUuid, PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType, PySide6.QtBluetooth.QBluetoothUuid.DescriptorType, PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid, PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid, PySide6.QtCore.QUuid]) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def __lshift__(self, s: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def __rshift__(self, s: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    @staticmethod
    def characteristicToString(uuid: PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType) -> str: ...
    @staticmethod
    def descriptorToString(uuid: PySide6.QtBluetooth.QBluetoothUuid.DescriptorType) -> str: ...
    def minimumSize(self) -> int: ...
    @staticmethod
    def protocolToString(uuid: PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid) -> str: ...
    @staticmethod
    def serviceClassToString(uuid: PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid) -> str: ...
    def toUInt16(self) -> Tuple[int, bool]: ...
    def toUInt32(self) -> Tuple[int, bool]: ...


class QIntList(object): ...


class QLowEnergyAdvertisingData(Shiboken.Object):

    DiscoverabilityNone      : QLowEnergyAdvertisingData.Discoverability = ... # 0x0
    DiscoverabilityLimited   : QLowEnergyAdvertisingData.Discoverability = ... # 0x1
    DiscoverabilityGeneral   : QLowEnergyAdvertisingData.Discoverability = ... # 0x2

    class Discoverability(Shiboken.Enum):

        DiscoverabilityNone      : QLowEnergyAdvertisingData.Discoverability = ... # 0x0
        DiscoverabilityLimited   : QLowEnergyAdvertisingData.Discoverability = ... # 0x1
        DiscoverabilityGeneral   : QLowEnergyAdvertisingData.Discoverability = ... # 0x2


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtBluetooth.QLowEnergyAdvertisingData) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def discoverability(self) -> PySide6.QtBluetooth.QLowEnergyAdvertisingData.Discoverability: ...
    def includePowerLevel(self) -> bool: ...
    @staticmethod
    def invalidManufacturerId() -> int: ...
    def localName(self) -> str: ...
    def manufacturerData(self) -> PySide6.QtCore.QByteArray: ...
    def manufacturerId(self) -> int: ...
    def rawData(self) -> PySide6.QtCore.QByteArray: ...
    def services(self) -> List[PySide6.QtBluetooth.QBluetoothUuid]: ...
    def setDiscoverability(self, mode: PySide6.QtBluetooth.QLowEnergyAdvertisingData.Discoverability) -> None: ...
    def setIncludePowerLevel(self, doInclude: bool) -> None: ...
    def setLocalName(self, name: str) -> None: ...
    def setManufacturerData(self, id: int, data: Union[PySide6.QtCore.QByteArray, bytes]) -> None: ...
    def setRawData(self, data: Union[PySide6.QtCore.QByteArray, bytes]) -> None: ...
    def setServices(self, services: Sequence[PySide6.QtBluetooth.QBluetoothUuid]) -> None: ...
    def swap(self, other: PySide6.QtBluetooth.QLowEnergyAdvertisingData) -> None: ...


class QLowEnergyAdvertisingParameters(Shiboken.Object):

    IgnoreWhiteList          : QLowEnergyAdvertisingParameters.FilterPolicy = ... # 0x0
    UseWhiteListForScanning  : QLowEnergyAdvertisingParameters.FilterPolicy = ... # 0x1
    UseWhiteListForConnecting: QLowEnergyAdvertisingParameters.FilterPolicy = ... # 0x2
    UseWhiteListForScanningAndConnecting: QLowEnergyAdvertisingParameters.FilterPolicy = ... # 0x3
    AdvInd                   : QLowEnergyAdvertisingParameters.Mode = ... # 0x0
    AdvScanInd               : QLowEnergyAdvertisingParameters.Mode = ... # 0x2
    AdvNonConnInd            : QLowEnergyAdvertisingParameters.Mode = ... # 0x3

    class AddressInfo(Shiboken.Object):

        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, AddressInfo: PySide6.QtBluetooth.QLowEnergyAdvertisingParameters.AddressInfo) -> None: ...
        @overload
        def __init__(self, addr: PySide6.QtBluetooth.QBluetoothAddress, t: PySide6.QtBluetooth.QLowEnergyController.RemoteAddressType) -> None: ...

        @staticmethod
        def __copy__() -> None: ...

    class FilterPolicy(Shiboken.Enum):

        IgnoreWhiteList          : QLowEnergyAdvertisingParameters.FilterPolicy = ... # 0x0
        UseWhiteListForScanning  : QLowEnergyAdvertisingParameters.FilterPolicy = ... # 0x1
        UseWhiteListForConnecting: QLowEnergyAdvertisingParameters.FilterPolicy = ... # 0x2
        UseWhiteListForScanningAndConnecting: QLowEnergyAdvertisingParameters.FilterPolicy = ... # 0x3

    class Mode(Shiboken.Enum):

        AdvInd                   : QLowEnergyAdvertisingParameters.Mode = ... # 0x0
        AdvScanInd               : QLowEnergyAdvertisingParameters.Mode = ... # 0x2
        AdvNonConnInd            : QLowEnergyAdvertisingParameters.Mode = ... # 0x3


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtBluetooth.QLowEnergyAdvertisingParameters) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def filterPolicy(self) -> PySide6.QtBluetooth.QLowEnergyAdvertisingParameters.FilterPolicy: ...
    def maximumInterval(self) -> int: ...
    def minimumInterval(self) -> int: ...
    def mode(self) -> PySide6.QtBluetooth.QLowEnergyAdvertisingParameters.Mode: ...
    def setInterval(self, minimum: int, maximum: int) -> None: ...
    def setMode(self, mode: PySide6.QtBluetooth.QLowEnergyAdvertisingParameters.Mode) -> None: ...
    def setWhiteList(self, whiteList: Sequence[PySide6.QtBluetooth.QLowEnergyAdvertisingParameters.AddressInfo], policy: PySide6.QtBluetooth.QLowEnergyAdvertisingParameters.FilterPolicy) -> None: ...
    def swap(self, other: PySide6.QtBluetooth.QLowEnergyAdvertisingParameters) -> None: ...
    def whiteList(self) -> List[PySide6.QtBluetooth.QLowEnergyAdvertisingParameters.AddressInfo]: ...


class QLowEnergyCharacteristic(Shiboken.Object):

    Unknown                  : QLowEnergyCharacteristic.PropertyType = ... # 0x0
    Broadcasting             : QLowEnergyCharacteristic.PropertyType = ... # 0x1
    Read                     : QLowEnergyCharacteristic.PropertyType = ... # 0x2
    WriteNoResponse          : QLowEnergyCharacteristic.PropertyType = ... # 0x4
    Write                    : QLowEnergyCharacteristic.PropertyType = ... # 0x8
    Notify                   : QLowEnergyCharacteristic.PropertyType = ... # 0x10
    Indicate                 : QLowEnergyCharacteristic.PropertyType = ... # 0x20
    WriteSigned              : QLowEnergyCharacteristic.PropertyType = ... # 0x40
    ExtendedProperty         : QLowEnergyCharacteristic.PropertyType = ... # 0x80

    class PropertyType(Shiboken.Enum):

        Unknown                  : QLowEnergyCharacteristic.PropertyType = ... # 0x0
        Broadcasting             : QLowEnergyCharacteristic.PropertyType = ... # 0x1
        Read                     : QLowEnergyCharacteristic.PropertyType = ... # 0x2
        WriteNoResponse          : QLowEnergyCharacteristic.PropertyType = ... # 0x4
        Write                    : QLowEnergyCharacteristic.PropertyType = ... # 0x8
        Notify                   : QLowEnergyCharacteristic.PropertyType = ... # 0x10
        Indicate                 : QLowEnergyCharacteristic.PropertyType = ... # 0x20
        WriteSigned              : QLowEnergyCharacteristic.PropertyType = ... # 0x40
        ExtendedProperty         : QLowEnergyCharacteristic.PropertyType = ... # 0x80

    class PropertyTypes(object): ...


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtBluetooth.QLowEnergyCharacteristic) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def clientCharacteristicConfiguration(self) -> PySide6.QtBluetooth.QLowEnergyDescriptor: ...
    def descriptor(self, uuid: Union[PySide6.QtBluetooth.QBluetoothUuid, PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType, PySide6.QtBluetooth.QBluetoothUuid.DescriptorType, PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid, PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid, PySide6.QtCore.QUuid]) -> PySide6.QtBluetooth.QLowEnergyDescriptor: ...
    def descriptors(self) -> List[PySide6.QtBluetooth.QLowEnergyDescriptor]: ...
    def isValid(self) -> bool: ...
    def name(self) -> str: ...
    def properties(self) -> PySide6.QtBluetooth.QLowEnergyCharacteristic.PropertyTypes: ...
    def uuid(self) -> PySide6.QtBluetooth.QBluetoothUuid: ...
    def value(self) -> PySide6.QtCore.QByteArray: ...


class QLowEnergyCharacteristicData(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtBluetooth.QLowEnergyCharacteristicData) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def addDescriptor(self, descriptor: PySide6.QtBluetooth.QLowEnergyDescriptorData) -> None: ...
    def descriptors(self) -> List[PySide6.QtBluetooth.QLowEnergyDescriptorData]: ...
    def isValid(self) -> bool: ...
    def maximumValueLength(self) -> int: ...
    def minimumValueLength(self) -> int: ...
    def properties(self) -> PySide6.QtBluetooth.QLowEnergyCharacteristic.PropertyTypes: ...
    def readConstraints(self) -> PySide6.QtBluetooth.QBluetooth.AttAccessConstraints: ...
    def setDescriptors(self, descriptors: Sequence[PySide6.QtBluetooth.QLowEnergyDescriptorData]) -> None: ...
    def setProperties(self, properties: PySide6.QtBluetooth.QLowEnergyCharacteristic.PropertyTypes) -> None: ...
    def setReadConstraints(self, constraints: PySide6.QtBluetooth.QBluetooth.AttAccessConstraints) -> None: ...
    def setUuid(self, uuid: Union[PySide6.QtBluetooth.QBluetoothUuid, PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType, PySide6.QtBluetooth.QBluetoothUuid.DescriptorType, PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid, PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid, PySide6.QtCore.QUuid]) -> None: ...
    def setValue(self, value: Union[PySide6.QtCore.QByteArray, bytes]) -> None: ...
    def setValueLength(self, minimum: int, maximum: int) -> None: ...
    def setWriteConstraints(self, constraints: PySide6.QtBluetooth.QBluetooth.AttAccessConstraints) -> None: ...
    def swap(self, other: PySide6.QtBluetooth.QLowEnergyCharacteristicData) -> None: ...
    def uuid(self) -> PySide6.QtBluetooth.QBluetoothUuid: ...
    def value(self) -> PySide6.QtCore.QByteArray: ...
    def writeConstraints(self) -> PySide6.QtBluetooth.QBluetooth.AttAccessConstraints: ...


class QLowEnergyConnectionParameters(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtBluetooth.QLowEnergyConnectionParameters) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def latency(self) -> int: ...
    def maximumInterval(self) -> float: ...
    def minimumInterval(self) -> float: ...
    def setIntervalRange(self, minimum: float, maximum: float) -> None: ...
    def setLatency(self, latency: int) -> None: ...
    def setSupervisionTimeout(self, timeout: int) -> None: ...
    def supervisionTimeout(self) -> int: ...
    def swap(self, other: PySide6.QtBluetooth.QLowEnergyConnectionParameters) -> None: ...


class QLowEnergyController(PySide6.QtCore.QObject):

    UnconnectedState         : QLowEnergyController.ControllerState = ... # 0x0
    ConnectingState          : QLowEnergyController.ControllerState = ... # 0x1
    ConnectedState           : QLowEnergyController.ControllerState = ... # 0x2
    DiscoveringState         : QLowEnergyController.ControllerState = ... # 0x3
    DiscoveredState          : QLowEnergyController.ControllerState = ... # 0x4
    ClosingState             : QLowEnergyController.ControllerState = ... # 0x5
    AdvertisingState         : QLowEnergyController.ControllerState = ... # 0x6
    NoError                  : QLowEnergyController.Error = ... # 0x0
    UnknownError             : QLowEnergyController.Error = ... # 0x1
    UnknownRemoteDeviceError : QLowEnergyController.Error = ... # 0x2
    NetworkError             : QLowEnergyController.Error = ... # 0x3
    InvalidBluetoothAdapterError: QLowEnergyController.Error = ... # 0x4
    ConnectionError          : QLowEnergyController.Error = ... # 0x5
    AdvertisingError         : QLowEnergyController.Error = ... # 0x6
    RemoteHostClosedError    : QLowEnergyController.Error = ... # 0x7
    AuthorizationError       : QLowEnergyController.Error = ... # 0x8
    PublicAddress            : QLowEnergyController.RemoteAddressType = ... # 0x0
    RandomAddress            : QLowEnergyController.RemoteAddressType = ... # 0x1
    CentralRole              : QLowEnergyController.Role = ... # 0x0
    PeripheralRole           : QLowEnergyController.Role = ... # 0x1

    class ControllerState(Shiboken.Enum):

        UnconnectedState         : QLowEnergyController.ControllerState = ... # 0x0
        ConnectingState          : QLowEnergyController.ControllerState = ... # 0x1
        ConnectedState           : QLowEnergyController.ControllerState = ... # 0x2
        DiscoveringState         : QLowEnergyController.ControllerState = ... # 0x3
        DiscoveredState          : QLowEnergyController.ControllerState = ... # 0x4
        ClosingState             : QLowEnergyController.ControllerState = ... # 0x5
        AdvertisingState         : QLowEnergyController.ControllerState = ... # 0x6

    class Error(Shiboken.Enum):

        NoError                  : QLowEnergyController.Error = ... # 0x0
        UnknownError             : QLowEnergyController.Error = ... # 0x1
        UnknownRemoteDeviceError : QLowEnergyController.Error = ... # 0x2
        NetworkError             : QLowEnergyController.Error = ... # 0x3
        InvalidBluetoothAdapterError: QLowEnergyController.Error = ... # 0x4
        ConnectionError          : QLowEnergyController.Error = ... # 0x5
        AdvertisingError         : QLowEnergyController.Error = ... # 0x6
        RemoteHostClosedError    : QLowEnergyController.Error = ... # 0x7
        AuthorizationError       : QLowEnergyController.Error = ... # 0x8

    class RemoteAddressType(Shiboken.Enum):

        PublicAddress            : QLowEnergyController.RemoteAddressType = ... # 0x0
        RandomAddress            : QLowEnergyController.RemoteAddressType = ... # 0x1

    class Role(Shiboken.Enum):

        CentralRole              : QLowEnergyController.Role = ... # 0x0
        PeripheralRole           : QLowEnergyController.Role = ... # 0x1


    def addService(self, service: PySide6.QtBluetooth.QLowEnergyServiceData, parent: Optional[PySide6.QtCore.QObject] = ...) -> PySide6.QtBluetooth.QLowEnergyService: ...
    def connectToDevice(self) -> None: ...
    @overload
    @staticmethod
    def createCentral(remoteDevice: PySide6.QtBluetooth.QBluetoothDeviceInfo, localDevice: PySide6.QtBluetooth.QBluetoothAddress, parent: Optional[PySide6.QtCore.QObject] = ...) -> PySide6.QtBluetooth.QLowEnergyController: ...
    @overload
    @staticmethod
    def createCentral(remoteDevice: PySide6.QtBluetooth.QBluetoothDeviceInfo, parent: Optional[PySide6.QtCore.QObject] = ...) -> PySide6.QtBluetooth.QLowEnergyController: ...
    @overload
    @staticmethod
    def createPeripheral(localDevice: PySide6.QtBluetooth.QBluetoothAddress, parent: Optional[PySide6.QtCore.QObject] = ...) -> PySide6.QtBluetooth.QLowEnergyController: ...
    @overload
    @staticmethod
    def createPeripheral(parent: Optional[PySide6.QtCore.QObject] = ...) -> PySide6.QtBluetooth.QLowEnergyController: ...
    def createServiceObject(self, service: Union[PySide6.QtBluetooth.QBluetoothUuid, PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType, PySide6.QtBluetooth.QBluetoothUuid.DescriptorType, PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid, PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid, PySide6.QtCore.QUuid], parent: Optional[PySide6.QtCore.QObject] = ...) -> PySide6.QtBluetooth.QLowEnergyService: ...
    def disconnectFromDevice(self) -> None: ...
    def discoverServices(self) -> None: ...
    def error(self) -> PySide6.QtBluetooth.QLowEnergyController.Error: ...
    def errorString(self) -> str: ...
    def localAddress(self) -> PySide6.QtBluetooth.QBluetoothAddress: ...
    def mtu(self) -> int: ...
    def remoteAddress(self) -> PySide6.QtBluetooth.QBluetoothAddress: ...
    def remoteAddressType(self) -> PySide6.QtBluetooth.QLowEnergyController.RemoteAddressType: ...
    def remoteDeviceUuid(self) -> PySide6.QtBluetooth.QBluetoothUuid: ...
    def remoteName(self) -> str: ...
    def requestConnectionUpdate(self, parameters: PySide6.QtBluetooth.QLowEnergyConnectionParameters) -> None: ...
    def role(self) -> PySide6.QtBluetooth.QLowEnergyController.Role: ...
    def services(self) -> List[PySide6.QtBluetooth.QBluetoothUuid]: ...
    def setRemoteAddressType(self, type: PySide6.QtBluetooth.QLowEnergyController.RemoteAddressType) -> None: ...
    def startAdvertising(self, parameters: PySide6.QtBluetooth.QLowEnergyAdvertisingParameters, advertisingData: PySide6.QtBluetooth.QLowEnergyAdvertisingData, scanResponseData: PySide6.QtBluetooth.QLowEnergyAdvertisingData = ...) -> None: ...
    def state(self) -> PySide6.QtBluetooth.QLowEnergyController.ControllerState: ...
    def stopAdvertising(self) -> None: ...


class QLowEnergyDescriptor(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtBluetooth.QLowEnergyDescriptor) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def isValid(self) -> bool: ...
    def name(self) -> str: ...
    def type(self) -> PySide6.QtBluetooth.QBluetoothUuid.DescriptorType: ...
    def uuid(self) -> PySide6.QtBluetooth.QBluetoothUuid: ...
    def value(self) -> PySide6.QtCore.QByteArray: ...


class QLowEnergyDescriptorData(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtBluetooth.QLowEnergyDescriptorData) -> None: ...
    @overload
    def __init__(self, uuid: Union[PySide6.QtBluetooth.QBluetoothUuid, PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType, PySide6.QtBluetooth.QBluetoothUuid.DescriptorType, PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid, PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid, PySide6.QtCore.QUuid], value: Union[PySide6.QtCore.QByteArray, bytes]) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def isReadable(self) -> bool: ...
    def isValid(self) -> bool: ...
    def isWritable(self) -> bool: ...
    def readConstraints(self) -> PySide6.QtBluetooth.QBluetooth.AttAccessConstraints: ...
    def setReadPermissions(self, readable: bool, constraints: PySide6.QtBluetooth.QBluetooth.AttAccessConstraints = ...) -> None: ...
    def setUuid(self, uuid: Union[PySide6.QtBluetooth.QBluetoothUuid, PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType, PySide6.QtBluetooth.QBluetoothUuid.DescriptorType, PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid, PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid, PySide6.QtCore.QUuid]) -> None: ...
    def setValue(self, value: Union[PySide6.QtCore.QByteArray, bytes]) -> None: ...
    def setWritePermissions(self, writable: bool, constraints: PySide6.QtBluetooth.QBluetooth.AttAccessConstraints = ...) -> None: ...
    def swap(self, other: PySide6.QtBluetooth.QLowEnergyDescriptorData) -> None: ...
    def uuid(self) -> PySide6.QtBluetooth.QBluetoothUuid: ...
    def value(self) -> PySide6.QtCore.QByteArray: ...
    def writeConstraints(self) -> PySide6.QtBluetooth.QBluetooth.AttAccessConstraints: ...


class QLowEnergyService(PySide6.QtCore.QObject):

    FullDiscovery            : QLowEnergyService.DiscoveryMode = ... # 0x0
    SkipValueDiscovery       : QLowEnergyService.DiscoveryMode = ... # 0x1
    NoError                  : QLowEnergyService.ServiceError = ... # 0x0
    OperationError           : QLowEnergyService.ServiceError = ... # 0x1
    CharacteristicWriteError : QLowEnergyService.ServiceError = ... # 0x2
    DescriptorWriteError     : QLowEnergyService.ServiceError = ... # 0x3
    UnknownError             : QLowEnergyService.ServiceError = ... # 0x4
    CharacteristicReadError  : QLowEnergyService.ServiceError = ... # 0x5
    DescriptorReadError      : QLowEnergyService.ServiceError = ... # 0x6
    InvalidService           : QLowEnergyService.ServiceState = ... # 0x0
    DiscoveryRequired        : QLowEnergyService.ServiceState = ... # 0x1
    RemoteService            : QLowEnergyService.ServiceState = ... # 0x1
    DiscoveringService       : QLowEnergyService.ServiceState = ... # 0x2
    RemoteServiceDiscovering : QLowEnergyService.ServiceState = ... # 0x2
    RemoteServiceDiscovered  : QLowEnergyService.ServiceState = ... # 0x3
    ServiceDiscovered        : QLowEnergyService.ServiceState = ... # 0x3
    LocalService             : QLowEnergyService.ServiceState = ... # 0x4
    PrimaryService           : QLowEnergyService.ServiceType = ... # 0x1
    IncludedService          : QLowEnergyService.ServiceType = ... # 0x2
    WriteWithResponse        : QLowEnergyService.WriteMode = ... # 0x0
    WriteWithoutResponse     : QLowEnergyService.WriteMode = ... # 0x1
    WriteSigned              : QLowEnergyService.WriteMode = ... # 0x2

    class DiscoveryMode(Shiboken.Enum):

        FullDiscovery            : QLowEnergyService.DiscoveryMode = ... # 0x0
        SkipValueDiscovery       : QLowEnergyService.DiscoveryMode = ... # 0x1

    class ServiceError(Shiboken.Enum):

        NoError                  : QLowEnergyService.ServiceError = ... # 0x0
        OperationError           : QLowEnergyService.ServiceError = ... # 0x1
        CharacteristicWriteError : QLowEnergyService.ServiceError = ... # 0x2
        DescriptorWriteError     : QLowEnergyService.ServiceError = ... # 0x3
        UnknownError             : QLowEnergyService.ServiceError = ... # 0x4
        CharacteristicReadError  : QLowEnergyService.ServiceError = ... # 0x5
        DescriptorReadError      : QLowEnergyService.ServiceError = ... # 0x6

    class ServiceState(Shiboken.Enum):

        InvalidService           : QLowEnergyService.ServiceState = ... # 0x0
        DiscoveryRequired        : QLowEnergyService.ServiceState = ... # 0x1
        RemoteService            : QLowEnergyService.ServiceState = ... # 0x1
        DiscoveringService       : QLowEnergyService.ServiceState = ... # 0x2
        RemoteServiceDiscovering : QLowEnergyService.ServiceState = ... # 0x2
        RemoteServiceDiscovered  : QLowEnergyService.ServiceState = ... # 0x3
        ServiceDiscovered        : QLowEnergyService.ServiceState = ... # 0x3
        LocalService             : QLowEnergyService.ServiceState = ... # 0x4

    class ServiceType(Shiboken.Enum):

        PrimaryService           : QLowEnergyService.ServiceType = ... # 0x1
        IncludedService          : QLowEnergyService.ServiceType = ... # 0x2

    class ServiceTypes(object): ...

    class WriteMode(Shiboken.Enum):

        WriteWithResponse        : QLowEnergyService.WriteMode = ... # 0x0
        WriteWithoutResponse     : QLowEnergyService.WriteMode = ... # 0x1
        WriteSigned              : QLowEnergyService.WriteMode = ... # 0x2


    def characteristic(self, uuid: Union[PySide6.QtBluetooth.QBluetoothUuid, PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType, PySide6.QtBluetooth.QBluetoothUuid.DescriptorType, PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid, PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid, PySide6.QtCore.QUuid]) -> PySide6.QtBluetooth.QLowEnergyCharacteristic: ...
    def characteristics(self) -> List[PySide6.QtBluetooth.QLowEnergyCharacteristic]: ...
    @overload
    def contains(self, characteristic: PySide6.QtBluetooth.QLowEnergyCharacteristic) -> bool: ...
    @overload
    def contains(self, descriptor: PySide6.QtBluetooth.QLowEnergyDescriptor) -> bool: ...
    def discoverDetails(self, mode: PySide6.QtBluetooth.QLowEnergyService.DiscoveryMode = ...) -> None: ...
    def error(self) -> PySide6.QtBluetooth.QLowEnergyService.ServiceError: ...
    def includedServices(self) -> List[PySide6.QtBluetooth.QBluetoothUuid]: ...
    def readCharacteristic(self, characteristic: PySide6.QtBluetooth.QLowEnergyCharacteristic) -> None: ...
    def readDescriptor(self, descriptor: PySide6.QtBluetooth.QLowEnergyDescriptor) -> None: ...
    def serviceName(self) -> str: ...
    def serviceUuid(self) -> PySide6.QtBluetooth.QBluetoothUuid: ...
    def state(self) -> PySide6.QtBluetooth.QLowEnergyService.ServiceState: ...
    def type(self) -> PySide6.QtBluetooth.QLowEnergyService.ServiceTypes: ...
    def writeCharacteristic(self, characteristic: PySide6.QtBluetooth.QLowEnergyCharacteristic, newValue: Union[PySide6.QtCore.QByteArray, bytes], mode: PySide6.QtBluetooth.QLowEnergyService.WriteMode = ...) -> None: ...
    def writeDescriptor(self, descriptor: PySide6.QtBluetooth.QLowEnergyDescriptor, newValue: Union[PySide6.QtCore.QByteArray, bytes]) -> None: ...


class QLowEnergyServiceData(Shiboken.Object):

    ServiceTypePrimary       : QLowEnergyServiceData.ServiceType = ... # 0x2800
    ServiceTypeSecondary     : QLowEnergyServiceData.ServiceType = ... # 0x2801

    class ServiceType(Shiboken.Enum):

        ServiceTypePrimary       : QLowEnergyServiceData.ServiceType = ... # 0x2800
        ServiceTypeSecondary     : QLowEnergyServiceData.ServiceType = ... # 0x2801


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtBluetooth.QLowEnergyServiceData) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def addCharacteristic(self, characteristic: PySide6.QtBluetooth.QLowEnergyCharacteristicData) -> None: ...
    def addIncludedService(self, service: PySide6.QtBluetooth.QLowEnergyService) -> None: ...
    def characteristics(self) -> List[PySide6.QtBluetooth.QLowEnergyCharacteristicData]: ...
    def includedServices(self) -> List[PySide6.QtBluetooth.QLowEnergyService]: ...
    def isValid(self) -> bool: ...
    def setCharacteristics(self, characteristics: Sequence[PySide6.QtBluetooth.QLowEnergyCharacteristicData]) -> None: ...
    def setIncludedServices(self, services: Sequence[PySide6.QtBluetooth.QLowEnergyService]) -> None: ...
    def setType(self, type: PySide6.QtBluetooth.QLowEnergyServiceData.ServiceType) -> None: ...
    def setUuid(self, uuid: Union[PySide6.QtBluetooth.QBluetoothUuid, PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType, PySide6.QtBluetooth.QBluetoothUuid.DescriptorType, PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid, PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid, PySide6.QtCore.QUuid]) -> None: ...
    def swap(self, other: PySide6.QtBluetooth.QLowEnergyServiceData) -> None: ...
    def type(self) -> PySide6.QtBluetooth.QLowEnergyServiceData.ServiceType: ...
    def uuid(self) -> PySide6.QtBluetooth.QBluetoothUuid: ...


# eof
