---
layout: default
title: "PersONAL: Towards a Comprehensive Benchmark for Personalized Embodied Agents"
---

# PersONAL: Towards a Comprehensive Benchmark for Personalized Embodied Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.19843" class="toolbar-btn" target="_blank">📄 arXiv: 2509.19843v1</a>
  <a href="https://arxiv.org/pdf/2509.19843.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.19843v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.19843v1', 'PersONAL: Towards a Comprehensive Benchmark for Personalized Embodied Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Filippo Ziliotto, Jelin Raphael Akkara, Alessandro Daniele, Lamberto Ballan, Luciano Serafini, Tommaso Campari

**分类**: cs.CV, cs.RO

**发布日期**: 2025-09-24

---

## 💡 一句话要点

**PersONAL：面向个性化具身智能代理的综合基准测试**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身智能` `个性化` `基准测试` `物体导航` `自然语言理解`

## 📋 核心要点

1. 现有具身智能代理难以在家庭等真实场景中建模个体人类的偏好和行为。
2. PersONAL基准测试通过构建个性化物体导航和定位任务，促进代理理解用户特定语义。
3. 实验表明现有方法与人类水平差距明显，亟需提升代理的个性化信息处理能力。

## 📝 摘要（中文）

本文提出了PersONAL，一个用于研究具身智能中个性化问题的综合基准。该基准旨在解决在以人为中心的真实场景（如家庭环境）中部署具身智能代理的挑战，特别是建模个体人类偏好和行为的难题。PersONAL要求代理识别、检索并导航到与特定用户相关的物体，响应自然语言查询，例如“找到Lily的书包”。PersONAL包含来自HM3D数据集的30多个逼真家庭场景中超过2000个高质量episode。每个episode都包含自然语言场景描述，明确了物体与其所有者之间的关联，要求代理对用户特定的语义进行推理。该基准支持两种评估模式：(1)在未见过的环境中进行主动导航，以及(2)在先前映射的场景中进行物体定位。与最先进的基线模型进行的实验表明，与人类性能之间存在显著差距，突出了对能够感知、推理和记忆个性化信息的具身智能代理的需求，为现实世界的辅助机器人铺平了道路。

## 🔬 方法详解

**问题定义**：论文旨在解决具身智能代理在个性化环境中的导航和物体定位问题。现有方法难以理解和利用用户特定的信息，导致在真实家庭场景中的应用受限。代理需要能够根据自然语言指令，找到属于特定用户的物体，这需要对场景中的物体和用户关系进行推理和记忆。

**核心思路**：论文的核心思路是构建一个包含丰富个性化信息的基准数据集，PersONAL。通过提供大量带有用户-物体关联的场景和任务，鼓励研究人员开发能够有效利用这些信息的具身智能代理。该基准测试旨在推动代理在理解用户偏好和行为方面的能力，从而提高其在真实世界中的实用性。

**技术框架**：PersONAL基准测试包含两个主要的评估模式：主动导航和物体定位。在主动导航模式中，代理需要在未见过的环境中导航到目标物体。在物体定位模式中，代理需要在先前已经探索过的场景中找到目标物体。每个episode都包含自然语言场景描述，以及物体与其所有者之间的明确关联。代理需要利用这些信息来完成任务。

**关键创新**：PersONAL的关键创新在于其对个性化信息的强调。与以往的具身智能基准测试相比，PersONAL更加关注代理对用户特定语义的理解和利用。通过提供丰富的用户-物体关联信息，PersONAL鼓励研究人员开发能够进行个性化推理的代理。

**关键设计**：PersONAL基准测试使用了HM3D数据集中的30多个逼真家庭场景，并构建了超过2000个高质量的episode。每个episode都包含详细的场景描述和用户-物体关联信息。基准测试提供了标准的评估指标，例如导航成功率和物体定位精度。研究人员可以使用这些指标来评估其代理的性能，并与其他方法进行比较。

## 📊 实验亮点

论文通过在PersONAL基准上对现有最先进的基线模型进行评估，发现这些模型在个性化任务上的表现与人类水平存在显著差距。这表明现有方法在理解和利用用户特定信息方面存在不足，突出了开发更智能、更个性化具身智能代理的必要性。该基准的发布将促进相关研究的发展。

## 🎯 应用场景

PersONAL的研究成果可应用于开发更智能、更个性化的辅助机器人，例如帮助老年人或残疾人在家中寻找物品、完成任务。此外，该研究还可应用于智能家居、虚拟助手等领域，提升用户体验和智能化水平。未来，具备个性化理解能力的具身智能代理将在医疗、教育等领域发挥重要作用。

## 📄 摘要（原文）

> Recent advances in Embodied AI have enabled agents to perform increasingly complex tasks and adapt to diverse environments. However, deploying such agents in realistic human-centered scenarios, such as domestic households, remains challenging, particularly due to the difficulty of modeling individual human preferences and behaviors. In this work, we introduce PersONAL (PERSonalized Object Navigation And Localization, a comprehensive benchmark designed to study personalization in Embodied AI. Agents must identify, retrieve, and navigate to objects associated with specific users, responding to natural-language queries such as "find Lily's backpack". PersONAL comprises over 2,000 high-quality episodes across 30+ photorealistic homes from the HM3D dataset. Each episode includes a natural-language scene description with explicit associations between objects and their owners, requiring agents to reason over user-specific semantics. The benchmark supports two evaluation modes: (1) active navigation in unseen environments, and (2) object grounding in previously mapped scenes. Experiments with state-of-the-art baselines reveal a substantial gap to human performance, highlighting the need for embodied agents capable of perceiving, reasoning, and memorizing over personalized information; paving the way towards real-world assistive robot.

