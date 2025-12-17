---
layout: default
title: Referring Change Detection in Remote Sensing Imagery
---

# Referring Change Detection in Remote Sensing Imagery

**arXiv**: [2512.11719v1](https://arxiv.org/abs/2512.11719) | [PDF](https://arxiv.org/pdf/2512.11719.pdf)

**作者**: Yilmaz Korkmaz, Jay N. Paranjape, Celso M. de Melo, Vishal M. Patel

---

## 💡 一句话要点

**提出基于自然语言提示的遥感图像指代变化检测框架，以解决传统方法无法针对特定变化类型的问题。**

**关键词**: `遥感图像变化检测` `指代变化检测` `自然语言提示` `跨模态融合` `扩散模型数据生成`

## 📋 核心要点

1. 传统遥感变化检测方法识别所有变化，不区分类型，难以满足用户特定需求。
2. 引入指代变化检测，通过自然语言提示指定变化类别，结合跨模态融合网络和扩散模型生成数据。
3. 在多个数据集上实验，框架支持可扩展和针对性的变化检测，降低数据创建门槛。

## 📄 摘要（原文）

> Change detection in remote sensing imagery is essential for applications such as urban planning, environmental monitoring, and disaster management. Traditional change detection methods typically identify all changes between two temporal images without distinguishing the types of transitions, which can lead to results that may not align with specific user needs. Although semantic change detection methods have attempted to address this by categorizing changes into predefined classes, these methods rely on rigid class definitions and fixed model architectures, making it difficult to mix datasets with different label sets or reuse models across tasks, as the output channels are tightly coupled with the number and type of semantic classes. To overcome these limitations, we introduce Referring Change Detection (RCD), which leverages natural language prompts to detect specific classes of changes in remote sensing images. By integrating language understanding with visual analysis, our approach allows users to specify the exact type of change they are interested in. However, training models for RCD is challenging due to the limited availability of annotated data and severe class imbalance in existing datasets. To address this, we propose a two-stage framework consisting of (I) \textbf{RCDNet}, a cross-modal fusion network designed for referring change detection, and (II) \textbf{RCDGen}, a diffusion-based synthetic data generation pipeline that produces realistic post-change images and change maps for a specified category using only pre-change image, without relying on semantic segmentation masks and thereby significantly lowering the barrier to scalable data creation. Experiments across multiple datasets show that our framework enables scalable and targeted change detection. Project website is here: https://yilmazkorkmaz1.github.io/RCD.

