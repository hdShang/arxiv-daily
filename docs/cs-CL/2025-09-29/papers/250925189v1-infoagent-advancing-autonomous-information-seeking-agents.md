---
layout: default
title: "InfoAgent: Advancing Autonomous Information-Seeking Agents"
---

# InfoAgent: Advancing Autonomous Information-Seeking Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25189" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25189v1</a>
  <a href="https://arxiv.org/pdf/2509.25189.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25189v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25189v1', 'InfoAgent: Advancing Autonomous Information-Seeking Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gongrui Zhang, Jialiang Zhu, Ruiqi Yang, Kai Qiu, Miaosen Zhang, Zhirong Wu, Qi Dai, Bei Liu, Chong Luo, Zhengyuan Yang, Linjie Li, Lijuan Wang, Weizhu Chen, Yuan Zhang, Xin Li, Zhaoyi Liu, Xin Geng, Baining Guo

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-29

---

## 💡 一句话要点

**InfoAgent：通过创新数据合成和自建搜索工具，提升自主信息搜寻Agent能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自主Agent` `信息搜寻` `大型语言模型` `数据合成` `自托管搜索`

## 📋 核心要点

1. 现有LLM Agent依赖商业搜索工具，环境不透明且能力受限，难以应对复杂信息搜寻任务。
2. InfoAgent通过构建实体树和自托管搜索基础设施，系统性地生成高难度问题，并提升Agent环境透明度。
3. InfoAgent在BrowseComp、BrowseComp-ZH和Xbench-DS数据集上显著优于现有开源Agent，验证了数据流程和工具的有效性。

## 📝 摘要（中文）

本文介绍了InfoAgent，一个基于大型语言模型（LLM）的深度研究Agent，它通过创新的数据合成流程和精心设计的网络搜索工具来扩展自身能力。为了构建具有挑战性的、难以找到答案的查询，我们构建了实体树，并应用子树采样和实体模糊化来系统地增加问题的难度。与先前严重依赖商业搜索工具的工作不同，我们开发了一个专用的自托管搜索基础设施，增强了Agent环境的透明度，并促进了Agent能力的进一步发展。我们通过测量正确回答问题所需的平均工具调用次数来评估数据流程的有效性，并表明我们的Agent在配备我们的工具时能产生更好的性能。InfoAgent基于Qwen3-14B进行后训练，采用两阶段方法：冷启动监督微调以灌输长程搜索行为，然后进行强化学习，显著提高推理驱动的工具使用能力。通过我们的方法，InfoAgent在BrowseComp上达到15.3%的准确率，在BrowseComp-ZH上达到29.2%的准确率，在Xbench-DS上达到40.4%的准确率，优于先前的开源深度研究Agent，如WebSailor-72B和DeepDive-32B。

## 🔬 方法详解

**问题定义**：论文旨在解决现有大型语言模型Agent在复杂信息搜寻任务中的不足。现有方法通常依赖于商业搜索工具，这导致Agent环境的不透明性，并且Agent的能力受到商业工具的限制。此外，构建具有挑战性的、难以找到答案的查询也是一个难题。

**核心思路**：InfoAgent的核心思路是通过创新的数据合成流程和自建的搜索基础设施来增强Agent的能力。通过构建实体树和应用子树采样与实体模糊化，可以系统性地生成高难度问题，从而训练Agent更好地处理复杂查询。自建搜索基础设施可以提高Agent环境的透明度，并允许针对特定任务进行优化。

**技术框架**：InfoAgent的整体框架包括数据合成流程、自托管搜索基础设施和Agent训练流程。数据合成流程负责生成具有挑战性的查询。自托管搜索基础设施提供透明且可控的搜索环境。Agent训练流程包括冷启动监督微调和强化学习两个阶段。冷启动监督微调用于灌输长程搜索行为，强化学习用于提高推理驱动的工具使用能力。

**关键创新**：InfoAgent的关键创新在于数据合成流程和自托管搜索基础设施。数据合成流程能够系统性地生成高难度问题，这与以往依赖人工标注或简单规则生成问题的方法不同。自托管搜索基础设施提供了透明且可控的搜索环境，这与以往依赖商业搜索工具的方法不同。

**关键设计**：在数据合成流程中，实体树的构建和子树采样是关键设计。实体树用于表示实体之间的关系，子树采样用于生成不同的查询。在Agent训练流程中，冷启动监督微调和强化学习的结合是关键设计。冷启动监督微调使用Qwen3-14B进行初始化，强化学习使用特定的奖励函数来鼓励Agent进行有效的工具使用。具体的参数设置和损失函数细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

InfoAgent在BrowseComp上达到15.3%的准确率，在BrowseComp-ZH上达到29.2%的准确率，在Xbench-DS上达到40.4%的准确率。这些结果显著优于先前的开源深度研究Agent，如WebSailor-72B和DeepDive-32B，证明了InfoAgent的有效性。

## 🎯 应用场景

InfoAgent可应用于自动化研究、智能客服、知识图谱构建等领域。它能够帮助用户高效地获取和整合信息，解决复杂问题。未来，InfoAgent有望成为科研人员和决策者的强大助手，加速知识发现和创新。

## 📄 摘要（原文）

> Building Large Language Model agents that expand their capabilities by interacting with external tools represents a new frontier in AI research and applications. In this paper, we introduce InfoAgent, a deep research agent powered by an innovative data synthesis pipeline and orchestrated web search tools. To construct challenging, hard-to-find queries,we build entity trees and apply sub-tree sampling with entity fuzzification to systematically increase question difficulty. Unlike prior work that relies heavily on commercial search tools, we develop a dedicated self-hosted search infrastructure, enhancing transparency of agent environments and facilitating further advancement of agent capacity. We evaluate the effectiveness of our data pipeline by measuring the average number of tool calls required to correctly answer a question, and also show that our agent yields better performance when equipped with our tools. Our \mbox{InfoAgent} is post-trained from Qwen3-14B using a two-stage recipe: cold-start supervised finetuning to instill long-horizon search behaviors, followed by reinforcement learning which significantly improves reasoning-driven tool use. With our methods, InfoAgent achieves 15.3\% accuracy on BrowseComp, 29.2\% on BrowseComp-ZH, and 40.4\% on Xbench-DS, outperforming prior open-source deep research agents such as WebSailor-72B and DeepDive-32B.

