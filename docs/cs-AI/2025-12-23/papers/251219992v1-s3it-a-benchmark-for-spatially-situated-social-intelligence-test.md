---
layout: default
title: S$^3$IT: A Benchmark for Spatially Situated Social Intelligence Test
---

# S$^3$IT: A Benchmark for Spatially Situated Social Intelligence Test

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19992" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19992v1</a>
  <a href="https://arxiv.org/pdf/2512.19992.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19992v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19992v1', 'S$^3$IT: A Benchmark for Spatially Situated Social Intelligence Test')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhe Sun, Xueyuan Yang, Yujie Lu, Zhenliang Zhang

**分类**: cs.AI, cs.CY

**发布日期**: 2025-12-23

**备注**: 10 pages, 9 figures

---

## 💡 一句话要点

**提出S$^3$IT基准测试，用于评估具身智能体在复杂社交环境中的推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身智能` `社会智能` `基准测试` `大型语言模型` `空间推理`

## 📋 核心要点

1. 现有评估方法要么局限于非具身的社会推理，要么是社会无关的物理任务，无法评估智能体在现实环境中整合物理和社会约束的能力。
2. S$^3$IT基准测试通过座位安排任务，要求智能体在3D环境中为具有复杂社交关系的NPC安排座位，从而评估具身社会智能。
3. 实验结果表明，现有LLM在空间智能方面存在不足，但在解决具有明确文本线索的冲突方面表现出接近人类水平的能力。

## 📝 摘要（中文）

本文提出了一个名为空间情境化社会智能测试(S$^3$IT)的基准，旨在评估具身智能体的社会智能。该基准的核心是一个新颖且具有挑战性的座位安排任务，要求智能体在一个3D环境中为一群由大型语言模型(LLM)驱动的NPC安排座位，这些NPC具有不同的身份、偏好和复杂的人际关系。该框架具有程序可扩展性，能够生成大量且多样化的场景，并控制难度。智能体需要通过主动对话获取偏好，通过自主探索感知环境，并在复杂的约束网络中执行多目标优化。在S$^3$IT上评估了最先进的LLM，结果表明它们仍然难以解决这个问题，与人类基线相比存在明显的差距。结果表明LLM在空间智能方面存在不足，但同时证明了它们在解决具有明确文本线索的冲突方面具有接近人类水平的能力。

## 🔬 方法详解

**问题定义**：现有方法无法有效评估具身智能体在同时考虑物理和社会约束下的推理能力。具体来说，现有基准测试要么侧重于非具身的文本社会推理，要么侧重于与社会因素无关的物理任务，忽略了真实世界中物理和社会因素相互作用的复杂性。因此，需要一个能够综合评估智能体在具身环境中进行社会推理能力的基准。

**核心思路**：S$^3$IT的核心思路是创建一个具有挑战性的座位安排任务，该任务要求智能体在3D环境中为一群具有不同身份、偏好和复杂人际关系的NPC安排座位。智能体需要通过主动对话获取NPC的偏好，通过自主探索感知环境，并在复杂的约束网络中进行多目标优化，从而实现最佳的座位安排。

**技术框架**：S$^3$IT的整体框架包含以下几个主要模块：1) **场景生成器**：用于生成具有不同NPC身份、偏好和人际关系的3D环境。该模块具有程序可扩展性，可以生成大量且多样化的场景，并控制难度。2) **对话模块**：允许智能体与NPC进行对话，从而获取NPC的座位偏好。3) **环境感知模块**：允许智能体通过自主探索感知3D环境，获取座位的位置和可用性信息。4) **座位安排模块**：根据NPC的偏好、人际关系和环境约束，进行多目标优化，从而生成最佳的座位安排方案。5) **评估模块**：用于评估智能体的座位安排方案的质量，例如，是否满足NPC的偏好，是否避免了冲突等。

**关键创新**：S$^3$IT的关键创新在于它将社会智能与具身环境相结合，创造了一个更真实、更具挑战性的评估场景。与现有基准测试相比，S$^3$IT能够更全面地评估智能体在复杂社交环境中的推理能力。此外，S$^3$IT的程序可扩展性使其能够生成大量且多样化的场景，从而避免了过拟合问题。

**关键设计**：S$^3$IT的关键设计包括：1) 使用LLM驱动的NPC，使其具有更真实、更自然的对话能力。2) 设计了复杂的NPC人际关系网络，使得座位安排任务更具挑战性。3) 采用了多目标优化算法，以平衡不同NPC的偏好和约束。4) 设计了多种评估指标，以全面评估智能体的座位安排方案的质量。具体参数设置和损失函数等细节未在论文中详细描述，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19992v1/S3IT/figures/teaser.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19992v1/S3IT/figures/elements.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19992v1/S3IT/figures/room.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，最先进的LLM在S$^3$IT基准测试中表现不佳，与人类基线相比存在明显的差距。这表明LLM在空间智能方面存在不足，需要进一步改进。然而，LLM在解决具有明确文本线索的冲突方面表现出接近人类水平的能力，表明LLM在社会推理方面具有一定的潜力。具体的性能数据和提升幅度未在摘要中给出，属于未知信息。

## 🎯 应用场景

S$^3$IT基准测试可以应用于开发更智能、更具社会意识的具身智能体，例如，社交机器人、虚拟助手等。这些智能体可以在各种现实场景中提供帮助，例如，组织会议、安排座位、协调活动等。此外，S$^3$IT还可以用于研究人类的社会推理能力，从而更好地理解人类的社交行为。

## 📄 摘要（原文）

> The integration of embodied agents into human environments demands embodied social intelligence: reasoning over both social norms and physical constraints. However, existing evaluations fail to address this integration, as they are limited to either disembodied social reasoning (e.g., in text) or socially-agnostic physical tasks. Both approaches fail to assess an agent's ability to integrate and trade off both physical and social constraints within a realistic, embodied context. To address this challenge, we introduce Spatially Situated Social Intelligence Test (S$^{3}$IT), a benchmark specifically designed to evaluate embodied social intelligence. It is centered on a novel and challenging seat-ordering task, requiring an agent to arrange seating in a 3D environment for a group of large language model-driven (LLM-driven) NPCs with diverse identities, preferences, and intricate interpersonal relationships. Our procedurally extensible framework generates a vast and diverse scenario space with controllable difficulty, compelling the agent to acquire preferences through active dialogue, perceive the environment via autonomous exploration, and perform multi-objective optimization within a complex constraint network. We evaluate state-of-the-art LLMs on S$^{3}$IT and found that they still struggle with this problem, showing an obvious gap compared with the human baseline. Results imply that LLMs have deficiencies in spatial intelligence, yet simultaneously demonstrate their ability to achieve near human-level competence in resolving conflicts that possess explicit textual cues.

