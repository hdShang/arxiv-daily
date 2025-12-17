---
layout: default
title: MatPedia: A Universal Generative Foundation for High-Fidelity Material Synthesis
---

# MatPedia: A Universal Generative Foundation for High-Fidelity Material Synthesis

**arXiv**: [2511.16957v1](https://arxiv.org/abs/2511.16957) | [PDF](https://arxiv.org/pdf/2511.16957.pdf)

**作者**: Di Luo, Shuhui Yang, Mingxin Yang, Jiawei Lu, Yixuan Tang, Xintong Han, Zhuo Chen, Beibei Wang, Chunchao Guo

---

## 💡 一句话要点

**提出MatPedia统一生成基础模型，以解决高保真材料合成中的表示分裂问题。**

**关键词**: `材料合成` `联合表示` `视频扩散` `PBR材料` `生成模型` `高保真渲染`

## 📋 核心要点

1. 核心问题：现有材料生成方法缺乏统一表示，无法桥接自然图像外观与PBR属性。
2. 方法要点：采用联合RGB-PBR表示，将材料编码为RGB和PBR潜在序列，使用视频扩散架构。
3. 实验或效果：在MatHybrid-410K数据集上训练，实现1024×1024合成，质量和多样性超越现有方法。

## 📄 摘要（原文）

> Physically-based rendering (PBR) materials are fundamental to photorealistic graphics, yet their creation remains labor-intensive and requires specialized expertise. While generative models have advanced material synthesis, existing methods lack a unified representation bridging natural image appearance and PBR properties, leading to fragmented task-specific pipelines and inability to leverage large-scale RGB image data. We present MatPedia, a foundation model built upon a novel joint RGB-PBR representation that compactly encodes materials into two interdependent latents: one for RGB appearance and one for the four PBR maps encoding complementary physical properties. By formulating them as a 5-frame sequence and employing video diffusion architectures, MatPedia naturally captures their correlations while transferring visual priors from RGB generation models. This joint representation enables a unified framework handling multiple material tasks--text-to-material generation, image-to-material generation, and intrinsic decomposition--within a single architecture. Trained on MatHybrid-410K, a mixed corpus combining PBR datasets with large-scale RGB images, MatPedia achieves native $1024\times1024$ synthesis that substantially surpasses existing approaches in both quality and diversity.

