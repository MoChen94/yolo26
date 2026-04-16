# 检查是否支持GPU训练
import torch
print(f"PyTorch 版本: {torch.__version__}")
print(f"CUDA 是否可用: {torch.cuda.is_available()}")
print(f"当前可用显卡数: {torch.cuda.device_count()}")
print(f"正在使用的显卡型号: {torch.cuda.get_device_name(0)}")