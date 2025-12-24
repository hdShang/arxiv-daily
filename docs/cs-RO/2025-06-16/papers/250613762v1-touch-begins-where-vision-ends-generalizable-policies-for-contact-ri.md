---
layout: default
title: "Touch begins where vision ends: Generalizable policies for contact-rich manipulation"
---

# Touch begins where vision ends: Generalizable policies for contact-rich manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.13762" class="toolbar-btn" target="_blank">📄 arXiv: 2506.13762v1</a>
  <a href="https://arxiv.org/pdf/2506.13762.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.13762v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.13762v1', 'Touch begins where vision ends: Generalizable policies for contact-rich manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zifan Zhao, Siddhant Haldar, Jinda Cui, Lerrel Pinto, Raunaq Bhirangi

**分类**: cs.RO, cs.CV

**发布日期**: 2025-06-16

---

## 💡 一句话要点

**提出ViTaL框架以解决接触丰富的操控任务**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `接触丰富操控` `视觉-语言模型` `局部策略` `强化学习` `机器人技术`

## 📋 核心要点

1. 现有的数据驱动方法在精确操控任务中表现不佳，模仿学习和强化学习各有局限性。
2. ViTaL框架通过分阶段处理操控任务，结合视觉-语言模型和可重用的局部策略，实现了更好的泛化能力。
3. 实验结果显示，ViTaL在未见环境中的接触丰富任务上成功率达到90%，且对干扰物具有良好的适应性。

## 📝 摘要（中文）

数据驱动的方法在精确操控方面面临挑战；模仿学习需要大量难以获得的示范，而强化学习则产生脆弱且不可泛化的策略。我们提出了ViTaL政策学习框架，通过将精细操控任务分解为两个阶段来解决这一问题：首先是利用视觉-语言模型进行场景级推理的到达阶段，其次是使用自我中心视觉和触觉传感器进行接触丰富操控的局部交互阶段。ViTaL在未见环境中的接触丰富任务上取得了约90%的成功率，并且对干扰物具有鲁棒性。

## 🔬 方法详解

**问题定义**：本论文旨在解决精细操控任务中的泛化能力不足问题。现有方法在处理接触丰富的操控时，往往依赖大量示范或产生不稳定的策略，导致效果不理想。

**核心思路**：我们提出的ViTaL框架通过将操控任务分为到达阶段和局部交互阶段，利用视觉-语言模型进行场景推理，并通过可重用的局部策略进行接触操控，从而提高了任务的泛化能力。

**技术框架**：ViTaL的整体架构包括两个主要阶段：第一阶段是利用视觉-语言模型进行目标定位，第二阶段是通过局部策略实现接触操控。这种分阶段的设计使得模型能够在不同场景中保持一致的低级交互能力。

**关键创新**：ViTaL的核心创新在于结合了视觉-语言模型和触觉传感，利用基础模型进行分割训练，从而提高了视觉编码器的鲁棒性和策略的泛化能力。这与传统方法的单一策略学习方式有本质区别。

**关键设计**：在模型设计中，我们采用了行为克隆的方式训练视觉编码器，并使用残差强化学习来提升策略的泛化能力。此外，触觉传感器的引入显著提升了在接触丰富任务中的表现。实验中的消融研究验证了这些设计的有效性。

## 📊 实验亮点

实验结果表明，ViTaL在未见环境中的接触丰富任务上成功率达到90%，显著优于传统方法。通过消融研究，验证了视觉编码器和触觉传感器对策略泛化能力的提升，展示了ViTaL在复杂任务中的鲁棒性。

## 🎯 应用场景

该研究的ViTaL框架具有广泛的应用潜力，特别是在需要精确操控的机器人领域，如自动化装配、医疗机器人和服务机器人等。通过提高机器人在复杂环境中的操控能力，ViTaL有望推动智能机器人技术的进一步发展。

## 📄 摘要（原文）

> Data-driven approaches struggle with precise manipulation; imitation learning requires many hard-to-obtain demonstrations, while reinforcement learning yields brittle, non-generalizable policies. We introduce VisuoTactile Local (ViTaL) policy learning, a framework that solves fine-grained manipulation tasks by decomposing them into two phases: a reaching phase, where a vision-language model (VLM) enables scene-level reasoning to localize the object of interest, and a local interaction phase, where a reusable, scene-agnostic ViTaL policy performs contact-rich manipulation using egocentric vision and tactile sensing. This approach is motivated by the observation that while scene context varies, the low-level interaction remains consistent across task instances. By training local policies once in a canonical setting, they can generalize via a localize-then-execute strategy. ViTaL achieves around 90% success on contact-rich tasks in unseen environments and is robust to distractors. ViTaL's effectiveness stems from three key insights: (1) foundation models for segmentation enable training robust visual encoders via behavior cloning; (2) these encoders improve the generalizability of policies learned using residual RL; and (3) tactile sensing significantly boosts performance in contact-rich tasks. Ablation studies validate each of these insights, and we demonstrate that ViTaL integrates well with high-level VLMs, enabling robust, reusable low-level skills. Results and videos are available at https://vitalprecise.github.io.

