import streamlit as st
import streamlit.components.v1 as components

# 1. App Layout and Title Configurations
st.set_page_config(page_title="BruxBot App", page_icon="🦷", layout="centered")
st.title("🦷 BruxBot Diagnostic Core")
st.caption("Real-Time Autonomous Acoustic Biofeedback System")

# 2. User Mode Selection Panel
st.subheader("🛡️ Clinical System Controls")
mode = st.radio("Select Sensory Biofeedback Mechanism:", ["Sound-Only Mode (Acoustic)", "Smartwatch Mode (Kinematic)"])

# 3. Your Teachable Machine link is already embedded right here!
teachable_machine_link = "https://withgoogle.com"

# 4. Processing Sandboxed Audio input
html_code = f"""
<div style="background-color: #f0f2f6; padding: 15px; border-radius: 10px; font-family: sans-serif;">
    <h4 style="margin-top: 0; color: #1f2937;">🎙️ Live Detection Sandbox</h4>
    <button id="start-btn" onclick="init()" style="background-color: #ff4b4b; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-weight: bold;">
        🌙 Start Overnight Monitoring
    </button>
    <div id="status" style="margin-top: 10px; font-weight: bold; color: #4b5563;">System Status: Offline</div>
    <div id="label-container" style="margin-top: 15px; display: flex; flex-direction: column; gap: 8px;"></div>
</div>

<script src="https://jsdelivr.net"></script>
<script src="https://jsdelivr.net"></script>

<script type="text/javascript">
    const URL = "{teachable_machine_link}";
    let recognizer;
    let audioContext;

    function playBiofeedbackHum() {{
        if (!audioContext) audioContext = new (window.AudioContext || window.webkitAudioContext)();
        let oscillator = audioContext.createOscillator();
        let gainNode = audioContext.createGain();
        
        oscillator.type = 'sine';
        oscillator.frequency.setValueAtTime(150, audioContext.currentTime); 
        gainNode.gain.setValueAtTime(0.15, audioContext.currentTime);        
        
        oscillator.connect(gainNode);
        gainNode.connect(audioContext.destination);
        oscillator.start();
        oscillator.stop(audioContext.currentTime + 1.2); 
    }}

    async function createModel() {{
        const checkpointURL = URL + "model.json";
        const metadataURL = URL + "metadata.json";
        const recognizer = speechCommands.create("BROWSER_FFT", undefined, checkpointURL, metadataURL);
        await recognizer.ensureModelLoaded();
        return recognizer;
    }}

    async function init() {{
        document.getElementById("status").innerText = "Scanning Audio Frequencies... (Active)";
        document.getElementById("status").style.color = "#10b981";
        
        recognizer = await createModel();
        const classLabels = recognizer.wordLabels();
        const labelContainer = document.getElementById("label-container");
        labelContainer.innerHTML = "";
        
        for (let i = 0; i < classLabels.length; i++) {{
            labelContainer.appendChild(document.createElement("div"));
        }}

        recognizer.listen(result => {{
            for (let i = 0; i < classLabels.length; i++) {{
                const scorePercentage = (result.scores[i] * 100).toFixed(0);
                const labelName = classLabels[i];
                
                labelContainer.childNodes[i].innerHTML = `
                    <div style="display: flex; justify-content: space-between; font-size: 14px;">
                        <span>${{labelName}}</span>
                        <strong>${{scorePercentage}}%</strong>
                    </div>
                    <div style="background-color: #ddd; border-radius: 4px; height: 8px; width: 100%;">
                        <div style="background-color: ${{labelName.toLowerCase().includes("grind") ? '#ff4b4b' : '#3b82f6'}}; height: 100%; width: ${{scorePercentage}}%;"></div>
                    </div>
                `;

                if (labelName.toLowerCase().includes("grind") && result.scores[i] > 0.85) {{
                    playBiofeedbackHum();
                }}
            }
        }}, {{
            includeSpectrogram: true,
            probabilityThreshold: 0.75,
            invokeCallbackOnNoiseAndUnknown: true,
            overlapFactor: 0.25
        }});
    }}
</script>
"""

components.html(html_code, height=340)

# 5. Core Safety Protocols Formatted for CWSF Evaluation
st.divider()
st.subheader("🔒 Verification, Safety & Privacy Protocols")
st.markdown("""
* **Local Sandboxed Processing:** All microphone tracking signals stay enclosed inside the browser layout engine. Zero audio data passes out to the web.
* **Hardware Hazard Mitigation:** System runs via nightstand placement coupled with a remote microphone line, keeping computing devices isolated from combustible sheets.
* **Arousal Threshold Safeguards:** Sensory outputs are heavily constrained to prevent waking the user or disturbing normal sleep architectures.
""")
