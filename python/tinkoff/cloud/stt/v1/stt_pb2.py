# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tinkoff/cloud/stt/v1/stt.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from tinkoff.cloud.longrunning.v1 import longrunning_pb2 as tinkoff_dot_cloud_dot_longrunning_dot_v1_dot_longrunning__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1etinkoff/cloud/stt/v1/stt.proto\x12\x14tinkoff.cloud.stt.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/api/annotations.proto\x1a.tinkoff/cloud/longrunning/v1/longrunning.proto\"D\n\x10RecognitionAudio\x12\x11\n\x07\x63ontent\x18\x01 \x01(\x0cH\x00\x12\r\n\x03uri\x18\x02 \x01(\tH\x00\x42\x0e\n\x0c\x61udio_source\"2\n\x13SpeechContextPhrase\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x02\"W\n\rSpeechContext\x12:\n\x07phrases\x18\x03 \x03(\x0b\x32).tinkoff.cloud.stt.v1.SpeechContextPhraseJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03\"\x88\x01\n\x08WordInfo\x12-\n\nstart_time\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\x12+\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x0c\n\x04word\x18\x03 \x01(\t\x12\x12\n\nconfidence\x18\x04 \x01(\x02\"\xb4\x01\n\x1cVoiceActivityDetectionConfig\x12\x1b\n\x13min_speech_duration\x18\x01 \x01(\x02\x12\x1b\n\x13max_speech_duration\x18\x02 \x01(\x02\x12\"\n\x1asilence_duration_threshold\x18\x03 \x01(\x02\x12\x1e\n\x16silence_prob_threshold\x18\x04 \x01(\x02\x12\x16\n\x0e\x61ggressiveness\x18\x05 \x01(\x02\"\xdb\x04\n\x11RecognitionConfig\x12\x35\n\x08\x65ncoding\x18\x01 \x01(\x0e\x32#.tinkoff.cloud.stt.v1.AudioEncoding\x12\x19\n\x11sample_rate_hertz\x18\x02 \x01(\r\x12\x15\n\rlanguage_code\x18\x03 \x01(\t\x12\x18\n\x10max_alternatives\x18\x04 \x01(\r\x12\x18\n\x10profanity_filter\x18\x05 \x01(\x08\x12<\n\x0fspeech_contexts\x18\x06 \x03(\x0b\x32#.tinkoff.cloud.stt.v1.SpeechContext\x12$\n\x1c\x65nable_automatic_punctuation\x18\x08 \x01(\x08\x12\r\n\x05model\x18\n \x01(\t\x12\x14\n\x0cnum_channels\x18\x0c \x01(\r\x12\x1c\n\x12\x64o_not_perform_vad\x18\r \x01(\x08H\x00\x12H\n\nvad_config\x18\x0e \x01(\x0b\x32\x32.tinkoff.cloud.stt.v1.VoiceActivityDetectionConfigH\x00\x12\x1e\n\x16\x65nable_denormalization\x18\x10 \x01(\x08\x12!\n\x19\x65nable_sentiment_analysis\x18\x11 \x01(\x08\x12$\n\x1c\x65nable_gender_identification\x18\x12 \x01(\x08\x42\x05\n\x03vadJ\x04\x08\x07\x10\x08J\x04\x08\t\x10\nJ\x04\x08\x0b\x10\x0cJ\x04\x08\x0f\x10\x10R\x18\x65nable_word_time_offsetsR\x08metadataR\x0cuse_enhanced\"\x82\x01\n\x10RecognizeRequest\x12\x37\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\'.tinkoff.cloud.stt.v1.RecognitionConfig\x12\x35\n\x05\x61udio\x18\x02 \x01(\x0b\x32&.tinkoff.cloud.stt.v1.RecognitionAudio\"u\n\x1cSpeechRecognitionAlternative\x12\x12\n\ntranscript\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12-\n\x05words\x18\x03 \x03(\x0b\x32\x1e.tinkoff.cloud.stt.v1.WordInfo\"^\n\x1dSpeechSentimentAnalysisResult\x12\x1b\n\x13negative_prob_audio\x18\x01 \x01(\x02\x12 \n\x18negative_prob_audio_text\x18\x02 \x01(\x02\"L\n SpeechGenderIdentificationResult\x12\x12\n\nmale_proba\x18\x01 \x01(\x02\x12\x14\n\x0c\x66\x65male_proba\x18\x02 \x01(\x02\"\x86\x03\n\x17SpeechRecognitionResult\x12H\n\x0c\x61lternatives\x18\x01 \x03(\x0b\x32\x32.tinkoff.cloud.stt.v1.SpeechRecognitionAlternative\x12\x0f\n\x07\x63hannel\x18\x02 \x01(\x05\x12-\n\nstart_time\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12+\n\x08\x65nd_time\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12V\n\x19sentiment_analysis_result\x18\x05 \x01(\x0b\x32\x33.tinkoff.cloud.stt.v1.SpeechSentimentAnalysisResult\x12\\\n\x1cgender_identification_result\x18\x06 \x01(\x0b\x32\x36.tinkoff.cloud.stt.v1.SpeechGenderIdentificationResult\"S\n\x11RecognizeResponse\x12>\n\x07results\x18\x01 \x03(\x0b\x32-.tinkoff.cloud.stt.v1.SpeechRecognitionResult\"H\n\x14InterimResultsConfig\x12\x1e\n\x16\x65nable_interim_results\x18\x01 \x01(\x08\x12\x10\n\x08interval\x18\x02 \x01(\x02\"\x9c\x01\n\x1bLongRunningRecognizeRequest\x12\x37\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\'.tinkoff.cloud.stt.v1.RecognitionConfig\x12\x35\n\x05\x61udio\x18\x02 \x01(\x0b\x32&.tinkoff.cloud.stt.v1.RecognitionAudio\x12\r\n\x05group\x18\x03 \x01(\t\"\xbb\x01\n\x1aStreamingRecognitionConfig\x12\x37\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\'.tinkoff.cloud.stt.v1.RecognitionConfig\x12\x18\n\x10single_utterance\x18\x02 \x01(\x08\x12J\n\x16interim_results_config\x18\x03 \x01(\x0b\x32*.tinkoff.cloud.stt.v1.InterimResultsConfig\"\x97\x01\n\x19StreamingRecognizeRequest\x12L\n\x10streaming_config\x18\x01 \x01(\x0b\x32\x30.tinkoff.cloud.stt.v1.StreamingRecognitionConfigH\x00\x12\x17\n\raudio_content\x18\x02 \x01(\x0cH\x00\x42\x13\n\x11streaming_request\"\x8c\x01\n\x1aStreamingRecognitionResult\x12I\n\x12recognition_result\x18\x01 \x01(\x0b\x32-.tinkoff.cloud.stt.v1.SpeechRecognitionResult\x12\x10\n\x08is_final\x18\x02 \x01(\x08\x12\x11\n\tstability\x18\x03 \x01(\x02\"k\n\x1aStreamingRecognizeResponse\x12\x41\n\x07results\x18\x02 \x03(\x0b\x32\x30.tinkoff.cloud.stt.v1.StreamingRecognitionResultJ\x04\x08\x01\x10\x02J\x04\x08\x03\x10\x04\"\x8f\x01\n\x1eStreamingUnaryRecognizeRequest\x12\x39\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\'.tinkoff.cloud.stt.v1.RecognitionConfigH\x00\x12\x17\n\raudio_content\x18\x02 \x01(\x0cH\x00\x42\x19\n\x17streaming_unary_request*\xe0\x01\n\rAudioEncoding\x12\x18\n\x14\x45NCODING_UNSPECIFIED\x10\x00\x12\x0c\n\x08LINEAR16\x10\x01\x12\t\n\x05MULAW\x10\x03\x12\x08\n\x04\x41LAW\x10\x08\x12\x0c\n\x08RAW_OPUS\x10\x0b\x12\x0e\n\nMPEG_AUDIO\x10\x0c\"\x04\x08\x02\x10\x02\"\x04\x08\x04\x10\x04\"\x04\x08\x05\x10\x05\"\x04\x08\x06\x10\x06\"\x04\x08\x07\x10\x07\"\x04\x08\t\x10\t\"\x04\x08\n\x10\n*\x04\x46LAC*\x03\x41MR*\x06\x41MR_WB*\x08OGG_OPUS*\x16SPEEX_WITH_HEADER_BYTE*\tLINEAR32F*\nOGG_VORBIS2\xd0\x04\n\x0cSpeechToText\x12z\n\tRecognize\x12&.tinkoff.cloud.stt.v1.RecognizeRequest\x1a\'.tinkoff.cloud.stt.v1.RecognizeResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\"\x11/v1/stt:recognize:\x01*\x12{\n\x12StreamingRecognize\x12/.tinkoff.cloud.stt.v1.StreamingRecognizeRequest\x1a\x30.tinkoff.cloud.stt.v1.StreamingRecognizeResponse(\x01\x30\x01\x12\x9b\x01\n\x14LongRunningRecognize\x12\x31.tinkoff.cloud.stt.v1.LongRunningRecognizeRequest\x1a\'.tinkoff.cloud.longrunning.v1.Operation\"\'\x82\xd3\xe4\x93\x02!\"\x1c/v1/stt:longrunningrecognize:\x01*\x12\xa8\x01\n\x17StreamingUnaryRecognize\x12\x34.tinkoff.cloud.stt.v1.StreamingUnaryRecognizeRequest\x1a\'.tinkoff.cloud.stt.v1.RecognizeResponse\",\x82\xd3\xe4\x93\x02&\"!/v1/stt:streaming_unary_recognize:\x01*(\x01\x42NZDgithub.com/Tinkoff/voicekit-examples/golang/pkg/tinkoff/cloud/stt/v1\xa2\x02\x05TVKSRb\x06proto3')

