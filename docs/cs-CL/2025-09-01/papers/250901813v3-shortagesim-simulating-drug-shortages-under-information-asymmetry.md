---
layout: default
title: "ShortageSim: Simulating Drug Shortages under Information Asymmetry"
---

# ShortageSim: Simulating Drug Shortages under Information Asymmetry

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01813" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01813v3</a>
  <a href="https://arxiv.org/pdf/2509.01813.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01813v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01813v3', 'ShortageSim: Simulating Drug Shortages under Information Asymmetry')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingxuan Cui, Yilan Jiang, Duo Zhou, Cheng Qian, Yuji Zhang, Qiong Wang

**分类**: cs.MA, cs.CL, cs.GT

**发布日期**: 2025-09-01 (更新: 2025-11-25)

**备注**: Accepted by AAAI 2026. Oral presentation. 25 pages

---

## 💡 一句话要点

**ShortageSim：首个信息不对称下药品短缺监管干预的模拟框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `药品短缺` `信息不对称` `供应链模拟` `大型语言模型` `智能体建模`

## 📋 核心要点

1. 现有方法难以有效评估药品短缺监管干预，主要挑战在于医药供应链中普遍存在信息不对称。
2. ShortageSim利用LLM智能体模拟制造商和买家的决策，考虑了对监管公告的异构解读，更贴近真实场景。
3. 实验表明，ShortageSim能显著减少生产中断的解决延迟，并开源了包含大量FDA短缺事件的数据集。

## 📝 摘要（中文）

药品短缺对全球患者护理和医疗系统构成严重风险，但由于医药供应链中存在信息不对称，监管干预的有效性仍不清楚。我们提出了ShortageSim，这是第一个模拟框架，旨在评估信息不对称下监管干预对竞争动态的影响。该框架使用基于大型语言模型（LLM）的智能体，模拟药品制造商和机构买家对监管机构发布的短缺警报做出的战略决策。与假设完全理性和完全信息的传统博弈论模型不同，ShortageSim模拟了对监管公告的异构解读以及由此产生的决策。在自行处理的历史短缺事件数据集上的实验表明，ShortageSim将生产中断案例的解决延迟减少了高达84％，比零样本基线更接近真实世界的轨迹。我们的框架证实了监管警报在解决短缺问题中的作用，并引入了一种新的方法来理解不确定性下多阶段环境中的竞争。我们开源了ShortageSim和一个包含2,925个FDA短缺事件的数据集，为未来在信息不对称的供应链中进行政策设计和测试的研究提供了一个新的框架。

## 🔬 方法详解

**问题定义**：论文旨在解决药品短缺问题中，由于信息不对称导致监管干预效果难以评估的难题。现有方法，如传统的博弈论模型，通常假设完全理性和完全信息，这与实际情况不符，无法准确模拟市场参与者的行为，从而难以有效评估监管政策的影响。

**核心思路**：论文的核心思路是构建一个基于智能体的模拟框架，该框架能够模拟药品制造商和机构买家在信息不对称情况下的决策过程。通过引入基于大型语言模型（LLM）的智能体，模拟不同参与者对监管信息的异构解读，从而更真实地反映市场动态。

**技术框架**：ShortageSim框架主要包含以下几个模块：1) 数据集构建模块，用于收集和处理历史药品短缺事件数据；2) 智能体建模模块，利用LLM构建药品制造商和机构买家的智能体，模拟其决策行为；3) 监管干预模块，模拟监管机构发布短缺警报等干预措施；4) 模拟执行模块，运行模拟，观察市场参与者的反应和短缺情况的变化；5) 评估模块，评估监管干预的效果，并与真实数据进行对比。

**关键创新**：该论文最重要的技术创新点在于利用LLM来模拟市场参与者对监管信息的异构解读。与传统的理性模型不同，LLM能够捕捉到不同参与者对同一信息的不同理解，从而更真实地反映市场动态。此外，该框架还提供了一个开源的药品短缺数据集，为相关研究提供了便利。

**关键设计**：在智能体建模方面，论文使用了预训练的LLM，并针对药品短缺场景进行了微调。智能体的决策过程包括信息接收、信息解读、策略选择和行动执行等步骤。在模拟执行方面，论文采用了离散事件模拟方法，模拟了药品生产、采购和销售等环节。具体参数设置和损失函数等技术细节在论文中未详细描述，属于未知信息。

## 📊 实验亮点

实验结果表明，ShortageSim能够显著减少生产中断案例的解决延迟，最高可达84%，并且模拟结果更接近真实世界的轨迹。与零样本基线相比，ShortageSim能够更准确地预测药品短缺的发展趋势，验证了监管警报在解决短缺问题中的有效性。该框架的开源和数据集的发布，为后续研究提供了便利。

## 🎯 应用场景

ShortageSim可用于评估不同监管政策对药品短缺的影响，帮助决策者制定更有效的干预措施。该框架还可应用于其他供应链领域，例如医疗器械、电子元件等，以提高供应链的韧性和稳定性。此外，该研究为利用LLM模拟复杂社会经济系统提供了新的思路。

## 📄 摘要（原文）

> Drug shortages pose critical risks to patient care and healthcare systems worldwide, yet the effectiveness of regulatory interventions remains poorly understood due to information asymmetries in pharmaceutical supply chains. We propose \textbf{ShortageSim}, addresses this challenge by providing the first simulation framework that evaluates the impact of regulatory interventions on competition dynamics under information asymmetry. Using Large Language Model (LLM)-based agents, the framework models the strategic decisions of drug manufacturers and institutional buyers, in response to shortage alerts given by the regulatory agency. Unlike traditional game theory models that assume perfect rationality and complete information, ShortageSim simulates heterogeneous interpretations on regulatory announcements and the resulting decisions. Experiments on self-processed dataset of historical shortage events show that ShortageSim reduces the resolution lag for production disruption cases by up to 84\%, achieving closer alignment to real-world trajectories than the zero-shot baseline. Our framework confirms the effect of regulatory alert in addressing shortages and introduces a new method for understanding competition in multi-stage environments under uncertainty. We open-source ShortageSim and a dataset of 2,925 FDA shortage events, providing a novel framework for future research on policy design and testing in supply chains under information asymmetry.

