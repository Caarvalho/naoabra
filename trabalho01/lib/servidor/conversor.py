from enum import Enum
import abc


class AllowedGrandezas(Enum):
    speed = "Velocidade", 1
    volume = "Volume", 2


class SpeedUnit(Enum):
    mps = "Metro por Segundo", 3
    kmph = "Kilômetro por Hora", 4
    mph = "Milha por Hora", 5


class VolumeUnit(Enum):
    m3 = "Metro Cúbico", 6
    liter = "Litro", 7
    barrel = "Barril", 8


class Conversor(abc.ABC):
    @abc.abstractmethod
    def convert(self, input, inputUnit, outputUnit):
        pass


class SpeedConversor(Conversor):
    _constantes_ = {
        SpeedUnit.mps: {
            SpeedUnit.kmph: 3.6,
            SpeedUnit.mph: 2.237,
            SpeedUnit.mps: 1,
        },
        SpeedUnit.kmph: {
            SpeedUnit.mps: 0.278,
            SpeedUnit.mph: 0.621,
            SpeedUnit.kmph: 1,
        },
        SpeedUnit.mph: {
            SpeedUnit.mps: 0.447,
            SpeedUnit.kmph: 1.609,
            SpeedUnit.mph: 1,
        },
    }

    @classmethod
    def convert(cls, input, inputUnit, outputUnit):
        return round(input * cls._constantes_[inputUnit][outputUnit], 3)


class VolumeConversor(Conversor):
    _constantes_ = {
        VolumeUnit.m3: {
            VolumeUnit.liter: 1000,
            VolumeUnit.barrel: 6.111,
            VolumeUnit.m3: 1,
        },
        VolumeUnit.liter: {
            VolumeUnit.m3: 0.001,
            VolumeUnit.barrel: 0.006,
            VolumeUnit.liter: 1,
        },
        VolumeUnit.barrel: {
            VolumeUnit.liter: 163.65,
            VolumeUnit.m3: 0.164,
            VolumeUnit.barrel: 1,
        },
    }

    @classmethod
    def convert(cls, input, inputUnit, outputUnit):
        return round(input * cls._constantes_[inputUnit][outputUnit], 3)


# print(SpeedConversor.convert(10, SpeedUnit.kmph, SpeedUnit.mps))
# print(SpeedUnit.mph.value)

# print()

# print(VolumeConversor.convert(10, VolumeUnit.barrel, VolumeUnit.liter))
# print(VolumeUnit.m3.value)
