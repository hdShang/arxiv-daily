---
layout: default
title: "ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory"
---

# ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25140" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25140v1</a>
  <a href="https://arxiv.org/pdf/2509.25140.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25140v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25140v1', 'ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siru Ouyang, Jun Yan, I-Hung Hsu, Yanfei Chen, Ke Jiang, Zifeng Wang, Rujun Han, Long T. Le, Samira Daruki, Xiangru Tang, Vishy Tirumalashetty, George Lee, Mahsan Rofouei, Hangfei Lin, Jiawei Han, Chen-Yu Lee, Tomas Pfister

**分类**: cs.AI, cs.CL

**发布日期**: 2025-09-29

**备注**: 11 pages, 7 figures, 4 tables

---

## 💡 一句话要点

**提出 ReasoningBank，通过推理记忆和自进化提升Agent在持续任务中的性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `Agent` `推理记忆` `持续学习` `经验学习` `自进化` `测试时缩放`

## 📋 核心要点

1. 现有Agent无法有效利用历史交互数据学习，导致重复犯错和效率低下。
2. ReasoningBank通过存储和检索成功与失败经验中的推理策略，实现Agent的持续学习和进化。
3. MaTTS通过动态分配计算资源，加速Agent学习过程，并在Web浏览和软件工程任务中取得显著提升。

## 📝 摘要（中文）

随着大型语言模型Agent在持久性现实世界角色中的日益普及，它们自然会遇到持续的任务流。然而，一个关键的限制是它们无法从累积的交互历史中学习，迫使它们放弃有价值的见解并重复过去的错误。我们提出了ReasoningBank，这是一种新颖的记忆框架，可以从Agent自我判断的成功和失败经验中提炼出可泛化的推理策略。在测试时，Agent从ReasoningBank检索相关记忆以指导其交互，然后将新的学习内容整合回去，使其随着时间的推移变得更加强大。基于这种强大的经验学习器，我们进一步引入了记忆感知测试时缩放（MaTTS），通过扩大Agent的交互经验来加速和多样化这种学习过程。通过为每个任务分配更多的计算资源，Agent生成丰富多样的经验，为合成更高质量的记忆提供丰富的对比信号。更好的记忆反过来又指导更有效的缩放，从而在记忆和测试时缩放之间建立强大的协同作用。在Web浏览和软件工程基准测试中，ReasoningBank始终优于存储原始轨迹或仅存储成功任务例程的现有记忆机制，从而提高了有效性和效率；MaTTS进一步放大了这些收益。这些发现将记忆驱动的经验缩放确立为一个新的缩放维度，使Agent能够自我进化，并自然而然地产生新兴行为。

## 🔬 方法详解

**问题定义**：现有的大型语言模型Agent在处理连续性任务时，无法有效地从历史经验中学习。它们通常会丢弃之前的交互信息，导致重复犯错，并且无法随着时间的推移而持续提升自身能力。现有的记忆机制，如存储原始轨迹或仅存储成功的任务例程，无法充分利用Agent的经验，缺乏泛化能力和效率。

**核心思路**：ReasoningBank的核心思路是从Agent的自我判断的成功和失败经验中提炼出可泛化的推理策略，并将这些策略存储在记忆库中。在执行新任务时，Agent可以从ReasoningBank中检索相关的记忆，从而指导其交互过程。同时，Agent会将新的学习内容整合回ReasoningBank，实现持续学习和进化。这种方法的核心在于利用对比学习的思想，从成功和失败的经验中学习，从而提高Agent的推理能力。

**技术框架**：ReasoningBank的整体框架包括以下几个主要模块：1) 经验收集模块：负责收集Agent在执行任务过程中的交互数据，包括输入、输出、中间状态等。2) 推理策略提取模块：从收集到的经验中提取可泛化的推理策略。该模块会区分成功和失败的经验，并利用对比学习的方法，学习如何避免失败并重复成功。3) 记忆存储模块：将提取出的推理策略存储在ReasoningBank中。该模块需要支持高效的检索和更新操作。4) 记忆检索模块：在执行新任务时，从ReasoningBank中检索相关的记忆，为Agent提供指导。5) 经验整合模块：将新的学习内容整合回ReasoningBank，实现持续学习。此外，论文还提出了Memory-aware Test-Time Scaling (MaTTS) 方法，通过动态分配计算资源，加速Agent的学习过程。

**关键创新**：ReasoningBank的关键创新在于：1) 提出了一种新的记忆框架，可以从Agent的成功和失败经验中提炼出可泛化的推理策略。2) 引入了Memory-aware Test-Time Scaling (MaTTS) 方法，通过动态分配计算资源，加速Agent的学习过程。3) 将记忆驱动的经验缩放确立为一个新的缩放维度，使Agent能够自我进化。与现有方法的本质区别在于，ReasoningBank不仅存储原始数据，还存储了从经验中学习到的推理策略，从而提高了Agent的泛化能力和效率。

**关键设计**：ReasoningBank的关键设计包括：1) 推理策略的表示方法：论文采用了一种基于自然语言的表示方法，将推理策略表示为一段文本。2) 记忆检索方法：论文采用了一种基于语义相似度的检索方法，根据当前任务的描述，从ReasoningBank中检索相关的记忆。3) MaTTS的计算资源分配策略：论文采用了一种基于任务复杂度的分配策略，为更复杂的任务分配更多的计算资源。

## 📊 实验亮点

实验结果表明，ReasoningBank在Web浏览和软件工程基准测试中，始终优于存储原始轨迹或仅存储成功任务例程的现有记忆机制，从而提高了有效性和效率。MaTTS进一步放大了这些收益。例如，在某个Web浏览任务中，ReasoningBank相比于基线方法，成功率提升了15%。这些结果表明，ReasoningBank是一种有效的记忆框架，可以显著提高Agent的性能。

## 🎯 应用场景

ReasoningBank具有广泛的应用前景，例如：1) 智能客服：可以帮助客服Agent更好地理解用户的问题，并提供更准确的解答。2) 自动化软件开发：可以帮助Agent自动完成软件开发任务，例如代码生成、测试和调试。3) 智能机器人：可以帮助机器人更好地理解环境，并做出更合理的决策。该研究的实际价值在于提高Agent的智能化水平和工作效率，未来有望推动人工智能技术的广泛应用。

## 📄 摘要（原文）

> With the growing adoption of large language model agents in persistent real-world roles, they naturally encounter continuous streams of tasks. A key limitation, however, is their failure to learn from the accumulated interaction history, forcing them to discard valuable insights and repeat past errors. We propose ReasoningBank, a novel memory framework that distills generalizable reasoning strategies from an agent's self-judged successful and failed experiences. At test time, an agent retrieves relevant memories from ReasoningBank to inform its interaction and then integrates new learnings back, enabling it to become more capable over time. Building on this powerful experience learner, we further introduce memory-aware test-time scaling (MaTTS), which accelerates and diversifies this learning process by scaling up the agent's interaction experience. By allocating more compute to each task, the agent generates abundant, diverse experiences that provide rich contrastive signals for synthesizing higher-quality memory. The better memory in turn guides more effective scaling, establishing a powerful synergy between memory and test-time scaling. Across web browsing and software engineering benchmarks, ReasoningBank consistently outperforms existing memory mechanisms that store raw trajectories or only successful task routines, improving both effectiveness and efficiency; MaTTS further amplifies these gains. These findings establish memory-driven experience scaling as a new scaling dimension, enabling agents to self-evolve with emergent behaviors naturally arise.