_AUDIOENCODING = DESCRIPTOR.enum_types_by_name['AudioEncoding']
AudioEncoding = enum_type_wrapper.EnumTypeWrapper(_AUDIOENCODING)
ENCODING_UNSPECIFIED = 0
LINEAR16 = 1
MULAW = 3
ALAW = 8
RAW_OPUS = 11
MPEG_AUDIO = 12


_RECOGNITIONAUDIO = DESCRIPTOR.message_types_by_name['RecognitionAudio']
_SPEECHCONTEXTPHRASE = DESCRIPTOR.message_types_by_name['SpeechContextPhrase']
_SPEECHCONTEXT = DESCRIPTOR.message_types_by_name['SpeechContext']
_WORDINFO = DESCRIPTOR.message_types_by_name['WordInfo']
_VOICEACTIVITYDETECTIONCONFIG = DESCRIPTOR.message_types_by_name['VoiceActivityDetectionConfig']
_RECOGNITIONCONFIG = DESCRIPTOR.message_types_by_name['RecognitionConfig']
_RECOGNIZEREQUEST = DESCRIPTOR.message_types_by_name['RecognizeRequest']
_SPEECHRECOGNITIONALTERNATIVE = DESCRIPTOR.message_types_by_name['SpeechRecognitionAlternative']
_SPEECHSENTIMENTANALYSISRESULT = DESCRIPTOR.message_types_by_name['SpeechSentimentAnalysisResult']
_SPEECHGENDERIDENTIFICATIONRESULT = DESCRIPTOR.message_types_by_name['SpeechGenderIdentificationResult']
_SPEECHRECOGNITIONRESULT = DESCRIPTOR.message_types_by_name['SpeechRecognitionResult']
_RECOGNIZERESPONSE = DESCRIPTOR.message_types_by_name['RecognizeResponse']
_INTERIMRESULTSCONFIG = DESCRIPTOR.message_types_by_name['InterimResultsConfig']
_LONGRUNNINGRECOGNIZEREQUEST = DESCRIPTOR.message_types_by_name['LongRunningRecognizeRequest']
_STREAMINGRECOGNITIONCONFIG = DESCRIPTOR.message_types_by_name['StreamingRecognitionConfig']
_STREAMINGRECOGNIZEREQUEST = DESCRIPTOR.message_types_by_name['StreamingRecognizeRequest']
_STREAMINGRECOGNITIONRESULT = DESCRIPTOR.message_types_by_name['StreamingRecognitionResult']
_STREAMINGRECOGNIZERESPONSE = DESCRIPTOR.message_types_by_name['StreamingRecognizeResponse']
_STREAMINGUNARYRECOGNIZEREQUEST = DESCRIPTOR.message_types_by_name['StreamingUnaryRecognizeRequest']
RecognitionAudio = _reflection.GeneratedProtocolMessageType('RecognitionAudio', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNITIONAUDIO,
  '__module__' : 'tinkoff.cloud.stt.v1.stt_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.stt.v1.RecognitionAudio)
  })
