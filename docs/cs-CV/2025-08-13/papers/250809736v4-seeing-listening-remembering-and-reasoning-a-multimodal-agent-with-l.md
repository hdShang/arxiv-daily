---
layout: default
title: "Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory"
---

# Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09736" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09736v4</a>
  <a href="https://arxiv.org/pdf/2508.09736.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09736v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09736v4', 'Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lin Long, Yichen He, Wentao Ye, Yiyuan Pan, Yuan Lin, Hang Li, Junbo Zhao, Wei Li

**分类**: cs.CV

**发布日期**: 2025-08-13 (更新: 2025-10-09)

**🔗 代码/项目**: [GITHUB](https://github.com/bytedance-seed/m3-agent)

---

## 💡 一句话要点

**提出M3-Agent以解决多模态智能体的长期记忆问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态智能体` `长期记忆` `推理能力` `视觉听觉融合` `强化学习` `长视频问答` `机器人技术`

## 📋 核心要点

1. 现有多模态智能体在长期记忆和推理能力方面存在不足，难以有效处理复杂任务。
2. M3-Agent通过实时处理视觉和听觉输入，构建多模态的长期记忆，支持自主推理和任务完成。
3. 实验结果显示，M3-Agent在M3-Bench基准上分别比基线提高了6.7%、7.7%和5.3%的准确率，验证了其有效性。

## 📝 摘要（中文）

我们介绍了M3-Agent，一个新颖的多模态智能体框架，具备长期记忆功能。M3-Agent能够处理实时的视觉和听觉输入，构建和更新情节记忆和语义记忆，逐步积累世界知识。其记忆以实体为中心，以多模态方式组织，从而实现对环境的更深刻和一致的理解。在接收到指令后，M3-Agent能够自主进行多轮推理，并检索相关记忆以完成任务。为评估多模态智能体的记忆有效性和基于记忆的推理能力，我们开发了M3-Bench，一个包含100个新录制的机器人视角视频和920个多样化网络来源视频的长视频问答基准。实验结果表明，经过强化学习训练的M3-Agent在多个基准上超越了最强基线，显示出显著的性能提升。

## 🔬 方法详解

**问题定义**：本论文旨在解决多模态智能体在长期记忆和推理能力方面的不足，现有方法难以有效整合多种输入并进行复杂推理。

**核心思路**：M3-Agent通过构建实体中心的多模态记忆，模拟人类的记忆机制，能够实时更新和检索信息，从而提升智能体的任务执行能力。

**技术框架**：M3-Agent的整体架构包括输入处理模块、记忆管理模块和推理模块。输入处理模块负责接收视觉和听觉信息，记忆管理模块用于存储和更新记忆，而推理模块则执行任务相关的推理过程。

**关键创新**：M3-Agent的主要创新在于其多模态记忆的组织方式和自主推理能力，这与传统的单一模态或静态记忆方法有本质区别。

**关键设计**：在模型设计中，采用了强化学习训练策略，优化了损失函数以平衡记忆更新和任务执行的效率，同时在网络结构上实现了多模态信息的融合。

## 📊 实验亮点

实验结果表明，M3-Agent在M3-Bench-robot、M3-Bench-web和VideoMME-long基准上分别比最强基线提高了6.7%、7.7%和5.3%的准确率，显示出其在多模态记忆和推理方面的显著优势。

## 🎯 应用场景

M3-Agent的研究成果在多个领域具有广泛的应用潜力，包括智能家居、机器人助手和教育领域等。通过更好地理解和处理多模态信息，M3-Agent能够提供更自然的人机交互体验，推动智能体向更高层次的智能发展。

## 📄 摘要（原文）

> We introduce M3-Agent, a novel multimodal agent framework equipped with long-term memory. Like humans, M3-Agent can process real-time visual and auditory inputs to build and update episodic and semantic memories, gradually accumulating world knowledge. Its memory is organized in an entity-centric, multimodal manner, enabling deeper and more consistent understanding of the environment. Given an instruction, M3-Agent autonomously performs multi-turn reasoning and retrieves relevant memories to complete tasks. To evaluate memory effectiveness and memory-based reasoning in multimodal agents, we develop M3-Bench, a long-video question answering benchmark comprising 100 newly recorded robot-perspective videos (M3-Bench-robot) and 920 diverse web-sourced videos (M3-Bench-web). We annotate QA pairs designed to test capabilities essential for agent applications, such as person understanding, general knowledge extraction, and cross-modal reasoning. Experimental results show that M3-Agent, trained via reinforcement learning, outperforms the strongest baseline, a prompting agent using Gemini-1.5-pro and GPT-4o, achieving 6.7%, 7.7%, and 5.3% higher accuracy on M3-Bench-robot, M3-Bench-web and VideoMME-long, respectively. Our work advances multimodal agents toward more human-like long-term memory and provides insights for their practical design. Model, code and data are available at https://github.com/bytedance-seed/m3-agent.

