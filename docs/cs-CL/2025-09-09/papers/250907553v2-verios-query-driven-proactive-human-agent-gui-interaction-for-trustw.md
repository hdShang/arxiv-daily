---
layout: default
title: "VeriOS: Query-Driven Proactive Human-Agent-GUI Interaction for Trustworthy OS Agents"
---

# VeriOS: Query-Driven Proactive Human-Agent-GUI Interaction for Trustworthy OS Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07553" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07553v2</a>
  <a href="https://arxiv.org/pdf/2509.07553.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07553v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07553v2', 'VeriOS: Query-Driven Proactive Human-Agent-GUI Interaction for Trustworthy OS Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zheng Wu, Heyuan Huang, Xingyu Lou, Xiangmou Qu, Pengzhou Cheng, Zongru Wu, Weiwen Liu, Weinan Zhang, Jun Wang, Zhaoxiang Wang, Zhuosheng Zhang

**分类**: cs.CL

**发布日期**: 2025-09-09 (更新: 2025-09-17)

**🔗 代码/项目**: [GITHUB](https://github.com/Wuzheng02/VeriOS)

---

## 💡 一句话要点

**提出VeriOS，通过查询驱动的人机交互提升OS Agent在不可信环境下的可靠性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `操作系统代理` `人机交互` `可信赖AI` `查询驱动` `多模态学习` `GUI自动化` `两阶段学习`

## 📋 核心要点

1. 现有OS Agent在理想环境下表现良好，但在真实不可信环境下容易过度执行，存在安全风险。
2. VeriOS提出查询驱动的人机交互框架，使Agent能在不确定时主动向人类请求帮助，避免错误操作。
3. 实验表明，VeriOS在不可信场景下成功率显著提升，同时保持了正常环境下的性能，具有良好的泛化性。

## 📝 摘要（中文）

随着多模态大语言模型的快速发展，操作系统(OS)代理越来越有能力通过设备上的图形用户界面(GUI)自动执行任务。然而，现有的大多数OS代理都是为理想化环境设计的，而真实世界的环境往往存在不可信的情况。为了降低在这种场景下过度执行的风险，我们提出了一个查询驱动的人机GUI交互框架，使OS代理能够决定何时向人类查询，以更可靠地完成任务。基于此框架，我们引入了VeriOS-Agent，这是一个值得信赖的OS代理，它采用两阶段学习范式进行训练，从而促进元知识的解耦和利用。具体而言，VeriOS-Agent在正常情况下自主执行操作，而在不可信的情况下主动查询人类。实验表明，在不可信场景下，VeriOS-Agent的平均步进成功率比最先进的方法提高了20.64%，且不影响正常性能。分析突出了VeriOS-Agent的合理性、泛化性和可扩展性。代码、数据集和模型可在https://github.com/Wuzheng02/VeriOS获取。

## 🔬 方法详解

**问题定义**：现有OS Agent主要针对理想化的环境设计，缺乏在真实、不可信环境下处理复杂情况的能力。当Agent遇到不确定性或潜在风险时，容易做出错误的决策并执行，导致任务失败甚至产生负面影响。因此，如何提升OS Agent在不可信环境下的可靠性和安全性是一个关键问题。

**核心思路**：VeriOS的核心思路是引入人机交互，让Agent在遇到不确定或风险较高的情境时，主动向人类用户请求指导。通过人类的介入，可以有效避免Agent在信息不足或判断失误的情况下做出错误决策，从而提高任务完成的可靠性。这种查询驱动的交互方式使得Agent能够根据环境的信任程度动态调整其自主性和依赖性。

**技术框架**：VeriOS框架包含以下几个主要模块：1) 环境感知模块，用于识别当前环境的信任程度；2) 决策模块，根据环境信任程度决定是否需要向人类查询；3) 人机交互模块，负责向人类用户提出问题并获取反馈；4) 动作执行模块，根据决策结果执行相应的动作。整个流程是Agent首先感知环境，然后根据信任程度决定是否查询人类，最后根据人类的反馈执行动作。

**关键创新**：VeriOS的关键创新在于其查询驱动的人机交互机制。与传统的Agent自主执行模式不同，VeriOS允许Agent在不确定时主动寻求人类的帮助，从而提高了Agent的可靠性和安全性。此外，VeriOS采用两阶段学习范式，解耦了元知识的学习和利用，使得Agent能够更好地泛化到新的环境。

**关键设计**：VeriOS-Agent采用两阶段学习范式。第一阶段，Agent学习如何识别不可信场景并生成合适的查询问题。第二阶段，Agent学习如何根据人类的反馈执行动作。具体的损失函数设计包括用于训练环境感知模块的分类损失和用于训练动作执行模块的强化学习损失。网络结构方面，采用了多模态Transformer模型来处理GUI界面信息和自然语言输入。

## 📊 实验亮点

实验结果表明，VeriOS-Agent在不可信场景下的平均步进成功率比最先进的方法提高了20.64%，证明了其在复杂环境下的优越性能。同时，VeriOS-Agent在正常环境下的性能没有受到影响，表明其具有良好的泛化能力。此外，实验还验证了VeriOS-Agent的合理性、通用性和可扩展性。

## 🎯 应用场景

VeriOS具有广泛的应用前景，可应用于智能家居、智能办公、自动驾驶等领域。通过引入人机交互，可以显著提升Agent在复杂、不确定环境下的可靠性和安全性，降低潜在风险。未来，VeriOS有望成为构建可信赖OS Agent的重要技术手段，推动人机协作的智能化发展。

## 📄 摘要（原文）

> With the rapid progress of multimodal large language models, operating system (OS) agents become increasingly capable of automating tasks through on-device graphical user interfaces (GUIs). However, most existing OS agents are designed for idealized settings, whereas real-world environments often present untrustworthy conditions. To mitigate risks of over-execution in such scenarios, we propose a query-driven human-agent-GUI interaction framework that enables OS agents to decide when to query humans for more reliable task completion. Built upon this framework, we introduce VeriOS-Agent, a trustworthy OS agent trained with a two-stage learning paradigm that falicitate the decoupling and utilization of meta-knowledge. Concretely, VeriOS-Agent autonomously executes actions in normal conditions while proactively querying humans in untrustworthy scenarios. Experiments show that VeriOS-Agent improves the average step-wise success rate by 20.64\% in untrustworthy scenarios over the state-of-the-art, without compromising normal performance. Analysis highlights VeriOS-Agent's rationality, generalizability, and scalability. The codes, datasets and models are available at https://github.com/Wuzheng02/VeriOS.

