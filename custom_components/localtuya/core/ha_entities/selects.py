"""
    This a file contains available tuya data
    https://developer.tuya.com/en/docs/iot/standarddescription?id=K9i5ql6waswzq

    Credits: official HA Tuya integration.
    Modified by: xZetsubou
"""

from .base import (
    DPCode,
    LocalTuyaEntity,
    CONF_DEVICE_CLASS,
    EntityCategory,
    CLOUD_VALUE,
)

# from const.py this is temporarily.

from ...select import CONF_OPTIONS as OPS_VALS


def localtuya_selector(options):
    """Generate localtuya select configs"""
    data = {OPS_VALS: CLOUD_VALUE(options, "id", "range", dict)}
    return data


COUNT_DOWN = {
    "cancel": "Disable",
    "1": "1 Hour",
    "2": "2 Hours",
    "3": "3 Hours",
    "4": "4 Hours",
    "5": "5 Hours",
    "6": "6 Hours",
}
COUNT_DOWN_HOURS = {
    "off": "Disable",
    "1h": "1 Hour",
    "2h": "2 Hours",
    "3h": "3 Hours",
    "4h": "4 Hours",
    "5h": "5 Hours",
    "6h": "6 Hours",
}

SELECTS: dict[str, tuple[LocalTuyaEntity, ...]] = {
    # Smart panel with switches and zigbee hub ?
    # Not documented
    "dgnzk": (
        LocalTuyaEntity(
            id=DPCode.SOURCE,
            name="Source",
            icon="mdi:volume-source",
            entity_category=EntityCategory.CONFIG,
            custom_configs=localtuya_selector(
                {
                    "cloud": "Cloud",
                    "local": "Local",
                    "aux": "Aux",
                    "bluetooth": "Bluetooth",
                }
            ),
        ),
        LocalTuyaEntity(
            id=DPCode.PLAY_MODE,
            name="Mode",
            icon="mdi:cog-outline",
            entity_category=EntityCategory.CONFIG,
            custom_configs=localtuya_selector(
                {
                    "order": "Order",
                    "repeat_all": "Repeat ALL",
                    "repeat_one": "Repeat one",
                    "random": "Random",
                }
            ),
        ),
        LocalTuyaEntity(
            id=DPCode.SOUND_EFFECTS,
            name="Sound Effects",
            icon="mdi:sine-wave",
            entity_category=EntityCategory.CONFIG,
            custom_configs=localtuya_selector(
                {
                    "normal": "Normal",
                    "pop": "Pop",
                    "opera": "Opera",
                    "classical": "Classical",
                    "jazz": "Jazz",
                    "rock": "Rock",
                    "folk": "Folk",
                    "heavy_metal": "Metal",
                    "hip_hop": "HipHop",
                    "wave": "Wave",
                }
            ),
        ),
    ),
    # Multi-functional Sensor
    # https://developer.tuya.com/en/docs/iot/categorydgnbj?id=Kaiuz3yorvzg3
    "dgnbj": (
        LocalTuyaEntity(
            id=DPCode.ALARM_VOLUME,
            name="volume",
            entity_category=EntityCategory.CONFIG,
            custom_configs=localtuya_selector(
                {
                    "low": "Low",
                    "middle": "Middle",
                    "high": "High",
                    "mute": "Mute",
                }
            ),
        ),
        LocalTuyaEntity(
            id=DPCode.ALARM_RINGTONE,
            name="Ringtone",
            entity_category=EntityCategory.CONFIG,
            custom_configs=localtuya_selector(
                {
                    "1": "1",
                    "2": "2",
                    "3": "3",
                    "4": "4",
                    "5": "5",
                }
            ),
        ),
    ),
    # Heater
    "kt": (
        LocalTuyaEntity(
            id=(DPCode.C_F, DPCode.TEMP_UNIT_CONVERT),
            name="Temperature Unit",
            custom_configs=localtuya_selector({"c": "Celsius", "f": "Fahrenheit"}),
        ),
    ),
    # Heater
    "rs": (
        LocalTuyaEntity(
            id=(DPCode.C_F, DPCode.TEMP_UNIT_CONVERT),
            name="Temperature Unit",
            custom_configs=localtuya_selector({"c": "Celsius", "f": "Fahrenheit"}),
        ),
        LocalTuyaEntity(
            id=DPCode.CRUISE_MODE,
            name="Cruise mode",
            custom_configs=localtuya_selector(
                {"all_day": "Always", "water_control": "Water", "single_cruise": "Once"}
            ),
        ),
    ),
    # Coffee maker
    # https://developer.tuya.com/en/docs/iot/categorykfj?id=Kaiuz2p12pc7f
    "kfj": (
        LocalTuyaEntity(
            id=DPCode.CUP_NUMBER,
            name="Cups",
            icon="mdi:numeric",
            custom_configs=localtuya_selector("1,2,3,4,5,6,7,8,9,10,11,12"),
        ),
        LocalTuyaEntity(
            id=DPCode.CONCENTRATION_SET,
            name="Concentration",
            icon="mdi:altimeter",
            entity_category=EntityCategory.CONFIG,
            custom_configs=localtuya_selector("regular,middle,bold"),
        ),
        LocalTuyaEntity(
            id=DPCode.MATERIAL,
            name="Material",
            entity_category=EntityCategory.CONFIG,
            custom_configs=localtuya_selector("bean,powder"),
        ),
        LocalTuyaEntity(
            id=DPCode.MODE,
            name="Mode",
            icon="mdi:coffee",
            custom_configs=localtuya_selector(
                "espresso,americano,machiatto,caffe_latte,cafe_mocha,cappuccino"
            ),
        ),
    ),
    # Switch
    # https://developer.tuya.com/en/docs/iot/s?id=K9gf7o5prgf7s
    "kg": (
        LocalTuyaEntity(
            id=DPCode.RELAY_STATUS,
            icon="mdi:circle-double",
            entity_category=EntityCategory.CONFIG,
            name="Power-on behavior",
            custom_configs=localtuya_selector(
                {"power_on": "ON", "power_off": "OFF", "last": "Last State"}
            ),
            condition_contains_any=["power_on", "power_off", "last"],
        ),
        LocalTuyaEntity(
            id=DPCode.RELAY_STATUS,
            icon="mdi:circle-double",
            entity_category=EntityCategory.CONFIG,
            name="Power-on behavior",
            custom_configs=localtuya_selector(
                {"on": "ON", "off": "OFF", "memory": "Last State"}
            ),
            condition_contains_any=["on", "off", "memory"],
        ),
        LocalTuyaEntity(
            id=DPCode.RELAY_STATUS,
            icon="mdi:circle-double",
            entity_category=EntityCategory.CONFIG,
            name="Power-on behavior",
            custom_configs=localtuya_selector(
                {"0": "ON", "1": "OFF", "2": "Last State"}
            ),
        ),
        LocalTuyaEntity(
            id=DPCode.RELAY_STATUS_1,
            icon="mdi:circle-double",
            entity_category=EntityCategory.CONFIG,
            name="Power-on behavior 1",
            custom_configs=localtuya_selector(
                {"power_on": "ON", "power_off": "OFF", "last": "Last State"}
            ),
            condition_contains_any=["power_on", "power_off", "last"],
        ),
        LocalTuyaEntity(
            id=DPCode.RELAY_STATUS_1,
            icon="mdi:circle-double",
            entity_category=EntityCategory.CONFIG,
            name="Power-on behavior 1",
            custom_configs=localtuya_selector(
                {"on": "ON", "off": "OFF", "memory": "Last State"}
            ),
            condition_contains_any=["on", "off", "memory"],
        ),
        LocalTuyaEntity(
            id=DPCode.RELAY_STATUS_1,
            icon="mdi:circle-double",
            entity_category=EntityCategory.CONFIG,
            name="Power-on behavior 1",
            custom_configs=localtuya_selector(
                {"0": "ON", "1": "OFF", "2": "Last State"}
            ),
        ),
        LocalTuyaEntity(
            id=DPCode.RELAY_STATUS_2,
            icon="mdi:circle-double",
            entity_category=EntityCategory.CONFIG,
            name="Power-on behavior 2",
            custom_configs=localtuya_selector(
                {"power_on": "ON", "power_off": "OFF", "last": "Last State"}
            ),
            condition_contains_any=["power_on", "power_off", "last"],
        ),
        LocalTuyaEntity(
            id=DPCode.RELAY_STATUS_2,
            icon="mdi:circle-double",
            entity_category=EntityCategory.CONFIG,
            name="Power-on behavior 2",
            custom_configs=localtuya_selector(
                {"on": "ON", "off": "OFF", "memory": "Last State"}
            ),
            condition_contains_any=["on", "off", "memory"],
        ),
        LocalTuyaEntity(
            id=DPCode.RELAY_STATUS_2,
            icon="mdi:circle-double",
            entity_category=EntityCategory.CONFIG,
            name="Power-on behavior 2",
            custom_configs=localtuya_selector(
                {"0": "ON", "1": "OFF", "2": "Last State"}
            ),
        ),
        LocalTuyaEntity(
            id=DPCode.RELAY_STATUS_3,
            icon="mdi:circle-double",
            entity_category=EntityCategory.CONFIG,
            name="Power-on behavior 3",
            custom_configs=localtuya_selector(
                {"power_on": "ON", "power_off": "OFF", "last": "Last State"}
            ),
            condition_contains_any=["power_on", "power_off", "last"],
        ),
        LocalTuyaEntity(
            id=DPCode.RELAY_STATUS_3,
            icon="mdi:circle-double",
            entity_category=EntityCategory.CONFIG,
            name="Power-on behavior 3",
            custom_configs=localtuya_selector(
                {"on": "ON", "off": "OFF", "memory": "Last State"}
            ),
            condition_contains_any=["on", "off", "memory"],
        ),
        LocalTuyaEntity(
            id=DPCode.RELAY_STATUS_3,
            icon="mdi:circle-double",
            entity_category=EntityCategory.CONFIG,
            name="Power-on behavior 3",
            custom_configs=localtuya_selector(
                {"0": "ON", "1": "OFF", "2": "Last State"}
            ),
        ),
        LocalTuyaEntity(
            id=DPCode.RELAY_STATUS_4,
            icon="mdi:circle-double",
            entity_category=EntityCategory.CONFIG,
            name="Power-on behavior 4",
            custom_configs=localtuya_selector(
                {"power_on": "ON", "power_off": "OFF", "last": "Last State"}
            ),
            condition_contains_any=["power_on", "power_off", "last"],
        ),
        LocalTuyaEntity(
            id=DPCode.RELAY_STATUS_4,
            icon="mdi:circle-double",
            entity_category=EntityCategory.CONFIG,
            name="Power-on behavior 4",
            custom_configs=localtuya_selector(
                {"on": "ON", "off": "OFF", "memory": "Last State"}
            ),
            condition_contains_any=["on", "off", "memory"],
        ),
        LocalTuyaEntity(
            id=DPCode.RELAY_STATUS_4,
            icon="mdi:circle-double",
            entity_category=EntityCategory.CONFIG,
            name="Power-on behavior 4",
            custom_configs=localtuya_selector(
                {"0": "ON", "1": "OFF", "2": "Last State"}
            ),
        ),
        LocalTuyaEntity(
            id=DPCode.RELAY_STATUS_5,
            icon="mdi:circle-double",
            entity_category=EntityCategory.CONFIG,
            name="Power-on behavior 5",
            custom_configs=localtuya_selector(
                {"power_on": "ON", "power_off": "OFF", "last": "Last State"}
            ),
            condition_contains_any=["power_on", "power_off", "last"],
        ),
        LocalTuyaEntity(
            id=DPCode.RELAY_STATUS_5,
            icon="mdi:circle-double",
            entity_category=EntityCategory.CONFIG,
            name="Power-on behavior 5",
            custom_configs=localtuya_selector(
                {"on": "ON", "off": "OFF", "memory": "Last State"}
            ),
            condition_contains_any=["on", "off", "memory"],
        ),
        LocalTuyaEntity(
            id=DPCode.RELAY_STATUS_5,
            icon="mdi:circle-double",
            entity_category=EntityCategory.CONFIG,
            name="Power-on behavior 5",
            custom_configs=localtuya_selector(
                {"0": "ON", "1": "OFF", "2": "Last State"}
            ),
        ),
        LocalTuyaEntity(
            id=DPCode.RELAY_STATUS_6,
            icon="mdi:circle-double",
            entity_category=EntityCategory.CONFIG,
            name="Power-on behavior 6",
            custom_configs=localtuya_selector(
                {"power_on": "ON", "power_off": "OFF", "last": "Last State"}
            ),
            condition_contains_any=["power_on", "power_off", "last"],
        ),
        LocalTuyaEntity(
            id=DPCode.RELAY_STATUS_6,
            icon="mdi:circle-double",
            entity_category=EntityCategory.CONFIG,
            name="Power-on behavior 6",
            custom_configs=localtuya_selector(
                {"on": "ON", "off": "OFF", "memory": "Last State"}
            ),
            condition_contains_any=["on", "off", "memory"],
        ),
        LocalTuyaEntity(
            id=DPCode.RELAY_STATUS_6,
            icon="mdi:circle-double",
            entity_category=EntityCategory.CONFIG,
            name="Power-on behavior 6",
            custom_configs=localtuya_selector(
                {"0": "ON", "1": "OFF", "2": "Last State"}
            ),
        ),
        LocalTuyaEntity(
            id=DPCode.LIGHT_MODE,
            entity_category=EntityCategory.CONFIG,
            custom_configs=localtuya_selector(
                {"relay": "State", "pos": "Position", "none": "OFF"}
            ),
            name="Light Mode",
        ),
    ),
    # Heater
    # https://developer.tuya.com/en/docs/iot/categoryqn?id=Kaiuz18kih0sm
    "qn": (
        LocalTuyaEntity(
            id=DPCode.LEVEL,
            name="Temperature Level",
            icon="mdi:thermometer-lines",
            custom_configs=localtuya_selector(
                {"1": "Level 1", "2": " Levell 2", "3": " Level 3"}
            ),
        ),
        LocalTuyaEntity(
            id=DPCode.COUNTDOWN,
            name="Set Countdown",
            icon="mdi:timer-cog-outline",
            custom_configs=localtuya_selector(COUNT_DOWN),
        ),
        LocalTuyaEntity(
            id=DPCode.COUNTDOWN_SET,
            name="Set Countdown",
            icon="mdi:timer-cog-outline",
            custom_configs=localtuya_selector(COUNT_DOWN_HOURS),
        ),
    ),
    # Siren Alarm
    # https://developer.tuya.com/en/docs/iot/categorysgbj?id=Kaiuz37tlpbnu
    "sgbj": (
        LocalTuyaEntity(
            id=DPCode.ALARM_VOLUME,
            name="Volume",
            entity_category=EntityCategory.CONFIG,
            custom_configs=localtuya_selector("low,middle,high,mute"),
        ),
        LocalTuyaEntity(
            id=DPCode.ALARM_STATE,
            name="State",
            entity_category=EntityCategory.CONFIG,
            custom_configs=localtuya_selector(
                "alarm_sound,alarm_light,alarm_sound_light,normal"
            ),
        ),
        LocalTuyaEntity(
            id=DPCode.BRIGHT_STATE,
            name="Brightness",
            entity_category=EntityCategory.CONFIG,
            custom_configs=localtuya_selector("low,middle,high,strong"),
        ),
    ),
    # Smart Camera
    # https://developer.tuya.com/en/docs/iot/categorysp?id=Kaiuz35leyo12
    "sp": (
        LocalTuyaEntity(
            id=DPCode.IPC_WORK_MODE,
            entity_category=EntityCategory.CONFIG,
            name="Working mode",
            custom_configs=localtuya_selector({"0": "Low Power", "1": "Continuous"}),
        ),
        LocalTuyaEntity(
            id=DPCode.DECIBEL_SENSITIVITY,
            icon="mdi:volume-vibrate",
            entity_category=EntityCategory.CONFIG,
            name="Decibel Sensitivity",
            custom_configs=localtuya_selector(
                {"0": "Low Sensitivity", "1": "High Sensitivity"}
            ),
        ),
        LocalTuyaEntity(
            id=DPCode.RECORD_MODE,
            icon="mdi:record-rec",
            entity_category=EntityCategory.CONFIG,
            name="Record Mode",
            custom_configs=localtuya_selector(
                {"1": "Record Events Only", "2": "Allways Record"}
            ),
        ),
        LocalTuyaEntity(
            id=DPCode.BASIC_NIGHTVISION,
            icon="mdi:theme-light-dark",
            entity_category=EntityCategory.CONFIG,
            name="IR Night Vision",
            custom_configs=localtuya_selector({"0": "Auto", "1": "OFF", "2": "ON"}),
        ),
        LocalTuyaEntity(
            id=DPCode.BASIC_ANTI_FLICKER,
            icon="mdi:image-outline",
            entity_category=EntityCategory.CONFIG,
            name="Anti-Flicker",
            custom_configs=localtuya_selector(
                {"0": "Disable", "1": "50 Hz", "2": "60 Hz"}
            ),
        ),
        LocalTuyaEntity(
            id=DPCode.MOTION_SENSITIVITY,
            icon="mdi:motion-sensor",
            entity_category=EntityCategory.CONFIG,
            name="Motion Sensitivity",
            custom_configs=localtuya_selector({"0": "Low", "1": "Medium", "2": "High"}),
        ),
        LocalTuyaEntity(
            id=DPCode.PTZ_CONTROL,
            icon="mdi:image-filter-tilt-shift",
            entity_category=EntityCategory.CONFIG,
            name="PTZ control",
            custom_configs=localtuya_selector(
                {
                    "0": "UP",
                    "1": "Upper Right",
                    "2": "Right",
                    "3": "Bottom Right",
                    "4": "Down",
                    "5": "Bottom Left",
                    "6": "Left",
                    "7": "Upper Left",
                }
            ),
        ),
        LocalTuyaEntity(
            id=DPCode.FLIGHT_BRIGHT_MODE,
            entity_category=EntityCategory.CONFIG,
            name="Brightness mode",
            custom_configs=localtuya_selector({"0": "Manual", "1": "Auto"}),
        ),
        LocalTuyaEntity(
            id=DPCode.PIR_SENSITIVITY,
            entity_category=EntityCategory.CONFIG,
            name="PIR sensitivity",
            custom_configs=localtuya_selector({"0": "Low", "1": "Medium", "2": "High"}),
        ),
    ),
    # Dimmer Switch
    # https://developer.tuya.com/en/docs/iot/categorytgkg?id=Kaiuz0ktx7m0o
    "tgkg": (
        LocalTuyaEntity(
            id=DPCode.RELAY_STATUS,
            icon="mdi:circle-double",
            entity_category=EntityCategory.CONFIG,
            name="Power-on behavior",
            custom_configs=localtuya_selector(
                {"on": "ON", "off": "OFF", "memory": "Last State"}
            ),
            condition_contains_any=["on", "off", "memory"],
        ),
        LocalTuyaEntity(
            id=DPCode.RELAY_STATUS,
            icon="mdi:circle-double",
            entity_category=EntityCategory.CONFIG,
            name="Power-on behavior",
            custom_configs=localtuya_selector(
                {"0": "ON", "1": "OFF", "2": "Last State"}
            ),
        ),
        LocalTuyaEntity(
            id=DPCode.LIGHT_MODE,
            entity_category=EntityCategory.CONFIG,
            name="Light Mode",
            custom_configs=localtuya_selector(
                {"relay": "State", "pos": "Position", "none": "OFF"}
            ),
        ),
        LocalTuyaEntity(
            id=DPCode.LED_TYPE_1,
            entity_category=EntityCategory.CONFIG,
            name="Led Type 1",
            custom_configs=localtuya_selector("led,incandescent,halogen"),
        ),
        LocalTuyaEntity(
            id=DPCode.LED_TYPE_2,
            entity_category=EntityCategory.CONFIG,
            name="Led Type 2",
            custom_configs=localtuya_selector("led,incandescent,halogen"),
        ),
        LocalTuyaEntity(
            id=DPCode.LED_TYPE_3,
            entity_category=EntityCategory.CONFIG,
            name="Led Type 3",
            custom_configs=localtuya_selector("led,incandescent,halogen"),
        ),
    ),
    # Dimmer
    # https://developer.tuya.com/en/docs/iot/tgq?id=Kaof8ke9il4k4
    "tgq": (
        LocalTuyaEntity(
            id=DPCode.LED_TYPE_1,
            entity_category=EntityCategory.CONFIG,
            name="Led Type 1",
            custom_configs=localtuya_selector("led,incandescent,halogen"),
        ),
        LocalTuyaEntity(
            id=DPCode.LED_TYPE_2,
            entity_category=EntityCategory.CONFIG,
            name="Led Type 2",
            custom_configs=localtuya_selector("led,incandescent,halogen"),
        ),
    ),
    # Fingerbot
    "szjqr": (
        LocalTuyaEntity(
            id=DPCode.MODE,
            entity_category=EntityCategory.CONFIG,
            name="Fingerbot Mode",
            custom_configs=localtuya_selector("click,switch,toggle"),
        ),
    ),
    # Robot Vacuum
    # https://developer.tuya.com/en/docs/iot/fsd?id=K9gf487ck1tlo
    "sd": (
        LocalTuyaEntity(
            id=DPCode.CISTERN,
            entity_category=EntityCategory.CONFIG,
            icon="mdi:water-opacity",
            name="Water Tank Adjustment",
            custom_configs=localtuya_selector("low,middle,high,closed"),
        ),
        LocalTuyaEntity(
            id=DPCode.COLLECTION_MODE,
            entity_category=EntityCategory.CONFIG,
            icon="mdi:air-filter",
            name="Dust Collection Mode",
            custom_configs=localtuya_selector("small,middle,large"),
        ),
        LocalTuyaEntity(
            id=DPCode.MODE,
            entity_category=EntityCategory.CONFIG,
            icon="mdi:layers-outline",
            name="Mode",
            custom_configs=localtuya_selector(
                "standby,random,smart,wall_follow,mop,spiral,left_spiral,right_spiral,right_bow,left_bow,partial_bow,chargego"
            ),
        ),
    ),
    # Fan
    # https://developer.tuya.com/en/docs/iot/f?id=K9gf45vs7vkge
    "fs": (
        LocalTuyaEntity(
            id=DPCode.MODE,
            entity_category=EntityCategory.CONFIG,
            icon="mdi:cog",
            name="Mode",
            custom_configs=localtuya_selector(
                {"sleep": "Sleep", "normal": "Normal", "nature": "Nature"}
            ),
        ),
        LocalTuyaEntity(
            id=DPCode.FAN_VERTICAL,
            entity_category=EntityCategory.CONFIG,
            icon="mdi:format-vertical-align-center",
            name="Vertical swing",
            custom_configs=localtuya_selector(
                {"30": "30 Deg", "60": "60 Deg", "90": "90 Deg"}
            ),
        ),
        LocalTuyaEntity(
            id=DPCode.FAN_HORIZONTAL,
            entity_category=EntityCategory.CONFIG,
            icon="mdi:format-horizontal-align-center",
            name="Horizontal swing",
            custom_configs=localtuya_selector(
                {"30": "30 Deg", "60": "60 Deg", "90": "90 Deg"}
            ),
        ),
        LocalTuyaEntity(
            id=DPCode.WORK_MODE,
            entity_category=EntityCategory.CONFIG,
            icon="mdi:ceiling-fan-light",
            name="Light mode",
            custom_configs=localtuya_selector("white,colour,colourful"),
        ),
        LocalTuyaEntity(
            id=DPCode.COUNTDOWN,
            entity_category=EntityCategory.CONFIG,
            icon="mdi:timer-cog-outline",
            name="Countdown",
            custom_configs=localtuya_selector(COUNT_DOWN),
        ),
        LocalTuyaEntity(
            id=DPCode.COUNTDOWN_SET,
            entity_category=EntityCategory.CONFIG,
            icon="mdi:timer-cog-outline",
            name="Countdown",
            custom_configs=localtuya_selector(COUNT_DOWN_HOURS),
        ),
    ),
    # Curtain
    # https://developer.tuya.com/en/docs/iot/f?id=K9gf46o5mtfyc
    "cl": (
        LocalTuyaEntity(
            id=(DPCode.CONTROL_BACK_MODE, DPCode.CONTROL_BACK),
            name="Motor Direction",
            entity_category=EntityCategory.CONFIG,
            icon="mdi:swap-vertical",
            custom_configs=localtuya_selector({"forward": "Forward", "back": "Back"}),
        ),
        LocalTuyaEntity(
            id=DPCode.MOTOR_MODE,
            name="Motor Mode",
            entity_category=EntityCategory.CONFIG,
            icon="mdi:cog-transfer",
            custom_configs=localtuya_selector(
                {"contiuation": "Auto", "point": "Manual"}
            ),
        ),
        LocalTuyaEntity(
            id=DPCode.MODE,
            entity_category=EntityCategory.CONFIG,
            name="Cover Mode",
            custom_configs=localtuya_selector({"morning": "Morning", "night": "Night"}),
        ),
    ),
    # Humidifier
    # https://developer.tuya.com/en/docs/iot/categoryjsq?id=Kaiuz1smr440b
    "jsq": (
        LocalTuyaEntity(
            id=DPCode.SPRAY_MODE,
            entity_category=EntityCategory.CONFIG,
            icon="mdi:spray",
            name="Spraying mode",
            custom_configs=localtuya_selector("auto,health,baby,sleep,humidity,work"),
        ),
        LocalTuyaEntity(
            id=DPCode.LEVEL,
            entity_category=EntityCategory.CONFIG,
            icon="mdi:spray",
            name="Spraying level",
            custom_configs=localtuya_selector(
                "level_1,level_2,level_3,level_4,level_5,level_6,level_7,level_8,level_9,level_10"
            ),
        ),
        LocalTuyaEntity(
            id=DPCode.MOODLIGHTING,
            entity_category=EntityCategory.CONFIG,
            icon="mdi:lightbulb-multiple",
            name="Mood light",
            custom_configs=localtuya_selector("1,2,3,4,5"),
        ),
        LocalTuyaEntity(
            id=DPCode.COUNTDOWN,
            entity_category=EntityCategory.CONFIG,
            icon="mdi:timer-cog-outline",
            name="Countdown",
            custom_configs=localtuya_selector(COUNT_DOWN),
        ),
        LocalTuyaEntity(
            id=DPCode.COUNTDOWN_SET,
            entity_category=EntityCategory.CONFIG,
            icon="mdi:timer-cog-outline",
            name="Countdown",
            custom_configs=localtuya_selector(COUNT_DOWN_HOURS),
        ),
    ),
    # Air Purifier
    # https://developer.tuya.com/en/docs/iot/f?id=K9gf46h2s6dzm
    "kj": (
        LocalTuyaEntity(
            id=DPCode.COUNTDOWN,
            entity_category=EntityCategory.CONFIG,
            icon="mdi:timer-cog-outline",
            name="Countdown",
            custom_configs=localtuya_selector(COUNT_DOWN),
        ),
        LocalTuyaEntity(
            id=DPCode.COUNTDOWN_SET,
            entity_category=EntityCategory.CONFIG,
            icon="mdi:timer-cog-outline",
            name="Countdown",
            custom_configs=localtuya_selector(COUNT_DOWN_HOURS),
        ),
    ),
    # Dehumidifier
    # https://developer.tuya.com/en/docs/iot/categorycs?id=Kaiuz1vcz4dha
    "cs": (
        LocalTuyaEntity(
            id=DPCode.COUNTDOWN_SET,
            entity_category=EntityCategory.CONFIG,
            icon="mdi:timer-cog-outline",
            name="Countdown",
            custom_configs=localtuya_selector(
                {"cancel": "Disable", "2h": "2 Hours", "4h": "4 Hours", "8h": "8 Hours"}
            ),
        ),
        LocalTuyaEntity(
            id=DPCode.DEHUMIDITY_SET_ENUM,
            name="Target Humidity",
            entity_category=EntityCategory.CONFIG,
            icon="mdi:water-percent",
            custom_configs=localtuya_selector(
                {"10": "10", "20": "20", "30": "30", "40": "40", "50": "50", "60": "60"}
            ),
        ),
        LocalTuyaEntity(
            id=DPCode.SPRAY_VOLUME,
            name="Intensity",
            entity_category=EntityCategory.CONFIG,
            icon="mdi:volume-source",
            custom_configs=localtuya_selector(
                {"small": "Low", "middle": "Medium", "large": "High"}
            ),
        ),
    ),
    # sous vide cookers
    # https://developer.tuya.com/en/docs/iot/f?id=K9r2v9hgmyk3h
    "mzj": (
        LocalTuyaEntity(
            id=DPCode.MODE,
            entity_category=EntityCategory.CONFIG,
            name="Cooking Mode",
            custom_configs=localtuya_selector(
                "vegetables,meat,shrimp,fish,chicken,drumsticks,beef,rice"
            ),
        ),
    ),
    # PIR Detector
    # https://developer.tuya.com/en/docs/iot/categorypir?id=Kaiuz3ss11b80
    "pir": (
        LocalTuyaEntity(
            id=DPCode.MOD,
            icon="mdi:cog",
            entity_category=EntityCategory.CONFIG,
            name="Mode",
            custom_configs=localtuya_selector(
                {"mode_auto": "AUTO", "mode_on": "ON", "mode_off": "OFF"}
            ),
        ),
    ),
    # Thermostat
    # https://developer.tuya.com/en/docs/iot/f?id=K9gf45ld5l0t9
    "wk": (
        LocalTuyaEntity(
            id=DPCode.SENSORTYPE,
            entity_category=EntityCategory.CONFIG,
            name="Temperature sensor",
            custom_configs=localtuya_selector(
                {"0": "Internal", "1": "External", "2": "Both"}
            ),
        ),
    ),
}
# Wireless Switch  # also can come as knob switch.
# https://developer.tuya.com/en/docs/iot/wxkg?id=Kbeo9t3ryuqm5
SELECTS["wxkg"] = (
    LocalTuyaEntity(
        id=DPCode.WORK_MODE,
        name="Display mode",
        icon="mdi:square-outline",
        entity_category=EntityCategory.CONFIG,
        custom_configs=localtuya_selector(
            {"brightness": "Brightness", "temperature": "Temperature"}
        ),
    ),
    *SELECTS["kg"],
)

# Scene Switch
# https://developer.tuya.com/en/docs/iot/f?id=K9gf7nx6jelo8
SELECTS["cjkg"] = SELECTS["kg"]

# Fan wall switch
# For Power-on behavior
SELECTS["fskg"] = SELECTS["kg"]

# Socket (duplicate of `kg`)
# https://developer.tuya.com/en/docs/iot/s?id=K9gf7o5prgf7s
SELECTS["cz"] = SELECTS["kg"]

# Power Socket (duplicate of `kg`)
# https://developer.tuya.com/en/docs/iot/s?id=K9gf7o5prgf7s
SELECTS["pc"] = SELECTS["kg"]

SELECTS["tdq"] = SELECTS["kg"]

# Heater
SELECTS["rs"] = SELECTS["kt"]
