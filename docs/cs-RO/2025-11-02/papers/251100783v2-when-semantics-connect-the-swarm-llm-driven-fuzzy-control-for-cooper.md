---
layout: default
title: "When Semantics Connect the Swarm: LLM-Driven Fuzzy Control for Cooperative Multi-Robot Underwater Coverage"
---

# When Semantics Connect the Swarm: LLM-Driven Fuzzy Control for Cooperative Multi-Robot Underwater Coverage

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.00783" class="toolbar-btn" target="_blank">📄 arXiv: 2511.00783v2</a>
  <a href="https://arxiv.org/pdf/2511.00783.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.00783v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.00783v2', 'When Semantics Connect the Swarm: LLM-Driven Fuzzy Control for Cooperative Multi-Robot Underwater Coverage')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingzehua Xu, Weihang Zhang, Yangyang Li, Hongmiaoyi Zhang, Guanwen Xie, Jiwei Tang, Shuai Zhang, Yi Li

**分类**: cs.RO, eess.SY

**发布日期**: 2025-11-02 (更新: 2025-11-06)

**备注**: This paper has been submitted to IEEE Transactions on Mobile Computing. Jingzehua Xu, Weihang Zhang, and Yangyang Li contributed equally to this work and are recognized as the co-first authors of the paper

---

## 💡 一句话要点

**提出基于LLM的模糊控制框架，解决水下多机器人协同覆盖问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `水下机器人` `协同覆盖` `大型语言模型` `模糊控制` `语义通信`

## 📋 核心要点

1. 水下多机器人协同覆盖面临感知受限、通信不足、环境复杂和缺乏全局定位等难题。
2. 利用LLM压缩多模态信息为语义token，结合模糊控制生成运动指令，实现无全局定位的可靠导航。
3. 通过语义通信协调多机器人，共享探索意图和局部信息，避免重复探索，提升覆盖效率。

## 📝 摘要（中文）

本文提出了一种语义引导的模糊控制框架，用于解决水下多机器人协同覆盖问题，该问题面临部分可观测性、有限通信、环境不确定性和缺乏全局定位等挑战。该框架将大型语言模型（LLM）与可解释的控制和轻量级协调相结合。LLM将原始多模态观测压缩成紧凑且易于理解的语义token，概括了不确定感知下的障碍物、未探索区域和感兴趣对象（OOI）。然后，具有预定义隶属函数的模糊推理系统将这些token映射为平滑稳定的转向和步态命令，无需全局定位即可实现可靠导航。此外，通过引入语义通信，以语言形式共享意图和局部上下文，协调多个机器人，从而就探索地点达成一致，同时避免冗余访问。在未知礁石环境中的大量仿真表明，在有限的感知和通信条件下，该框架实现了鲁棒的面向OOI导航和协同覆盖，提高了效率和适应性，缩小了语义认知与GPS拒止、无地图条件下的分布式水下控制之间的差距。

## 🔬 方法详解

**问题定义**：水下多机器人协同覆盖任务在缺乏全局定位（GPS拒止环境）和地图信息的情况下，面临着感知不确定性、通信带宽限制以及环境复杂性带来的挑战。现有的方法通常依赖于精确的定位信息或复杂的地图构建，难以适应水下环境的特殊性，导致覆盖效率低下，鲁棒性不足。

**核心思路**：论文的核心思路是将大型语言模型（LLM）的语义理解能力与模糊控制的鲁棒性相结合。LLM用于从多模态传感器数据中提取高层次的语义信息，将复杂的环境感知转化为人类可理解的语义token。模糊控制则利用这些语义token进行决策，生成平滑稳定的运动指令，从而实现无需精确全局定位的自主导航和协同覆盖。

**技术框架**：该框架主要包含三个模块：1) **语义感知模块**：利用LLM将多模态传感器数据（如图像、声呐等）压缩成语义token，描述障碍物、未探索区域和感兴趣对象（OOI）等信息。2) **模糊控制模块**：基于预定义的隶属函数和模糊规则，将语义token映射为转向和步态命令，控制机器人的运动。3) **语义通信模块**：机器人之间通过共享语义token进行通信，协调探索行为，避免重复覆盖。整体流程是，机器人首先进行环境感知，然后通过LLM提取语义信息，再利用模糊控制生成运动指令，最后通过语义通信与其他机器人进行协同。

**关键创新**：该论文的关键创新在于将LLM引入水下机器人控制领域，利用其强大的语义理解能力来处理复杂的水下环境信息。与传统的基于数值计算的方法相比，该方法能够更好地处理感知不确定性，并实现更高效的协同覆盖。此外，语义通信的引入也使得机器人之间的协同更加自然和高效。

**关键设计**：在语义感知模块中，LLM的选择和训练至关重要，需要根据水下环境的特点进行调整。模糊控制模块中的隶属函数和模糊规则需要根据具体的机器人运动学和环境特点进行设计。语义通信模块需要考虑通信带宽的限制，选择合适的语义token表示方法。论文中具体参数设置和网络结构等技术细节未详细描述，属于未知内容。

## 📊 实验亮点

在模拟礁石环境中的实验表明，该框架在有限感知和通信条件下，实现了鲁棒的面向OOI导航和协同覆盖，提高了效率和适应性。具体的性能数据和对比基线未在摘要中给出，属于未知内容。但结论表明，该方法缩小了语义认知与GPS拒止、无地图条件下的分布式水下控制之间的差距。

## 🎯 应用场景

该研究成果可应用于水下环境监测、水下资源勘探、水下搜救等领域。通过提高水下机器人的自主性和协同能力，可以降低人工干预的需求，提高作业效率和安全性。未来，该技术有望应用于更复杂的海洋环境中，例如深海探测和海底维护。

## 📄 摘要（原文）

> Underwater multi-robot cooperative coverage remains challenging due to partial observability, limited communication, environmental uncertainty, and the lack of access to global localization. To address these issues, this paper presents a semantics-guided fuzzy control framework that couples Large Language Models (LLMs) with interpretable control and lightweight coordination. Raw multimodal observations are compressed by the LLM into compact, human-interpretable semantic tokens that summarize obstacles, unexplored regions, and Objects Of Interest (OOIs) under uncertain perception. A fuzzy inference system with pre-defined membership functions then maps these tokens into smooth and stable steering and gait commands, enabling reliable navigation without relying on global positioning. Then, we further coordinate multiple robots by introducing semantic communication that shares intent and local context in linguistic form, enabling agreement on who explores where while avoiding redundant revisits. Extensive simulations in unknown reef-like environments show that, under limited sensing and communication, the proposed framework achieves robust OOI-oriented navigation and cooperative coverage with improved efficiency and adaptability, narrowing the gap between semantic cognition and distributed underwater control in GPS-denied, map-free conditions.

