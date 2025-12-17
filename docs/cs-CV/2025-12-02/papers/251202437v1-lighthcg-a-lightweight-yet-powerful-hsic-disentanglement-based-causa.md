---
layout: default
title: LightHCG: a Lightweight yet powerful HSIC Disentanglement based Causal Glaucoma Detection Model framework
---

# LightHCG: a Lightweight yet powerful HSIC Disentanglement based Causal Glaucoma Detection Model framework

**arXiv**: [2512.02437v1](https://arxiv.org/abs/2512.02437) | [PDF](https://arxiv.org/pdf/2512.02437.pdf)

**作者**: Daeyoung Kim

---

## 💡 一句话要点

**提出LightHCG，一种基于HSIC解缠的轻量级因果青光眼检测模型框架**

**关键词**: `青光眼检测` `因果表示学习` `HSIC解缠` `轻量模型` `卷积VAE` `图自编码器`

## 📋 核心要点

1. 核心问题：现有AI青光眼检测模型存在可靠性不足、参数冗余和虚假相关等问题
2. 方法要点：采用HSIC解缠和图自编码器进行无监督因果表示学习，结合卷积VAE构建轻量模型
3. 实验或效果：相比InceptionV3等模型，分类性能更高，权重减少93~99%，支持干预分析

## 📄 摘要（原文）

> As a representative optic degenerative condition, glaucoma has been a threat to millions due to its irreversibility and severe impact on human vision fields. Mainly characterized by dimmed and blurred visions, or peripheral vision loss, glaucoma is well known to occur due to damages in the optic nerve from increased intraocular pressure (IOP) or neovascularization within the retina. Traditionally, most glaucoma related works and clinical diagnosis focused on detecting these damages in the optic nerve by using patient data from perimetry tests, optic papilla inspections and tonometer-based IOP measurements. Recently, with advancements in computer vision AI models, such as VGG16 or Vision Transformers (ViT), AI-automatized glaucoma detection and optic cup segmentation based on retinal fundus images or OCT recently exhibited significant performance in aiding conventional diagnosis with high performance. However, current AI-driven glaucoma detection approaches still have significant room for improvement in terms of reliability, excessive parameter usage, possibility of spurious correlation within detection, and limitations in applications to intervention analysis or clinical simulations. Thus, this research introduced a novel causal representation driven glaucoma detection model: LightHCG, an extremely lightweight Convolutional VAE-based latent glaucoma representation model that can consider the true causality among glaucoma-related physical factors within the optic nerve region. Using HSIC-based latent space disentanglement and Graph Autoencoder based unsupervised causal representation learning, LightHCG not only exhibits higher performance in classifying glaucoma with 93~99% less weights, but also enhances the possibility of AI-driven intervention analysis, compared to existing advanced vision models such as InceptionV3, MobileNetV2 or VGG16.

