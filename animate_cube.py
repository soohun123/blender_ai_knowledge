import bpy

# 현재 씬을 보존하면서 예제 큐브를 새로 추가합니다.
scene = bpy.context.scene
name = "AI_Animation_Demo_Cube"
if bpy.data.objects.get(name):
    raise RuntimeError(f"{name} 이름이 이미 사용 중입니다. 기존 오브젝트는 변경하지 않습니다.")
mesh = bpy.data.meshes.new(name + "_Mesh")
mesh.from_pydata([(-1,-1,-1),(-1,-1,1),(-1,1,-1),(-1,1,1),(1,-1,-1),(1,-1,1),(1,1,-1),(1,1,1)], [], [(0,4,6,2),(1,3,7,5),(0,1,5,4),(2,6,7,3),(0,2,3,1),(4,5,7,6)])
mesh.update()
obj = bpy.data.objects.new(name, mesh)
scene.collection.objects.link(obj)
obj.location = (0, 0, 0)
obj.keyframe_insert(data_path="location", frame=1)
obj.location = (5, 0, 0)
obj.keyframe_insert(data_path="location", frame=60)
print("키프레임 생성 완료:", obj.name)
