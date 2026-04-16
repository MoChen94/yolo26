# YOLO26 - 目标检测模型训练框架

![GitHub release (latest by date)](https://img.shields.io/github/v/release/MoChen94/yolo26)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![CUDA](https://img.shields.io/badge/CUDA-supported-green)

YOLO26 是一个基于 YOLO（You Only Look Once）算法的目标检测模型训练框架，提供快速、准确的目标检测解决方案。**v2.0.0 版本现已发布，支持 GPU 训练！**

## 🚀 功能特点

- **高效的目标检测**：基于 YOLO 算法，实现实时目标检测
- **模型训练支持**：完整的训练流程，支持自定义数据集
- **预训练模型**：内置 YOLO 预训练模型，开箱即用
- **易于扩展**：模块化设计，便于添加新的检测任务和模型

## 📋 环境要求

- **Python**: 3.10.20 或更高版本
- **依赖库**: Ultralytics YOLO 框架
- **硬件**: 推荐使用 GPU 进行模型训练

## 🛠️ 安装步骤

1. **克隆仓库**
   ```bash
   git clone https://github.com/MoChen94/yolo26.git
   cd yolo26
   ```

2. **安装依赖**
   ```bash
   pip install -U ultralytics
   ```

3. **验证安装**
   ```bash
   python -c "from ultralytics import YOLO; print('YOLO 安装成功！')"
   ```

## 🎯 训练模式选择

### CPU 训练（默认）
默认使用 CPU 进行训练，适合：
- 无 GPU 的环境
- 小数据集快速验证
- 资源受限的开发环境

### GPU 训练（推荐）
如需使用 GPU 训练，请按以下步骤配置：

#### 1. 验证 GPU 环境
```bash
nvidia-smi
```
确认 CUDA 版本（如 12.1），确保驱动版本符合 PyTorch 要求。

#### 2. 安装 GPU 版本 PyTorch
```bash
pip uninstall torch torchvision torchaudio -y
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```
**注意**：`cu121` 对应 CUDA 12.1，请根据实际 CUDA 版本调整。

#### 3. 验证 GPU 可用性
```bash
python test_cuda.py
```
如果返回 `True`，则表示 GPU 训练环境配置成功。

### 📊 性能对比
| 训练模式 | 推荐场景 | 训练速度 | 内存要求 |
|---------|---------|---------|---------|
| CPU | 快速验证、小数据集 | 约 10-20 张/分钟 | 8GB+ |
| GPU | 大规模训练、生产环境 | 约 100-200 张/分钟 | 根据显卡配置 |

### ⚡ 切换建议
- **开发阶段**：使用 CPU 训练快速验证模型
- **生产环境**：推荐使用 GPU 训练提升效率

## 💻 使用示例

```python
from ultralytics import YOLO

# 加载预训练模型
model = YOLO('yolo26n.pt')

# 进行目标检测
results = model('input_image.jpg')

# 显示结果
results.show()
```

## 📁 项目结构

```
yolo26/
├── main.py                 # 主程序入口
├── train_main.py           # 训练主程序
├── test_cuda.py           # GPU 验证工具 (v2.0.0新增)
├── yolo_detect.py         # USB 摄像头实时检测 (v2.0.2新增)
├── yolo26n.pt             # YOLO 预训练模型
├── runs/                  # 训练结果输出
├── ultralytics/           # YOLO 库
└── ultralytics-main/      # YOLO 主代码库
```

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request 来改进这个项目！

## 📄 许可证

本项目基于 MIT 许可证开源。

## 📞 联系方式

如有问题或建议，欢迎通过 GitHub Issues 与我们联系。

---

**YOLO26** - 让目标检测变得更简单、更高效！

### 🚀 v2.1.0 版本亮点
- ✅ **train_data 目录优化**：本地目录颜色显示正常化
- ✅ **Git 配置完善**：确保训练数据不会意外提交
- ✅ **仓库结构精简**：只保留核心代码文件
- ✅ **版本管理优化**：更好的文件忽略策略