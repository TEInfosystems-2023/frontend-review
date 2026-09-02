import streamlit as st
import streamlit.components.v1 as components


def voice_to_voice():

    # =====================================================
    # PAGE TITLE
    # =====================================================

    st.markdown(
        """
<h1 class="speak-title">Speak</h1>
""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # MICROPHONE + CONVERSION UI
    # =====================================================

    components.html(
        """
<!DOCTYPE html>
<html>

<head>

<style>

* {
    box-sizing: border-box;
}

html,
body {

    margin: 0;
    padding: 0;

    background: transparent;

    font-family: Arial, sans-serif;
}


/* =====================================================
   MAIN CONTAINER
   ===================================================== */

.voice-container {

    width: 100%;

    display: flex;

    flex-direction: column;

    align-items: center;

    padding-top: 5px;

    padding-bottom: 25px;
}


/* =====================================================
   ONE INSTRUCTION
   ===================================================== */

.instruction {

    margin: 0 0 25px 0;

    font-size: 15px;

    color: #766960;

    text-align: center;
}


/* =====================================================
   MICROPHONE BUTTON
   ===================================================== */

.microphone-button {

    width: 190px;
    height: 190px;

    padding: 0;

    border-radius: 50%;

    border: 2px solid #f1d2ba;

    background:
        radial-gradient(
            circle,
            #fffdf9 0%,
            #fff7ee 58%,
            #f8dfca 100%
        );

    display: flex;

    align-items: center;

    justify-content: center;

    cursor: pointer;

    box-shadow:
        0 0 0 10px rgba(244, 207, 178, 0.18),
        0 0 0 20px rgba(244, 207, 178, 0.08),
        0 18px 40px rgba(120, 85, 65, 0.14);

    transition:
        transform 0.15s ease,
        box-shadow 0.15s ease;
}


/* =====================================================
   INNER MICROPHONE
   ===================================================== */

.microphone-icon {

    width: 110px;
    height: 110px;

    border-radius: 50%;

    display: flex;

    align-items: center;

    justify-content: center;

    background:
        linear-gradient(
            135deg,
            #f6c7a8,
            #ee9e73
        );

    font-size: 48px;

    box-shadow:
        inset 0 2px 5px rgba(255, 255, 255, 0.75),
        0 10px 25px rgba(192, 128, 84, 0.20);
}


/* =====================================================
   RECORDING STATE
   ===================================================== */

.microphone-button.recording {

    animation: pulse 1.4s infinite;

    box-shadow:
        0 0 0 10px rgba(232, 137, 102, 0.25),
        0 0 0 20px rgba(232, 137, 102, 0.12),
        0 18px 40px rgba(190, 100, 70, 0.22);
}


.microphone-button.recording .microphone-icon {

    background:
        linear-gradient(
            135deg,
            #e98f6b,
            #d96f50
        );
}


@keyframes pulse {

    0% {
        transform: scale(1);
    }

    50% {
        transform: scale(1.03);
    }

    100% {
        transform: scale(1);
    }
}


/* =====================================================
   STATUS
   ===================================================== */

.status {

    margin-top: 25px;

    min-height: 20px;

    font-size: 14px;

    color: #766960;

    text-align: center;
}


.status.recording {

    color: #c75f42;

    font-weight: 700;
}


/* =====================================================
   AUDIO PLAYER
   ===================================================== */

audio {

    width: 100%;

    max-width: 600px;

    margin-top: 20px;

    border-radius: 12px;
}


/* =====================================================
   CONVERSION AREA
   ===================================================== */

.convert-area {

    width: 100%;

    max-width: 560px;

    margin-top: 28px;

    display: none;

    flex-direction: column;

    align-items: center;
}


/* =====================================================
   CONVERT ROW
   ===================================================== */

.convert-row {

    width: 100%;

    display: flex;

    align-items: center;

    justify-content: center;

    gap: 12px;
}


/* =====================================================
   LANGUAGE SELECT
   ===================================================== */

.language-select {

    height: 50px;

    min-width: 210px;

    padding: 0 16px;

    border-radius: 14px;

    border: 1px solid #ded5ce;

    background: #fffdfa;

    color: #302923;

    font-size: 14px;

    outline: none;

    cursor: pointer;

    box-shadow:
        0 5px 18px rgba(90, 70, 55, 0.07);
}


/* =====================================================
   CONVERT BUTTON
   ===================================================== */

.convert-button {

    height: 50px;

    padding: 0 28px;

    border: none;

    border-radius: 14px;

    background:
        linear-gradient(
            100deg,
            #f3b18d 0%,
            #efa47c 50%,
            #e88f68 100%
        );

    color: #302720;

    font-size: 14px;

    font-weight: 700;

    cursor: pointer;

    box-shadow:
        0 9px 24px rgba(190, 122, 83, 0.20);

    transition:
        transform 0.15s ease,
        box-shadow 0.15s ease;
}


.convert-button:hover {

    transform: translateY(-1px);

    box-shadow:
        0 12px 28px rgba(190, 122, 83, 0.27);
}


.convert-button:active {

    transform: scale(0.98);
}


/* =====================================================
   CONVERT STATUS
   ===================================================== */

.convert-status {

    margin-top: 14px;

    font-size: 13px;

    color: #766960;

    text-align: center;
}


/* =====================================================
   MOBILE
   ===================================================== */

@media (max-width: 700px) {

    .microphone-button {

        width: 155px;
        height: 155px;
    }


    .microphone-icon {

        width: 90px;
        height: 90px;

        font-size: 40px;
    }


    .convert-row {

        flex-direction: column;

        width: 100%;
    }


    .language-select {

        width: 100%;

        min-width: 0;
    }


    .convert-button {

        width: 100%;
    }
}

</style>

</head>


<body>

<div class="voice-container">


    <!-- ONE SIMPLE INSTRUCTION -->

    <div class="instruction">
        Tap the microphone and speak
    </div>


    <!-- =================================================
         MICROPHONE
         ================================================= -->

    <button
        id="microphoneButton"
        class="microphone-button"
        type="button"
        aria-label="Start recording"
    >

        <div class="microphone-icon">
            🎙️
        </div>

    </button>


    <!-- =================================================
         RECORDING STATUS
         ================================================= -->

    <div
        id="status"
        class="status"
    >
        Tap the microphone to start
    </div>


    <!-- =================================================
         AUDIO
         ================================================= -->

    <audio
        id="audioPlayer"
        controls
        style="display: none;"
    ></audio>


    <!-- =================================================
         CONVERT
         ================================================= -->

    <div
        id="convertArea"
        class="convert-area"
    >

        <div class="convert-row">

            <select
                id="languageSelect"
                class="language-select"
            >

                <option value="Odia">
                    Convert to Odia
                </option>

                <option value="English">
                    Convert to English
                </option>

                <option value="Hindi">
                    Convert to Hindi
                </option>

                <option value="Bengali">
                    Convert to Bengali
                </option>

            </select>


            <button
                id="convertButton"
                class="convert-button"
                type="button"
            >
                Convert
            </button>

        </div>


        <div
            id="convertStatus"
            class="convert-status"
        ></div>

    </div>

</div>


<script>

/* =====================================================
   VARIABLES
   ===================================================== */

let mediaRecorder = null;

let audioChunks = [];

let stream = null;

let isRecording = false;


/* =====================================================
   ELEMENTS
   ===================================================== */

const microphoneButton =
    document.getElementById(
        "microphoneButton"
    );


const status =
    document.getElementById(
        "status"
    );


const audioPlayer =
    document.getElementById(
        "audioPlayer"
    );


const convertArea =
    document.getElementById(
        "convertArea"
    );


const convertButton =
    document.getElementById(
        "convertButton"
    );


const languageSelect =
    document.getElementById(
        "languageSelect"
    );


const convertStatus =
    document.getElementById(
        "convertStatus"
    );


/* =====================================================
   START RECORDING
   ===================================================== */

async function startRecording() {

    try {

        stream =
            await navigator.mediaDevices.getUserMedia({
                audio: true
            });


        audioChunks = [];


        mediaRecorder =
            new MediaRecorder(stream);


        mediaRecorder.ondataavailable =
            function(event) {

                if (event.data.size > 0) {

                    audioChunks.push(
                        event.data
                    );
                }
            };


        mediaRecorder.onstop =
            function() {

                const audioBlob =
                    new Blob(
                        audioChunks,
                        {
                            type: "audio/webm"
                        }
                    );


                const audioUrl =
                    URL.createObjectURL(
                        audioBlob
                    );


                audioPlayer.src =
                    audioUrl;


                audioPlayer.style.display =
                    "block";


                status.textContent =
                    "Recording finished";


                status.classList.remove(
                    "recording"
                );


                microphoneButton.classList.remove(
                    "recording"
                );


                microphoneButton.setAttribute(
                    "aria-label",
                    "Start recording"
                );


                convertArea.style.display =
                    "flex";


                if (stream) {

                    stream
                        .getTracks()
                        .forEach(
                            track =>
                                track.stop()
                        );
                }


                isRecording = false;
            };


        mediaRecorder.start();


        isRecording = true;


        convertArea.style.display =
            "none";


        convertStatus.textContent =
            "";


        microphoneButton.classList.add(
            "recording"
        );


        microphoneButton.setAttribute(
            "aria-label",
            "Stop recording"
        );


        status.textContent =
            "Recording... Speak now";


        status.classList.add(
            "recording"
        );

    }

    catch (error) {

        status.textContent =
            "Please allow microphone access";

        console.error(error);
    }
}


/* =====================================================
   STOP RECORDING
   ===================================================== */

function stopRecording() {

    if (
        mediaRecorder &&
        mediaRecorder.state !== "inactive"
    ) {

        mediaRecorder.stop();
    }
}


/* =====================================================
   MICROPHONE CLICK
   ===================================================== */

microphoneButton.addEventListener(
    "click",
    function() {

        if (!isRecording) {

            startRecording();

        }

        else {

            stopRecording();
        }
    }
);


/* =====================================================
   CONVERT CLICK
   ===================================================== */

convertButton.addEventListener(
    "click",
    function() {

        const language =
            languageSelect.value;


        convertStatus.textContent =
            "Converting your voice to " +
            language +
            "...";


        /*
         * Backend voice translation
         * will be connected here.
         */

    }
);

</script>

</body>

</html>
""",
        height=560,
        scrolling=False,
    )