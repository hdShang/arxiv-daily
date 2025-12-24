---
layout: default
title: "Ferret-UI Lite: Lessons from Building Small On-Device GUI Agents"
---

# Ferret-UI Lite: Lessons from Building Small On-Device GUI Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26539" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26539v1</a>
  <a href="https://arxiv.org/pdf/2509.26539.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26539v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26539v1', 'Ferret-UI Lite: Lessons from Building Small On-Device GUI Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhen Yang, Zi-Yi Dou, Di Feng, Forrest Huang, Anh Nguyen, Keen You, Omar Attia, Yuhao Yang, Michael Feng, Haotian Zhang, Ram Ramrakhya, Chao Jia, Jeffrey Nichols, Alexander Toshev, Yinfei Yang, Zhe Gan

**分类**: cs.CV, cs.CL, cs.LG

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出Ferret-UI Lite，一个紧凑型端到端GUI智能体，用于跨平台交互。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `GUI智能体` `端侧部署` `视觉语言模型` `思维链推理` `强化学习` `GUI grounding` `GUI导航`

## 📋 核心要点

1. 现有GUI智能体模型通常较大，难以在端侧设备上部署和运行，限制了其应用场景。
2. Ferret-UI Lite通过数据混合、思维链推理、视觉工具使用和强化学习等方法，构建了一个紧凑且高效的GUI智能体。
3. 实验表明，Ferret-UI Lite在GUI grounding和导航任务上取得了与同等规模模型相比具有竞争力的性能。

## 📝 摘要（中文）

本文提出了Ferret-UI Lite，一个紧凑的端到端GUI智能体，能够在移动、网页和桌面等多种平台上运行。该智能体利用针对小型模型优化的技术构建，通过整合来自真实和合成来源的多样化GUI数据混合进行训练。为了增强推理时的性能，采用了思维链推理和视觉工具使用。此外，还使用了带有精心设计的奖励的强化学习。Ferret-UI Lite在GUI grounding方面取得了具有竞争力的性能，在ScreenSpot-V2、ScreenSpot-Pro和OSWorld-G基准测试中分别获得了91.6%、53.3%和61.2%的分数。在GUI导航方面，Ferret-UI Lite在AndroidWorld和OSWorld上的成功率分别为28.0%和19.8%。本文分享了开发紧凑型、端到端GUI智能体的方法和经验。

## 🔬 方法详解

**问题定义**：现有GUI智能体通常模型较大，计算资源消耗高，难以在移动设备等资源受限的端侧设备上部署和运行。这限制了它们在实际应用中的广泛使用。因此，需要开发一种能够在端侧设备上高效运行的GUI智能体。

**核心思路**：Ferret-UI Lite的核心思路是构建一个紧凑的端到端模型，通过优化数据、推理和训练过程，在保证性能的同时，显著降低模型大小和计算复杂度。具体来说，通过精心策划的数据混合、思维链推理、视觉工具使用和强化学习等技术来实现这一目标。

**技术框架**：Ferret-UI Lite的整体框架是一个端到端的模型，它直接接收GUI的视觉输入和任务指令，并输出相应的操作。主要包含以下几个阶段：1) 数据收集与混合：收集真实和合成的GUI数据，并进行混合，以提高模型的泛化能力。2) 模型训练：使用混合数据训练一个3B参数的视觉语言模型。3) 推理优化：采用思维链推理和视觉工具使用来提高推理时的性能。4) 强化学习：使用设计的奖励函数进行强化学习，以进一步优化模型的行为。

**关键创新**：Ferret-UI Lite的关键创新在于它在模型大小和性能之间取得了良好的平衡。通过数据混合、思维链推理、视觉工具使用和强化学习等技术的结合，构建了一个能够在端侧设备上高效运行的GUI智能体。与现有方法相比，Ferret-UI Lite更加注重模型的轻量化和端侧部署能力。

**关键设计**：在数据方面，采用了真实数据和合成数据的混合策略，以提高模型的泛化能力。在推理方面，采用了思维链推理，使模型能够逐步推理并做出决策。在训练方面，使用了强化学习，并设计了合适的奖励函数，以引导模型学习正确的行为。模型大小为3B参数，是一个相对较小的模型，适合在端侧设备上部署。

## 📊 实验亮点

Ferret-UI Lite在GUI grounding任务中，在ScreenSpot-V2、ScreenSpot-Pro和OSWorld-G基准测试中分别获得了91.6%、53.3%和61.2%的分数。在GUI导航任务中，在AndroidWorld和OSWorld上的成功率分别为28.0%和19.8%。这些结果表明，Ferret-UI Lite在小型GUI智能体中具有竞争力。

## 🎯 应用场景

Ferret-UI Lite具有广泛的应用前景，例如：移动设备上的自动化测试、智能助手、无障碍辅助等。它可以帮助用户更高效地与GUI进行交互，提高生产力。未来，可以进一步优化模型，使其能够处理更复杂的GUI任务，并支持更多的平台和设备。

## 📄 摘要（原文）

> Developing autonomous agents that effectively interact with Graphic User Interfaces (GUIs) remains a challenging open problem, especially for small on-device models. In this paper, we present Ferret-UI Lite, a compact, end-to-end GUI agent that operates across diverse platforms, including mobile, web, and desktop. Utilizing techniques optimized for developing small models, we build our 3B Ferret-UI Lite agent through curating a diverse GUI data mixture from real and synthetic sources, strengthening inference-time performance through chain-of-thought reasoning and visual tool-use, and reinforcement learning with designed rewards. Ferret-UI Lite achieves competitive performance with other small-scale GUI agents. In GUI grounding, Ferret-UI Lite attains scores of $91.6\%$, $53.3\%$, and $61.2\%$ on the ScreenSpot-V2, ScreenSpot-Pro, and OSWorld-G benchmarks, respectively. For GUI navigation, Ferret-UI Lite achieves success rates of $28.0\%$ on AndroidWorld and $19.8\%$ on OSWorld. We share our methods and lessons learned from developing compact, on-device GUI agents.

