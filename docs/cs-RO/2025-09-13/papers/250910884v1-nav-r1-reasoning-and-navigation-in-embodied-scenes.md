---
layout: default
title: "Nav-R1: Reasoning and Navigation in Embodied Scenes"
---

# Nav-R1: Reasoning and Navigation in Embodied Scenes

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10884" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10884v1</a>
  <a href="https://arxiv.org/pdf/2509.10884.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10884v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10884v1', 'Nav-R1: Reasoning and Navigation in Embodied Scenes')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qingxiang Liu, Ting Huang, Zeyu Zhang, Hao Tang

**分类**: cs.RO, cs.CV

**发布日期**: 2025-09-13

**🔗 代码/项目**: [GITHUB](https://github.com/AIGeeksGroup/Nav-R1) | [PROJECT_PAGE](https://aigeeksgroup.github.io/Nav-R1)

---

## 💡 一句话要点

**Nav-R1：具身环境中融合推理与导航的基座模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身导航` `思维链` `强化学习` `基座模型` `快-慢推理` `机器人` `具身智能`

## 📋 核心要点

1. 现有具身导航方法在复杂环境中泛化能力弱，主要原因是推理过程不稳定且缺乏连贯性。
2. Nav-R1通过构建大规模思维链数据集和设计快-慢推理范式，实现了高效且连贯的导航。
3. 实验表明，Nav-R1在多个具身AI基准测试中显著优于现有方法，并在真实机器人上验证了其鲁棒性。

## 📝 摘要（中文）

具身导航要求智能体整合感知、推理和行动，以便在复杂的3D环境中进行鲁棒的交互。现有方法通常存在推理轨迹不连贯和不稳定，阻碍了在不同环境中的泛化，并且难以平衡长程语义推理与低延迟控制以实现实时导航。为了解决这些挑战，我们提出了Nav-R1，一个统一具身环境推理的具身基座模型。我们首先构建了Nav-CoT-110K，一个用于具身任务的大规模逐步思维链（CoT）数据集，从而能够使用结构化推理进行冷启动初始化。在此基础上，我们设计了一个基于GRPO的强化学习框架，该框架具有三个互补的奖励：格式、理解和导航，以提高结构一致性、语义对齐和路径保真度。此外，我们引入了一种快-慢推理范式，将审慎的语义推理与低延迟的反应式控制分离，以实现高效且连贯的导航。在具身AI基准上的大量评估表明，Nav-R1始终优于强大的基线，在推理和导航性能方面平均提高了8%以上。在移动机器人上的真实部署进一步验证了其在有限的板载资源下的鲁棒性。

## 🔬 方法详解

**问题定义**：现有具身导航方法难以在复杂环境中实现鲁棒的推理和导航。主要痛点在于：1) 推理过程不连贯，导致泛化能力差；2) 难以平衡长程语义推理和低延迟控制，影响实时性。

**核心思路**：Nav-R1的核心思路是构建一个统一的具身环境推理基座模型，通过大规模思维链数据集进行预训练，并采用快-慢推理范式，将高层次的语义推理与低层次的运动控制解耦。这样既能保证推理的连贯性，又能实现实时的导航。

**技术框架**：Nav-R1的整体框架包括以下几个主要模块：1) Nav-CoT-110K数据集：用于预训练模型的思维链数据；2) GRPO-based强化学习框架：使用格式、理解和导航三个奖励函数进行微调；3) 快-慢推理范式：将语义推理和运动控制分离。整体流程是先使用Nav-CoT-110K进行预训练，然后使用GRPO进行强化学习微调，最后在导航任务中使用快-慢推理范式进行推理和控制。

**关键创新**：Nav-R1的关键创新点在于：1) 构建了大规模的具身任务思维链数据集Nav-CoT-110K，为模型提供了丰富的推理知识；2) 提出了快-慢推理范式，有效平衡了推理的连贯性和导航的实时性。与现有方法相比，Nav-R1能够进行更连贯、更高效的推理和导航。

**关键设计**：Nav-CoT-110K数据集包含11万个思维链样本，覆盖多种具身任务。GRPO框架中的三个奖励函数分别用于约束推理格式、提高语义理解和优化导航路径。快-慢推理范式中，慢速推理模块负责高层次的语义推理，而快速控制模块负责低层次的运动控制。具体网络结构和参数设置在论文中有详细描述（未知）。

## 📊 实验亮点

Nav-R1在多个具身AI基准测试中取得了显著的性能提升，平均提高了8%以上。例如，在Room-to-Room导航任务中，Nav-R1的成功率显著高于现有方法。此外，在真实机器人上的实验表明，Nav-R1在有限的计算资源下也能实现鲁棒的导航，验证了其在实际应用中的可行性。

## 🎯 应用场景

Nav-R1具有广泛的应用前景，例如家庭服务机器人、仓储物流机器人、自动驾驶等。它可以帮助机器人在复杂环境中进行自主导航和任务执行，提高机器人的智能化水平和服务能力。未来，Nav-R1有望成为具身智能领域的重要基石，推动相关技术的发展。

## 📄 摘要（原文）

> Embodied navigation requires agents to integrate perception, reasoning, and action for robust interaction in complex 3D environments. Existing approaches often suffer from incoherent and unstable reasoning traces that hinder generalization across diverse environments, and difficulty balancing long-horizon semantic reasoning with low-latency control for real-time navigation. To address these challenges, we propose Nav-R1, an embodied foundation model that unifies reasoning in embodied environments. We first construct Nav-CoT-110K, a large-scale dataset of step-by-step Chains-of-Thought (CoT) for embodied tasks, which enables cold-start initialization with structured reasoning. Building on this foundation, we design a GRPO-based reinforcement learning framework with three complementary rewards: format, understanding, and navigation, to improve structural adherence, semantic grounding, and path fidelity. Furthermore, we introduce a Fast-in-Slow reasoning paradigm, decoupling deliberate semantic reasoning from low-latency reactive control for efficient yet coherent navigation. Extensive evaluations on embodied AI benchmarks demonstrate that Nav-R1 consistently outperforms strong baselines, with over 8% average improvement in reasoning and navigation performance. Real-world deployment on a mobile robot further validates its robustness under limited onboard resources. Code: https://github.com/AIGeeksGroup/Nav-R1. Website: https://aigeeksgroup.github.io/Nav-R1.

