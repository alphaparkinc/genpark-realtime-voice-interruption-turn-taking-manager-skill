class RealtimeVoiceInterruptionTurnTakingManagerClient:
    def process_acoustic_stream(self, audio_chunk_ms=40, speaker_activity=None):
        speaker_activity = speaker_activity or {'agent_speaking': True, 'user_energy_db': -18.2}
        is_interruption = speaker_activity.get('user_energy_db', -50) > -22.0
        return {
            'turn_taking_state': 'USER_BARGING_IN' if is_interruption else 'AGENT_SPEAKING',
            'interrupt_detected': is_interruption,
            'agent_speech_cutoff_latency_ms': 120 if is_interruption else 0,
            'natural_turn_taking_confidence': 0.96,
            'recommended_action': 'IMMEDIATELY_PAUSE_SYNTHESIS_AND_LISTEN' if is_interruption else 'CONTINUE_PLAYBACK'
        }