_sym_db.RegisterMessage(RecognitionAudio)

SpeechContextPhrase = _reflection.GeneratedProtocolMessageType('SpeechContextPhrase', (_message.Message,), {
  'DESCRIPTOR' : _SPEECHCONTEXTPHRASE,
  '__module__' : 'tinkoff.cloud.stt.v1.stt_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.stt.v1.SpeechContextPhrase)
  })
_sym_db.RegisterMessage(SpeechContextPhrase)

SpeechContext = _reflection.GeneratedProtocolMessageType('SpeechContext', (_message.Message,), {
  'DESCRIPTOR' : _SPEECHCONTEXT,
  '__module__' : 'tinkoff.cloud.stt.v1.stt_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.stt.v1.SpeechContext)
  })
_sym_db.RegisterMessage(SpeechContext)

WordInfo = _reflection.GeneratedProtocolMessageType('WordInfo', (_message.Message,), {
  'DESCRIPTOR' : _WORDINFO,
  '__module__' : 'tinkoff.cloud.stt.v1.stt_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.stt.v1.WordInfo)
  })
_sym_db.RegisterMessage(WordInfo)

VoiceActivityDetectionConfig = _reflection.GeneratedProtocolMessageType('VoiceActivityDetectionConfig', (_message.Message,), {
  'DESCRIPTOR' : _VOICEACTIVITYDETECTIONCONFIG,
  '__module__' : 'tinkoff.cloud.stt.v1.stt_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.stt.v1.VoiceActivityDetectionConfig)
  })
