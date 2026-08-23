from client import RealtimeVoiceInterruptionTurnTakingManagerClient

def main():
    client = RealtimeVoiceInterruptionTurnTakingManagerClient()
    res1 = client.process_acoustic_stream(40, {'agent_speaking': True, 'user_energy_db': -45.0})
    print('State 1: ' + res1['turn_taking_state'] + ' | Interrupt: ' + str(res1['interrupt_detected']))
    res2 = client.process_acoustic_stream(40, {'agent_speaking': True, 'user_energy_db': -14.5})
    print('State 2: ' + res2['turn_taking_state'] + ' | Interrupt: ' + str(res2['interrupt_detected']) + ' (Cutoff: ' + str(res2['agent_speech_cutoff_latency_ms']) + 'ms)')
    print('Action: ' + res2['recommended_action'])

if __name__ == '__main__':
    main()
