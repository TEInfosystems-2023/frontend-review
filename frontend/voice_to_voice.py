import streamlit as st
import streamlit.components.v1 as components


def voice_to_voice():

    st.markdown(
        '<h1 class="speak-title">Speak</h1>',
        unsafe_allow_html=True,
    )

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
    overflow: hidden;
}


/* =====================================================
   MAIN CONTAINER
   ===================================================== */

.voice-container {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;

    margin: 0;
    padding: 0;
}


/* =====================================================
   INSTRUCTION
   ===================================================== */

.instruction {
    margin: 0 0 20px 0;

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
   MICROPHONE HELPER CALLOUT
   ===================================================== */

.microphone-wrap {
    position: relative;
    width: 440px;
    max-width: calc(100% - 30px);
    display: flex;
    justify-content: center;
    align-items: center;
}

.microphone-callout {
    position: absolute;
    right: calc(50% + 125px);
    top: 50%;
    transform: translateY(-50%);
    width: 125px;
    padding: 9px 12px;
    border-radius: 14px;
    background: #fff0e6;
    color: #a9472b;
    font-size: 14px;
    font-weight: 700;
    line-height: 1.25;
    text-align: center;
    box-shadow: 0 6px 18px rgba(190, 122, 83, 0.10);
    pointer-events: none;
}

.microphone-callout svg {
    position: absolute;
    width: 58px;
    height: 42px;
    right: -48px;
    top: 50%;
    transform: translateY(-15%);
    overflow: visible;
}

.microphone-callout path {
    fill: none;
    stroke: #d96f50;
    stroke-width: 3;
    stroke-linecap: round;
    stroke-linejoin: round;
}

.microphone-callout.hidden {
    display: none;
}

.status.ready {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 0;
    margin-top: 18px;
    padding: 8px 18px;
    border-radius: 999px;
    background: #e6f7e9;
    color: #2d7a3f;
    font-size: 14px;
    font-weight: 700;
}

.status.ready::before {
    content: "✓";
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 20px;
    height: 20px;
    margin-right: 7px;
    border-radius: 50%;
    background: #3ba655;
    color: #ffffff;
    font-size: 12px;
    font-weight: 800;
}

.language-label {
    width: 100%;
    margin-bottom: 7px;
    color: #302923;
    font-size: 14px;
    font-weight: 700;
    text-align: left;
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

    0%,
    100% {
        transform: scale(1);
    }

    50% {
        transform: scale(1.03);
    }

}


/* =====================================================
   STATUS
   ===================================================== */

.status {
    margin-top: 18px;

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

#audioPlayer {
    width: 440px;
    max-width: calc(100% - 30px);

    height: 48px;

    margin-top: 16px;

    border-radius: 12px;
}


/* =====================================================
   CONVERT AREA
   ===================================================== */

.convert-area {
    width: 440px;
    max-width: calc(100% - 30px);

    margin-top: 10px;

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
    width: 235px;
    height: 48px;

    padding: 0 14px;

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
    width: 190px;
    height: 48px;

    padding: 0;

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
    margin-top: 8px;

    font-size: 13px;

    color: #766960;

    text-align: center;
}


/* =====================================================
   UPLOAD AREA
   ===================================================== */

.upload-area {
    width: 440px;
    max-width: calc(100% - 30px);

    margin-top: 14px;

    display: flex;

    flex-direction: column;

    align-items: center;
}


/* =====================================================
   OR DIVIDER
   ===================================================== */

.or-divider {
    width: 100%;

    height: 18px;

    display: flex;

    align-items: center;

    gap: 12px;

    color: #9a918a;

    font-size: 13px;
}


.or-divider::before,
.or-divider::after {
    content: "";

    height: 1px;

    background: #ddd4ce;

    flex: 1;
}


/* =====================================================
   UPLOAD BUTTON
   ===================================================== */

.upload-label {
    width: 380px;
    height: 72px;

    margin-top: 10px;

    padding: 0 20px;

    border-radius: 15px;

    background: #e8f2ff;

    display: flex;

    align-items: center;

    justify-content: center;

    gap: 18px;

    cursor: pointer;

    transition:
        transform 0.15s ease,
        background 0.15s ease;

    box-shadow:
        0 6px 20px rgba(100, 130, 160, 0.07);
}


.upload-label:hover {
    transform: translateY(-1px);

    background: #e1eeff;
}


/* =====================================================
   UPLOAD CLOUD ICON
   ===================================================== */

.upload-icon {
    width: 48px;
    height: 48px;

    flex-shrink: 0;

    display: flex;

    align-items: center;
    justify-content: center;
}


.upload-icon svg {
    width: 48px;
    height: 48px;

    display: block;
}


/* =====================================================
   UPLOAD TEXT
   ===================================================== */

.upload-text {
    text-align: left;
}


.upload-title {
    font-size: 16px;

    line-height: 19px;

    font-weight: 700;

    color: #20242a;

    margin: 0 0 3px 0;
}


.upload-subtitle {
    font-size: 12px;

    line-height: 15px;

    color: #68717c;

    white-space: nowrap;
}


/* =====================================================
   HIDDEN FILE INPUT
   ===================================================== */

#fileInput {
    display: none;
}


/* =====================================================
   UPLOAD STATUS
   ===================================================== */

.upload-status {
    margin-top: 6px;

    min-height: 18px;
    padding-bottom: 2px;

    font-size: 12px;

    color: #766960;

    text-align: center;
}


/* =====================================================
   MOBILE
   ===================================================== */

