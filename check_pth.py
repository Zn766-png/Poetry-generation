import torch

# 只加载一次，用你真实存在的文件路径
pth_path = r"E:\term4.0\（已结课）\编程基础\Program\Final_project\checkpoint.pth"
data = torch.load(pth_path, map_location="cpu")

print("=" * 60)
print("✅ 文件加载成功！")
print("=" * 60)
print("文件包含字段：", list(data.keys()))
print()

print("=== 模型全部层名称 & 形状 ===")
for name, param in data["model_state_dict"].items():
    print(f"{name:<40} 形状: {tuple(param.shape)}")
print()
print("🎉 查看完成")