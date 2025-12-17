---
layout: default
title: FaithFusion: Harmonizing Reconstruction and Generation via Pixel-wise Information Gain
---

# FaithFusion: Harmonizing Reconstruction and Generation via Pixel-wise Information Gain

**arXiv**: [2511.21113v1](https://arxiv.org/abs/2511.21113) | [PDF](https://arxiv.org/pdf/2511.21113.pdf)

**作者**: YuAn Wang, Xiaofan Li, Chi Huang, Wenhao Zhang, Hao Li, Bosheng Wang, Xun Sun, Jun Wang

---

## 💡 一句话要点

**提出FaithFusion框架，通过像素级信息增益融合3DGS与扩散模型，提升可控驾驶场景重建与生成效果。**

**关键词**: `3D场景重建` `扩散模型` `几何保真` `像素级融合` `可控生成` `驾驶场景`

## 📋 核心要点

1. 核心问题：几何保真与视觉逼真在视角变化下难以平衡，融合模型易导致过修复和几何漂移。
2. 方法要点：使用像素级期望信息增益作为统一策略，指导扩散模型优化高不确定区域并蒸馏回3DGS。
3. 实验或效果：在Waymo数据集上实现SOTA性能，NTA-IoU、NTL-IoU和FID指标领先，FID保持107.47。

## 📄 摘要（原文）

> In controllable driving-scene reconstruction and 3D scene generation, maintaining geometric fidelity while synthesizing visually plausible appearance under large viewpoint shifts is crucial. However, effective fusion of geometry-based 3DGS and appearance-driven diffusion models faces inherent challenges, as the absence of pixel-wise, 3D-consistent editing criteria often leads to over-restoration and geometric drift. To address these issues, we introduce \textbf{FaithFusion}, a 3DGS-diffusion fusion framework driven by pixel-wise Expected Information Gain (EIG). EIG acts as a unified policy for coherent spatio-temporal synthesis: it guides diffusion as a spatial prior to refine high-uncertainty regions, while its pixel-level weighting distills the edits back into 3DGS. The resulting plug-and-play system is free from extra prior conditions and structural modifications.Extensive experiments on the Waymo dataset demonstrate that our approach attains SOTA performance across NTA-IoU, NTL-IoU, and FID, maintaining an FID of 107.47 even at 6 meters lane shift. Our code is available at https://github.com/wangyuanbiubiubiu/FaithFusion.

