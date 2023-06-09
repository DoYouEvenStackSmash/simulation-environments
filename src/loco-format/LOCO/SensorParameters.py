# automatically generated by the FlatBuffers compiler, do not modify

# namespace: LOCO

import flatbuffers
from flatbuffers.compat import import_numpy

np = import_numpy()


class SensorParameters(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAsSensorParameters(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SensorParameters()
        x.Init(buf, n + offset)
        return x

    # SensorParameters
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SensorParameters
    def FovRadius(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # SensorParameters
    def FovWidth(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(
                flatbuffers.number_types.Float32Flags, o + self._tab.Pos
            )
        return 0.0


def SensorParametersStart(builder):
    builder.StartObject(2)


def SensorParametersAddFovRadius(builder, fovRadius):
    builder.PrependInt32Slot(0, fovRadius, 0)


def SensorParametersAddFovWidth(builder, fovWidth):
    builder.PrependFloat32Slot(1, fovWidth, 0.0)


def SensorParametersEnd(builder):
    return builder.EndObject()


class SensorParametersT(object):
    # SensorParametersT
    def __init__(self):
        self.fovRadius = 0  # type: int
        self.fovWidth = 0.0  # type: float

    @classmethod
    def InitFromBuf(cls, buf, pos):
        sensorParameters = SensorParameters()
        sensorParameters.Init(buf, pos)
        return cls.InitFromObj(sensorParameters)

    @classmethod
    def InitFromObj(cls, sensorParameters):
        x = SensorParametersT()
        x._UnPack(sensorParameters)
        return x

    # SensorParametersT
    def _UnPack(self, sensorParameters):
        if sensorParameters is None:
            return
        self.fovRadius = sensorParameters.FovRadius()
        self.fovWidth = sensorParameters.FovWidth()

    # SensorParametersT
    def Pack(self, builder):
        SensorParametersStart(builder)
        SensorParametersAddFovRadius(builder, self.fovRadius)
        SensorParametersAddFovWidth(builder, self.fovWidth)
        sensorParameters = SensorParametersEnd(builder)
        return sensorParameters
