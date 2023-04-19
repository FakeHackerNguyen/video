from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
import av

# RTC_CONFIGURATION = RTCConfiguration(
#     {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
# )

RTC_CONFIGURATION = RTCConfiguration(
    {
      "RTCIceServer": [{
        "urls": ["turn:a.relay.metered.ca:80?transport=tcp"],
        "username": "1c8984b57b00688cab1ff9ce",
        "credential": "NVNrmuBuC6u5mVM",
      }]
    }
)

class VideoProcessor:
    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        img = frame.to_ndarray(format="bgr24")
        return av.VideoFrame.from_ndarray(img, format="bgr24")

webrtc_ctx = webrtc_streamer(
    key="WYH",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
    video_processor_factory=VideoProcessor,
    async_processing=True,
)
