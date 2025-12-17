---
layout: default
title: MagicWorld: Interactive Geometry-driven Video World Exploration
---

# MagicWorld: Interactive Geometry-driven Video World Exploration

**arXiv**: [2511.18886v1](https://arxiv.org/abs/2511.18886) | [PDF](https://arxiv.org/pdf/2511.18886.pdf)

**作者**: Guangyuan Li, Siming Zheng, Shuolin Xu, Jinwei Chen, Bo Li, Xiaobin Hu, Lei Zhao, Peng-Tao Jiang

---

## 💡 一句话要点

**提出MagicWorld集成3D几何先验与历史检索以提升交互视频世界模型的稳定性与连续性**

**关键词**: `交互视频世界模型` `3D几何先验` `历史检索机制` `场景稳定性` `多步交互` `点云构建`

## 📋 核心要点

1. 核心问题：现有方法忽视指令驱动运动与3D几何对应，导致视角变化时结构不稳定，且多步交互中易遗忘历史信息
2. 方法要点：引入AG3D模块构建点云提供几何约束，并采用HCR机制检索历史帧注入条件信号
3. 实验或效果：实验显示MagicWorld在交互迭代中显著改善场景稳定性和连续性

## 📄 摘要（原文）

> Recent interactive video world model methods generate scene evolution conditioned on user instructions. Although they achieve impressive results, two key limitations remain. First, they fail to fully exploit the correspondence between instruction-driven scene motion and the underlying 3D geometry, which results in structural instability under viewpoint changes. Second, they easily forget historical information during multi-step interaction, resulting in error accumulation and progressive drift in scene semantics and structure. To address these issues, we propose MagicWorld, an interactive video world model that integrates 3D geometric priors and historical retrieval. MagicWorld starts from a single scene image, employs user actions to drive dynamic scene evolution, and autoregressively synthesizes continuous scenes. We introduce the Action-Guided 3D Geometry Module (AG3D), which constructs a point cloud from the first frame of each interaction and the corresponding action, providing explicit geometric constraints for viewpoint transitions and thereby improving structural consistency. We further propose History Cache Retrieval (HCR) mechanism, which retrieves relevant historical frames during generation and injects them as conditioning signals, helping the model utilize past scene information and mitigate error accumulation. Experimental results demonstrate that MagicWorld achieves notable improvements in scene stability and continuity across interaction iterations.

