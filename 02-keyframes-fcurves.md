# 02. 키프레임과 F-Curve

**목표**: 값의 시간 변화를 정의한다.

`obj.keyframe_insert(data_path="location", frame=1)`은 오브젝트의 Location 속성을 해당 프레임에 기록한다. 회전은 `rotation_euler`, 크기는 `scale`을 사용한다.

```python
obj.location = (0, 0, 0)
obj.keyframe_insert(data_path="location", frame=1)
obj.location = (5, 0, 0)
obj.keyframe_insert(data_path="location", frame=60)
```

Graph Editor에서 키프레임을 선택하고 `T`로 보간 방식을 설정한다. `BEZIER`는 완만한 가감속, `LINEAR`는 선형 보간, `CONSTANT`는 값 유지 후 급변을 뜻한다.

**액션 주의**: Blender 4.4 이후에는 슬럿 기반 액션 구조 등 애니메이션 데이터 API가 달라질 수 있다. `animation_data.action.fcurves`에 무조건 접근하는 예제는 모든 버전에서 통하지 않을 수 있다. 버전별 API를 확인한다.

**검증**: 프레임 1과 60에서 `obj.location`을 검사하고 중간 프레임의 보간 결과를 확인한다.
