---
layout: default
title: Revisiting Generative Infrared and Visible Image Fusion Based on Human Cognitive Laws
---

# Revisiting Generative Infrared and Visible Image Fusion Based on Human Cognitive Laws

**arXiv**: [2510.26268v1](https://arxiv.org/abs/2510.26268) | [PDF](https://arxiv.org/pdf/2510.26268.pdf)

**作者**: Lin Guo, Xiaoqing Luo, Wei Xie, Zhancheng Zhang, Hui Li, Rui Wang, Zhenhua Feng, Xiaoning Song

---

## 💡 一句话要点

**提出HCLFuse方法以解决红外与可见光图像融合中的模态平衡与生成能力问题**

**关键词**: `图像融合` `生成模型` `变分编码器` `扩散模型` `认知启发` `多模态信息`

## 📋 核心要点

1. 现有方法难以平衡模态信息，生成能力有限且缺乏可解释性
2. 设计多尺度掩码调控变分瓶颈编码器，结合扩散模型与物理规律增强生成
3. 实验显示在多个数据集上实现最优融合性能，显著提升语义分割指标

## 📄 摘要（原文）

> Existing infrared and visible image fusion methods often face the dilemma of
> balancing modal information. Generative fusion methods reconstruct fused images
> by learning from data distributions, but their generative capabilities remain
> limited. Moreover, the lack of interpretability in modal information selection
> further affects the reliability and consistency of fusion results in complex
> scenarios. This manuscript revisits the essence of generative image fusion
> under the inspiration of human cognitive laws and proposes a novel infrared and
> visible image fusion method, termed HCLFuse. First, HCLFuse investigates the
> quantification theory of information mapping in unsupervised fusion networks,
> which leads to the design of a multi-scale mask-regulated variational
> bottleneck encoder. This encoder applies posterior probability modeling and
> information decomposition to extract accurate and concise low-level modal
> information, thereby supporting the generation of high-fidelity structural
> details. Furthermore, the probabilistic generative capability of the diffusion
> model is integrated with physical laws, forming a time-varying physical
> guidance mechanism that adaptively regulates the generation process at
> different stages, thereby enhancing the ability of the model to perceive the
> intrinsic structure of data and reducing dependence on data quality.
> Experimental results show that the proposed method achieves state-of-the-art
> fusion performance in qualitative and quantitative evaluations across multiple
> datasets and significantly improves semantic segmentation metrics. This fully
> demonstrates the advantages of this generative image fusion method, drawing
> inspiration from human cognition, in enhancing structural consistency and
> detail quality.

