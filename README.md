# Blender Animation AI Knowledge Base

한국어 Blender 3D 애니메이션 **AI 참고·검색(RAG)·학습 데이터** 저장소.

> Blender 4.x 중심의 예제이며 Blender 5.x에서는 API 변경 여부를 반드시 확인하세요. Blender 실행 환경에서 검증되지 않은 코드는 예제로만 취급합니다.

## 목적
- **참고 자료**: AI가 `docs/`를 검색해 작업 절차·API 사용법·오류 대응을 참조
- **코드 생성**: `examples/`의 `bpy` 예제를 바탕으로 Blender Python 스크립트 작성
- **학습 데이터**: `datasets/qa.jsonl`의 질의응답 샘플을 정제·검증한 후 학습 파이프라인에 사용
- **에이전트 운용**: `AGENTS.md`에 씬 백업, 도구 확인, 변경 범위 제한 지침 명시

## 문서 목차
| 문서 | 내용 |
|---|---|
| [기초](docs/01-foundations.md) | 오브젝트, 좌표, 모드, 프레임 |
| [키프레임과 F-Curve](docs/02-keyframes-fcurves.md) | `keyframe_insert`, 보간, 액션 |
| [리깅](docs/03-rigging.md) | Armature, 부모 설정, 가중치 |
| [캐릭터 애니메이션](docs/04-character-animation.md) | 포즈, 루프, 액션 관리 |
| [카메라와 렌더](docs/05-camera-render.md) | 카메라 키프레임, 출력 |
| [내보내기](docs/06-export.md) | FBX, glTF, Unity |
| [문제 해결](docs/07-troubleshooting.md) | 컨텍스트, 경로, MCP |
| [검증과 데이터 품질](docs/08-validation.md) | 학습용 데이터 검수 |

## 실행
Blender의 Scripting 워크스페이스에서 `examples/animate_cube.py`를 열고 Run Script를 실행하세요. **현재 씬을 지우지 않고** 새 큐브를 추가합니다.

## 데이터 포맷
`datasets/qa.jsonl`: 한 줄당 하나의 JSON 객체. 필드: `id`, `topic`, `question`, `answer`, `source`, `verified`.
`verified=false`는 Blender 실행 테스트를 아직 수행하지 않았다는 뜻입니다.

## AI 사용 예시
> `docs/02-keyframes-fcurves.md`와 `examples/animate_cube.py`를 참고하여 현재 씬을 삭제하지 않고 선택한 오브젝트에 1~60프레임 이동 애니메이션을 추가하는 bpy 스크립트를 작성해. Blender 버전과 컨텍스트 전제를 명시해.

## 한계
이 저장소는 사전학습된 LLM 자체가 아니며, GitHub 업로드만으로 모델이 학습하지 않습니다. RAG 인덱싱 또는 별도의 지도 미세조정이 필요합니다. 예제는 정적 문법 검사만 수행했고 Blender 내 동작 검증은 별도로 필요합니다.

## 라이선스
콘텐츠와 코드: MIT (`LICENSE`). Blender 및 기타 외부 자료의 상표·라이선스는 별개입니다.
