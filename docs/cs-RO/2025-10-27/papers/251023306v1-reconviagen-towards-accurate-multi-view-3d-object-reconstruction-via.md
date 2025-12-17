---
layout: default
title: ReconViaGen: Towards Accurate Multi-view 3D Object Reconstruction via Generation
---

# ReconViaGen: Towards Accurate Multi-view 3D Object Reconstruction via Generation

**arXiv**: [2510.23306v1](https://arxiv.org/abs/2510.23306) | [PDF](https://arxiv.org/pdf/2510.23306.pdf)

**作者**: Jiahao Chang, Chongjie Ye, Yushuang Wu, Yuantao Chen, Yidan Zhang, Zhongjin Luo, Chenghong Li, Yihao Zhi, Xiaoguang Han

---

## 💡 一句话要点

**提出ReconViaGen以解决多视角3D重建中因遮挡和稀疏覆盖导致的不完整问题**

**关键词**: `多视角3D重建` `扩散生成模型` `重建先验` `跨视图连接` `迭代去噪控制`

## 📋 核心要点

1. 核心问题：现有方法依赖视图重叠，但遮挡和稀疏覆盖导致重建不完整，扩散生成方法因随机性限制准确性
2. 方法要点：整合重建先验到生成框架，改进跨视图连接提取和迭代去噪可控性
3. 实验或效果：实验显示能重建完整且准确的3D模型，全局结构和局部细节与输入一致

## 📄 摘要（原文）

> Existing multi-view 3D object reconstruction methods heavily rely on
> sufficient overlap between input views, where occlusions and sparse coverage in
> practice frequently yield severe reconstruction incompleteness. Recent
> advancements in diffusion-based 3D generative techniques offer the potential to
> address these limitations by leveraging learned generative priors to
> hallucinate invisible parts of objects, thereby generating plausible 3D
> structures. However, the stochastic nature of the inference process limits the
> accuracy and reliability of generation results, preventing existing
> reconstruction frameworks from integrating such 3D generative priors. In this
> work, we comprehensively analyze the reasons why diffusion-based 3D generative
> methods fail to achieve high consistency, including (a) the insufficiency in
> constructing and leveraging cross-view connections when extracting multi-view
> image features as conditions, and (b) the poor controllability of iterative
> denoising during local detail generation, which easily leads to plausible but
> inconsistent fine geometric and texture details with inputs. Accordingly, we
> propose ReconViaGen to innovatively integrate reconstruction priors into the
> generative framework and devise several strategies that effectively address
> these issues. Extensive experiments demonstrate that our ReconViaGen can
> reconstruct complete and accurate 3D models consistent with input views in both
> global structure and local details.Project page:
> https://jiahao620.github.io/reconviagen.

