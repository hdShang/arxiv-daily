---
layout: default
title: "MobileWorld: Benchmarking Autonomous Mobile Agents in Agent-User Interactive, and MCP-Augmented Environments"
---

# MobileWorld: Benchmarking Autonomous Mobile Agents in Agent-User Interactive, and MCP-Augmented Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19432" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19432v1</a>
  <a href="https://arxiv.org/pdf/2512.19432.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19432v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19432v1', 'MobileWorld: Benchmarking Autonomous Mobile Agents in Agent-User Interactive, and MCP-Augmented Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Quyu Kong, Xu Zhang, Zhenyu Yang, Nolan Gao, Chen Liu, Panrong Tong, Chenglin Cai, Hanzhang Zhou, Jianan Zhang, Liangyu Chen, Zhidan Liu, Steven Hoi, Yue Wang

**分类**: cs.CL

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**MobileWorld：面向Agent-用户交互和MCP增强环境的移动Agent基准测试**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `移动Agent` `基准测试` `人机交互` `多应用协作` `移动云平台` `任务规划` `智能助手`

## 📋 核心要点

1. 现有AndroidWorld基准测试已饱和，缺乏对真实移动应用场景的模拟，尤其是在用户交互和多应用协作方面。
2. MobileWorld通过引入更复杂、长程的任务，以及Agent-用户交互和MCP增强任务，构建了一个更具挑战性的基准测试环境。
3. 实验结果表明，现有Agent在MobileWorld上的性能显著下降，尤其是在处理用户交互和MCP调用方面，揭示了未来研究方向。

## 📝 摘要（中文）

现有的在线移动应用基准测试中，AndroidWorld因其可复现的环境和确定性的评估而占据主导地位。然而，最近的Agent在该基准测试上取得了超过90%的成功率，表明其已趋于饱和，并促使人们需要更具挑战性的基准。此外，AndroidWorld缺乏关键的应用类别，如电子商务和企业通信，并且不能反映现实移动应用场景中模糊的用户指令和混合工具使用的特点。为了弥合这一差距，我们推出了MobileWorld，这是一个更具挑战性的基准，旨在更好地反映真实的移动应用使用情况，包含20个应用中的201个任务，同时保持与AndroidWorld相同水平的可复现评估。MobileWorld的难度体现在两个方面。首先，它强调具有跨应用交互的长程任务：MobileWorld平均需要近两倍的任务完成步骤（27.8 vs. 14.3），并且包含更多的多应用任务（62.2% vs. 9.5%）。其次，MobileWorld通过引入新的任务类别，包括Agent-用户交互和MCP增强任务，扩展了标准GUI操作。为了确保可靠的评估，我们提供了基于快照的容器环境和精确的功能验证，包括后端数据库检查和任务回调API。我们进一步开发了一个具有扩展动作空间的规划器-执行器Agent框架，以支持用户交互和MCP调用。我们的结果表明，与AndroidWorld相比，性能急剧下降，最佳Agent框架和端到端模型分别实现了51.7%和20.9%的成功率。我们的分析表明，当前模型在用户交互和MCP调用方面存在显著困难，为更强大、下一代移动智能提供了一个战略路线图。

## 🔬 方法详解

**问题定义**：现有AndroidWorld基准测试已无法有效评估移动Agent的性能，因为它过于简单，缺乏对真实世界移动应用场景的模拟，特别是忽略了用户交互和多应用协作。这导致Agent在真实场景中的泛化能力不足。

**核心思路**：MobileWorld的核心思路是构建一个更复杂、更真实的移动应用环境，包含更长程的任务、跨应用交互、用户交互和MCP（Mobile Cloud Platform）调用。通过增加任务的复杂性和多样性，更全面地评估Agent的性能和鲁棒性。

**技术框架**：MobileWorld的整体框架包括以下几个主要组成部分：1) 一个包含20个应用的移动应用环境，涵盖电子商务、企业通信等多个类别；2) 201个任务，包括标准GUI操作、Agent-用户交互和MCP增强任务；3) 一个基于快照的容器环境，用于保证评估的可复现性；4) 精确的功能验证机制，包括后端数据库检查和任务回调API；5) 一个规划器-执行器Agent框架，用于支持用户交互和MCP调用。

**关键创新**：MobileWorld的关键创新在于引入了Agent-用户交互和MCP增强任务。Agent-用户交互任务要求Agent能够理解用户的自然语言指令，并与用户进行多轮对话以完成任务。MCP增强任务要求Agent能够调用移动云平台提供的服务，例如图像识别、语音识别等，以辅助完成任务。

**关键设计**：MobileWorld的关键设计包括：1) 任务的长度和复杂性：MobileWorld的任务平均需要27.8个步骤完成，远高于AndroidWorld的14.3个步骤；2) 多应用任务的比例：MobileWorld中62.2%的任务涉及多个应用，而AndroidWorld仅为9.5%；3) 动作空间的设计：规划器-执行器Agent框架的动作空间扩展到包括用户交互和MCP调用，使其能够处理更复杂的任务。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19432v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19432v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19432v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，现有Agent在MobileWorld上的性能显著下降。最佳Agent框架的成功率为51.7%，端到端模型的成功率仅为20.9%，远低于在AndroidWorld上的表现。这表明现有Agent在处理用户交互和MCP调用方面存在显著困难，为未来的研究提供了明确的方向。

## 🎯 应用场景

MobileWorld为移动Agent的研究和开发提供了一个更具挑战性和现实意义的基准测试平台。它可以用于评估和比较不同Agent的性能，指导Agent的设计和优化，并促进移动智能的发展。潜在的应用领域包括智能助手、自动化测试、移动应用开发等，有助于提升移动设备的用户体验和效率。

## 📄 摘要（原文）

> Among existing online mobile-use benchmarks, AndroidWorld has emerged as the dominant benchmark due to its reproducible environment and deterministic evaluation; however, recent agents achieving over 90% success rates indicate its saturation and motivate the need for a more challenging benchmark. In addition, its environment lacks key application categories, such as e-commerce and enterprise communication, and does not reflect realistic mobile-use scenarios characterized by vague user instructions and hybrid tool usage. To bridge this gap, we introduce MobileWorld, a substantially more challenging benchmark designed to better reflect real-world mobile usage, comprising 201 tasks across 20 applications, while maintaining the same level of reproducible evaluation as AndroidWorld. The difficulty of MobileWorld is twofold. First, it emphasizes long-horizon tasks with cross-application interactions: MobileWorld requires nearly twice as many task-completion steps on average (27.8 vs. 14.3) and includes far more multi-application tasks (62.2% vs. 9.5%) compared to AndroidWorld. Second, MobileWorld extends beyond standard GUI manipulation by introducing novel task categories, including agent-user interaction and MCP-augmented tasks. To ensure robust evaluation, we provide snapshot-based container environment and precise functional verifications, including backend database inspection and task callback APIs. We further develop a planner-executor agentic framework with extended action spaces to support user interactions and MCP calls. Our results reveal a sharp performance drop compared to AndroidWorld, with the best agentic framework and end-to-end model achieving 51.7% and 20.9% success rates, respectively. Our analysis shows that current models struggle significantly with user interaction and MCP calls, offering a strategic roadmap toward more robust, next-generation mobile intelligence.

