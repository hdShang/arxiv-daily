---
layout: default
title: Learning Subglacial Bed Topography from Sparse Radar with Physics-Guided Residuals
---

# Learning Subglacial Bed Topography from Sparse Radar with Physics-Guided Residuals

**arXiv**: [2511.14473v1](https://arxiv.org/abs/2511.14473) | [PDF](https://arxiv.org/pdf/2511.14473.pdf)

**作者**: Bayu Adhi Tama, Jianwu Wang, Vandana Janeja, Mostafa Cham

---

## 💡 一句话要点

**提出物理引导残差学习框架，从稀疏雷达数据预测冰下床地形**

**关键词**: `冰下地形重建` `物理引导学习` `残差学习` `雷达数据处理` `深度学习模型` `泛化评估`

## 📋 核心要点

1. 冰下床地形建模中雷达观测稀疏且分布不均，影响冰盖模拟准确性。
2. 方法结合物理约束和残差学习，使用编码器-解码器网络预测床厚度残差。
3. 在格陵兰子区域测试中，优于多种基线模型，提升泛化能力和结构保真度。

## 📄 摘要（原文）

> Accurate subglacial bed topography is essential for ice sheet modeling, yet radar observations are sparse and uneven. We propose a physics-guided residual learning framework that predicts bed thickness residuals over a BedMachine prior and reconstructs bed from the observed surface. A DeepLabV3+ decoder over a standard encoder (e.g.,ResNet-50) is trained with lightweight physics and data terms: multi-scale mass conservation, flow-aligned total variation, Laplacian damping, non-negativity of thickness, a ramped prior-consistency term, and a masked Huber fit to radar picks modulated by a confidence map. To measure real-world generalization, we adopt leakage-safe blockwise hold-outs (vertical/horizontal) with safety buffers and report metrics only on held-out cores. Across two Greenland sub-regions, our approach achieves strong test-core accuracy and high structural fidelity, outperforming U-Net, Attention U-Net, FPN, and a plain CNN. The residual-over-prior design, combined with physics, yields spatially coherent, physically plausible beds suitable for operational mapping under domain shift.

