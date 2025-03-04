from enum import StrEnum
from dataclasses import dataclass, field
from typing import Any

from homeassistant.const import (
    CONF_FRIENDLY_NAME,
    CONF_ICON,
    CONF_ENTITY_CATEGORY,
    CONF_DEVICE_CLASS,
    Platform,
    EntityCategory,
)
from ...const import CONF_CLEAN_AREA_DP, CONF_DPS_STRINGS, CONF_STATE_CLASS


# Obtain values from cloud data.
@dataclass
class CLOUD_VALUE:
    """Retrieve a value from stored cloud data

    `default_value`: The value that will be used if it fails to retrieve from the cloud.\n
    `dp_config(str)`: The dp config key that will be used to look for the values into it.\n
    `value_key(str)`: The "key" name of the targeted value.\n
    `prefer_type(dict | str)`: Used for enums to convert the values to [dict or str splitted by comma, default is list].\n
    `remap_values(dict)`: Used to remap dict values, if prefer_type is dict.\n
    `reverse_dict(bool)`: Reverse dict keys, value, if prefer_type is dict.\n
    """

    default_value: Any
    dp_config: str
    value_key: str
    prefer_type: type = None
    remap_values: dict[str, Any] = field(default_factory=dict)
    reverse_dict: bool = False


class LocalTuyaEntity:
    """
    Localtuya entity config.
    Each platform has unique custom_configs to give the required data to validate entity setups.
    e.g. Switch req( Friendly_Name and DP(Code) )
    """

    def __init__(
        self,
        name: str = "",
        icon: str = "",
        entity_category="None",
        device_class=None,
        state_class=None,
        custom_configs: dict[str, Any | tuple[Any, CLOUD_VALUE]] = {},
        condition_contains_any: list = None,
        **kwargs,
    ):
        # platform, name, icon, entity_category, device_class, *key
        # self.platform = platform
        self.name = name
        self.data = {
            CONF_FRIENDLY_NAME: name,
            CONF_ICON: icon,
            CONF_ENTITY_CATEGORY: entity_category,
        }

        # Optional
        if device_class:
            self.data[CONF_DEVICE_CLASS] = device_class

        # Optional
        if state_class:
            self.data[CONF_STATE_CLASS] = state_class

        self.entity_configs = custom_configs

        self.contains_any = condition_contains_any

        # Replace key with id if needed
        if kwargs.get("key", False):
            kwargs["id"] = kwargs.pop("key")
        # e.g.e CONF_ID etc..

        self.localtuya_conf = kwargs


class DPType(StrEnum):
    """Data point types."""

    BOOLEAN = "Boolean"
    ENUM = "Enum"
    INTEGER = "Integer"
    JSON = "Json"
    RAW = "Raw"
    STRING = "String"


