---
layout: default
title: Ref-SAM3D: Bridging SAM3D with Text for Reference 3D Reconstruction
---

# Ref-SAM3D: Bridging SAM3D with Text for Reference 3D Reconstruction

**arXiv**: [2511.19426v1](https://arxiv.org/abs/2511.19426) | [PDF](https://arxiv.org/pdf/2511.19426.pdf)

**作者**: Yun Zhou, Yaoting Wang, Guangquan Jie, Jinyu Liu, Henghui Ding

---

## 💡 一句话要点

**提出Ref-SAM3D以解决SAM3D无法基于文本描述重建特定3D对象的问题**

**关键词**: `3D重建` `文本引导` `零样本学习` `单视图重建` `SAM3D扩展`

## 📋 核心要点

1. 核心问题：SAM3D缺乏基于文本描述重建特定3D对象的能力，限制实际应用
2. 方法要点：扩展SAM3D，引入文本描述作为先验，实现单RGB图像的文本引导3D重建
3. 实验或效果：零样本重建性能竞争且高保真，仅需自然语言和单2D视图

## 📄 摘要（原文）

> SAM3D has garnered widespread attention for its strong 3D object reconstruction capabilities. However, a key limitation remains: SAM3D cannot reconstruct specific objects referred to by textual descriptions, a capability that is essential for practical applications such as 3D editing, game development, and virtual environments. To address this gap, we introduce Ref-SAM3D, a simple yet effective extension to SAM3D that incorporates textual descriptions as a high-level prior, enabling text-guided 3D reconstruction from a single RGB image. Through extensive qualitative experiments, we show that Ref-SAM3D, guided only by natural language and a single 2D view, delivers competitive and high-fidelity zero-shot reconstruction performance. Our results demonstrate that Ref-SAM3D effectively bridges the gap between 2D visual cues and 3D geometric understanding, offering a more flexible and accessible paradigm for reference-guided 3D reconstruction. Code is available at: https://github.com/FudanCVL/Ref-SAM3D.