_sym_db.RegisterMessage(VoiceActivityDetectionConfig)

RecognitionConfig = _reflection.GeneratedProtocolMessageType('RecognitionConfig', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNITIONCONFIG,
  '__module__' : 'tinkoff.cloud.stt.v1.stt_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.stt.v1.RecognitionConfig)
  })
_sym_db.RegisterMessage(RecognitionConfig)

RecognizeRequest = _reflection.GeneratedProtocolMessageType('RecognizeRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNIZEREQUEST,
  '__module__' : 'tinkoff.cloud.stt.v1.stt_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.stt.v1.RecognizeRequest)
  })
_sym_db.RegisterMessage(RecognizeRequest)

SpeechRecognitionAlternative = _reflection.GeneratedProtocolMessageType('SpeechRecognitionAlternative', (_message.Message,), {
  'DESCRIPTOR' : _SPEECHRECOGNITIONALTERNATIVE,
  '__module__' : 'tinkoff.cloud.stt.v1.stt_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.stt.v1.SpeechRecognitionAlternative)
  })
_sym_db.RegisterMessage(SpeechRecognitionAlternative)

SpeechSentimentAnalysisResult = _reflection.GeneratedProtocolMessageType('SpeechSentimentAnalysisResult', (_message.Message,), {
  'DESCRIPTOR' : _SPEECHSENTIMENTANALYSISRESULT,
  '__module__' : 'tinkoff.cloud.stt.v1.stt_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.stt.v1.SpeechSentimentAnalysisResult)
  })
