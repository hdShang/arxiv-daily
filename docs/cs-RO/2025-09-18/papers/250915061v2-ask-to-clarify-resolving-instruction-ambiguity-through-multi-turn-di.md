---
layout: default
title: "Ask-to-Clarify: Resolving Instruction Ambiguity through Multi-turn Dialogue"
---

# Ask-to-Clarify: Resolving Instruction Ambiguity through Multi-turn Dialogue

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15061" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15061v2</a>
  <a href="https://arxiv.org/pdf/2509.15061.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15061v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15061v2', 'Ask-to-Clarify: Resolving Instruction Ambiguity through Multi-turn Dialogue')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xingyao Lin, Xinghao Zhu, Tianyi Lu, Sicheng Xie, Hui Zhang, Xipeng Qiu, Zuxuan Wu, Yu-Gang Jiang

**分类**: cs.RO

**发布日期**: 2025-09-18 (更新: 2025-09-19)

**备注**: 9 pages, 4 figures, 7 tables

---

## 💡 一句话要点

**提出Ask-to-Clarify框架，通过多轮对话解决具身智能体指令模糊问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身智能体` `视觉语言模型` `多轮对话` `指令模糊` `扩散模型`

## 📋 核心要点

1. 现有基于视觉语言动作模型（VLA）的具身智能体通常以单向模式运行，无法处理现实世界中常见的模糊指令。
2. Ask-to-Clarify框架通过多轮对话提问来消除指令歧义，然后生成低级动作，实现智能体与人类的协作。
3. 该框架在8个真实世界任务中表现优于现有VLA，证明了其在解决指令模糊问题上的有效性。

## 📝 摘要（中文）

本文提出Ask-to-Clarify框架，旨在解决具身智能体在执行模糊指令时表现不佳的问题。该框架通过多轮对话提问来消除指令歧义，然后端到端地生成低级动作。Ask-to-Clarify框架包含一个用于协作的视觉语言模型（VLM）和一个用于动作生成的扩散模型，以及一个连接模块，该模块基于VLM的输出为扩散模型生成条件，通过指令调整观察结果以创建可靠的条件。该框架采用两阶段知识隔离策略进行训练：首先，使用歧义解决对话数据微调协作组件以处理歧义；然后，冻结协作组件，同时集成动作组件，微调扩散模型以生成动作。推理时，信号检测器作为路由器，帮助框架在提问和执行动作之间切换。在8个真实世界任务中的评估表明，Ask-to-Clarify框架优于现有的最先进的视觉语言动作模型（VLA），为构建协作式具身智能体提供了一条途径。

## 🔬 方法详解

**问题定义**：现有具身智能体通常被动地执行指令，无法处理指令中存在的模糊性。这导致智能体在真实世界场景中表现不佳，因为人类指令往往是不明确的。因此，如何让智能体主动消除指令歧义，并根据人类反馈调整行为，是本文要解决的核心问题。

**核心思路**：本文的核心思路是让智能体具备“提问澄清”的能力。通过多轮对话，智能体可以主动向人类询问指令中不明确的部分，从而获得更清晰的指导。这种交互式的方式能够显著提高智能体对指令的理解和执行能力。

**技术框架**：Ask-to-Clarify框架包含三个主要模块：1) 协作模块（VLM）：负责与人类进行多轮对话，通过提问来消除指令歧义。2) 动作模块（Diffusion）：负责根据澄清后的指令生成低级动作。3) 连接模块：负责将VLM的输出转换为Diffusion模型的条件，指导动作生成。在训练过程中，采用两阶段知识隔离策略：首先微调VLM，使其具备对话能力；然后冻结VLM，微调Diffusion模型，使其能够根据VLM的输出生成动作。推理时，使用信号检测器判断何时提问，何时执行动作。

**关键创新**：该框架的关键创新在于引入了“提问澄清”机制，使智能体能够主动消除指令歧义。此外，两阶段知识隔离训练策略保证了智能体既能进行有效的对话，又能生成准确的动作。连接模块的设计也至关重要，它确保了VLM的输出能够有效地指导Diffusion模型的动作生成。

**关键设计**：在训练过程中，使用了两阶段知识隔离策略，避免了对话能力和动作生成能力之间的相互干扰。具体来说，第一阶段使用歧义解决对话数据微调VLM，使其具备提问能力。第二阶段，冻结VLM的参数，使用强化学习或模仿学习等方法微调Diffusion模型，使其能够根据VLM的输出生成动作。连接模块的设计需要仔细考虑VLM输出的表示形式，以及如何将其有效地融入Diffusion模型的输入中。信号检测器的设计也需要根据具体任务进行调整，以平衡提问的频率和执行动作的效率。

## 📊 实验亮点

Ask-to-Clarify框架在8个真实世界任务中进行了评估，实验结果表明，该框架显著优于现有的最先进的VLA模型。具体的性能提升数据在论文中给出，证明了该框架在解决指令模糊问题上的有效性，以及其在构建协作式具身智能体方面的潜力。

## 🎯 应用场景

该研究成果可应用于各种需要人机协作的具身智能体场景，例如家庭服务机器人、工业机器人、医疗辅助机器人等。通过让智能体具备提问澄清能力，可以显著提高其在复杂环境中的适应性和可靠性，从而更好地服务于人类。

## 📄 摘要（原文）

> The ultimate goal of embodied agents is to create collaborators that can interact with humans, not mere executors that passively follow instructions. This requires agents to communicate, coordinate, and adapt their actions based on human feedback. Recently, advances in VLAs have offered a path toward this goal. However, most current VLA-based embodied agents operate in a one-way mode: they receive an instruction and execute it without feedback. This approach fails in real-world scenarios where instructions are often ambiguous. In this paper, we address this problem with the Ask-to-Clarify framework. Our framework first resolves ambiguous instructions by asking questions in a multi-turn dialogue. Then it generates low-level actions end-to-end. Specifically, the Ask-to-Clarify framework consists of two components, one VLM for collaboration and one diffusion for action. We also introduce a connection module that generates conditions for the diffusion based on the output of the VLM. This module adjusts the observation by instructions to create reliable conditions. We train our framework with a two-stage knowledge-insulation strategy. First, we fine-tune the collaboration component using ambiguity-solving dialogue data to handle ambiguity. Then, we integrate the action component while freezing the collaboration one. This preserves the interaction abilities while fine-tuning the diffusion to generate actions. The training strategy guarantees our framework can first ask questions, then generate actions. During inference, a signal detector functions as a router that helps our framework switch between asking questions and taking actions. We evaluate the Ask-to-Clarify framework in 8 real-world tasks, where it outperforms existing state-of-the-art VLAs. The results suggest that our proposed framework, along with the training strategy, provides a path toward collaborative embodied agents.

