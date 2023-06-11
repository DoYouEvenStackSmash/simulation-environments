# automatically generated by the FlatBuffers compiler, do not modify

# namespace: LOCO

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Track(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsTrack(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Track()
        x.Init(buf, n + offset)
        return x

    # Track
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Track
    def TrackId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Track
    def CategoryId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Track
    def TrackLen(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Track
    def Steps(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # Track
    def StepsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # Track
    def StepsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Track
    def StepsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

def TrackStart(builder): builder.StartObject(4)
def TrackAddTrackId(builder, trackId): builder.PrependInt32Slot(0, trackId, 0)
def TrackAddCategoryId(builder, categoryId): builder.PrependFloat32Slot(1, categoryId, 0.0)
def TrackAddTrackLen(builder, trackLen): builder.PrependInt32Slot(2, trackLen, 0)
def TrackAddSteps(builder, steps): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(steps), 0)
def TrackStartStepsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def TrackEnd(builder): return builder.EndObject()

try:
    from typing import List
except:
    pass

class TrackT(object):

    # TrackT
    def __init__(self):
        self.trackId = 0  # type: int
        self.categoryId = 0.0  # type: float
        self.trackLen = 0  # type: int
        self.steps = None  # type: List[int]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        track = Track()
        track.Init(buf, pos)
        return cls.InitFromObj(track)

    @classmethod
    def InitFromObj(cls, track):
        x = TrackT()
        x._UnPack(track)
        return x

    # TrackT
    def _UnPack(self, track):
        if track is None:
            return
        self.trackId = track.TrackId()
        self.categoryId = track.CategoryId()
        self.trackLen = track.TrackLen()
        if not track.StepsIsNone():
            if np is None:
                self.steps = []
                for i in range(track.StepsLength()):
                    self.steps.append(track.Steps(i))
            else:
                self.steps = track.StepsAsNumpy()

    # TrackT
    def Pack(self, builder):
        if self.steps is not None:
            if np is not None and type(self.steps) is np.ndarray:
                steps = builder.CreateNumpyVector(self.steps)
            else:
                TrackStartStepsVector(builder, len(self.steps))
                for i in reversed(range(len(self.steps))):
                    builder.PrependInt32(self.steps[i])
                steps = builder.EndVector(len(self.steps))
        TrackStart(builder)
        TrackAddTrackId(builder, self.trackId)
        TrackAddCategoryId(builder, self.categoryId)
        TrackAddTrackLen(builder, self.trackLen)
        if self.steps is not None:
            TrackAddSteps(builder, steps)
        track = TrackEnd(builder)
        return track