@media (max-width: 700px) {

    .microphone-wrap {
        width: 100%;
        padding-top: 52px;
    }

    .microphone-callout {
        right: auto;
        left: 50%;
        top: 0;
        transform: translateX(-50%);
        width: 150px;
        padding: 7px 10px;
    }

    .microphone-callout svg {
        display: none;
    }

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
    }


    .language-select,
    .convert-button {
        width: 100%;
    }


    .upload-label {
        width: 100%;
    }


    .upload-subtitle {
        white-space: normal;
    }

}

</style>

</head>


<body>

<div class="voice-container">


    <!-- =================================================
         MAIN SPEAK SECTION
         ================================================= -->

    <div class="instruction">
        Tap the microphone and speak
    </div>


    <div class="microphone-wrap">

        <div
            id="microphoneCallout"
            class="microphone-callout"
        >
            Tap here<br>
            and speak

            <svg viewBox="0 0 70 50" aria-hidden="true">
                <path d="M3 10 C20 10, 29 15, 43 27 C50 33, 56 34, 65 34" />
                <path d="M54 25 L65 34 L53 39" />
            </svg>
        </div>

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

    </div>


    <div
        id="status"
        class="status"
    >
        Tap to start speaking
    </div>


    <!-- =================================================
         AUDIO PLAYER
         ================================================= -->

    <audio
        id="audioPlayer"
        controls
        style="display:none;"
    ></audio>


    <!-- =================================================
         CONVERT SECTION
         ================================================= -->

    <div
        id="convertArea"
        class="convert-area"
    >

        <div class="language-label">
            Choose language
        </div>

        <div class="convert-row">

            <select
                id="languageSelect"
                class="language-select"
            >

                <option value="Odia">
                    Odia
                </option>

                <option value="English">
                    English
                </option>

                <option value="Hindi">
                    Hindi
                </option>

                <option value="Bengali">
                    Bengali
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


    <!-- =================================================
         UPLOAD AUDIO
         ================================================= -->

    <div class="upload-area">


        <div class="or-divider">
            <span>OR</span>
        </div>


        <label
            class="upload-label"
            for="fileInput"
        >


            <div class="upload-icon">

                <svg
                    viewBox="0 0 64 64"
                    aria-hidden="true"
                >

                    <!-- Cloud -->
                    <path
                        d="M20 49h27c7 0 12-5 12-12s-5-12-12-12h-1C44 17 37 12 30 12c-8 0-14 5-16 12C7 25 3 30 3 37c0 7 6 12 13 12h4z"
                        fill="#4f9df8"
                    />


                    <!-- Upload arrow -->
                    <path
                        d="M32 45V25M25 32l7-7 7 7"
                        fill="none"
                        stroke="#ffffff"
                        stroke-width="4"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                    />

                </svg>

            </div>


            <div class="upload-text">

                <div class="upload-title">
                    Upload Audio
                </div>


                <div class="upload-subtitle">
                    Choose an audio file from your device
                </div>

            </div>


        </label>


        <input
            id="fileInput"
            type="file"
            accept="audio/*,.wav,.mp3,.m4a,.webm,.ogg"
        />


        <div
            id="uploadStatus"
            class="upload-status"
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

const microphoneCallout =
    document.getElementById(
        "microphoneCallout"
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


const fileInput =
    document.getElementById(
        "fileInput"
    );


const uploadStatus =
    document.getElementById(
        "uploadStatus"
    );


/* =====================================================
   SHOW AUDIO
   ===================================================== */

function showAudio(
    fileOrBlob,
    message
) {

    const audioUrl =
        URL.createObjectURL(
            fileOrBlob
        );


    audioPlayer.src =
        audioUrl;


    audioPlayer.style.display =
        "block";


    status.textContent =
        "Your voice is ready";


    status.classList.remove(
        "recording"
    );

    status.classList.add(
        "ready"
    );

    microphoneCallout.classList.add(
        "hidden"
    );


    convertArea.style.display =
        "flex";
}


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
            new MediaRecorder(
                stream
            );


        mediaRecorder.ondataavailable =
            function(event) {

                if (
                    event.data.size > 0
                ) {

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


                showAudio(
                    audioBlob,
                    "Recording finished"
                );


                microphoneButton.classList.remove(
                    "recording"
                );


                microphoneButton.setAttribute(
                    "aria-label",
                    "Start recording"
                );


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


        uploadStatus.textContent =
            "";


        status.classList.remove(
            "ready"
        );

        microphoneCallout.classList.add(
            "hidden"
        );

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

        status.classList.remove(
            "ready"
        );

        microphoneCallout.classList.remove(
            "hidden"
        );

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
   UPLOAD AUDIO
   ===================================================== */

fileInput.addEventListener(
    "change",
    function() {

        const file =
            this.files[0];


        if (!file) {
            return;
        }


        if (
            !file.type.startsWith(
                "audio/"
            )
        ) {

            uploadStatus.textContent =
                "Please choose an audio file";

            this.value = "";

            return;
        }


        showAudio(
            file,
            "Your voice is ready"
        );


        uploadStatus.textContent =
            file.name;


        convertStatus.textContent =
            "";

    }
);


/* =====================================================
   CONVERT
   ===================================================== */

convertButton.addEventListener(
    "click",
    function() {

        const language =
            languageSelect.value;


        convertStatus.textContent =
            "Please wait...";


        /*
         * Your backend conversion
         * connection can remain here.
         */

    }
);

</script>

</body>
</html>
""",
        height=650,
        scrolling=False,
    )