_sym_db.RegisterMessage(SpeechSentimentAnalysisResult)

SpeechGenderIdentificationResult = _reflection.GeneratedProtocolMessageType('SpeechGenderIdentificationResult', (_message.Message,), {
  'DESCRIPTOR' : _SPEECHGENDERIDENTIFICATIONRESULT,
  '__module__' : 'tinkoff.cloud.stt.v1.stt_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.stt.v1.SpeechGenderIdentificationResult)
  })
_sym_db.RegisterMessage(SpeechGenderIdentificationResult)

SpeechRecognitionResult = _reflection.GeneratedProtocolMessageType('SpeechRecognitionResult', (_message.Message,), {
  'DESCRIPTOR' : _SPEECHRECOGNITIONRESULT,
  '__module__' : 'tinkoff.cloud.stt.v1.stt_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.stt.v1.SpeechRecognitionResult)
  })
_sym_db.RegisterMessage(SpeechRecognitionResult)

RecognizeResponse = _reflection.GeneratedProtocolMessageType('RecognizeResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNIZERESPONSE,
  '__module__' : 'tinkoff.cloud.stt.v1.stt_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.stt.v1.RecognizeResponse)
  })
_sym_db.RegisterMessage(RecognizeResponse)

InterimResultsConfig = _reflection.GeneratedProtocolMessageType('InterimResultsConfig', (_message.Message,), {
  'DESCRIPTOR' : _INTERIMRESULTSCONFIG,
  '__module__' : 'tinkoff.cloud.stt.v1.stt_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.stt.v1.InterimResultsConfig)
  })
_sym_db.RegisterMessage(InterimResultsConfig)

LongRunningRecognizeRequest = _reflection.GeneratedProtocolMessageType('LongRunningRecognizeRequest', (_message.Message,), {
  'DESCRIPTOR' : _LONGRUNNINGRECOGNIZEREQUEST,
  '__module__' : 'tinkoff.cloud.stt.v1.stt_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.stt.v1.LongRunningRecognizeRequest)
  })
_sym_db.RegisterMessage(LongRunningRecognizeRequest)

StreamingRecognitionConfig = _reflection.GeneratedProtocolMessageType('StreamingRecognitionConfig', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGRECOGNITIONCONFIG,
  '__module__' : 'tinkoff.cloud.stt.v1.stt_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.stt.v1.StreamingRecognitionConfig)
  })
_sym_db.RegisterMessage(StreamingRecognitionConfig)

StreamingRecognizeRequest = _reflection.GeneratedProtocolMessageType('StreamingRecognizeRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGRECOGNIZEREQUEST,
  '__module__' : 'tinkoff.cloud.stt.v1.stt_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.stt.v1.StreamingRecognizeRequest)
  })
_sym_db.RegisterMessage(StreamingRecognizeRequest)

StreamingRecognitionResult = _reflection.GeneratedProtocolMessageType('StreamingRecognitionResult', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGRECOGNITIONRESULT,
  '__module__' : 'tinkoff.cloud.stt.v1.stt_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.stt.v1.StreamingRecognitionResult)
  })
_sym_db.RegisterMessage(StreamingRecognitionResult)

StreamingRecognizeResponse = _reflection.GeneratedProtocolMessageType('StreamingRecognizeResponse', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGRECOGNIZERESPONSE,
  '__module__' : 'tinkoff.cloud.stt.v1.stt_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.stt.v1.StreamingRecognizeResponse)
  })
_sym_db.RegisterMessage(StreamingRecognizeResponse)

StreamingUnaryRecognizeRequest = _reflection.GeneratedProtocolMessageType('StreamingUnaryRecognizeRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGUNARYRECOGNIZEREQUEST,
  '__module__' : 'tinkoff.cloud.stt.v1.stt_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.stt.v1.StreamingUnaryRecognizeRequest)
  })
_sym_db.RegisterMessage(StreamingUnaryRecognizeRequest)

