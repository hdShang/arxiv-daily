---
layout: default
title: "GigaBrain-0: A World Model-Powered Vision-Language-Action Model"
---

# GigaBrain-0: A World Model-Powered Vision-Language-Action Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.19430" class="toolbar-btn" target="_blank">📄 arXiv: 2510.19430v3</a>
  <a href="https://arxiv.org/pdf/2510.19430.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.19430v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.19430v3', 'GigaBrain-0: A World Model-Powered Vision-Language-Action Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: GigaBrain Team, Angen Ye, Boyuan Wang, Chaojun Ni, Guan Huang, Guosheng Zhao, Haoyun Li, Jie Li, Jiagang Zhu, Lv Feng, Peng Li, Qiuping Deng, Runqi Ouyang, Wenkang Qin, Xinze Chen, Xiaofeng Wang, Yang Wang, Yifan Li, Yilong Li, Yiran Ding, Yuan Xu, Yun Ye, Yukun Zhou, Zhehao Dong, Zhenan Wang, Zhichao Liu, Zheng Zhu

**分类**: cs.RO, cs.CV

**发布日期**: 2025-10-22 (更新: 2025-12-04)

**备注**: https://gigabrain0.github.io/

---

## 💡 一句话要点

**GigaBrain-0：基于世界模型赋能的视觉-语言-动作通用机器人模型**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作模型` `世界模型` `机器人学习` `泛化能力` `具身智能`

## 📋 核心要点

1. 现有VLA模型依赖昂贵的真实机器人数据，限制了模型的可扩展性和泛化能力。
2. GigaBrain-0利用世界模型生成多样化数据，减少对真实数据的依赖，提升跨任务泛化能力。
3. 通过RGBD输入和具身CoT监督，增强模型对空间几何、对象状态和长时依赖的推理能力。

## 📝 摘要（中文）

本文介绍了GigaBrain-0，一种新型的视觉-语言-动作（VLA）基础模型，该模型利用世界模型生成的数据（例如，视频生成、real2real迁移、人体迁移、视角迁移、sim2real迁移数据）进行训练。通过大规模利用世界模型生成多样化的数据，GigaBrain-0显著降低了对真实机器人数据的依赖，同时提高了跨任务泛化能力。该方法还通过RGBD输入建模和具身Chain-of-Thought（CoT）监督来提高策略的鲁棒性，使模型能够在任务执行期间推理空间几何、对象状态和长时依赖关系。这在灵巧、长时程和移动操作任务的真实世界性能方面带来了显著的提升。大量实验表明，GigaBrain-0在外观（例如，纹理、颜色）、对象放置和相机视点的变化方面实现了卓越的泛化能力。此外，我们还展示了GigaBrain-0-Small，这是一种优化的轻量级变体，旨在在NVIDIA Jetson AGX Orin等设备上高效运行。

## 🔬 方法详解

**问题定义**：当前视觉-语言-动作（VLA）模型训练严重依赖于大规模真实机器人数据，而真实数据的采集成本高昂且耗时，这成为制约VLA模型扩展性和泛化能力的关键瓶颈。现有方法难以有效应对真实世界中复杂多变的环境和任务需求。

**核心思路**：GigaBrain-0的核心思路是利用世界模型生成大量多样化的合成数据，包括视频生成、real2real迁移、人体迁移、视角迁移、sim2real迁移等，从而显著减少对真实机器人数据的依赖。通过在合成数据上进行预训练，模型能够学习到更通用的视觉和物理规律，从而提升在真实环境中的泛化能力。

**技术框架**：GigaBrain-0的整体框架包含数据生成模块、模型训练模块和策略执行模块。数据生成模块利用世界模型生成各种类型的合成数据，用于模型的预训练。模型训练模块采用Transformer架构，并结合RGBD输入建模和具身Chain-of-Thought（CoT）监督，以提高模型的鲁棒性和推理能力。策略执行模块将训练好的模型部署到真实机器人上，完成各种操作任务。

**关键创新**：GigaBrain-0最重要的技术创新在于利用世界模型生成数据来训练VLA模型。与传统的依赖真实数据的方法相比，该方法能够以更低的成本生成更大规模、更多样化的数据，从而显著提升模型的泛化能力。此外，RGBD输入建模和具身CoT监督也进一步提高了模型的性能。

**关键设计**：RGBD输入建模允许模型同时处理RGB图像和深度信息，从而更好地理解场景的几何结构。具身CoT监督通过引入中间推理步骤，引导模型进行更细粒度的推理，从而提高策略的准确性和可解释性。具体的网络结构和损失函数等技术细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

实验结果表明，GigaBrain-0在真实世界的灵巧操作、长时程操作和移动操作任务中表现出卓越的泛化能力。具体性能数据和对比基线在论文中未明确给出，属于未知信息。但论文强调，GigaBrain-0在外观、对象放置和相机视点变化等方面的泛化能力显著优于现有方法。

## 🎯 应用场景

GigaBrain-0在通用机器人领域具有广泛的应用前景，可用于开发能够执行各种复杂操作任务的智能机器人。例如，它可以应用于智能制造、仓储物流、家庭服务等领域，实现自动化生产、智能分拣、智能清洁等功能。该研究有望推动机器人技术的进步，加速机器人在各行各业的普及。

## 📄 摘要（原文）

> Training Vision-Language-Action (VLA) models for generalist robots typically requires large-scale real-world robot data, which is expensive and time-consuming to collect. The inefficiency of physical data collection severely limits the scalability, and generalization capacity of current VLA systems. To address this challenge, we introduce GigaBrain-0, a novel VLA foundation model empowered by world model-generated data (e.g., video generation, real2real transfer, human transfer, view transfer, sim2real transfer data). By leveraging world models to generate diverse data at scale, GigaBrain-0 significantly reduces reliance on real robot data while improving cross-task generalization. Our approach further improves policy robustness through RGBD input modeling and embodied Chain-of-Thought (CoT) supervision, enabling the model to reason about spatial geometry, object states, and long-horizon dependencies during task execution. This leads to substantial gains in real-world performance on dexterous, long-horizon, and mobile manipulation tasks. Extensive experiments demonstrate that GigaBrain-0 achieves superior generalization across variations in appearances (e.g., textures, colors), object placements, and camera viewpoints. Additionally, we present GigaBrain-0-Small, an optimized lightweight variant designed to run efficiently on devices such as the NVIDIA Jetson AGX Orin.

