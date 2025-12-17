---
layout: default
title: Training-Free Multi-View Extension of IC-Light for Textual Position-Aware Scene Relighting
---

# Training-Free Multi-View Extension of IC-Light for Textual Position-Aware Scene Relighting

**arXiv**: [2511.13684v1](https://arxiv.org/abs/2511.13684) | [PDF](https://arxiv.org/pdf/2511.13684.pdf)

**作者**: Jiangnan Ye, Jiedong Zhuang, Lianrui Mu, Wenjie Zheng, Jiaqi Hu, Xingze Zou, Jing Wang, Haoji Hu

---

## 💡 一句话要点

**提出GS-Light，实现基于文本的3D高斯溅射场景重光照，无需训练扩展多视图输入。**

**关键词**: `3D高斯溅射` `文本引导重光照` `多视图扩散模型` `光照先验融合` `训练免费扩展`

## 📋 核心要点

1. 核心问题：文本引导的3D场景重光照需处理多视图一致性与用户意图准确反映。
2. 方法要点：融合LVLM解析光照先验与几何约束，生成初始潜码指导扩散模型。
3. 实验或效果：在室内外场景评估，多视图一致性与成像质量优于基线方法。

## 📄 摘要（原文）

> We introduce GS-Light, an efficient, textual position-aware pipeline for text-guided relighting of 3D scenes represented via Gaussian Splatting (3DGS). GS-Light implements a training-free extension of a single-input diffusion model to handle multi-view inputs. Given a user prompt that may specify lighting direction, color, intensity, or reference objects, we employ a large vision-language model (LVLM) to parse the prompt into lighting priors. Using off-the-shelf estimators for geometry and semantics (depth, surface normals, and semantic segmentation), we fuse these lighting priors with view-geometry constraints to compute illumination maps and generate initial latent codes for each view. These meticulously derived init latents guide the diffusion model to generate relighting outputs that more accurately reflect user expectations, especially in terms of lighting direction. By feeding multi-view rendered images, along with the init latents, into our multi-view relighting model, we produce high-fidelity, artistically relit images. Finally, we fine-tune the 3DGS scene with the relit appearance to obtain a fully relit 3D scene. We evaluate GS-Light on both indoor and outdoor scenes, comparing it to state-of-the-art baselines including per-view relighting, video relighting, and scene editing methods. Using quantitative metrics (multi-view consistency, imaging quality, aesthetic score, semantic similarity, etc.) and qualitative assessment (user studies), GS-Light demonstrates consistent improvements over baselines. Code and assets will be made available upon publication.

