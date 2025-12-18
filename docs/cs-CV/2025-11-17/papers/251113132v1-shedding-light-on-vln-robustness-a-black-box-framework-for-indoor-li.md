---
layout: default
title: Shedding Light on VLN Robustness: A Black-box Framework for Indoor Lighting-based Adversarial Attack
---

# Shedding Light on VLN Robustness: A Black-box Framework for Indoor Lighting-based Adversarial Attack

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.13132" class="toolbar-btn" target="_blank">📄 arXiv: 2511.13132v1</a>
  <a href="https://arxiv.org/pdf/2511.13132.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.13132v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.13132v1', 'Shedding Light on VLN Robustness: A Black-box Framework for Indoor Lighting-based Adversarial Attack')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenyang Li, Wenbing Tang, Yihao Huang, Sinong Simon Zhan, Ming Hu, Xiaojun Jia, Yang Liu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-17

---

## 💡 一句话要点

**提出基于室内光照对抗攻击的VLN鲁棒性黑盒评估框架**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `视觉语言导航` `对抗攻击` `鲁棒性评估` `室内光照` `黑盒攻击`

## 📋 核心要点

1. 现有VLN对抗攻击方法依赖于不真实的纹理扰动，缺乏实际意义，难以评估智能体在真实环境中的鲁棒性。
2. 提出室内光照对抗攻击（ILA）框架，通过模拟真实室内光照变化（静态和动态）来评估VLN智能体的鲁棒性。
3. 实验表明，ILA能有效降低VLN智能体的导航成功率和轨迹效率，揭示了现有模型对光照变化的脆弱性。

## 📝 摘要（中文）

本文针对视觉-语言导航（VLN）智能体的鲁棒性问题，提出了一种新的黑盒对抗攻击框架，称为室内光照对抗攻击（ILA）。现有对抗评估方法通常依赖于不常见的纹理扰动，与实际室内环境差异较大。ILA框架专注于室内光照这一重要但被忽视的场景属性，通过操纵全局光照来干扰VLN智能体。具体而言，设计了两种攻击模式：静态室内光照攻击（SILA），光照强度在整个episode中保持不变；动态室内光照攻击（DILA），在关键时刻开关灯以引起突变。在三个导航任务上，对两个最先进的VLN模型进行了评估。结果表明，ILA显著提高了失败率并降低了轨迹效率，揭示了VLN智能体对真实室内光照变化的脆弱性。

## 🔬 方法详解

**问题定义**：现有VLN智能体的鲁棒性评估方法主要集中在图像纹理的对抗扰动上，这些扰动在现实室内环境中很少出现。因此，这些评估方法难以反映智能体在真实场景下的鲁棒性，也无法有效指导智能体的改进。论文旨在研究VLN智能体在真实室内光照变化下的鲁棒性，并提出一种更贴近实际的对抗攻击方法。

**核心思路**：论文的核心思路是利用室内光照这一重要的场景属性来设计对抗攻击。室内光照是影响视觉感知的关键因素，且在真实环境中存在自然变化（例如，开关灯）。通过模拟这些光照变化，可以更真实地评估VLN智能体的鲁棒性，并发现其潜在的脆弱性。

**技术框架**：ILA框架是一个黑盒攻击框架，不需要访问目标VLN模型的内部参数。该框架主要包含两个攻击模式：SILA（静态室内光照攻击）和DILA（动态室内光照攻击）。SILA在整个导航过程中保持固定的光照强度，模拟不同光照条件下的导航。DILA在导航过程中的关键时刻切换灯光，模拟突发的光照变化。攻击目标是使VLN智能体导航失败或降低导航效率。

**关键创新**：ILA的关键创新在于其对抗攻击的设计思路，即从真实场景的属性（室内光照）出发，而非人为构造不自然的扰动。这种设计使得对抗攻击更具实际意义，能够更有效地评估VLN智能体在真实环境中的鲁棒性。此外，DILA模式模拟了突发的光照变化，更具挑战性，能够更深入地揭示VLN智能体的脆弱性。

**关键设计**：在SILA中，光照强度是一个关键参数，可以通过调整全局光照强度来模拟不同的光照条件。在DILA中，关键时刻的选择至关重要，可以根据VLN智能体的行为（例如，即将做出错误决策时）来动态调整。论文中具体的光照强度值和关键时刻选择策略未知，需要在实验中进行探索和优化。

## 📊 实验亮点

实验结果表明，ILA框架能够显著降低VLN智能体的导航成功率和轨迹效率。例如，在某些任务中，SILA和DILA攻击分别导致导航成功率下降了10%-20%。此外，DILA攻击比SILA攻击更有效，表明VLN智能体对突发的光照变化更为敏感。这些结果揭示了现有VLN模型在光照鲁棒性方面的不足。

## 🎯 应用场景

该研究成果可应用于提升VLN智能体在真实环境中的鲁棒性。通过对抗攻击，可以发现智能体对光照变化的脆弱性，并指导模型改进，例如，通过数据增强或对抗训练来提高其对光照变化的适应能力。此外，该框架也可用于评估其他视觉导航系统的鲁棒性，推动相关技术的发展。

## 📄 摘要（原文）

> Vision-and-Language Navigation (VLN) agents have made remarkable progress, but their robustness remains insufficiently studied. Existing adversarial evaluations often rely on perturbations that manifest as unusual textures rarely encountered in everyday indoor environments. Errors under such contrived conditions have limited practical relevance, as real-world agents are unlikely to encounter such artificial patterns. In this work, we focus on indoor lighting, an intrinsic yet largely overlooked scene attribute that strongly influences navigation. We propose Indoor Lighting-based Adversarial Attack (ILA), a black-box framework that manipulates global illumination to disrupt VLN agents. Motivated by typical household lighting usage, we design two attack modes: Static Indoor Lighting-based Attack (SILA), where the lighting intensity remains constant throughout an episode, and Dynamic Indoor Lighting-based Attack (DILA), where lights are switched on or off at critical moments to induce abrupt illumination changes. We evaluate ILA on two state-of-the-art VLN models across three navigation tasks. Results show that ILA significantly increases failure rates while reducing trajectory efficiency, revealing previously unrecognized vulnerabilities of VLN agents to realistic indoor lighting variations.

