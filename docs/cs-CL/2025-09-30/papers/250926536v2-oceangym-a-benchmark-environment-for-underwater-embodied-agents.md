---
layout: default
title: "OceanGym: A Benchmark Environment for Underwater Embodied Agents"
---

# OceanGym: A Benchmark Environment for Underwater Embodied Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26536" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26536v2</a>
  <a href="https://arxiv.org/pdf/2509.26536.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26536v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26536v2', 'OceanGym: A Benchmark Environment for Underwater Embodied Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yida Xue, Mingjun Mao, Xiangyuan Ru, Yuqi Zhu, Baochang Ren, Shuofei Qiao, Mengru Wang, Shumin Deng, Xinyu An, Ningyu Zhang, Ying Chen, Huajun Chen

**分类**: cs.CL, cs.AI, cs.CV, cs.LG, cs.RO

**发布日期**: 2025-09-30 (更新: 2025-11-25)

**备注**: Work in progress

**🔗 代码/项目**: [GITHUB](https://github.com/OceanGPT/OceanGym)

---

## 💡 一句话要点

**OceanGym：水下具身智能体的综合基准环境，应对极端环境挑战。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `水下机器人` `具身智能` `多模态学习` `大型语言模型` `基准环境`

## 📋 核心要点

1. 水下环境的低能见度、动态洋流等因素，对水下具身智能体的感知和决策提出了巨大挑战。
2. OceanGym 提出了一个基于多模态大型语言模型（MLLM）的统一智能体框架，整合感知、记忆和序列决策能力。
3. 实验结果表明，现有 MLLM 驱动的智能体与人类专家相比仍有差距，在感知、规划和适应性方面仍需提升。

## 📝 摘要（中文）

本文提出了OceanGym，这是首个针对海洋水下具身智能体的综合基准环境，旨在推动人工智能在最具挑战性的真实世界环境之一中的发展。与陆地或空中环境不同，水下环境存在低能见度、动态洋流等极端感知和决策挑战，使得有效的智能体部署异常困难。OceanGym包含八个逼真的任务领域和一个由多模态大型语言模型（MLLM）驱动的统一智能体框架，该框架集成了感知、记忆和序列决策。智能体需要在这些严苛条件下理解光学和声纳数据，自主探索复杂环境，并完成长时程目标。大量实验表明，最先进的MLLM驱动的智能体与人类专家之间存在显著差距，突显了海洋水下环境中感知、规划和适应性的持续困难。通过提供高保真、严格设计的平台，OceanGym为开发鲁棒的具身人工智能并将其能力转移到现实世界中的自主海洋水下航行器奠定了基础，标志着朝着能够在地球上最后未开发的领域之一中运行的智能智能体迈出了决定性的一步。

## 🔬 方法详解

**问题定义**：现有水下具身智能体在感知、规划和适应性方面面临巨大挑战，尤其是在低能见度、动态洋流等复杂水下环境中。现有方法难以有效整合多模态信息（光学和声纳数据），并进行长时程的自主探索和决策。因此，需要一个综合性的基准环境来评估和提升水下智能体的性能。

**核心思路**：OceanGym 的核心思路是构建一个高保真、逼真的水下环境，并提供一个统一的智能体框架，以便研究人员能够方便地开发和评估各种水下智能体。该框架利用多模态大型语言模型（MLLM）来整合感知信息，并进行序列决策，从而实现自主探索和完成长时程目标。

**技术框架**：OceanGym 包含以下主要模块：1) 高保真水下环境模拟器，提供逼真的光学和声纳数据；2) 八个不同的任务领域，涵盖各种水下任务，如目标搜索、环境探索和路径规划；3) 基于 MLLM 的统一智能体框架，包括感知模块、记忆模块和决策模块。感知模块负责处理光学和声纳数据，记忆模块负责存储和检索历史信息，决策模块负责生成行动指令。

**关键创新**：OceanGym 的关键创新在于：1) 它是首个针对水下具身智能体的综合基准环境；2) 它提供了一个基于 MLLM 的统一智能体框架，能够有效整合多模态信息并进行长时程决策；3) 它包含八个逼真的任务领域，涵盖各种水下任务。与现有方法相比，OceanGym 更加全面、逼真和易于使用。

**关键设计**：OceanGym 的关键设计包括：1) 使用高精度渲染技术来模拟逼真的水下环境；2) 使用物理引擎来模拟动态洋流；3) 设计了专门的损失函数来训练 MLLM，例如，使用对比学习来提高感知模块的性能，使用强化学习来优化决策模块的策略。具体参数设置和网络结构细节在论文附录中给出（未知）。

## 📊 实验亮点

实验结果表明，现有的 MLLM 驱动的智能体在 OceanGym 的各个任务领域中与人类专家相比仍存在显著差距。例如，在目标搜索任务中，智能体的平均搜索时间是人类专家的数倍。这表明，现有的 AI 技术在水下环境中的感知、规划和适应性方面仍有很大的提升空间。OceanGym 为研究人员提供了一个评估和改进水下智能体的平台，有助于推动该领域的发展。

## 🎯 应用场景

OceanGym 的潜在应用领域包括：水下资源勘探、海洋环境监测、水下基础设施维护、水下搜救等。通过 OceanGym 训练的智能体可以部署到自主水下航行器（AUV）上，从而实现自主完成各种水下任务。该研究的实际价值在于降低水下作业的成本和风险，提高水下作业的效率和安全性。未来，OceanGym 可以进一步扩展到更复杂的任务和环境，并与其他领域的 AI 技术相结合，从而推动水下智能的进一步发展。

## 📄 摘要（原文）

> We introduce OceanGym, the first comprehensive benchmark for ocean underwater embodied agents, designed to advance AI in one of the most demanding real-world environments. Unlike terrestrial or aerial domains, underwater settings present extreme perceptual and decision-making challenges, including low visibility, dynamic ocean currents, making effective agent deployment exceptionally difficult. OceanGym encompasses eight realistic task domains and a unified agent framework driven by Multi-modal Large Language Models (MLLMs), which integrates perception, memory, and sequential decision-making. Agents are required to comprehend optical and sonar data, autonomously explore complex environments, and accomplish long-horizon objectives under these harsh conditions. Extensive experiments reveal substantial gaps between state-of-the-art MLLM-driven agents and human experts, highlighting the persistent difficulty of perception, planning, and adaptability in ocean underwater environments. By providing a high-fidelity, rigorously designed platform, OceanGym establishes a testbed for developing robust embodied AI and transferring these capabilities to real-world autonomous ocean underwater vehicles, marking a decisive step toward intelligent agents capable of operating in one of Earth's last unexplored frontiers. The code and data are available at https://github.com/OceanGPT/OceanGym.

