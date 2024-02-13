# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
# import requests
import boto3

import logging
import json

import paho.mqtt.publish as publish
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Surveillance Functions Opened! What function do you need me to perform?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello World!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class AllCameraToggleOnHandler(AbstractRequestHandler):
    """Handler for CameraToggleOn Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AllCameraToggleOn")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Create a list of cameras with their labels
            cameras_list = list(config_data["cameras"].values())

            payload = {
                "allcam": cameras_list,
                "feature": "detect",
                "value": "ON"
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/allcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="all-d1"
            )
            speak_output = "All Camera Detection Feature ON."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class AllCameraToggleOffHandler(AbstractRequestHandler):
    """Handler for CameraToggleOff Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AllCameraToggleOff")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Create a list of cameras with their labels
            cameras_list = list(config_data["cameras"].values())

            payload = {
                "allcam": cameras_list,
                "feature": "detect",
                "value": "OFF"
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/allcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="all-d0"
            )
            speak_output = "All Camera Detection Feature OFF."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class AllRecordingToggleOnHandler(AbstractRequestHandler):
    """Handler for RecordingToggleOn Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AllRecordingToggleOn")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Create a list of cameras with their labels
            cameras_list = list(config_data["cameras"].values())

            payload = {
                "allcam": cameras_list,
                "feature": "recordings",
                "value": "ON"
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/allcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="all-r1"
            )
            speak_output = "All Camera Recording Feature ON."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class AllRecordingToggleOffHandler(AbstractRequestHandler):
    """Handler for RecordingToggleOff Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AllRecordingToggleOff")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Create a list of cameras with their labels
            cameras_list = list(config_data["cameras"].values())

            payload = {
                "allcam": cameras_list,
                "feature": "recordings",
                "value": "OFF"
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/allcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="all-r0"
            )
            speak_output = "All Camera Recording Feature OFF."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class AllSnapshotOnIntentHandler(AbstractRequestHandler):
    """Handler for SnapshotOn Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AllSnapshotOnIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Create a list of cameras with their labels
            cameras_list = list(config_data["cameras"].values())

            payload = {
                "allcam": cameras_list,
                "feature": "snapshots",
                "value": "ON"
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/allcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="all-s1"
            )
            speak_output = "All Camera Snapshot Feature ON."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class AllSnapshotOffIntentHandler(AbstractRequestHandler):
    """Handler for SnapshotOff Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AllSnapshotOffIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Create a list of cameras with their labels
            cameras_list = list(config_data["cameras"].values())

            payload = {
                "allcam": cameras_list,
                "feature": "snapshots",
                "value": "OFF"
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/allcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="all-s0"
            )
            speak_output = "All Camera Snapshot Feature OFF."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CameraOneOnIntentHandler(AbstractRequestHandler):
    """Handler for CameraOneOnIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ParkingAreaCameraOnIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_01"]
            
            payload = {
                "allfeature":["detect","recordings","snapshots"],
                "camera":single_camera,
                "value":"ON"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/eachcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="c1-all-on"
            )
            speak_output = single_camera + " All Features ON."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CameraOneOffIntentHandler(AbstractRequestHandler):
    """Handler for CameraOneOffIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ParkingAreaCameraOffIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_01"]
            
            payload = {
                "allfeature":["detect","recordings","snapshots"],
                "camera":single_camera,
                "value":"OFF"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/eachcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="c1-all-off"
            )
            speak_output = single_camera + " All Features OFF."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CameraTwoOnIntentHandler(AbstractRequestHandler):
    """Handler for CameraTwoOnIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("EntranceCameraOnIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_02"]
            
            payload = {
                "allfeature":["detect","recordings","snapshots"],
                "camera":single_camera,
                "value":"ON"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/eachcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="c2-all-on"
            )
            speak_output = single_camera + " All Features ON."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CameraTwoOffIntentHandler(AbstractRequestHandler):
    """Handler for CameraTwoOffIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("EntranceCameraOffIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_02"]
            
            payload = {
                "allfeature":["detect","recordings","snapshots"],
                "camera":single_camera,
                "value":"OFF"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/eachcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="c2-all-off"
            )
            speak_output = single_camera + " All Features OFF."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CameraThreeOnIntentHandler(AbstractRequestHandler):
    """Handler for CameraThreeOnIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ExitCameraOnIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_03"]
            
            payload = {
                "allfeature":["detect","recordings","snapshots"],
                "camera":single_camera,
                "value":"ON"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/eachcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="c3-all-on"
            )
            speak_output = single_camera + " All Features ON."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CameraThreeOffIntentHandler(AbstractRequestHandler):
    """Handler for CameraThreeOffIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ExitCameraOffIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_03"]
            
            payload = {
                "allfeature":["detect","recordings","snapshots"],
                "camera":single_camera,
                "value":"OFF"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/eachcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="c3-all-off"
            )
            speak_output = single_camera + " All Features OFF."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CameraFourOnIntentHandler(AbstractRequestHandler):
    """Handler for CameraFourOnIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("LiftAreaCameraOnIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_04"]
            
            payload = {
                "allfeature":["detect","recordings","snapshots"],
                "camera":single_camera,
                "value":"ON"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/eachcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="c4-all-on"
            )
            speak_output = single_camera + " All Features ON."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CameraFourOffIntentHandler(AbstractRequestHandler):
    """Handler for CameraFourOffIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("LiftAreaCameraOffIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_04"]
            
            payload = {
                "allfeature":["detect","recordings","snapshots"],
                "camera":single_camera,
                "value":"OFF"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/eachcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="c4-all-off"
            )
            speak_output = single_camera + " All Features OFF."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CameraFiveOnIntentHandler(AbstractRequestHandler):
    """Handler for CameraFiveOnIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("BillingSectionCameraOnIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_05"]
            
            payload = {
                "allfeature":["detect","recordings","snapshots"],
                "camera":single_camera,
                "value":"ON"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/eachcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="c5-all-on"
            )
            speak_output = single_camera + " All Features ON."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CameraFiveOffIntentHandler(AbstractRequestHandler):
    """Handler for CameraFiveOffIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("BillingSectionCameraOffIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_05"]
            
            payload = {
                "allfeature":["detect","recordings","snapshots"],
                "camera":single_camera,
                "value":"OFF"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/eachcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="c5-all-off"
            )
            speak_output = single_camera + " All Features OFF."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CameraSixOnIntentHandler(AbstractRequestHandler):
    """Handler for CameraSixOnIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FrontDoorEntranceCameraOnIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_06"]
            
            payload = {
                "allfeature":["detect","recordings","snapshots"],
                "camera":single_camera,
                "value":"ON"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/eachcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="c6-all-on"
            )
            speak_output = single_camera + " All Features ON."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CameraSixOffIntentHandler(AbstractRequestHandler):
    """Handler for CameraSixOffIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FrontDoorEntranceCameraOffIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_06"]
            
            payload = {
                "allfeature":["detect","recordings","snapshots"],
                "camera":single_camera,
                "value":"OFF"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/eachcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="c6-all-off"
            )
            speak_output = single_camera + " All Features OFF."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CameraSevenOnIntentHandler(AbstractRequestHandler):
    """Handler for CameraSevenOnIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("LivingRoomCameraOnIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_07"]
            
            payload = {
                "allfeature":["detect","recordings","snapshots"],
                "camera":single_camera,
                "value":"ON"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/eachcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="c7-all-on"
            )
            speak_output = single_camera + " All Features ON."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CameraSevenOffIntentHandler(AbstractRequestHandler):
    """Handler for CameraSevenOffIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("LivingRoomCameraOffIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_07"]
            
            payload = {
                "allfeature":["detect","recordings","snapshots"],
                "camera":single_camera,
                "value":"OFF"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/eachcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="c7-all-off"
            )
            speak_output = single_camera + " All Features OFF."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CameraEightOnIntentHandler(AbstractRequestHandler):
    """Handler for CameraEightOnIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("BackDoorCameraOnIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_08"]
            
            payload = {
                "allfeature":["detect","recordings","snapshots"],
                "camera":single_camera,
                "value":"ON"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/eachcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="c8-all-on"
            )
            speak_output = single_camera + " All Features ON."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CameraEightOffIntentHandler(AbstractRequestHandler):
    """Handler for CameraEightOffIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("BackDoorCameraOffIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_08"]
            
            payload = {
                "allfeature":["detect","recordings","snapshots"],
                "camera":single_camera,
                "value":"OFF"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/eachcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="c8-all-off"
            )
            speak_output = single_camera + " All Features OFF."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CameraNineOnIntentHandler(AbstractRequestHandler):
    """Handler for CameraNineOnIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("KitchenCameraOnIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_09"]
            
            payload = {
                "allfeature":["detect","recordings","snapshots"],
                "camera":single_camera,
                "value":"ON"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/eachcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="c9-all-on"
            )
            speak_output = single_camera + " All Features ON."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CameraNineOffIntentHandler(AbstractRequestHandler):
    """Handler for CameraNineOffIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("KitchenCameraOffIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_09"]
            
            payload = {
                "allfeature":["detect","recordings","snapshots"],
                "camera":single_camera,
                "value":"OFF"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/eachcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="c9-all-off"
            )
            speak_output = single_camera + " All Features OFF."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CameraTenOnIntentHandler(AbstractRequestHandler):
    """Handler for CameraNineOffIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("BalconyCameraOnIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_10"]
            
            payload = {
                "allfeature":["detect","recordings","snapshots"],
                "camera":single_camera,
                "value":"ON"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/eachcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="c10-all-on"
            )
            speak_output = single_camera + " All Features OFF."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CameraTenOffIntentHandler(AbstractRequestHandler):
    """Handler for CameraNineOffIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("BalconyCameraOffIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_10"]
            
            payload = {
                "allfeature":["detect","recordings","snapshots"],
                "camera":single_camera,
                "value":"OFF"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/eachcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="c10-all-off"
            )
            speak_output = single_camera + " All Features OFF."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CameraElevenOnIntentHandler(AbstractRequestHandler):
    """Handler for CameraNineOffIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("BasementCameraOnIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_11"]
            
            payload = {
                "allfeature":["detect","recordings","snapshots"],
                "camera":single_camera,
                "value":"ON"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/eachcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="c11-all-on"
            )
            speak_output = single_camera + " All Features OFF."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CameraElevenOffIntentHandler(AbstractRequestHandler):
    """Handler for CameraNineOffIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("BasementCameraOffIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_11"]
            
            payload = {
                "allfeature":["detect","recordings","snapshots"],
                "camera":single_camera,
                "value":"OFF"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/eachcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="c11-all-off"
            )
            speak_output = single_camera + " All Features OFF."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CameraTwelveOnIntentHandler(AbstractRequestHandler):
    """Handler for CameraNineOffIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("MainGateCameraOnIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_12"]
            
            payload = {
                "allfeature":["detect","recordings","snapshots"],
                "camera":single_camera,
                "value":"ON"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/eachcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="c12-all-on"
            )
            speak_output = single_camera + " All Features OFF."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CameraTwelveOffIntentHandler(AbstractRequestHandler):
    """Handler for CameraNineOffIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("MainGateCameraOffIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_12"]
            
            payload = {
                "allfeature":["detect","recordings","snapshots"],
                "camera":single_camera,
                "value":"OFF"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/eachcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="c12-all-off"
            )
            speak_output = single_camera + " All Features OFF."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CameraThirteenOnIntentHandler(AbstractRequestHandler):
    """Handler for CameraNineOffIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("StoreRoomCameraOnIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_13"]
            
            payload = {
                "allfeature":["detect","recordings","snapshots"],
                "camera":single_camera,
                "value":"ON"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/eachcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="c13-all-on"
            )
            speak_output = single_camera + " All Features OFF."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CameraThirteenOffIntentHandler(AbstractRequestHandler):
    """Handler for CameraNineOffIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("StoreRoomCameraOffIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_13"]
            
            payload = {
                "allfeature":["detect","recordings","snapshots"],
                "camera":single_camera,
                "value":"OFF"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/eachcam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="c13-all-off"
            )
            speak_output = single_camera + " All Features OFF."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class OneAmSummaryHandler(AbstractRequestHandler):
    """Handler for OneAmSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("OneAmSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            payload = {
                "payload":"01:00:00"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/time",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-1am"
            )
            speak_output = "Which Camera Summary should be sent ?"
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class TwoAmSummaryHandler(AbstractRequestHandler):
    """Handler for TwoAmSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TwoAmSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            payload = {
                "payload":"02:00:00"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/time",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-2am"
            )
            speak_output = "Which Camera Summary should be sent ?"
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class ThreeAmSummaryHandler(AbstractRequestHandler):
    """Handler for ThreeAmSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ThreeAmSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            payload = {
                "payload":"03:00:00"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-3am"
            )
            speak_output = "Which Camera Summary should be sent ?"
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class FourAmSummaryHandler(AbstractRequestHandler):
    """Handler for ThreeAmSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FourAmSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            payload = {
                "payload":"04:00:00"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/time",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-4am"
            )
            speak_output = "Which Camera Summary should be sent ?"
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class FiveAmSummaryHandler(AbstractRequestHandler):
    """Handler for FiveAmSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FiveAmSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            payload = {
                "payload":"05:00:00"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/time",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-5am"
            )
            speak_output = "Which Camera Summary should be sent ?"
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class SixAmSummaryHandler(AbstractRequestHandler):
    """Handler for SixAmSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SixAmSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            payload = {
                "payload":"06:00:00"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/time",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-6am"
            )
            speak_output = "Which Camera Summary should be sent ?"
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class SevenAmSummaryHandler(AbstractRequestHandler):
    """Handler for SevenAmSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SevenAmSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            payload = {
                "payload":"07:00:00"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/time",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-7am"
            )
            speak_output = "Which Camera Summary should be sent ?"
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class EightAmSummaryHandler(AbstractRequestHandler):
    """Handler for EightAmSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("EightAmSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            payload = {
                "payload":"08:00:00"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/time",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-8am"
            )
            speak_output = "Which Camera Summary should be sent ?"
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class NineAmSummaryHandler(AbstractRequestHandler):
    """Handler for NineAmSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("NineAmSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            payload = {
                "payload":"09:00:00"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/time",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-9am"
            )
            speak_output = "Which Camera Summary should be sent ?"
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class TenAmSummaryHandler(AbstractRequestHandler):
    """Handler for TenAmSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TenAmSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            payload = {
                "payload":"10:00:00"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/time",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-10am"
            )
            speak_output = "Which Camera Summary should be sent ?"
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class ElevenAmSummaryHandler(AbstractRequestHandler):
    """Handler for ElevenAmSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ElevenAmSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            payload = {
                "payload":"11:00:00"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/time",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-11am"
            )
            speak_output = "Which Camera Summary should be sent ?"
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class TwelveAmSummaryHandler(AbstractRequestHandler):
    """Handler for TwelveAmSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TwelveAmSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            payload = {
                "payload":"24:00:00"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/time",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-12am"
            )
            speak_output = "Which Camera Summary should be sent ?"
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class OnePmSummaryHandler(AbstractRequestHandler):
    """Handler for OnePmSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("OnePmSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            payload = {
                "payload":"13:00:00"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/time",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-13pm"
            )
            speak_output = "Which Camera Summary should be sent ?"
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class TwoPmSummaryHandler(AbstractRequestHandler):
    """Handler for OnePmSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TwoPmSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            payload = {
                "payload":"14:00:00"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/time",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-14pm"
            )
            speak_output = "Which Camera Summary should be sent ?"
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class ThreePmSummaryHandler(AbstractRequestHandler):
    """Handler for OnePmSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ThreePmSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            payload = {
                "payload":"15:00:00"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/time",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-15pm"
            )
            speak_output = "Which Camera Summary should be sent ?"
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class FourPmSummaryHandler(AbstractRequestHandler):
    """Handler for FourPmSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FourPmSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            payload = {
                "payload":"16:00:00"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/time",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-16pm"
            )
            speak_output = "Which Camera Summary should be sent ?"
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class FivePmSummaryHandler(AbstractRequestHandler):
    """Handler for OnePmSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FivePmSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            payload = {
                "payload":"17:00:00"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/time",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-17pm"
            )
            speak_output = "Which Camera Summary should be sent ?"
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class SixPmSummaryHandler(AbstractRequestHandler):
    """Handler for SixPmSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SixPmSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            payload = {
                "payload":"18:00:00"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/time",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-18pm"
            )
            speak_output = "Which Camera Summary should be sent ?"
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class SevenPmSummaryHandler(AbstractRequestHandler):
    """Handler for SevenPmSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SevenPmSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            payload = {
                "payload":"19:00:00"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/time",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-19pm"
            )
            speak_output = "Which Camera Summary should be sent ?"
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class EightPmSummaryHandler(AbstractRequestHandler):
    """Handler for EightPmSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("EightPmSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            payload = {
                "payload":"20:00:00"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/time",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-20pm"
            )
            speak_output = "Which Camera Summary should be sent ?"
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class NinePmSummaryHandler(AbstractRequestHandler):
    """Handler for NinePmSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("NinePmSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            payload = {
                "payload":"21:00:00"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/time",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-21pm"
            )
            speak_output = "Which Camera Summary should be sent ?"
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class TenPmSummaryHandler(AbstractRequestHandler):
    """Handler for TenPmSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TenPmSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            payload = {
                "payload":"22:00:00"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/time",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-22pm"
            )
            speak_output = "Which Camera Summary should be sent ?"
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class ElevenPmSummaryHandler(AbstractRequestHandler):
    """Handler for ElevenPmSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ElevenPmSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            payload = {
                "payload":"23:00:00"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/time",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-23pm"
            )
            speak_output = "Which Camera Summary should be sent ?"
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class TwelvePmSummaryHandler(AbstractRequestHandler):
    """Handler for TwelvePmSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TwelvePmSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            payload = {
                "payload":"12:00:00"
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/time",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-24pm"
            )
            speak_output = "Which Camera Summary should be sent ?"
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CamOneSummaryHandler(AbstractRequestHandler):
    """Handler for LivingRoomCameraSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ParkingAreaCameraSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_01"]
            
            payload = {
                "payload":single_camera,
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/cam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-c1"
            )
            speak_output = "Summary of " + single_camera + " of Requested Time sent to your device."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CamTwoSummaryHandler(AbstractRequestHandler):
    """Handler for FrontDoorCameraSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("EntranceCameraSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_02"]
            
            payload = {
                "payload":single_camera,
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/cam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-c2"
            )
            speak_output = "Summary of " + single_camera + " of Requested Time sent to your device."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CamThreeSummaryHandler(AbstractRequestHandler):
    """Handler for CThreeSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ExitCameraSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_03"]
            
            payload = {
                "payload":single_camera,
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/cam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-c3"
            )
            speak_output = "Summary of " + single_camera + " of Requested Time sent to your device."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CamFourSummaryHandler(AbstractRequestHandler):
    """Handler for ConeSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("LiftAreaCameraSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_04"]
            
            payload = {
                "payload":single_camera,
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/cam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-c4"
            )
            speak_output = "Summary of " + single_camera + " of Requested Time sent to your device."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CamFiveSummaryHandler(AbstractRequestHandler):
    """Handler for ConeSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("BillingSectionCameraSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_05"]
            
            payload = {
                "payload":single_camera,
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/cam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-c5"
            )
            speak_output = "Summary of " + single_camera + " of Requested Time sent to your device."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CamSixSummaryHandler(AbstractRequestHandler):
    """Handler for ConeSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FrontDoorEntranceCameraSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_06"]
            
            payload = {
                "payload":single_camera,
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/cam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-c6"
            )
            speak_output = "Summary of " + single_camera + " of Requested Time sent to your device."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CamSevenSummaryHandler(AbstractRequestHandler):
    """Handler for ConeSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("LivingRoomCameraSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_07"]
            
            payload = {
                "payload":single_camera,
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/cam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-c7"
            )
            speak_output = "Summary of " + single_camera + " of Requested Time sent to your device."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CamEightSummaryHandler(AbstractRequestHandler):
    """Handler for ConeSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("BackDoorCameraSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_08"]
            
            payload = {
                "payload":single_camera,
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/cam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-c8"
            )
            speak_output = "Summary of " + single_camera + " of Requested Time sent to your device."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CamNineSummaryHandler(AbstractRequestHandler):
    """Handler for ConeSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("KitchenCameraSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_09"]
            
            payload = {
                "payload":single_camera,
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/cam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-c9"
            )
            speak_output = "Summary of " + single_camera + " of Requested Time sent to your device."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CamTenSummaryHandler(AbstractRequestHandler):
    """Handler for ConeSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("BalconyCameraSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_10"]
            
            payload = {
                "payload":single_camera,
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/cam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-c10"
            )
            speak_output = "Summary of " + single_camera + " of Requested Time sent to your device."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CamElevenSummaryHandler(AbstractRequestHandler):
    """Handler for ConeSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("BasementCameraSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_11"]
            
            payload = {
                "payload":single_camera,
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/cam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-c11"
            )
            speak_output = "Summary of " + single_camera + " of Requested Time sent to your device."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CamTwelveSummaryHandler(AbstractRequestHandler):
    """Handler for ConeSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("MainGateCameraSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_12"]
            
            payload = {
                "payload":single_camera,
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/cam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-c12"
            )
            speak_output = "Summary of " + single_camera + " of Requested Time sent to your device."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CamThirteenSummaryHandler(AbstractRequestHandler):
    """Handler for ConeSummaryIntent Intent """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("StoreRoomCameraSummaryIntent")(handler_input)

    def handle(self, handler_input):
        try:
            # Read data from a file named 'config.json' within the skill code
            with open("camera_config.json", "r") as file:
                config_data = json.load(file)

            # Fetch a single camera (e.g., "camera1")
            single_camera = config_data["cameras"]["camera_13"]
            
            payload = {
                "payload":single_camera,
                
            }
            
            response = publish.single(
            topic="deepcept/alexa/events/cam",
            payload=json.dumps(payload),
            hostname="broker.hivemq.com",
            port=1883,
            client_id="summary-c13"
            )
            speak_output = "Summary of " + single_camera + " of Requested Time sent to your device."
            reprompt = "What Other Functions You need Me to Perform."
        except Exception as e:
            print(f"Error publishing message: {e}")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(AllCameraToggleOnHandler())