_SPEECHTOTEXT = DESCRIPTOR.services_by_name['SpeechToText']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZDgithub.com/Tinkoff/voicekit-examples/golang/pkg/tinkoff/cloud/stt/v1\242\002\005TVKSR'
  _SPEECHTOTEXT.methods_by_name['Recognize']._options = None
  _SPEECHTOTEXT.methods_by_name['Recognize']._serialized_options = b'\202\323\344\223\002\026\"\021/v1/stt:recognize:\001*'
  _SPEECHTOTEXT.methods_by_name['LongRunningRecognize']._options = None
  _SPEECHTOTEXT.methods_by_name['LongRunningRecognize']._serialized_options = b'\202\323\344\223\002!\"\034/v1/stt:longrunningrecognize:\001*'
  _SPEECHTOTEXT.methods_by_name['StreamingUnaryRecognize']._options = None
  _SPEECHTOTEXT.methods_by_name['StreamingUnaryRecognize']._serialized_options = b'\202\323\344\223\002&\"!/v1/stt:streaming_unary_recognize:\001*'
  _AUDIOENCODING._serialized_start=3185
  _AUDIOENCODING._serialized_end=3409
  _RECOGNITIONAUDIO._serialized_start=166
  _RECOGNITIONAUDIO._serialized_end=234
  _SPEECHCONTEXTPHRASE._serialized_start=236
  _SPEECHCONTEXTPHRASE._serialized_end=286
  _SPEECHCONTEXT._serialized_start=288
  _SPEECHCONTEXT._serialized_end=375
  _WORDINFO._serialized_start=378
  _WORDINFO._serialized_end=514
  _VOICEACTIVITYDETECTIONCONFIG._serialized_start=517
  _VOICEACTIVITYDETECTIONCONFIG._serialized_end=697
  _RECOGNITIONCONFIG._serialized_start=700
  _RECOGNITIONCONFIG._serialized_end=1303
  _RECOGNIZEREQUEST._serialized_start=1306
  _RECOGNIZEREQUEST._serialized_end=1436
  _SPEECHRECOGNITIONALTERNATIVE._serialized_start=1438
  _SPEECHRECOGNITIONALTERNATIVE._serialized_end=1555
  _SPEECHSENTIMENTANALYSISRESULT._serialized_start=1557
  _SPEECHSENTIMENTANALYSISRESULT._serialized_end=1651
  _SPEECHGENDERIDENTIFICATIONRESULT._serialized_start=1653
  _SPEECHGENDERIDENTIFICATIONRESULT._serialized_end=1729
  _SPEECHRECOGNITIONRESULT._serialized_start=1732
  _SPEECHRECOGNITIONRESULT._serialized_end=2122
  _RECOGNIZERESPONSE._serialized_start=2124
  _RECOGNIZERESPONSE._serialized_end=2207
  _INTERIMRESULTSCONFIG._serialized_start=2209
  _INTERIMRESULTSCONFIG._serialized_end=2281
  _LONGRUNNINGRECOGNIZEREQUEST._serialized_start=2284
  _LONGRUNNINGRECOGNIZEREQUEST._serialized_end=2440
  _STREAMINGRECOGNITIONCONFIG._serialized_start=2443
  _STREAMINGRECOGNITIONCONFIG._serialized_end=2630
  _STREAMINGRECOGNIZEREQUEST._serialized_start=2633
  _STREAMINGRECOGNIZEREQUEST._serialized_end=2784
  _STREAMINGRECOGNITIONRESULT._serialized_start=2787
  _STREAMINGRECOGNITIONRESULT._serialized_end=2927
  _STREAMINGRECOGNIZERESPONSE._serialized_start=2929
  _STREAMINGRECOGNIZERESPONSE._serialized_end=3036
  _STREAMINGUNARYRECOGNIZEREQUEST._serialized_start=3039
  _STREAMINGUNARYRECOGNIZEREQUEST._serialized_end=3182
  _SPEECHTOTEXT._serialized_start=3412
  _SPEECHTOTEXT._serialized_end=4004
# @@protoc_insertion_point(module_scope)
