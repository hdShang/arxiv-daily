---
layout: default
title: OmniGen: Unified Multimodal Sensor Generation for Autonomous Driving
---

# OmniGen: Unified Multimodal Sensor Generation for Autonomous Driving

**arXiv**: [2512.14225v1](https://arxiv.org/abs/2512.14225) | [PDF](https://arxiv.org/pdf/2512.14225.pdf)

**作者**: Tao Tang, Enhui Ma, xia zhou, Letian Wang, Tianyi Yan, Xueyang Zhang, Kun Zhan, Peng Jia, XianPeng Lang, Jia-Wang Bian, Kaicheng Yu, Xiaodan Liang

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: ACM MM 2025

---

## 💡 一句话要点

**提出OmniGen统一框架以解决自动驾驶中多模态传感器数据生成效率低、对齐难的问题**

🎯 **匹配领域**: **自动驾驶** **视觉里程计** **强化学习**

**关键词**: `多模态传感器生成` `自动驾驶数据合成` `鸟瞰图空间` `体渲染` `扩散变换器` `可控生成` `激光雷达与相机融合` `统一框架`

## 📋 核心要点

1. 现有方法主要关注单模态生成，导致多模态传感器数据效率低下和对齐不准确，限制了自动驾驶数据合成的实用性。
2. 提出OmniGen统一框架，利用共享BEV空间统一多模态特征，并设计UAE方法通过体渲染联合解码激光雷达和相机数据，结合DiT和ControlNet实现可控生成。
3. 实验表明，OmniGen在多模态一致性和灵活传感器调整方面实现了期望性能，验证了其在统一多模态传感器数据生成中的有效性。

## 📝 摘要（中文）

自动驾驶的显著进步很大程度上依赖于大量真实世界数据的收集，但获取多样化和极端案例数据仍然成本高昂且效率低下。生成模型通过合成逼真的传感器数据成为一种有前景的解决方案。然而，现有方法主要关注单模态生成，导致多模态传感器数据效率低下和对齐不准确。为解决这些挑战，我们提出了OmniGen，在一个统一框架中生成对齐的多模态传感器数据。我们的方法利用共享的鸟瞰图空间来统一多模态特征，并设计了一种新颖的可泛化多模态重建方法UAE，以联合解码激光雷达和多视角相机数据。UAE通过体渲染实现多模态传感器解码，从而实现准确和灵活的重建。此外，我们结合了带有ControlNet分支的扩散变换器，以实现可控的多模态传感器生成。我们的全面实验表明，OmniGen在多模态一致性和灵活传感器调整方面，在统一多模态传感器数据生成中实现了期望的性能。

## 🔬 方法详解

OmniGen的整体框架是一个统一的多模态传感器数据生成系统。其核心创新点包括：利用共享的鸟瞰图空间来统一多模态特征表示，设计了一种新颖的可泛化多模态重建方法UAE，该方法通过体渲染技术联合解码激光雷达和多视角相机数据，实现准确和灵活的重建。此外，框架结合了扩散变换器与ControlNet分支，以支持可控的多模态传感器生成。与现有方法的主要区别在于，OmniGen不再局限于单模态生成，而是通过统一的BEV空间和UAE解码器，实现了多模态数据的对齐和协同生成，提高了数据合成的效率和一致性。

## 📊 实验亮点

实验结果显示，OmniGen在统一多模态传感器数据生成中实现了多模态一致性和灵活传感器调整的期望性能，验证了其框架的有效性，具体性能提升数据未知，但强调了其在解决现有方法不足方面的优势。

## 🎯 应用场景

该研究主要应用于自动驾驶领域，通过生成多样化和对齐的多模态传感器数据，可以高效合成极端案例数据，用于训练和测试自动驾驶系统，降低数据采集成本，提升模型鲁棒性和安全性。

## 📄 摘要（原文）

> Autonomous driving has seen remarkable advancements, largely driven by extensive real-world data collection. However, acquiring diverse and corner-case data remains costly and inefficient. Generative models have emerged as a promising solution by synthesizing realistic sensor data. However, existing approaches primarily focus on single-modality generation, leading to inefficiencies and misalignment in multimodal sensor data. To address these challenges, we propose OminiGen, which generates aligned multimodal sensor data in a unified framework. Our approach leverages a shared Bird\u2019s Eye View (BEV) space to unify multimodal features and designs a novel generalizable multimodal reconstruction method, UAE, to jointly decode LiDAR and multi-view camera data. UAE achieves multimodal sensor decoding through volume rendering, enabling accurate and flexible reconstruction. Furthermore, we incorporate a Diffusion Transformer (DiT) with a ControlNet branch to enable controllable multimodal sensor generation. Our comprehensive experiments demonstrate that OminiGen achieves desired performances in unified multimodal sensor data generation with multimodal consistency and flexible sensor adjustments.

