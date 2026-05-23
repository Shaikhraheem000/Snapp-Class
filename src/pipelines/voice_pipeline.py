from resemblyzer import VoiceEncoder, preprocess_wav
import numpy as np
import io
import librosa
import streamlit as st


@st.cache_resource
def load_voice_encoder():
    return VoiceEncoder()


def get_voice_embeddings(audio_bytes):
    try:
        encoder = load_voice_encoder()

        audio, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)

        wav = preprocess_wav(audio)

        embedding = encoder.embed_utterance(wav)

        return embedding.tolist()

    except Exception as e:
        st.error("Voice recog error")
        return None


def identify_speaker(new_embedding, candidates_dict, threshold=0.65):
    if new_embedding is None or not candidates_dict:
        return None, 0

    best_std_id = None
    best_score = -1.0

    for std_id, stored_emd in candidates_dict.items():
        if stored_emd:
            similarity = np.dot(
                np.array(new_embedding),
                np.array(stored_emd)
            )

            if similarity > best_score:
                best_score = similarity
                best_std_id = std_id

    if best_score >= threshold:
        return best_std_id, best_score

    return None, best_score


def process_bulk_audio(audio_bytes, candidates_dict, threshold=0.65):
    try:
        encoder = load_voice_encoder()

        audio, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)

        segments = librosa.effects.split(audio, top_db=30)

        identify_results = {}

        for start, end in segments:

            if (end - start) < sr * 0.5:
                continue

            segment_audio = audio[start:end]

            wav = preprocess_wav(segment_audio)

            embedding = encoder.embed_utterance(wav)

            std_id, score = identify_speaker(
                embedding,
                candidates_dict,
                threshold
            )

            if std_id:
                if (
                    std_id not in identify_results
                    or score > identify_results[std_id]
                ):
                    identify_results[std_id] = score

        return identify_results

    except Exception as e:
        st.error("Bulk process error")
        return {}