class DPCode(StrEnum):
    """Data Point Codes used by Tuya.

    https://developer.tuya.com/en/docs/iot/standarddescription?id=K9i5ql6waswzq
    """

    ADD_ELE = "add_ele"
    AIR_QUALITY = "air_quality"
    ALARM_LOCK = "alarm_lock"
    ALARM_MESSAGE = "alarm_message"
    ALARM_RINGTONE = "alarm_ringtone"
    ALARM_STATE = "alarm_state"
    ALARM_SWITCH = "alarm_switch"  # Alarm switch
    ALARM_TIME = "alarm_time"  # Alarm time
    ALARM_VOLUME = "alarm_volume"  # Alarm volume
    ANGLE_HORIZONTAL = "angle_horizontal"
    ANGLE_VERTICAL = "angle_vertical"
    ANION = "anion"  # Ionizer unit
    ANTILOCK_STATUS = "antilock_status"
    APPOINTMENT_TIME = "appointment_time"
    ARMING_SWITCH = "arming_switch"
    ARM_DOWN_PERCENT = "arm_down_percent"
    ARM_UP_PERCENT = "arm_up_percent"
    AUTOMATIC_LOCK = "automatic_lock"
    AUTO_LOCK_TIME = "auto_lock_time"
    BACKLIGHT_SWITCH = "backlight_switch"
    BASIC_ANTI_FLICKER = "basic_anti_flicker"
    BASIC_DEVICE_VOLUME = "basic_device_volume"
    BASIC_FLIP = "basic_flip"
    BASIC_INDICATOR = "basic_indicator"
    BASIC_NIGHTVISION = "basic_nightvision"
    BASIC_OSD = "basic_osd"
    BASIC_PRIVATE = "basic_private"
    BASIC_WDR = "basic_wdr"
    BASS_CONTROL = "bass_control"
    BATTERY = "battery"
    BATTERY_PERCENTAGE = "battery_percentage"  # Battery percentage
    BATTERY_STATE = "battery_state"  # Battery state
    BATTERY_VALUE = "battery_value"  # Battery value
    BRIGHTNESS_MAX_1 = "brightness_max_1"
    BRIGHTNESS_MAX_2 = "brightness_max_2"
    BRIGHTNESS_MAX_3 = "brightness_max_3"
    BRIGHTNESS_MIN_1 = "brightness_min_1"
    BRIGHTNESS_MIN_2 = "brightness_min_2"
    BRIGHTNESS_MIN_3 = "brightness_min_3"
    BRIGHT_CONTROLLER = "bright_controller"
    BRIGHT_STATE = "bright_state"  # Brightness status
    BRIGHT_VALUE = "bright_value"  # Brightness
    BRIGHT_VALUE_1 = "bright_value_1"
    BRIGHT_VALUE_2 = "bright_value_2"
    BRIGHT_VALUE_3 = "bright_value_3"
    BRIGHT_VALUE_4 = "bright_value_4"
    BRIGHT_VALUE_V2 = "bright_value_v2"
    CALLPHONE = "callphone"
    CH2O_STATE = "ch2o_state"
    CH2O_VALUE = "ch2o_value"
    CH4_SENSOR_STATE = "ch4_sensor_state"
    CH4_SENSOR_VALUE = "ch4_sensor_value"
    CHILDLOCK = "childlock"
    CHILD_LOCK = "child_lock"  # Child lock
    CISTERN = "cistern"
    CLEAN_AREA = "clean_area"
    CLEAN_RECORD = "clean_record"
    CLEAN_TIME = "clean_time"
    CLICK_SUSTAIN_TIME = "click_sustain_time"
    CLOSED_OPENED = "closed_opened"
    CLOSED_OPENED_KIT = "closed_opened_kit"
    CLOUD_RECIPE_NUMBER = "cloud_recipe_number"
    CO2_STATE = "co2_state"
    CO2_VALUE = "co2_value"  # CO2 concentration
    COLLECTION_MODE = "collection_mode"
    COLOR_DATA_V2 = "color_data_v2"
    COLOUR_DATA = "colour_data"  # Colored light mode
    COLOUR_DATA_HSV = "colour_data_hsv"  # Colored light mode
    COLOUR_DATA_V2 = "colour_data_v2"  # Colored light mode
    CONCENTRATION_SET = "concentration_set"  # Concentration setting
    CONTROL = "control"
    CONTROL_2 = "control_2"
    CONTROL_3 = "control_3"
    CONTROL_4 = "control_4"
    CONTROL_BACK = "control_back"
    CONTROL_BACK_MODE = "control_back_mode"
    COOK_TEMPERATURE = "cook_temperature"
    COOK_TIME = "cook_time"
    COUNTDOWN = "countdown"  # Countdown
    COUNTDOWN_1 = "countdown_1"  # Countdown 1
    COUNTDOWN_2 = "countdown_2"  # Countdown 2
    COUNTDOWN_3 = "countdown_3"  # Countdown 3
    COUNTDOWN_4 = "countdown_4"  # Countdown 4
    COUNTDOWN_5 = "countdown_5"  # Countdown 5
    COUNTDOWN_6 = "countdown_6"  # Countdown 6
    COUNTDOWN_LEFT = "countdown_left"
    COUNTDOWN_SET = "countdown_set"  # Countdown setting
    COUNTDOWN_USB = "countdown"  # Countdown
    COUNTDOWN_USB1 = "countdown_usb1"  # Countdown USBS 1
    COUNTDOWN_USB2 = "countdown_usb2"  # Countdown USBS 2
    COUNTDOWN_USB3 = "countdown_usb3"  # Countdown USBS 3
    COUNTDOWN_USB4 = "countdown_usb4"  # Countdown USBS 4
    COUNTDOWN_USB5 = "countdown_usb5"  # Countdown USBS 5
    COUNTDOWN_USB6 = "countdown_usb6"  # Countdown USBS 6
    CO_STATE = "co_state"
    CO_STATUS = "co_status"
    CO_VALUE = "co_value"
    CRUISE_MODE = "cruise_mode"
    CRY_DETECTION_SWITCH = "cry_detection_switch"
    CUP_NUMBER = "cup_number"  # NUmber of cups
    CUR_CURRENT = "cur_current"  # Actual current
    CUR_POWER = "cur_power"  # Actual power
    CUR_VOLTAGE = "cur_voltage"  # Actual voltage
    C_F = "c_f"  # Temperature unit switching
    DECIBEL_SENSITIVITY = "decibel_sensitivity"
    DECIBEL_SWITCH = "decibel_switch"
    DEHUMIDITY_SET_ENUM = "dehumidify_set_enum"
    DEHUMIDITY_SET_VALUE = "dehumidify_set_value"
    DISINFECTION = "disinfection"
    DOORBELL = "doorbell"
    DOORCONTACT_STATE = "doorcontact_state"  # Status of door window sensor
    DOORCONTACT_STATE_2 = "doorcontact_state_2"
    DOORCONTACT_STATE_3 = "doorcontact_state_3"
    DOOR_UNCLOSED = "door_unclosed"
    DOOR_UNCLOSED_TRIGGER = "door_unclosed_trigger"
    DOWN_CONFIRM = "down_confirm"  # cover reset.
    DO_NOT_DISTURB = "do_not_disturb"
    DUSTER_CLOTH = "duster_cloth"
    ECO2 = "eco2"
    EDGE_BRUSH = "edge_brush"
    ELECTRICITY_LEFT = "electricity_left"
    FAN_BEEP = "fan_beep"  # Sound
    FAN_COOL = "fan_cool"  # Cool wind
    FAN_DIRECTION = "fan_direction"  # Fan direction
    FAN_HORIZONTAL = "fan_horizontal"  # Horizontal swing flap angle
    FAN_MODE = "fan_mode"
    FAN_SPEED = "fan_speed"
    FAN_SPEED_ENUM = "fan_speed_enum"  # Speed mode
    FAN_SPEED_PERCENT = "fan_speed_percent"  # Stepless speed
    FAN_SWITCH = "fan_switch"
    FAN_VERTICAL = "fan_vertical"  # Vertical swing flap angle
    FAR_DETECTION = "far_detection"
    FAULT = "fault"
    FEED_REPORT = "feed_report"
    FEED_STATE = "feed_state"
    FILTER = "filter"
    FILTER_LIFE = "filter"
    FILTER_RESET = "filter_reset"  # Filter (cartridge) reset
    FLIGHT_BRIGHT_MODE = "flight_bright_mode"
    FLOODLIGHT_LIGHTNESS = "floodlight_lightness"
    FLOODLIGHT_SWITCH = "floodlight_switch"
    FORWARD_ENERGY_TOTAL = "forward_energy_total"
    GAS_SENSOR_STATE = "gas_sensor_state"
    GAS_SENSOR_STATUS = "gas_sensor_status"
    GAS_SENSOR_VALUE = "gas_sensor_value"
    HIGHTPROTECTVALUE = "hightprotectvalue"
    HIJACK = "hijack"
    HUMIDIFIER = "humidifier"  # Humidification
    HUMIDITY = "humidity"  # Humidity
    HUMIDITY_CURRENT = "humidity_current"  # Current humidity
    HUMIDITY_INDOOR = "humidity_indoor"  # Indoor humidity
    HUMIDITY_SET = "humidity_set"  # Humidity setting
    HUMIDITY_VALUE = "humidity_value"  # Humidity
    IPC_WORK_MODE = "ipc_work_mode"
    LED_TYPE_1 = "led_type_1"
    LED_TYPE_2 = "led_type_2"
    LED_TYPE_3 = "led_type_3"
    LEVEL = "level"
    LEVEL_CURRENT = "level_current"
    LIGHT = "light"  # Light
    LIGHT_MODE = "light_mode"
    LOADSTATUS = "loadstatus"
    LOCK = "lock"  # Lock / Child lock
    LOWPROTECTVALUE = "lowprotectvalue"
    LOW_POWER_THRESHOLD = "low_power_threshold"
    LUX = "lux"  # Ikuu SXSEN003PIR IP65 Motion Detector (Wi-Fi)
    MACH_OPERATE = "mach_operate"
    MANUAL_FEED = "manual_feed"
    MASTER_MODE = "master_mode"  # alarm mode
    MASTER_STATE = "master_state"  # alarm mode
    MATERIAL = "material"  # Material
    MIDDLE_CONFIRM = "middle_confirm"  # cover reset.
    MOD = "mod"  # Ikuu SXSEN003PIR IP65 Motion Detector (Wi-Fi)
    MODE = "mode"  # Working mode / Mode
    MODE_1 = "mode_1"  # Working mode / Mode
    MODE_2 = "mode_2"  # Working mode / Mode
    MODE_3 = "mode_3"  # Working mode / Mode
    MODE_4 = "mode_4"  # Working mode / Mode
    MODE_5 = "mode_5"  # Working mode / Mode
    MODE_6 = "mode_6"  # Working mode / Mode
    MOD_ON_TMR = "mod_on_tmr"  # Ikuu SXSEN003PIR IP65 Motion Detector (Wi-Fi)
    MOD_ON_TMR_CD = "mod_on_tmr_cd"  # Ikuu SXSEN003PIR IP65 Motion Detector (Wi-Fi)
    MOODLIGHTING = "moodlighting"  # Mood light
    MOTION_INTERVAL = "motion_interval"
    MOTION_RECORD = "motion_record"
    MOTION_SENSITIVITY = "motion_sensitivity"
    MOTION_SWITCH = "motion_switch"  # Motion switch
    MOTION_TRACKING = "motion_tracking"
    MOTOR_MODE = "motor_mode"
    MOVEMENT_DETECT_PIC = "movement_detect_pic"
    MUFFLING = "muffling"  # Muffling
    MUTE = "mute"
    NEAR_DETECTION = "near_detection"
    NORMAL_OPEN_SWITCH = "normal_open_switch"
    OPPOSITE = "opposite"
    OPTIMUMSTART = "optimumstart"
    OVERCHARGE_SWITCH = "overcharge_switch"
    OXYGEN = "oxygen"  # Oxygen bar
    PAUSE = "pause"
    PERCENT_CONTROL = "percent_control"
    PERCENT_CONTROL_2 = "percent_control_2"
    PERCENT_CONTROL_3 = "percent_control_3"
    PERCENT_CONTROL_4 = "percent_control_4"
    PERCENT_STATE = "percent_state"
    PERCENT_STATE_2 = "percent_state_2"
    PERCENT_STATE_3 = "percent_state_3"
    PERCENT_STATE_4 = "percent_state_4"
    PHASE_A = "phase_a"
    PHASE_B = "phase_b"
    PHASE_C = "phase_c"
    PHOTO_MODE = "photo_mode"
    PIR = "pir"  # Motion sensor
    PIR_SENSITIVITY = "pir_sensitivity"
    PLAY_INFO = "play_info"
    PLAY_MODE = "play_mode"
    PLAY_TIME = "play_time"
    PM1 = "pm1"
    PM10 = "pm10"
    PM100_STATE = "pm100_state"
    PM100_VALUE = "pm100_value"
    PM10_STATE = "pm10_state"
    PM10_VALUE = "pm10_value"
    PM25 = "pm25"
    PM25_STATE = "pm25_state"
    PM25_VALUE = "pm25_value"
    POSITION = "position"
    POWDER_SET = "powder_set"  # Powder
    POWER = "power"
    POWER_GO = "power_go"
    PRESENCE_STATE = "presence_state"
    PRESSURE_STATE = "pressure_state"
    PRESSURE_VALUE = "pressure_value"
    PRM_CONTENT = "prm_content"
    PRM_TEMPERATURE = "prm_temperature"
    PTZ_CONTROL = "ptz_control"
    PUMP_RESET = "pump_reset"  # Water pump reset
    RECORD_MODE = "record_mode"
    RECORD_SWITCH = "record_switch"  # Recording switch
    RELAY_STATUS = "relay_status"
    RELAY_STATUS_1 = "relay_status_1"  # Scene Switch cjkg
    RELAY_STATUS_2 = "relay_status_2"  # Scene Switch cjkg
    RELAY_STATUS_3 = "relay_status_3"  # Scene Switch cjkg
    RELAY_STATUS_4 = "relay_status_4"  # Scene Switch cjkg
    RELAY_STATUS_5 = "relay_status_5"  # Scene Switch cjkg
    RELAY_STATUS_6 = "relay_status_6"  # Scene Switch cjkg
    RELAY_STATUS_7 = "relay_status_7"  # Scene Switch cjkg
    RELAY_STATUS_8 = "relay_status_8"  # Scene Switch cjkg
    REMAIN_TIME = "remain_time"
    REMOTE_REGISTER = "remote_register"
    RESET_DUSTER_CLOTH = "reset_duster_cloth"
    RESET_EDGE_BRUSH = "reset_edge_brush"
    RESET_FILTER = "reset_filter"
    RESET_LIMIT = "reset_limit"
    RESET_MAP = "reset_map"
    RESET_ROLL_BRUSH = "reset_roll_brush"
    ROLL_BRUSH = "roll_brush"
    SCENE_1 = "scene_1"
    SCENE_10 = "scene_10"
    SCENE_11 = "scene_11"
    SCENE_12 = "scene_12"
    SCENE_13 = "scene_13"
    SCENE_14 = "scene_14"
    SCENE_15 = "scene_15"
    SCENE_16 = "scene_16"
    SCENE_17 = "scene_17"
    SCENE_18 = "scene_18"
    SCENE_19 = "scene_19"
    SCENE_2 = "scene_2"
    SCENE_20 = "scene_20"
    SCENE_3 = "scene_3"
    SCENE_4 = "scene_4"
    SCENE_5 = "scene_5"
    SCENE_6 = "scene_6"
    SCENE_7 = "scene_7"
    SCENE_8 = "scene_8"
    SCENE_9 = "scene_9"
    SCENE_DATA = "scene_data"  # Colored light mode
    SCENE_DATA_V2 = "scene_data_v2"  # Colored light mode
    SEEK = "seek"
    SENS = "sens"  # Ikuu SXSEN003PIR IP65 Motion Detector (Wi-Fi)
    SENSITIVITY = "sensitivity"  # Sensitivity
    SENSORTYPE = "sensortype"
    SENSOR_HUMIDITY = "sensor_humidity"
    SENSOR_TEMPERATURE = "sensor_temperature"
    SHAKE = "shake"  # Oscillating
    SHOCK_STATE = "shock_state"  # Vibration status
    SIREN_SWITCH = "siren_switch"
    SITUATION_SET = "situation_set"
    SLEEP = "sleep"  # Sleep function
    SLOW_FEED = "slow_feed"
    SMOKE_SENSOR_STATE = "smoke_sensor_state"
    SMOKE_SENSOR_STATUS = "smoke_sensor_status"
    SMOKE_SENSOR_VALUE = "smoke_sensor_value"
    SOS = "sos"  # Emergency State
    SOS_STATE = "sos_state"  # Emergency mode
    SOUND_EFFECTS = "sound_effects"
    SOUND_MODE = "sound_mode"
    SOURCE = "source"
    SPEED = "speed"  # Speed level
    SPRAY_MODE = "spray_mode"  # Spraying mode
    SPRAY_VOLUME = "spray_volume"  # Dehumidifier
    STA = "sta"  # Ikuu SXSEN003PIR IP65 Motion Detector (Wi-Fi)
    START = "start"  # Start
    STATUS = "status"
    STERILIZATION = "sterilization"  # Sterilization
    SUCTION = "suction"
    SWING = "swing"  # Swing mode
    SWITCH = "switch"  # Switch
    SWITCH1 = "switch1"  # Switch 1 no underscore
    SWITCH2 = "switch2"  # Switch 2 no underscore
    SWITCH3 = "switch3"  # Switch 3 no underscore
    SWITCH4 = "switch4"  # Switch 4 no underscore
    SWITCH5 = "switch5"  # Switch 5 no underscore
    SWITCH6 = "switch6"  # Switch 6 no underscore
    SWITCH7 = "switch7"  # Switch 7 no underscore
    SWITCH8 = "switch8"  # Switch 8 no underscore
    SWITCH_1 = "switch_1"  # Switch 1
    SWITCH_2 = "switch_2"  # Switch 2
    SWITCH_3 = "switch_3"  # Switch 3
    SWITCH_4 = "switch_4"  # Switch 4
    SWITCH_5 = "switch_5"  # Switch 5
    SWITCH_6 = "switch_6"  # Switch 6
    SWITCH_7 = "switch_7"  # Switch 7
    SWITCH_8 = "switch_8"  # Switch 8
    SWITCH_ALARM_SOUND = "switch_alarm_sound"
    SWITCH_BACKLIGHT = "switch_backlight"  # Backlight switch
    SWITCH_CHARGE = "switch_charge"
    SWITCH_CONTROLLER = "switch_controller"
    SWITCH_DISTURB = "switch_disturb"
    SWITCH_FAN = "switch_fan"
    SWITCH_HORIZONTAL = "switch_horizontal"  # Horizontal swing flap switch
    SWITCH_LED = "switch_led"  # Switch
    SWITCH_LED_1 = "switch_led_1"
    SWITCH_LED_2 = "switch_led_2"
    SWITCH_LED_3 = "switch_led_3"
    SWITCH_LED_4 = "switch_led_4"
    SWITCH_NIGHT_LIGHT = "switch_night_light"
    SWITCH_SAVE_ENERGY = "switch_save_energy"
    SWITCH_SOUND = "switch_sound"  # Voice switch
    SWITCH_SPRAY = "switch_spray"  # Spraying switch
    SWITCH_USB1 = "switch_usb1"  # USB 1
    SWITCH_USB2 = "switch_usb2"  # USB 2
    SWITCH_USB3 = "switch_usb3"  # USB 3
    SWITCH_USB4 = "switch_usb4"  # USB 4
    SWITCH_USB5 = "switch_usb5"  # USB 5
    SWITCH_USB6 = "switch_usb6"  # USB 6
    SWITCH_VERTICAL = "switch_vertical"  # Vertical swing flap switch
    SWITCH_VOICE = "switch_voice"  # Voice switch
    SWITCH_WELCOME = "switch_welcome"
    TEMP = "temp"  # Temperature setting
    TEMPACTIVATE = "tempactivate"
    TEMPCOMP = "tempcomp"
    TEMPER_ALARM = "temper_alarm"  # Tamper alarm
    TEMPFLOOR = "TempFloor"
    TEMPPROGRAM = "tempprogram"
    TEMP_BOILING_C = "temp_boiling_c"
    TEMP_BOILING_F = "temp_boiling_f"
    TEMP_CONTROLLER = "temp_controller"
    TEMP_CURRENT = "temp_current"  # Current temperature in °C
    TEMP_CURRENT_F = "temp_current_f"  # Current temperature in °F
    TEMP_INDOOR = "temp_indoor"  # Indoor temperature in °C
    TEMP_SET = "temp_set"  # Set the temperature in °C
    TEMP_SET_F = "temp_set_f"  # Set the temperature in °F
    TEMP_UNIT_CONVERT = "temp_unit_convert"  # Temperature unit switching
    TEMP_VALUE = "temp_value"  # Color temperature
    TEMP_VALUE_V2 = "temp_value_v2"
    TIM = "tim"  # Ikuu SXSEN003PIR IP65 Motion Detector (Wi-Fi)
    TIME_TOTAL = "time_total"
    TOTAL_CLEAN_AREA = "total_clean_area"
    TOTAL_CLEAN_COUNT = "total_clean_count"
    TOTAL_CLEAN_TIME = "total_clean_time"
    TOTAL_FORWARD_ENERGY = "total_forward_energy"
    TOTAL_PM = "total_pm"
    TOTAL_TIME = "total_time"
    TREBLE_CONTROL = "treble_control"
    TVOC = "tvoc"
    UNLOCK_APP = "unlock_app"
    UNLOCK_BLE = "unlock_ble"
    UNLOCK_CARD = "unlock_card"
    UNLOCK_DOUBLE = "unlock_double"
    UNLOCK_DYNAMIC = "unlock_dynamic"
    UNLOCK_EYE = "unlock_eye"
    UNLOCK_FACE = "unlock_face"
    UNLOCK_FINGERPRINT = "unlock_fingerprint"
    UNLOCK_FINGER_VEIN = "unlock_finger_vein"
    UNLOCK_HAND = "unlock_hand"
    UNLOCK_IDENTITY_CARD = "unlock_identity_card"
    UNLOCK_KEY = "unlock_key"
    UNLOCK_PASSWORD = "unlock_password"
    UNLOCK_PHONE_REMOTE = "unlock_phone_remote"
    UNLOCK_REMOTE = "unlock_remote"
    UNLOCK_REQUEST = "unlock_request"
    UNLOCK_SPECIAL = "unlock_special"
    UNLOCK_SWITCH = "unlock_switch"
    UNLOCK_TEMPORARY = "unlock_temporary"
    UNLOCK_VOICE_REMOTE = "unlock_voice_remote"
    UPPER_TEMP = "upper_temp"
    UPPER_TEMP_F = "upper_temp_f"
    UP_CONFIRM = "up_confirm"  # cover reset.
    UV = "uv"  # UV sterilization
    VA_BATTERY = "va_battery"
    VA_HUMIDITY = "va_humidity"
    VA_TEMPERATURE = "va_temperature"
    VOC_STATE = "voc_state"
    VOC_VALUE = "voc_value"
    VOICE_BT_PLAY = "voice_bt_play"
    VOICE_MIC = "voice_mic"
    VOICE_PLAY = "voice_play"
    VOICE_SWITCH = "voice_switch"
    VOICE_TIMES = "voice_times"
    VOICE_VOL = "voice_vol"
    VOLUME_SET = "volume_set"
    WARM = "warm"  # Heat preservation
    WARM_TIME = "warm_time"  # Heat preservation time
    WATER = "water"
    WATERSENSOR_STATE = "watersensor_state"
    WATER_RESET = "water_reset"  # Resetting of water usage days
    WATER_SET = "water_set"  # Water level
    WET = "wet"  # Humidification
    WINDOWDETECT = "windowdetect"
    WINDOW_CHECK = "window_check"
    WINDOW_STATE = "window_state"
    WINDSPEED = "windspeed"
    WIRELESS_BATTERYLOCK = "wireless_batterylock"
    WIRELESS_ELECTRICITY = "wireless_electricity"
    WORK_MODE = "work_mode"  # Working mode
    WORK_POWER = "work_power"
    WORK_STATE = "work_state"
    WORK_STATUS = "work_status"