sb.add_request_handler(AllCameraToggleOffHandler())
sb.add_request_handler(AllRecordingToggleOnHandler())
sb.add_request_handler(AllRecordingToggleOffHandler())
sb.add_request_handler(AllSnapshotOnIntentHandler())
sb.add_request_handler(AllSnapshotOffIntentHandler())
sb.add_request_handler(CameraOneOnIntentHandler())
sb.add_request_handler(CameraOneOffIntentHandler())
sb.add_request_handler(CameraTwoOnIntentHandler())
sb.add_request_handler(CameraTwoOffIntentHandler())
sb.add_request_handler(CameraThreeOnIntentHandler())
sb.add_request_handler(CameraThreeOffIntentHandler())
sb.add_request_handler(CameraFourOnIntentHandler())
sb.add_request_handler(CameraFourOffIntentHandler())
sb.add_request_handler(CameraFiveOnIntentHandler())
sb.add_request_handler(CameraFiveOffIntentHandler())
sb.add_request_handler(CameraSixOnIntentHandler())
sb.add_request_handler(CameraSixOffIntentHandler())
sb.add_request_handler(CameraSevenOnIntentHandler())
sb.add_request_handler(CameraSevenOffIntentHandler())
sb.add_request_handler(CameraEightOnIntentHandler())
sb.add_request_handler(CameraEightOffIntentHandler())
sb.add_request_handler(CameraNineOnIntentHandler())
sb.add_request_handler(CameraNineOffIntentHandler())
sb.add_request_handler(CameraTenOnIntentHandler())
sb.add_request_handler(CameraTenOffIntentHandler())
sb.add_request_handler(CameraElevenOnIntentHandler())
sb.add_request_handler(CameraElevenOffIntentHandler())
sb.add_request_handler(CameraTwelveOnIntentHandler())
sb.add_request_handler(CameraTwelveOffIntentHandler())
sb.add_request_handler(CameraThirteenOnIntentHandler())
sb.add_request_handler(CameraThirteenOffIntentHandler())
sb.add_request_handler(OneAmSummaryHandler())
sb.add_request_handler(TwoAmSummaryHandler())
sb.add_request_handler(ThreeAmSummaryHandler())
sb.add_request_handler(FourAmSummaryHandler())
sb.add_request_handler(FiveAmSummaryHandler())
sb.add_request_handler(SixAmSummaryHandler())
sb.add_request_handler(SevenAmSummaryHandler())
sb.add_request_handler(EightAmSummaryHandler())
sb.add_request_handler(NineAmSummaryHandler())
sb.add_request_handler(TenAmSummaryHandler())
sb.add_request_handler(ElevenAmSummaryHandler())
sb.add_request_handler(TwelveAmSummaryHandler())
sb.add_request_handler(OnePmSummaryHandler())
sb.add_request_handler(TwoPmSummaryHandler())
sb.add_request_handler(ThreePmSummaryHandler())
sb.add_request_handler(FourPmSummaryHandler())
sb.add_request_handler(FivePmSummaryHandler())
sb.add_request_handler(SixPmSummaryHandler())
sb.add_request_handler(SevenPmSummaryHandler())
sb.add_request_handler(EightPmSummaryHandler())
sb.add_request_handler(NinePmSummaryHandler())
sb.add_request_handler(TenPmSummaryHandler())
sb.add_request_handler(ElevenPmSummaryHandler())
sb.add_request_handler(TwelvePmSummaryHandler())
sb.add_request_handler(CamOneSummaryHandler())
sb.add_request_handler(CamTwoSummaryHandler())
sb.add_request_handler(CamThreeSummaryHandler())
sb.add_request_handler(CamFourSummaryHandler())
sb.add_request_handler(CamFiveSummaryHandler())
sb.add_request_handler(CamSixSummaryHandler())
sb.add_request_handler(CamSevenSummaryHandler())
sb.add_request_handler(CamEightSummaryHandler())
sb.add_request_handler(CamNineSummaryHandler())
sb.add_request_handler(CamTenSummaryHandler())
sb.add_request_handler(CamElevenSummaryHandler())
sb.add_request_handler(CamTwelveSummaryHandler())
sb.add_request_handler(CamThirteenSummaryHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()