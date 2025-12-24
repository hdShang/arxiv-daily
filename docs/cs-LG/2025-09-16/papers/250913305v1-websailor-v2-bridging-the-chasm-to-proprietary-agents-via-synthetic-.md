---
layout: default
title: "WebSailor-V2: Bridging the Chasm to Proprietary Agents via Synthetic Data and Scalable Reinforcement Learning"
---

# WebSailor-V2: Bridging the Chasm to Proprietary Agents via Synthetic Data and Scalable Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13305" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13305v1</a>
  <a href="https://arxiv.org/pdf/2509.13305.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13305v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13305v1', 'WebSailor-V2: Bridging the Chasm to Proprietary Agents via Synthetic Data and Scalable Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kuan Li, Zhongwang Zhang, Huifeng Yin, Rui Ye, Yida Zhao, Liwen Zhang, Litu Ou, Dingchu Zhang, Xixi Wu, Jialong Wu, Xinyu Wang, Zile Qiao, Zhen Zhang, Yong Jiang, Pengjun Xie, Fei Huang, Jingren Zhou

**分类**: cs.LG, cs.CL

**发布日期**: 2025-09-16

**备注**: https://tongyi-agent.github.io/blog/introducing-tongyi-deep-research/

---

## 💡 一句话要点

**WebSailor-V2：通过合成数据和可扩展强化学习弥合专有Agent的差距**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `信息搜索` `强化学习` `Agent` `合成数据` `不确定性推理`

## 📋 核心要点

1. 现有开源模型在复杂信息搜索任务中表现不足，缺乏有效降低不确定性的推理能力。
2. WebSailor通过生成高不确定性任务、RFT冷启动和DUPO算法，提升Agent在复杂环境下的推理能力。
3. 实验表明，WebSailor在复杂信息搜索任务中性能与专有Agent相当，显著优于开源Agent。

## 📝 摘要（中文）

超越人类认知局限性是LLM训练的关键前沿。诸如DeepResearch之类的专有Agent系统已在BrowseComp等极其复杂的信息搜索基准上展示了超人的能力，这是以前无法实现的壮举。我们认为，它们的成功取决于开源模型中缺乏的复杂推理模式：在导航广阔的信息环境时系统地降低极端不确定性的能力。基于此，我们引入了WebSailor，这是一种完整的后训练方法，旨在灌输这种关键能力。我们的方法包括通过结构化采样和信息混淆生成新颖的、高不确定性的任务，RFT冷启动，以及一种高效的Agent强化学习训练算法，即重复采样策略优化（DUPO）。通过这种集成管道，WebSailor在复杂的信息搜索任务中显著优于所有开源Agent，与专有Agent的性能相匹配，并缩小了能力差距。

## 🔬 方法详解

**问题定义**：论文旨在解决开源Agent在复杂信息搜索任务中表现不佳的问题。现有开源模型缺乏有效降低不确定性的推理能力，难以应对信息量大、干扰因素多的环境。专有Agent如DeepResearch在BrowseComp等基准测试中表现出超人能力，但其技术细节未公开，开源社区难以复现。

**核心思路**：论文的核心思路是通过后训练（post-training）的方式，使开源Agent具备类似专有Agent的复杂推理能力。具体而言，通过精心设计的合成数据和强化学习算法，让Agent学习如何在信息不确定性极高的环境中进行有效探索和决策，从而提升其信息搜索能力。

**技术框架**：WebSailor的整体框架包含三个主要阶段：1) **高不确定性任务生成**：通过结构化采样和信息混淆技术，生成具有挑战性的信息搜索任务。2) **RFT冷启动**：利用Reasoning from Task (RFT) 方法进行冷启动，为Agent提供初步的推理能力。3) **DUPO强化学习训练**：采用Duplicating Sampling Policy Optimization (DUPO) 算法进行强化学习训练，提升Agent的策略优化能力。

**关键创新**：论文的关键创新在于提出了一种完整的后训练方法，能够有效提升开源Agent在复杂信息搜索任务中的性能。DUPO算法是另一个创新点，它是一种高效的Agent强化学习训练算法，能够加速Agent的学习过程并提升其性能。此外，高不确定性任务生成方法也为Agent提供了更具挑战性的训练环境。

**关键设计**：在任务生成方面，论文采用了结构化采样和信息混淆技术，以确保生成的任务具有足够的不确定性和挑战性。在DUPO算法方面，论文可能涉及对策略梯度算法的改进，例如引入了重复采样机制，以提高样本利用率和训练效率。具体的损失函数和网络结构等技术细节在论文中应该有更详细的描述（未知）。

## 📊 实验亮点

WebSailor在复杂信息搜索任务中显著优于所有开源Agent，与专有Agent的性能相匹配，缩小了能力差距。具体性能数据和对比基线需要在论文中查找（未知），但摘要明确指出WebSailor达到了与专有Agent相当的水平，这是一个重要的突破。

## 🎯 应用场景

该研究成果可应用于智能客服、知识图谱构建、舆情分析、金融风险评估等领域。通过提升Agent的信息搜索和推理能力，可以帮助用户更高效地获取所需信息，并做出更明智的决策。未来，该技术有望应用于更广泛的领域，例如自动驾驶、医疗诊断等。

## 📄 摘要（原文）

> Transcending human cognitive limitations represents a critical frontier in LLM training. Proprietary agentic systems like DeepResearch have demonstrated superhuman capabilities on extremely complex information-seeking benchmarks such as BrowseComp, a feat previously unattainable. We posit that their success hinges on a sophisticated reasoning pattern absent in open-source models: the ability to systematically reduce extreme uncertainty when navigating vast information landscapes. Based on this insight, we introduce WebSailor, a complete post-training methodology designed to instill this crucial capability. Our approach involves generating novel, high-uncertainty tasks through structured sampling and information obfuscation, RFT cold start, and an efficient agentic RL training algorithm, Duplicating Sampling Policy Optimization (DUPO). With this integrated pipeline, WebSailor significantly outperforms all open-source agents in complex information-seeking tasks, matching proprietary agents' performance and closing the capability gap.

